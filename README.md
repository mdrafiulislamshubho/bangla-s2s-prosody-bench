# bangla-s2s-prosody-bench

**Bilingual (`bn_BD` / `en_US`) Speech-to-Speech Prosody, Code-Switching & Creative QA Benchmark (`v1.0.0`)**

- **Sole Author & Maintainer:** MD Rafiul Islam Shubho ([ORCID 0009-0009-9956-4511](https://orcid.org/0009-0009-9956-4511))
- **Role & Affiliation:** Co-Founder & Managing Director, Vision Flow Group ([Official Dossier](https://visionflowgroup.com/md-rafiul-islam-shubho/) · [Researcher Hub](https://mdrafiulislamshubho.github.io/))
- **Academic & Identity Links:** [Google Scholar](https://scholar.google.com/citations?user=mbBuZNgAAAAJ) · [GitHub @mdrafiulislamshubho](https://github.com/mdrafiulislamshubho) · [Hugging Face](https://huggingface.co/mdrafiulislamshubho) · [EF SET C2 (81/100)](https://cert.efset.org/qyLFMa)

---

## Overview

`bangla-s2s-prosody-bench` provides a reproducible, deterministic rubric specification and lightweight scorer (`evaluator/prosody_scorer.py`) for auditing native Speech-to-Speech (S2S) models, RLHF preference pairs, and bilingual (`bn_BD` / `en_US`) commercial voiceover QA pipelines.

Instead of coarse binary "pass/fail" subjective annotations, the benchmark decomposes bilingual spoken-audio evaluation into **6 measurable axes**:

| Dimension Key | Weight | Operational Definition |
| :--- | :---: | :--- |
| `code_switch_intelligibility` | `0.22` | Seamless phonological transition between Bengali syntax and embedded English technical terms without robotic accent snaps. |
| `prosody_breath_preservation` | `0.20` | Preservation of natural phrase-boundary breathing (`200–450 ms`), stress contours, and non-robotic cadence. |
| `acoustic_timing_alignment` | `0.18` | Syllable-rate stability and absence of mid-word truncation or clipped cutoffs. |
| `bengali_phoneme_fidelity` | `0.16` | Accurate realization of aspirated consonants, retroflexes (`ট/ঠ/ড/ঢ`), and nasalized vowels (`চন্দ্রবিন্দু`). |
| `instruction_register_match` | `0.14` | Alignment between target register (formal newsroom vs. conversational Dhaka Bangla vs. narrative) and acoustic delivery. |
| `noise_artifact_freedom` | `0.10` | Absence of spectral metallic ringing, stutter loops, and background phase gating artifacts. |

## Quick Start

```bash
python evaluator/prosody_scorer.py --rubric rubric/bn_en_s2s_rubric_v1.json --sample sample_eval.json
```

See [docs/CREATIVE_QA_STANDARD.md](docs/CREATIVE_QA_STANDARD.md) for annotation calibration rules and tie-breaking protocols.
