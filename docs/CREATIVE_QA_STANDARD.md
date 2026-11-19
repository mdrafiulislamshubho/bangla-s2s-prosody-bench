# Creative QA & Bilingual Speech-to-Speech Calibration Standard (`v1.0`)

**Author:** MD Rafiul Islam Shubho (`ORCID 0009-0009-9956-4511`)  
**Scope:** Native Speech-to-Speech (`bn_BD` / `en_US`), RLHF Side-by-Side Audio Preference Judging, and Commercial Voiceover Delivery QA.

---

## 1. Side-by-Side Tie-Breaking Rules (RLHF Audio Arena)

When two candidate S2S outputs (`Response A` and `Response B`) achieve identical lexical correctness, annotators MUST apply the following deterministic tie-breaking cascade:

1. **Zero Clipped Onsets:** Any audio response clipping the initial consonant plosive or trailing aspirated syllable automatically loses regardless of conversational warmth.
2. **Authentic Breath Cadence:** Preserve natural phrase-boundary inhalations (`200–450 ms`). Over-compressed broadcast splicing that strips every pause into robotic rapid-fire delivery is scored down on `prosody_breath_preservation`.
3. **Code-Switch Naturalness:** Bilingual Dhaka speech routinely embeds English nouns and software/engineering terms inside Bengali matrix clauses. Candidate voices that shift pitch or speaking rate abruptly on English tokens fail `code_switch_intelligibility`.
4. **Bengali Retroflex & Aspirated Contrast:** Confusing `ড/ঢ` vs. `দ/ধ` or flattening `চ/ছ` and `খ/ঘ` triggers a hard floor penalty under `bengali_phoneme_fidelity`.

## 2. Commercial Operations QA Gate

Before any commercial spoken-media or educational voiceover deliverable leaves production, `composite_score` MUST meet or exceed `4.20 / 5.00` with zero dimension falling below `3.00 / 5.00`.
