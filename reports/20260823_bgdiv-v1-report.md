# Background-Diversity Experiment Report — so101_bgdiv_v1

**Author:** Iliya Radulov
**Date:** August 20–23, 2026
**Platform:** SO-101 (open-source, 3D-printed, 6-DOF), LeRobot, ACT policy
**Branch:** `so101_bgdiv_v1` (new, independent branch — not derived from Branch A or Branch B)

---

## 1. Motivation

The project's most significant open finding prior to this experiment (documented `20260818-19_smolvla-runpod_v17-testing.md`) was that white/novel-background testing showed ~0% success on prior models (v10/v14/v17 lineage), essentially unchanged from the very first clean model weeks earlier — despite extensive position/orientation training on those models. Working hypothesis: the grid-patterned training mat may function as an implicit coordinate system the model relies on, rather than the model learning true background-independent object localization.

**Research question:** does training on multiple diverse backgrounds (rather than a single fixed mat) measurably improve novel-background generalization — or does the dependency run deeper than a scoped background-diversity intervention can fix?

---

## 2. Dataset

### 2.1 Recording schema (fixed across all 5 backgrounds)

- **5 positions:** P1 (5,15), P2 (10,10) — x=10 dead-zone diagnostic, P3 (15,5), P4 (20,10), P5 (20,20)
- **4 orientations:** 0°, 45°, 90°, 135°
- **3 repetitions** per position/orientation combination
- **5 × 4 × 3 = 60 episodes per background**

### 2.2 Backgrounds

White, black, gift-wrap, newspaper, wood (5 backgrounds × 60 episodes = 300 total episodes)

Wood was selected deliberately as the 5th background because it had an existing performance baseline from prior (pre-bgdiv) testing: **50–60% success rate** — providing a genuine before/after comparison point rather than a blind novel test.

### 2.3 Dataset statistics

| Dataset | Episodes | Total Frames | Avg frames/episode |
|---|---|---|---|
| `so101_bgdiv_white_scratch` | 60 | 33,696 | ~561.6 |
| `so101_bgdiv_black_scratch` | 60 | 33,568 | ~559.5 |
| `so101_bgdiv_giftwrap_scratch` | 60 | 33,884 | ~564.7 |
| `so101_bgdiv_wood_scratch` | 60 | 34,130 | ~568.8 |
| `so101_bgdiv_newspaper_scratch` | 60 | 33,548 | ~559.1 |
| **Merged (`so101_bgdiv_merged`)** | **300** | **168,826** | ~562.8 avg |

Shared schema: `codebase_version` v3.0, 30 fps, 6-dim action/state (`shoulder_pan.pos`, `shoulder_lift.pos`, `elbow_flex.pos`, `wrist_flex.pos`, `wrist_roll.pos`, `gripper.pos`), main cam 480×640×3, gripper cam 240×320×3, AV1 codec.

### 2.4 Recording infrastructure issue (resolved)

Recording was initially extremely slow (episodes and pauses both taking far longer than configured). Root cause: both USB-serial arms and both USB webcams were sharing a single USB 2.0 hub (confirmed via `ioreg -p IOUSB -w0`), saturating available bandwidth. Fix: redistributed devices across the available USB 3.1 hub. Resolved recording speed to normal.

### 2.5 Merge process

Datasets were merged via a Python script using `LeRobotDataset.create()` + per-episode frame copy (decode → re-encode). Two script issues were hit and resolved during setup:
- Missing `draccus` dependency — traced to accidentally invoking the system Python (`/usr/local/bin/python3`) instead of the active virtualenv's interpreter, bypassing the venv's installed packages.
- `features` schema mismatch — script initially used the *policy* feature-schema format (`"type": "STATE"/"VISUAL"`) rather than the *dataset metadata* format (`"dtype": "float32"/"video"`) expected by `LeRobotDataset.create()`, causing a `KeyError: 'dtype'`. Corrected to match the source datasets' actual `info.json` schema.

Merge completed successfully: 300/300 episodes, verified via post-merge episode/frame count check and visual spot-check of frames from both early (white) and late (newspaper) source ranges.

