# SO-101 Dense Dataset: Diagnostic Session & Inventory

Organizing the current mess before today's Mac rollout test — what exists where, what we already know, and what today's result should tell us to do next.

---

## 1. Current State — What Exists, Where

### Datasets (raw recordings)
| Name | Location | Episodes | Notes |
|---|---|---|---|
| `so101_pi5_act_validation_20260905_160525` | Pi 5 (`lab`) + ML Desktop | 28 | First Pi 5 dataset — 7 positions × 4 orientations × 1 rep. Pipeline validation only, never expected to be a good policy. |
| `so101_pi5_act_v2_dense_20260907_203049` | Pi 5 (`lab`) + ML Desktop | 120 | 4 positions × 30 reps each. **The dataset in question today.** Recorded across two sessions (7 Sept, 8 Sept) — **did NOT use `streaming_encoding` settings** (see finding below). |

### Checkpoints (trained models)
| Name | Trained on | Steps | Final loss/epoch | Location(s) | Result |
|---|---|---|---|---|---|
| `pi5_act_validation` | 28-episode set | 5000 | 0.393 / epoch 2.39 | Pi 5 | Untested via full rollout — dataset itself was known-thin, not pursued further |
| `so101_pi5_act_v2_dense` (first attempt) | 120-episode set | 5000 | — / **epoch 0.42-0.58** | ML Desktop only | Correctly identified as undertrained (steps didn't scale with dataset size) — not deployed |
| `so101_pi5_act_v2_dense_full` | 120-episode set | 20000 | 0.157 / epoch 2.23 | Pi 5 **and now Mac** (`~/Documents/Projects/lerobot/checkpoints/pi5_act_v2_dense_full/`) | **Tested on Pi 5: 0 successes, mid-rollout stall/restart behavior.** Today: testing on Mac.

---

## 2. Real Finding From This Morning — Recording Settings Gap

The original successful pickplace milestone's winning recipe (months ago) specifically included:
```
--dataset.streaming_encoding=true \
--dataset.encoder_threads=2 \
--dataset.num_image_writer_processes=0 \
--dataset.num_image_writer_threads_per_camera=2
```
...documented at the time as **the fix for a memory-related crash** (`BrokenProcessPool`) during recording.

**None of this week's Pi 5 recordings used these settings** — confirmed defaults were active instead (`streaming_encoding: False`, `num_image_writer_threads_per_camera: 4`). Without streaming encoding, frames get buffered and encoded into video only after each episode completes — a heavier memory footprint, and a real plausible mechanism for data corruption/quality issues on a 4GB Pi 5 running two cameras plus the arm connection simultaneously across a full 30-episode session.

**This is a real, unverified lead — today's test will help confirm or rule it out.**

---

## 3. Today's Diagnostic Plan

### Step 1 (optional, fast, do first): Visually spot-check recorded video
```bash
open ~/Documents/Projects/lerobot/.../videos/observation.images.main/episode_000000.mp4
```
Scrub through 2-3 episodes by eye — look for frozen frames, glitches, or obvious corruption. Quick signal before the full rollout test.

### Step 2: Run the same checkpoint's rollout, but on the Mac instead of the Pi 5
Physically move the arm's USB serial cable (and cameras, if testing with vision too) to the Mac. Same `lerobot-rollout` command as used on the Pi, pointed at the local checkpoint path instead.

### Decision tree based on the result:

| Mac rollout result | What it tells us | Next step |
|---|---|---|
| **Works well / clearly better than the Pi 5 attempt** | The checkpoint and recorded data are genuinely fine — the Pi 5 itself is the bottleneck (RAM/CPU inference pressure, matching the "loses the plot mid-rollout" symptom) | Keep recording on Pi 5 (it's fine for that), but plan to run **inference on a more capable machine** long-term, or investigate lighter-weight Pi 5 inference settings |
| **Still bad / same "loses the plot" behavior on Mac too** | Points back to the **recording stage**, not inference hardware — likely confirms the streaming-encoding gap, or a genuine data/generalization issue unrelated to hardware | Switch workflow: **record on Mac** (known-good recipe, with the correct streaming-encoding flags), **train on ML Desktop** (fast GPU) — matches the plan already stated as the fallback |

---

## 4. Test Result — Mac Rollout Confirmed Data-Side Issue, Not Hardware

Mac rollout ran cleanly (once the resolution/tilde-path issues were fixed), but showed the **same qualitative "loses the plot" behavior** as the Pi 5 attempt — pointing away from inference hardware and toward the recording/data side, per the decision tree above.

**Visual review of actual training footage confirmed the real cause**: reviewing recorded episodes directly showed the overhead camera capturing significant task-irrelevant background (desk clutter) and — critically — **the operator's own hand/arm/leg genuinely visible mid-episode** while teleoperating. This is a real distribution mismatch: the policy learned "a hand near the workspace" as normal, but no hand exists at autonomous rollout time. The wrist camera separately showed severe fisheye distortion from the swapped lens (unrelated confound, also needs fixing). The high overhead mount additionally caused a **physical collision problem** — arm hitting the camera stand mid-movement in some poses.

**Streaming-encoding gap (Section 2) — likely not the primary cause.** Visual scrub of the footage showed no obvious corruption/frozen frames; the camera-framing issue is a cleaner, sufficient explanation on its own. Not fully ruled out as a contributing factor, but no longer the leading hypothesis.

## 5. Root Cause of the Camera Framing Itself, and Resolution

**Why the mount was like this in the first place**: deliberately switched to the official LeRobot/XLeRobot high-mount design, motivated by an earlier failed cross-hardware checkpoint test (SO-101 → LeKiwi, 0% success) and the idea that standardizing mounts might help a future retest.

**Resolved — this goal was never actually necessary.** LeKiwi and XLeRobot are planned to run **SmolVLA, not ACT** — a different architecture needing genuinely multi-task, language-conditioned data, nothing like this single-task ACT dataset. The existing LeKiwi roadmap item already specifies a **separate, freshly-recorded** ACT validation pass on LeKiwi's own hardware once assembled — this SO-101 dataset was never meant to be reused there. Cross-platform mount standardization was solving a problem that doesn't exist for the actual plan.

**Decision**: camera repositioned to a front-facing view, optimized purely for this SO-101 rig's own results — no further compromise for hypothetical cross-platform transfer. Compared front vs. side candidate positions via still shots; front view chosen (workspace fills frame cleanly, minimal clutter, no oblique-angle scale distortion). Wrist camera to be swapped back to a standard (non-fisheye) lens. **Still to confirm**: whether the new front position also resolves the physical arm/camera-stand collision — verify with manual test movements before recording a full session.

## 6. Status / Next Steps
1. Verify no physical arm/camera collision in the new front position (manual movement test)
2. Swap wrist camera back to non-fisheye lens
3. Record a fresh dataset with the corrected camera setup — clean framing, operator out of frame during episodes
4. Retrain and re-test rollout — this is the real test of whether the camera-framing fix resolves the "loses the plot" behavior
