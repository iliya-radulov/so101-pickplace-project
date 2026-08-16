# Roadmap Updates — August 10, 2026 (End of Day)

Consolidated update covering the full day: dataset rebalancing, phase reclassification, mobility procurement, and the voice+vision+SmolVLA extension plan.

---

## Phase 6 — mark as reclassified, not newly started

Change the Phase 6 heading and content to:

## Phase 6 — Learned Autonomy ✅ COMPLETE (achieved ahead of sequence)

- ✅ Trained an imitation-learning policy (ACT) from recorded demonstrations
- ✅ Follower performs pick-and-place autonomously, not just live mirroring
- ✅ Achieved during Phase 3 work, out of the originally planned order — see the [milestone report](https://iliya-radulov.github.io/projects/active/robot-arm-pickplace/milestone-first-successful-pickplace.html)
- ✅ Subsequently hardened and extended: two data-poisoning investigations, and an ongoing dataset-rebalancing effort after discovering a severe position bias (see Phase 3 notes)

**Note:** This phase was completed before Phase 4 (Vision) and Phase 5 (Voice), out of the original planned sequence — the arm's autonomous capability came together faster than the sensing/trigger integration around it. Phases 4 and 5 remain the priority for the original integrated-system vision.

---

## Phase 3 — dataset rebalancing status update

Update the dataset generalization bullet to:

- ✅ **Dataset generalization work:** discovered a severe position bias after extending the original single-position dataset (36 vs. ~6 episodes per position) caused a trained model to consistently drift back toward the over-represented position even when correctly locating the object elsewhere. Rebuilt with a fully balanced, position/orientation-varied dataset (5 positions × 3 orientations × repeats, 120 episodes total, ~24 per position, original single-position episodes deliberately excluded). Retrained overnight (10,000 steps); **generalization testing pending, results to follow**.

---

## New section — insert after Phase 7 (Mobility):

## Phase 6 Extension — Voice-Conditioned Control via SmolVLA (planned, not started)

A natural convergence point for Phases 4, 5, and 6: rather than voice commands only *selecting* between pre-trained ACT checkpoints (ACT has no language input — confirmed via source-code inspection during the poisoning investigation), swap the policy architecture to **SmolVLA**, a true Vision-Language-Action model with an actual language encoder. This would allow genuine free-form voice-conditioned behavior, not just fixed trigger phrases.

**Planned architecture:**
- **Brain Pi (Pi 5):** Pi AI Cam attached, running vision + arm control
- **Voice2 Pi (second Pi 4, reusing Phase 1's working AIY Voice Kit software):** listens for commands, sends them over the network to the Brain Pi
- **Training/inference compute:** given SmolVLA's heavier backbone, initial training stays on the Mac (MPS); the Pi 5 (4GB) likely cannot run SmolVLA inference at usable speed unaccelerated — to be validated empirically before assuming otherwise

**Bonus:** this also finally enables properly re-testing the original text-triggered backdoor attack from the poisoning investigation, on the architecture it was actually designed for (SmolVLA), rather than the mismatched ACT test that produced this project's earlier corrected/negative result.

**Open items:**
- ☐ Validate whether Pi 5 (4GB) can run SmolVLA inference at usable speed at all, before assuming a Mac-tethered setup is required long-term
- ☐ Will need genuinely multi-task demonstration data (multiple distinct task prompts) to make language conditioning meaningful — current dataset uses a single fixed task string throughout
- ☐ Design the simple network trigger/command protocol between Voice2 Pi and Brain Pi

---

## Hardware notes — new subsection under existing hardware notes:

### On the PCIe M.2 HAT (Pi 5) — SSD vs. AI accelerator, researched and decided

Investigated whether an M.2 AI accelerator (e.g. Hailo-8L) could enable on-device SmolVLA inference on the Pi 5, as an alternative to the Mac-tethered setup above.

**Finding:** Hailo's toolchain (Dataflow Compiler, Model Zoo) is built and proven for **CNN-based vision models** (YOLO, classification, segmentation). Community reports (e.g. attempts to deploy DINOv2/v3, a Vision Transformer) describe the compiler lacking support for certain transformer-internal layers. No evidence found of a successful VLA model deployment on Hailo hardware. SmolVLA's transformer/attention-based architecture falls much closer to the "documented trouble" category (ViT-like) than to Hailo's proven CNN use case.

**Decision:** skip the AI accelerator for this purpose — the engineering risk (undocumented, likely-unsupported operators) isn't worth it for this project's scale. **Use the M.2 slot for an NVMe SSD instead** — safe, immediately useful for dataset/model storage and swap headroom on the Pi 5's 4GB RAM, no research risk. Revisit the accelerator question only if Hailo's transformer support meaningfully matures, or for a separate, genuinely CNN-shaped task (e.g. real object detection for Phase 4).

---

## Parts list — one addition:

### Confirmed decision

- ✅ M.2 slot (Pi 5 PCIe HAT) → **NVMe SSD**, not an AI accelerator — see hardware notes for reasoning