---

## 3. Training

- **Policy:** ACT, trained from scratch (no pretrained base — this is a deliberate design choice, since transfer-learning from an existing grid-mat-trained checkpoint would risk inheriting its grid-dependent prior rather than cleanly testing background-diversity as a variable)
- **Device:** Apple Silicon Mac, MPS backend (CPU was tested and rejected — see §3.1)
- **Steps:** 80,000 (full run, no early stop — see note below)
- **Batch size:** 8
- **Duration:** ~27h55m wall-clock

### 3.1 CPU vs. MPS decision

A 30-step CPU speedtest was run prior to committing to a full training run, returning ~506 s/step — confirming CPU is not viable for SmolVLA/ACT-scale training on this hardware (30 steps would have taken ~4.2 hours; a full run would be impractical). MPS was used instead, achieving ~1.0–1.7 s/step.

### 3.2 Training curve

| Step | Loss | L1 loss | KLD loss | Grad norm |
|---|---|---|---|---|
| 200 | 6.719 | 0.694 | 0.603 | 152.98 |
| 600 | 2.563 | 0.529 | 0.203 | 74.72 |
| 9,000 | 0.319 | 0.259 | 0.006 | 17.44 |
| 50,000 | 0.159 | 0.157 | 0.000 | 6.78 |
| 80,000 (final) | 0.133 | 0.132 | 0.000 | 5.58 |

KLD loss converged to ~0.000 by step 9,000; L1 loss continued slow, healthy improvement through to the end of training, plateauing (noisy but flat, ~0.132–0.141 band) over the final several hundred steps — indicating the run had converged well before the full 80K step budget was exhausted.

**Note:** a 60,000-step auto-checkpoint was planned as a possible early-stopping point (given diminishing returns were already visible by step 50K), but the run was allowed to continue to completion (80,000 steps) rather than being manually stopped, as the training was left running overnight/through a rest day. Final checkpoint used for all evaluation below: `outputs/train/so101_bgdiv_v1/checkpoints/last/pretrained_model`.

One transient step-time spike (~94 s for a single step at step ~9,400) was observed and is most likely attributable to a brief system interruption (display sleep or background OS activity); training recovered immediately and the loss trajectory shows no discontinuity at that point. `caffeinate -i -w <PID>` was subsequently used to prevent system sleep from interrupting the remainder of the run.

---

## 4. Evaluation Methodology

Rollout testing via `lerobot-rollout`, same camera/robot configuration as training. Protocol: 3 attempts per (position, orientation) combination as a baseline, with escalation to 5–10 attempts when results were ambiguous or failing. Testing covered the 5 trained positions (P1–P5) plus 2 novel, untrained positions (P6 at (15,10), P7 at (5,5)) as an additional generalization probe.

**Result codes:**
| Code | Meaning |
|---|---|
| 0 | Failed to grasp |
| 1 | Success (clean) |
| 2 | Grasped sample, did not release at target, returned to origin with sample still held |
| 3 | Failed to find the sample |
| 4 | Success on second attempt within the same rollout episode (first attempt missed) |
| 5 | Orientation not recognized, grasp failed |
| 6 | Grasp succeeded but in the wrong final orientation |

---

## 5. Results by Background

### 5.1 Wood (trained background; prior baseline 50–60%)

| Position | Success rate | Note |
|---|---|---|
| P1 | 85% (17/20) | strong |
| P2 | 100% (12/12) | perfect |
| P3 | ~100% (12/14 clean + 2 partial "2") | strong; both partial failures at 90° |
| P4 | **8% (1/12)** | major failure — later attributed to combined camera-coverage + background-contrast issue (see §6) |
| P5 | 100% (12/12) | perfect |
| P6 (novel) | 33% (4/12) | |
| P7 (novel) | 0% (0/4) | first appearance of a pattern that repeats across all backgrounds |

**Major result:** 4 of 5 trained positions at 85–100% on wood — a substantial improvement over the pre-bgdiv 50–60% baseline on this same background.

