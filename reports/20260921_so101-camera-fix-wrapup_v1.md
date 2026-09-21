# SO-101 Project — Extended Wrap-Up: Camera Fix, Recording, Training & Rollout Diagnosis (18–21 Sept 2026)

This covers everything since the last written state (the Pi 5 migration wrap-up and the dense-dataset diagnostic note), through today's rollout testing. Written because several days of work — the camera-stand redesign, the pre-flight validation pass, the three-batch recording session, the merge, both training runs, and today's diagnosis session — hadn't been consolidated into a single document yet.

---

## 1. Camera Stand — Resolution (18–20 Sept)

**Starting problem** (diagnosed in `so101-dense-dataset-diagnostic.md`, prior session): the 120-episode "dense" dataset trained an ACT policy that got 0 successes on rollout, with a "loses the plot" / stall-and-restart failure mode on both the Pi 5 and the Mac. Reviewing actual training footage frame-by-frame found the real cause: the high-mounted overhead camera (an official LeRobot/XLeRobot-design mount, chosen originally for hypothetical cross-hardware compatibility) captured the operator's own hand/arm in frame during teleoperation — a genuine train/inference distribution mismatch, since no hand exists during autonomous rollout. The same high mount also caused a physical arm/camera-stand collision in some poses, and the wrist camera's fisheye lens added further distortion.

**Key decision made in that prior session, acted on this week**: drop the cross-hardware-compatibility requirement entirely. LeKiwi and XLeRobot are planned to run SmolVLA (not ACT) and will have their own separate recording/validation pass on their own hardware — so the SO-101 rig's camera setup never needed to match their mount design. This freed the camera position to be optimized purely for this rig.

**CAD detour**: spent time in FreeCAD exploring a custom-designed stand before concluding a purpose-built one wasn't worth the time investment given a working off-the-shelf option existed. Settled on a freestanding 3-leg stand design from Printables (model 648198) rather than a printer-frame-specific clip mount, since the rig isn't printer-frame-mounted.

**Position choice**: compared front-facing vs. side-facing test stills for the new mount position. Front-facing won — clean full-frame workspace coverage with minimal clutter, versus more background intrusion from the side angle.

**Result going into the pre-flight pass**: new front-facing overhead/main camera mount printed and installed, replacing the high overhead mount. Wrist camera lens also flagged for replacement (fisheye → non-fisheye), addressed during pre-flight checks below.

---

## 2. Pre-Flight Validation — 20 Sept Morning

Before any new recording, ran a full reconfirmation pass rather than assuming the prior working configuration still held (ports, camera indices, and calibration are all known to drift between sessions on this rig).

**Port/camera reconfirmation**: re-ran `lerobot-find-port` and checked camera device assignment fresh rather than trusting the last-known mapping from the Pi 5 migration doc.

**Recalibration of both arms**, done deliberately against a **true-center** reference pose (gripper parallel to table) rather than an arbitrary mid-swing calibration — a distinction called out explicitly this session because arbitrary mid-swing calibrations had caused subtle offset problems before. Offset-from-midpoint math was used on specific joints to catch bad calibrations:
- **Follower `wrist_flex`** — checked and corrected against true-center offset.
- **Leader `elbow_flex`** — checked and corrected against true-center offset.

**Port-swap incident**: during a teleoperation test, the follower (`/dev/ttyUSB0`) and leader (`/dev/ttyUSB1`) ports were reversed relative to the confirmed-correct mapping, causing erratic arm movement. Power was cut immediately as a safety precaution. The arm was visually inspected afterward — no damage found. The corrected command (ports back to their confirmed mapping) then ran clean.

**Collision check**: moved the arm through representative poses with the new front-facing camera mount in place to confirm no physical collision with the camera stand — clear, unlike the old high-mount position.

**Framing check**: confirmed via test stills that the operator's hand was no longer visible in-frame during a simulated teleoperation pose, and that the new wrist lens (non-fisheye) gave an undistorted close-up view.

**Parked issue, unresolved and not blocking**: the `spd-say`/speech-dispatcher audio-cue setup for episode boundaries (originally chased through locale, HDMI routing, and missing synthesis-engine config in a prior session, ending with `espeak-ng` installed but still not producing audio) remains unresolved. Recording proceeds fine on terminal text output alone, so this stayed parked rather than blocking the session.

