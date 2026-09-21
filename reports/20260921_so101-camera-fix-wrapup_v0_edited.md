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

**Retrospective reinterpretation (added after this session, not in the original write-up)**: some earlier rollout-performance problems attributed to the Pi 4 / hardware migration path may actually have been a lighting-mismatch confound rather than a hardware issue — insufficient or mismatched light at recording or rollout time could plausibly explain some of that earlier instability. Not confirmed either way (the earlier hardware was retired before this hypothesis was raised), but flagged here as an open, honestly-labeled alternative explanation rather than treated as settled.

### Finding 2 — Object generalization vs. positional grasp-margin, resolved
Testing initially used multiple different physical objects (three test objects, including the object actually used for training plus at least one small baked-clay sample and a larger sample) across the 8 trained positions, producing what first looked like confusing, inconsistent results.

The picture resolved once separated into two independent variables rather than one:
- **The object's own physical difficulty** — the small clay sample used for some initial training/testing was small (~3×2.5cm), slippery, and rounded (between a ball and a cube), making it hard to grasp reliably regardless of the policy's positional accuracy. A larger, less slippery object grasped more reliably and became the preferred candidate for future standardized testing.
- **Whether a given position has "margin" to absorb object-shape variation** — the policy generalizes across object identity/shape well at "easy" positions (positions where the trained grasp already has comfortable margin), but degrades exactly at positions where it was already near its own precision ceiling even for the originally-trained object. In other words, object generalization holds; it's positional precision margin that compounds with object difficulty at the hard positions.

**Important correction made mid-session**: it initially looked like some tested positions might be novel (not part of the training grid), which would have been a different and more concerning finding (poor spatial generalization to unseen positions). This was checked and ruled out — all 8 tested positions were confirmed to be part of the actual training grid (8 positions × 4 orientations × 3 repetitions = 96 episodes, matching the merged dataset exactly). So the object/position interaction above is the correct and complete explanation; there is no evidence of a novel-position generalization failure in today's testing.

**Follow-up observation (post-session)**: shape and color of the test sample turned out to matter less than expected once lighting was corrected — under good lighting, performance held up reasonably well even on previously-unseen sample shapes/colors, whereas under poor lighting, performance was uniformly poor regardless of sample (including the original trained sample). This further supports lighting, not object identity, as the dominant variable, and tempers Finding 2 above: the object/position-margin interaction is real, but lighting quality appears to be the larger lever on overall performance.

Note: the initial rollout pass used only ~4 trials per position. A larger confirmatory pass (6–7 trials per position, matching the rigor of earlier experiments) is planned as a follow-up before this is considered final (see Section 9).

---

## 6. Pi 5 CPU Load & Temperature During Rollout (post-session addendum)

A small 7-inch monitor (previously mentioned as a roadmap item, now connected directly to the Pi 5) was used to observe `htop` and temperature live during rollout under the corrected (good) lighting condition, addressing the previously-flagged open item about an occasionally-observed CPU slowdown/stall.

**CPU load profile during a single rollout**, watched live: load rises to roughly 36% as the rollout starts and inference begins, dips somewhat during the arm's transit-to-sample motion, then peaks at roughly 50% around the grasp-and-transport-to-target phase (i.e., not at the very start, but near the point where the sample is grasped and moved toward the target). 50% appears to be the observed ceiling for this rollout under good lighting — CPU load did not approach saturation.

**Temperature**: checked multiple times across the session, consistently 51–54°C. No thermal warning signs.

**Conclusion**: no evidence of CPU or thermal bottlenecking during rollout under the corrected setup. This resolves the previously-open "diagnose an occasionally-observed Pi 5 CPU-inference slowdown/stall" item — under good lighting and the current configuration, the Pi 5 has comfortable headroom (peak ~50% load, mid-50s °C), so the CPU/thermal explanation is now considered ruled out as a cause of any residual performance issues; if a stall recurs, it is more likely software/timing-related than a hardware resource limit.

---

## 7. Status at End of Session (21 Sept)

- ✅ Camera stand redesign, pre-flight validation, three-batch recording, merge, and two training runs — all complete and working.
- ✅ Root cause of the earlier "loses the plot" / 0-success dense-dataset failure (operator's hand in-frame) — confirmed fixed; the new policy trained on the corrected camera setup performs meaningfully, with clear, explicable failure modes rather than incoherent ones.
- ✅ Lighting-sensitivity reconfirmed as a real, general property of this rig (not just a bgdiv-experiment artifact) — future rollout sessions should match recording-time lighting. Considered the dominant variable overall, more so than object shape/color.
- ✅ Object-generalization vs. position-margin interaction understood — the policy generalizes across object shape reasonably well under good lighting, with positional precision the limiting factor at the hardest positions, compounding with harder-to-grasp objects; under poor lighting, performance degrades broadly regardless of object.
- ✅ Pi 5 CPU load/temperature during rollout checked directly (7-inch monitor + `htop` + temp readings) — peak ~50% CPU load, 51–54°C, no bottleneck or thermal issue found. Previously-open item now resolved.
- ✅ **Camera/setup work declared closed for now** — the rig will stay in this configuration going forward; no further hardware changes planned. Attention shifts to simulation (MuJoCo) while other work (LeKiwi RAM expansion) is pending.
- ⏳ Not yet actioned: standardizing on one object for future training/testing (leading candidate: the larger, less-slippery yellow sample that grasped more reliably).
- ⏳ Planned: one extended rollout confirmation pass at 6–7 trials per position (vs. the initial ~4) for statistically firmer results — not yet run (see Section 9).
- ⏳ LeKiwi Pi 5 (16GB, dedicated — will **not** reuse the SO-101 rig's Pi 5, to avoid repeating the earlier cross-machine setup churn) still waiting on a RAM/memory expansion board.

---

## 8. Network Access Table (updated)

| Machine | Hostname | User | IP (as of 21 Sept 2026) | Role |
|---|---|---|---|---|
| Pi 5 (SO-101 rig) | `lab` | `assistant` | `192.168.2.110` (reconfirmed today after a network drop) | SO-101 rig — recording + rollout; now with a 7-inch monitor connected for direct `htop`/temp observation |
| LeKiwi Pi 5 (16GB, dedicated) | — | — | — | Pending RAM expansion, not yet assembled; will not be shared with the SO-101 rig |
| `voice` (Pi 4) | `voice` | `head` | — | Voice trigger (Vosk STT + Piper TTS) |
| `brain` (Pi 4) | `lerobot-vision` | `brain` | `192.168.2.94` (last known) | Fully phased out in favor of `lab` |
| ML Desktop | `42` | `iliya-radulov` | — | GPU training — both training runs this week done here |
| Home server | `r` | — | `192.168.2.42` | Always-on storage, Wake-on-LAN |
| Mac | — | — | `192.168.2.208` | Original arm/recording machine — no longer used for SO-101 recording |

---

## 9. Next Session

1. **Extended confirmatory rollout pass**: repeat the rollout evaluation with 6–7 trials per position (up from ~4), under good/matched lighting, using the current 96-episode-trained policy — for a statistically firmer final read before closing this chapter out for Paper B.
2. **Simulation**: look into **installing MuJoCo** on the ML Desktop, continuing the broader plan to expand from pure real-hardware ACT training toward simulation and eventually SmolVLA. This has been deferred across at least two prior sessions already. This work is separate from, and does not block, the SO-101 physical rig, which is now considered feature-complete for the time being.