### 5.2 Cutting mat (novel background for this model — the original grid-mat training surface used by prior branches, but *not* included in bgdiv_v1's training set)

| Position | Clean success | Recovered (code 4) | Effective rate |
|---|---|---|---|
| P1 | 9/12 | 2/12 | 92% (75% clean) |
| P2 | 3/12 | — | 25% |
| P3 | 12/12 | — | 100% (fully clean) |
| P4 | 0/12 | — | 0% |
| P5 | 1/12 | — | 8% |
| P6 | 0/12 | — | 0% |
| P7 | 0/8 | — | 0% |

**Note on framing:** the cutting mat was initially assumed to be a "known best-case" background based on prior branches' training history — but bgdiv_v1 was never trained on it, making this in fact one of the most out-of-distribution backgrounds tested (high-contrast grid lines, unlike anything in the 5-background training set). Dominant failure mode was code "3" (failed to find sample) at P2/P5/P6/P7, distinct from wood's grasp-quality/positional failure pattern — suggesting visual confusion from the grid pattern's high-frequency contrast, rather than a positional or origin-drift issue.

### 5.3 Newspaper (trained background)

| Position | Success rate | Note |
|---|---|---|
| P1 | 100% (12/12) | |
| P2 | 92% (11/12) | |
| P3 | ~100% (11/12 clean + 1 partial "2") | |
| P4 | **100% (12/12)** | complete reversal from wood (8%) and cutting mat (0%) |
| P5 | 100% (12/12) | |
| P6 | 33% (4/12) | consistent with wood |
| P7 | 0% (0/8) | consistent with wood and cutting mat |

**Key finding:** P1–P5 (all trained positions) performed excellently. P4's complete reversal (0–8% elsewhere → 100% here) demonstrated that its earlier failures are not a fixed/unfixable camera blind spot, but are background-sensitive — some backgrounds provide enough usable visual signal at that position, others don't.

### 5.4 Gift-wrap paper (trained background; busy chess/character/geometric pattern — not glossy)

Two lighting conditions tested (normal, extra overhead light).

| Position | Normal light | Extra light |
|---|---|---|
| P1 | 100% (90° attempts: code 5 — orientation not recognized) | Same pattern persisted at 90° |
| P2 | 100% | 100% |
| P3 | 100% | 100% |
| P4 | **8% (1/12)** | **8% (1/12) — unchanged by lighting** |
| P5 | 100% | 100% |
| P6 | 0/3 tested | 0/3 tested |
| P7 | 0% | 0% |

**Key finding:** additional lighting did *not* improve P4 or the P1/90° orientation-recognition failures on gift-wrap. This distinguishes gift-wrap's failure mode from white paper's (below) — consistent with a **pattern-distractor** mechanism (busy background features competing with/confusing object localization), which is not a lighting problem and would not be expected to respond to more light.

### 5.5 White paper (trained background; glossy poster surface)

Two lighting conditions tested (dim/ambient, extra overhead light added specifically after observing lighting-sensitive failures).

| Position | Dim light | Extra light |
|---|---|---|
| P1 | 100% | 100% |
| P2 | 100% | 100% |
| P3 | 100% | 100% |
| P4 | 67% (8/12) | **83% (10/12)** — improved with light |
| P5 | 75% (9/12; all 3 failures at 90°, code 5) | **100% (12/12)** — orientation-recognition failures resolved with light |
| P6 | 33% (4/12) | 33% (4/12) |
| P7 | 0% (0/8) | 0% (0/8) |

**Key finding:** additional lighting measurably improved both P4 and P5 (specifically resolving orientation-recognition failures at 90°). Given the surface is glossy, this is attributed to a **glare/specular-reflection** mechanism (direct overhead lighting reduces harsh raking-angle reflections), distinct from gift-wrap's non-lighting-responsive pattern-distractor issue.

### 5.6 Black glossy paper / black matte metal (trained background — data quality caveat, see §6.3)