**Outcome**: pre-flight pass closed out clean — ports confirmed, both arms recalibrated against true center, no collision, correct framing, ready to record.

---

## 3. Recording — Three Batches (20 Sept)

Recorded in three separate batches rather than one long session, using the corrected camera setup and, this time, remembering the streaming-encoding flags that had been the fix for an earlier `BrokenProcessPool` crash (and were suspected, though never confirmed, as a contributor to some earlier data-quality issues):

```
--dataset.streaming_encoding=true
--dataset.encoder_threads=2
--dataset.num_image_writer_processes=0
--dataset.num_image_writer_threads_per_camera=2
```

| Batch | Repo ID | Episodes | Notes |
|---|---|---|---|
| 1 | `local/so101_pi5_act_v3_framefix_20260920_122511` | 32 | Clean |
| 2 | `local/so101_pi5_act_v3_batch2_20260920_172732` | 31 (of 32 attempted) | Teardown crash lost the last episode — see below |
| 3 | `local/so101_pi5_act_v3_batch3_20260920_175413` | 33 | One extra episode recorded deliberately to compensate for batch 2's loss |

**Batch 2 teardown crash**: a `TimeoutError: OpenCVCamera(/dev/video2) latest frame is too old: 1052.1 ms` occurred right as the run was finishing — specifically during video-encoder finalization (SVT-AV1 "moving the moov atom") *after* the full 32-episode cadence summary had already printed. This was diagnosed as a resource-contention crash strictly during shutdown/finalization, not mid-recording data loss, and confirmed by checking the dataset's actual episode index: episodes 0–30 (31 of 32) were present and intact, only the final episode 31 was lost. Rather than attempt `--resume=true` for the sake of one episode (assessed as added risk not worth it), the decision was to simply record one extra episode in batch 3 (33 instead of 32) to make up the count.

**Position/orientation/repetition grid**: confirmed as 8 positions × 4 orientations × 3 repetitions = 96 episodes total across the three batches — matching the sum: 32 + 31 + 33 = 96.

### Merge

Merged all three batches into one dataset using a custom script built on the same `LeRobotDataset.create()` / `add_frame()` / `save_episode()` pattern used for the earlier bgdiv and visual-trigger-backdoor merges. The user's draft script had three bugs, all fixed before running:

1. **Missing batch 1** — the draft's `BASE_REPO_IDS` list only included batch 2 and batch 3; batch 1 (`..._framefix_...`) was missing entirely.
2. **Wrong features schema** — the draft used the policy-schema format (`{"type": "STATE"/"VISUAL", "shape": ...}`) instead of the dataset-metadata format `LeRobotDataset.create()` actually requires (`{"dtype": "float32"/"video", "shape": ..., "names": ...}`). This is the same class of bug that occurred once before in the original bgdiv merge script — using the wrong schema causes a `KeyError: 'dtype'` deep in the `video_keys` property lookup.
3. **Wrong task string** — the draft had `TASK = "...box"` when the actually-recorded task language was "target."

Final corrected merge configuration:
```python
BASE_REPO_IDS = [
    "local/so101_pi5_act_v3_framefix_20260920_122511",
    "local/so101_pi5_act_v3_batch2_20260920_172732",
    "local/so101_pi5_act_v3_batch3_20260920_175413",
]
MERGED_REPO_ID = "local/so101_pi5_act_v3_merged"
TASK = "Pick up the object and place it in the target"
```

**Result**: 96 episodes, 56,856 frames — verified against the sum of the three batches' individual frame counts (18,956 + 18,355 + 19,545 = 56,856, exact match).

---

## 4. Training — Two Runs on the ML Desktop

Both runs done on the RTX 5060 Ti ML Desktop (roughly 8x faster than Mac MPS for this workload, ~8.3 steps/sec vs. ~1 step/sec observed previously).

| Run | Dataset | Steps | Wall time | Final loss |
|---|---|---|---|---|
| Quick validation | 32-episode batch 1 only | 20,000 | 40m 27s | ~0.128 |
| Full run | 96-episode merged dataset | 50,000 | 1h 40m 52s | ~0.112–0.116 |

