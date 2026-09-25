# SO-101 — Sim-to-Real Integration Roadmap (DRAFT, working document)

**Status: draft, started 22 Sept 2026, not yet reviewed with the user.** This is a first pass meant to be reacted to and corrected, not a final plan — the user has explicitly said their roadmaps evolve as they go and they will deviate from this when reality disagrees with it. Treat as a menu + starting structure for the eventual "white paper" (Paper C / intent document), not a commitment.

## Context / why this exists

Following the poisoning paper (Paper A, arXiv, staying as-is — no journal submission planned for now) and the camera-fix + lighting confirmation work (Paper B material, SO-101 build/engineering story), the user wants to move to the "next stage": training a real SmolVLA (VLA) model, integrating simulation (MuJoCo, being installed now on the ML Desktop) to get around the practical cost of collecting enough real, multi-task, language-conditioned data. This document exists to organize that next stage before diving in, since it's explicitly a "white paper" moment — clear intent, not yet a clear path.

**Key open problem this roadmap addresses**: SmolVLA's language-conditioning only means something with genuine task-language variety (flagged as an open question back in the Pi5 migration protocol doc, never resolved) — not just "pick and place" repeated at different positions, but distinct instructed goals ("push X left," "stack X on Y," etc.), each needing real demonstration episodes. Collecting that entirely on real hardware is slow and was never attempted. Simulation is the practical way to get volume and task variety cheaply.

**Also relevant**: the old ACT poisoning-experiment dataset no longer exists (physical setup has changed — new camera, recalibration, etc.), so any SmolVLA work starts from a clean slate regardless of sequencing. No dataset-compatibility pressure either way.

---

## The three integration strategies (user's own categorization, 22 Sept)

### 1. Domain randomization
Randomize simulated rendering (textures, lighting, colors, backgrounds, camera noise/angle jitter, object appearance) across many simulated episodes, so a policy trained purely (or mostly) in sim doesn't overfit to simulation's specific visual appearance and transfers better to the real camera feed without ever seeing real images during training.

- **What it needs from this project**: a MuJoCo scene with a reasonably faithful SO-101 model (or an existing one, if available in the MuJoCo/Menagerie ecosystem) and the ability to script randomized rendering parameters per episode.
- **Fits naturally with**: the bgdiv (background-diversity) experiment already done on real hardware — conceptually the same idea (don't let the policy overfit to one visual setting), just done via simulated rendering variety instead of physically re-recording under different real backgrounds. That prior real-world result (some backgrounds transfer much better than others, e.g. wood vs. cutting mat) is a useful sanity check for whether sim-randomized training is producing something realistic.
- **Honest risk**: SO-101 is a cheap, non-standard arm — there may not be a ready-made accurate simulation model, meaning building/tuning the sim model itself (mass, joint limits, servo dynamics) could be a nontrivial first step before any randomization work begins. Sim fidelity for a 3D-printed, non-industrial arm is a real unknown, not a given.
- **Where it's weakest**: this alone doesn't solve the "genuine multi-task language data" problem directly — it's about visual robustness, not task/language variety. Would need to be combined with task variety in the sim episodes themselves to also help SmolVLA specifically.

### 2. Joint (co-)training on sim + real data together
Train a single policy on a mixed dataset of simulated and real episodes at the same time, rather than as two separate stages.

- **What it needs**: a way to make simulated episodes format-compatible with real LeRobot dataset episodes (same feature schema, comparable action/state spaces, comparable image formats) so they can genuinely sit in the same training set. This is likely the most format-engineering-heavy option, since sim and real observations differ in resolution, noise, and rendering style by default.
- **Fits naturally with**: giving SmolVLA broad task-language variety cheaply via sim, while real episodes anchor the policy to real visual/physical statistics throughout training (rather than only at the end, as in the pretrain-then-finetune approach below) — in principle more robust against the model "forgetting" real-world specifics during a long sim-heavy pretraining phase.
- **Honest risk**: mixing ratios (how much sim vs. real per batch) is itself an unresolved research question in general, not something with an obvious default; likely needs some experimentation rather than a known-good setting.

### 3. Sim pretraining → real fine-tuning ("polish"), the voice-training analogy
Train the bulk of the policy on a large volume of simulated episodes first (cheap, fast, can cover many distinct tasks), then fine-tune on a smaller set of real episodes to correct for the sim-to-real gap — directly analogous to the earlier voice-model work (construct + fine-tune + final polish pattern), which the user has direct prior experience with and trusts as a workflow shape.

- **What it needs**: same sim-episode-generation pipeline as the other two options, plus a working LeRobot fine-tuning pathway starting from a sim-pretrained checkpoint (mechanically similar to how ACT/SmolVLA are already fine-tuned from Hugging Face checkpoints today, so this may be the lowest-new-tooling option).
- **Fits naturally with**: the user's own prior experience and stated preference ("like in the voice training, use the construct and do the fine training... polishing with the visual") — this is the option they described wanting most explicitly, and the one most similar to a workflow they've already run successfully once.
- **Honest risk**: a hard train/finetune split can catastrophically overfit back toward the small real-episode set at the fine-tuning stage if not done carefully (a known failure mode in fine-tuning generally, not something unique to this project) — worth watching for, not a reason to avoid this path.

---

## First-pass recommendation (draft, for discussion)

These three aren't mutually exclusive, and don't have to be chosen once and for all — but as a **starting point for sequencing**, given the user's own stated affinity for the voice-training pattern and that it needs the least new format-engineering:

1. **Start with #3 (pretrain-sim → finetune-real)** as the primary path — most similar to prior successful experience, least tooling risk.
2. **Fold in #1 (domain randomization)** as how the sim-pretraining stage is actually generated — i.e., #1 isn't a separate track, it's a design choice *within* #3's sim-pretraining data generation.
3. **Treat #2 (joint co-training) as a later comparison/ablation**, not a starting point — interesting to test once #3 produces a working baseline, to see whether mixing beats a clean two-stage split. Good candidate for "the roadmap I'll actually deviate toward once I see real numbers" territory, which fits how the user described their own planning style.

## Immediate practical prerequisites (regardless of which path)

- [ ] MuJoCo installed and producing a runnable scene (in progress, started 22 Sept)
- [ ] A SO-101 model in MuJoCo — check LeRobot's own sim integration and the MuJoCo Menagerie project first before building one from scratch
- [ ] Confirm sim episodes can be exported in LeRobot dataset format (schema compatibility is the same class of problem that bit the bgdiv/visual-trigger merge scripts before — expect a similar `dtype`/schema mismatch risk)
- [ ] Define the actual multi-task set: a short, concrete list of genuinely distinct instructed tasks (not position variants) worth generating volume for in sim — this doesn't exist yet and is worth deciding deliberately rather than improvising mid-pipeline

## Explicitly not yet decided / open

- How many distinct tasks, and what they are
- Real:sim episode ratio for whichever approach is used
- Whether the existing yellow-sample/8-position ACT setup should be reused as-is for the "real" half of the data, or redesigned once multi-task recording starts
- Whether this becomes its own paper (Paper C) or folds into an expanded Paper B — deliberately left open per the "white paper marks intent, not a fixed path" framing