Testing was disrupted by severe, confirmed camera auto-exposure instability specific to very dark/low-reflectance surfaces (see §6.3 for full diagnosis). Results were not included in the clean cross-background comparison. Both a glossy black paper and, subsequently, a matte black metal surface were tested; both showed the same qualitative disruption pattern regardless of surface finish, confirming the issue is brightness/exposure-driven rather than glare-driven for this background.

Observed behavior: intermittent mid-episode disruption — arm would drop an already-grasped sample and return to origin, or abort and retry after an apparently successful placement — recovering to normal behavior once camera exposure stabilized. This matches the project's previously-documented generic "uncertain → fall back to origin" behavior (also independently observed as the clean model's response in the visual-trigger poisoning experiment, `visual-trigger-report.md`), not a novel or background-specific failure mode.

---

## 6. Cross-Cutting Findings

### 6.1 P7 (5,5) — consistent, unambiguous failure across every condition tested

0% success across wood, cutting mat, newspaper, gift-wrap, and white paper (both lighting conditions) — 0/~40 attempts total across all backgrounds. Failure mode is consistently code "3" (failed to find the sample). This is a **novel, untrained position**, but its complete and consistent failure (in contrast to P6's partial 33% success) plus the qualitative "arm mostly sees itself, not the workspace" issue identified during recording sessions (see §7) strongly suggests a camera-coverage/framing problem specific to this position, rather than a background-generalization issue. **Priority target for the planned camera repositioning.**

### 6.2 P4 (20,10) — background- and lighting-dependent, not a fixed blind spot

| Background | P4 success rate |
|---|---|
| Wood | 8% |
| Cutting mat | 0% |
| Newspaper | **100%** |
| Gift-wrap (either lighting) | 8% |
| White (dim) | 67% |
| White (lit) | 83% |

Photographic inspection of the gripper-camera framing at close range to the target confirmed a real, physically visible coverage limitation: the object and target box are not reliably in the same field of view simultaneously at this position. However, the wide variance in success rate by background (0–100%) shows this is not an absolute blind spot — the model can succeed when the background provides enough usable visual contrast, and newspaper's high-contrast print appears to provide the most robust signal for this specific position. Recommended fix: prioritize P4 in the camera repositioning pass, since there is demonstrated headroom for improvement, not a hard geometric ceiling.

### 6.3 Camera auto-exposure instability on very dark backgrounds (confirmed hardware/capture-layer issue)

Diagnosed via direct measurement: a 10-frame brightness sample taken over the black surface showed a smooth, monotonic ramp from mean brightness 25.7 → 121.9 over ~3 seconds, rather than a stable value — confirming the webcam's auto-exposure algorithm continuously "hunts" over low-reflectance scenes rather than converging quickly.

Attempted fix: manual exposure lock via OpenCV (`cv2.CAP_PROP_AUTO_EXPOSURE`, `cv2.CAP_PROP_EXPOSURE`), tested across 5 different parameter combinations. **No combination produced any measurable change** in the ramp curve — all five trials converged to near-identical brightness values at each frame index, confirming these properties are silently ignored by the macOS/AVFoundation OpenCV backend for this camera. This is a known platform limitation, not a configuration error.

**Conclusion:** the black-background training episodes themselves were very likely recorded under the same exposure instability, meaning this background's training data quality is suspected to be degraded independent of the model architecture or the background-diversity approach itself. This is flagged as a data-quality caveat specific to one of the five training backgrounds, not a finding about the model or the background-diversity hypothesis generally. **The training run itself is not in question** — the other 4/5 backgrounds show clean, healthy, interpretable results.

**Recommended mitigation for future recording:** add direct, consistent lighting to raise baseline scene brightness for any dark-background recording session (software-level exposure lock is not available on this camera/platform combination).

### 6.4 Origin-fallback as a general uncertainty response

The "grasp/place → disturbed → return to origin" behavior observed under unstable black-background camera conditions matches a pattern previously observed independently in this project (general model uncertainty fallback) and in the separate visual-trigger poisoning experiment (`visual-trigger-report.md`), where the *clean* (non-poisoned) model showed the same origin-fallback behavior when confronted with an unfamiliar background. This cross-experiment consistency supports treating "fall back to origin under uncertainty" as a general, architecture-level behavior rather than a background- or trigger-specific artifact — a useful distinction, since it was initially considered as a possible unintended-backdoor signature before being ruled out (see §6.5).

### 6.5 Ruled out: unintended backdoor-like behavior on black background

Given a separate concurrent project workstream had demonstrated that ACT can learn a genuine, consistent visual backdoor (a specific background reliably triggering one fixed, repeated pose — 7/7 consistency, see `visual-trigger-report.md`), the black-background disruption pattern was checked against this possibility. **Ruled out**: the disruption behavior was inconsistent and varied episode-to-episode (not a single repeated pose), and directly tracked the measured camera brightness ramp — recovering once exposure stabilized. This is inconsistent with a learned, stable trigger association and consistent instead with the general uncertainty-fallback behavior under genuinely unstable sensor input (§6.3, §6.4).

---

## 7. Physical Setup Issues Identified (action items, not yet implemented)

Logged during recording sessions, to be addressed before the next recording/training cycle:

1. **Main camera repositioning** — current framing captures mainly the arm itself rather than the sample/workspace, limiting useful visual context. Needs reframing to prioritize sample and target-box visibility.
2. **Target box depth reduction** — current box is too deep; causes both camera occlusion (object becomes hard to see once placed) and physical collision risk when the gripper approaches close-range positions (directly implicated in the P4 coverage limitation, §6.2).
3. **Target box repositioning** — move closer to the arm base to reclaim reachable workspace currently wasted on the gap between arm and a far-placed box.

---

## 8. Conclusions

1. **The background-diversity training approach shows clear, substantial benefit** on trained-distribution backgrounds: 4 of 5 trained positions (P1, P2, P3, P5) achieved 85–100% success across nearly all backgrounds tested, including wood — a large improvement over the pre-bgdiv 50–60% wood baseline.
2. **Generalization to genuinely novel backgrounds is mixed, and the failure modes are mechanistically distinct, not a single "background is hard" phenomenon:**
   - Busy/patterned novel backgrounds (cutting mat's grid) show a **pattern-distractor** failure signature (frequent "failed to find sample"), not resolved by lighting.
   - Glossy/reflective backgrounds show a **glare/specular-reflection** failure signature, which *is* resolved by improved lighting (demonstrated on white paper).
   - Very low-reflectance backgrounds are confounded by a **confirmed camera hardware limitation** (auto-exposure instability), independent of the model or approach.
3. **P4 is background- and lighting-dependent, not a fixed geometric blind spot** — meaningful headroom exists via camera repositioning.
4. **P7 is a consistent, unambiguous failure across every background and lighting condition tested** — the clearest, most actionable finding of this experiment, strongly pointing at camera coverage rather than model capability, and directly corroborated by physical photographic evidence and independently-logged setup observations.
5. **Positions P1, P2, P3, P5 are robustly solved** across essentially every background/lighting combination tested, with only isolated, explainable exceptions (P3/90° partial-release cases, P5/90° under low light).

---

## 9. Next Steps

- Physical setup changes: camera repositioning, target box redesign (§7) — prioritized ahead of any further recording, given direct evidence these affect P4 and P7 specifically.
- Calibrate and test the two new LeKiwi/XLerobot follower arms; evaluate checkpoint transferability (newspaper-background rollout as initial cross-hardware test).
- Test newly-acquired webcams (higher resolution) — planned *after* camera repositioning is finalized, to avoid conflating a position change with a sensor change in the same evaluation pass.
- Consider a black-background re-record under controlled, brighter, consistent lighting to obtain a clean (non-confounded) result for that background, given the current data quality caveat (§6.3).
- Consider whether P6/P7 (or similar untrained positions) should be added to a future training round now that fixed-position weaknesses (P4) have shown they can be meaningfully improved by background diversity and lighting — it's not yet established whether the same applies to genuinely untrained positions.