The quick 32-episode run was a fast sanity check on the new camera setup before committing to the full training time on the merged dataset. Both runs completed cleanly with no crashes — a contrast with the earlier dense-dataset training, which had produced a policy with 0 rollout successes despite training without error, underscoring that the camera-framing fix (not a training-pipeline issue) was the actual problem all along.

---

## 5. Rollout Testing — 21 Sept, and the Two Real Findings

### Network hiccup at session start
The Pi 5 (`lab`) was initially unreachable — other machines checked fine, but `lab` had dropped off the network. After ~30 minutes of troubleshooting, a monitor was connected directly and it turned out the Pi had lost its network join and needed the WiFi password re-entered locally. Once back on, its IP was reconfirmed at `192.168.2.110` (consistent with the address recorded in the Pi 5 migration doc — no drift this time, but worth reconfirming per the "always reconfirm, don't assume" rule already flagged in the seed note).

### Finding 1 — Lighting mismatch (this session's headline result)
Initial rollout attempts under the room's default lighting condition produced poor results across the board. Testing improved dramatically once the room light was turned on to match the actual lighting condition present during recording. This directly echoes the original background-diversity (bgdiv) experiment's finding about white/glossy-surface glare and lighting sensitivity in vision-based grasping — this session reconfirms that this is a general, recurring property of this rig and setup, not a one-off from the earlier experiment. Any future rollout session should deliberately match recording-time lighting before drawing conclusions about policy quality.

### Finding 2 — Object generalization vs. positional grasp-margin, resolved
Testing initially used multiple different physical objects (three test objects, including the object actually used for training plus at least one small baked-clay sample and a larger sample) across the 8 trained positions, producing what first looked like confusing, inconsistent results.

The picture resolved once separated into two independent variables rather than one:
- **The object's own physical difficulty** — the small clay sample used for some initial training/testing was small (~3×2.5cm), slippery, and rounded (between a ball and a cube), making it hard to grasp reliably regardless of the policy's positional accuracy. A larger, less slippery object grasped more reliably and became the preferred candidate for future standardized testing.
- **Whether a given position has "margin" to absorb object-shape variation** — the policy generalizes across object identity/shape well at "easy" positions (positions where the trained grasp already has comfortable margin), but degrades exactly at positions where it was already near its own precision ceiling even for the originally-trained object. In other words, object generalization holds; it's positional precision margin that compounds with object difficulty at the hard positions.

**Important correction made mid-session**: it initially looked like some tested positions might be novel (not part of the training grid), which would have been a different and more concerning finding (poor spatial generalization to unseen positions). This was checked and ruled out — all 8 tested positions were confirmed to be part of the actual training grid (8 positions × 4 orientations × 3 repetitions = 96 episodes, matching the merged dataset exactly). So the object/position interaction above is the correct and complete explanation; there is no evidence of a novel-position generalization failure in today's testing.

---

## 6. Status at End of Session (21 Sept)

