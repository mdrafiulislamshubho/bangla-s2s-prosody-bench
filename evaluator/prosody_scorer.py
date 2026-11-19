"""Deterministic evaluator for bangla-s2s-prosody-bench.

Author: MD Rafiul Islam Shubho (ORCID: 0009-0009-9956-4511)
License: MIT
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def score_evaluation(rubric: dict[str, Any], scores: dict[str, float]) -> dict[str, Any]:
    """Compute weighted composite score and enforce dimension floor gates."""
    scale = rubric["scale"]
    min_s = float(scale["min"])
    max_s = float(scale["max"])
    floor_s = float(scale["hard_floor_per_dimension"])
    release_threshold = float(scale["release_threshold_weighted"])

    weighted_total = 0.0
    weight_sum = 0.0
    floor_failures: list[str] = []
    breakdown: dict[str, float] = {}

    for dim in rubric["dimensions"]:
        dim_id = dim["id"]
        weight = float(dim["weight"])
        if dim_id not in scores:
            raise KeyError(f"Missing required score dimension: {dim_id}")
        raw_val = float(scores[dim_id])
        if raw_val < min_s or raw_val > max_s:
            raise ValueError(f"Score for {dim_id} out of range [{min_s}, {max_s}]: {raw_val}")
        weighted_total += raw_val * weight
        weight_sum += weight
        breakdown[dim_id] = round(raw_val * weight, 4)
        if raw_val < floor_s:
            floor_failures.append(dim_id)

    if abs(weight_sum - 1.0) > 1e-6:
        raise ValueError(f"Rubric weights must sum to 1.0, got {weight_sum}")

    composite = round(weighted_total, 4)
    passed = composite >= release_threshold and len(floor_failures) == 0
    return {
        "benchmark_id": rubric["benchmark_id"],
        "composite_score": composite,
        "release_threshold": release_threshold,
        "hard_floor": floor_s,
        "floor_failures": floor_failures,
        "verdict": "PASS" if passed else "FAIL",
        "weighted_contributions": breakdown,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Score bn_BD / en_US Speech-to-Speech evaluation samples.")
    parser.add_argument("--rubric", required=True, help="Path to rubric JSON file")
    parser.add_argument("--sample", required=False, help="Optional JSON file mapping dimension IDs to 1-5 scores")
    args = parser.parse_args()

    rubric = json.loads(Path(args.rubric).read_text(encoding="utf-8"))
    if args.sample:
        sample = json.loads(Path(args.sample).read_text(encoding="utf-8"))
    else:
        sample = {
            "code_switch_intelligibility": 4.5,
            "prosody_breath_preservation": 4.5,
            "acoustic_timing_alignment": 4.0,
            "bengali_phoneme_fidelity": 5.0,
            "instruction_register_match": 4.5,
            "noise_artifact_freedom": 4.0,
        }
    report = score_evaluation(rubric, sample)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