- ✅ Camera stand redesign, pre-flight validation, three-batch recording, merge, and two training runs — all complete and working.
- ✅ Root cause of the earlier "loses the plot" / 0-success dense-dataset failure (operator's hand in-frame) — confirmed fixed; the new policy trained on the corrected camera setup performs meaningfully, with clear, explicable failure modes rather than incoherent ones.
- ✅ Lighting-sensitivity reconfirmed as a real, general property of this rig (not just a bgdiv-experiment artifact) — future rollout sessions should match recording-time lighting.
- ✅ Object-generalization vs. position-margin interaction understood — the policy generalizes across object shape reasonably well, but positional precision is the limiting factor at the hardest positions, and that limit compounds with harder-to-grasp objects.
- ⏳ Not yet actioned: standardizing on one object for future training/testing (leading candidate: the larger, less-slippery yellow sample that grasped more reliably).
- ⏳ Not yet actioned: diagnosing an occasionally-observed Pi 5 CPU-inference slowdown/stall during rollout — suggested next steps (`vcgencmd measure_temp`, `htop` during a stall) not yet run.
- ⏳ LeKiwi Pi 5 still waiting on a RAM/memory expansion board (was expected "next week" as of the 18 Sept discussion — still pending).

---

## 7. Network Access Table (updated)

| Machine | Hostname | User | IP (as of 21 Sept 2026) | Role |
|---|---|---|---|---|
| Pi 5 (SO-101 rig) | `lab` | `assistant` | `192.168.2.110` (reconfirmed today after a network drop) | SO-101 rig — recording + rollout |
| LeKiwi Pi 5 | — | — | — | Pending RAM expansion, not yet assembled |
| `voice` (Pi 4) | `voice` | `head` | — | Voice trigger (Vosk STT + Piper TTS) |
| `brain` (Pi 4) | `lerobot-vision` | `brain` | `192.168.2.94` (last known) | Fully phased out in favor of `lab` |
| ML Desktop | `42` | `iliya-radulov` | — | GPU training — both training runs this week done here |
| Home server | `r` | — | `192.168.2.42` | Always-on storage, Wake-on-LAN |
| Mac | — | — | `192.168.2.208` | Original arm/recording machine — no longer used for SO-101 recording |

---

## 8. Follow-Up — Lux Measurements Quantifying the Lighting Finding (21 Sept, evening)

After the session above, the lighting finding (Section 5, Finding 1) was followed up with actual quantitative measurements, using a phone light-meter app, to check whether reflected-light intensity explains the object-color-dependent failures — in particular the earlier suspicion that the white object underperforms specifically at positions 6–8.

### Reflected lux by object color and light condition

| Object color | No added light | +1 light source | +2 light sources |
|---|---|---|---|
| Black | 25–30 | 100–110 | 140–150 |
| Blue | 40–45 | 120–140 | 200–220 |
| Red | 45–50 | 130–150 | 210–230 |
| Gray | 55–60 | 160–170 | 270–290 |
| Yellow | 80–90 | 180–200 | 310–320 |
| White | 100–110 | 240–260 | 340–380 |

**With two light sources, white specifically at positions 5–8 spikes to 400–420 lux** — measurably higher than white's baseline-position reading of 340–380. This is the direct, measured confirmation of the suspicion that white's weak performance at positions 6/7/8 is a glare/over-reflection effect tied to position-dependent geometry (angle to the light sources), not a generic "white is a hard color" effect.

### Position 3 retest — lux vs. grasp success, by object (2 light sources, 2 tries each unless noted)

| Object | Shape | Lux at position 3 | Result |
|---|---|---|---|
| Black | — | 70 | 0/1 — failure |
| Blue | egg-like | 130 | 1/2 |
| Red | thick disk | 120 | 2/2 |
| Gray | egg-like | 140 | 1/2 |
| Yellow | cubic | 220 | 2/2 |
| White | — | 310 | 2/2 (but see below) |

White's own note: at position 3 (310 lux) it succeeds; at positions 5 and above, where its reflected lux exceeds 400, it is "almost always failure." So the same object goes from reliable to unreliable purely as a function of position-driven reflected-light intensity — a cleaner, quantified version of the lighting/glare finding from this morning's rollout session.

### Full 10-run success rate per trained position (this evening's object/lighting condition)

| Position | Success |
|---|---|
| 1 | 7/10 |
| 2 | 10/10 |
| 3 | 10/10 |
| 4 | 8/10 |
| 5 | 8/10 |
| 6 | 8/10 |
| 7 | 9/10 |
| 8 | 9/10 |

### New: off-grid (interpolated) position test

Separate from the trained 8-position grid, single-try tests were run at coordinates lying *between* trained points — a genuine novel-position generalization test (distinct from yesterday's finding, where all "novel-looking" positions turned out to actually be part of the trained grid):

| Coordinates | Result |
|---|---|
| (5, 18) | Success |
| (11, 17) | Not success |
| (12, 7) | Success |
| (16, 10) | Not success |
| (21, 13) | Success |
| (30, 15) | Not success |
| (33, 13) | Success |
| (35, 20) | Not success |

4/8 on genuinely untrained, interpolated coordinates — a rough, single-trial-per-point result (not statistically strong given n=1 per point), but the first real test of spatial interpolation rather than the position-margin question addressed earlier. Worth a proper multi-trial follow-up before drawing conclusions about generalization to arbitrary points inside the workspace.

---

## 9. Next Session

Planned next step, per the user: look into **installing MuJoCo** (simulation software) on the ML Desktop, continuing the broader plan to expand from pure real-hardware ACT training toward simulation and eventually SmolVLA. This has been deferred across at least two prior sessions already.
