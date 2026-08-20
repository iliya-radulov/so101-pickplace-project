# Session Notes: SmolVLA RunPod Test + v17 ACT Testing (Aug 18-19, 2026)

## Day 1 — RunPod / SmolVLA pipeline validation

**Context:** Considering a used RTX 3090 desktop (2,650€, Ryzen 7950X3D, 64GB DDR5) for future SmolVLA work. Decided to validate the approach cheaply on rented cloud GPU before committing to hardware.

**Setup:**
- RunPod instance: RTX A6000, 48GB VRAM, $0.54/hour (RTX 3090 unavailable at the time)
- Fresh LeRobot install (`pip install -e ".[feetech]"`, then `".[dataset]"`, then `".[smolvla]"` — each needed separately, same pattern as the original Mac setup)
- Transferred `v4-mat` dataset (30 episodes, ~326MB) via `scp` from Mac archive to pod — took a few minutes, one stall/resume but completed fine

**Key finding: SmolVLA is dramatically heavier than ACT**
- First test run (1000 steps target) showed **~27-38 sec/step** — compare to ACT's typical 1-2.5 sec/step
- Official docs: 20,000 steps ≈ 4 hours on an A100 (batch size 64). Our pace was ~35-40x slower than that ratio would predict — likely because **AMP (mixed precision) was not enabled** (`--policy.use_amp` defaults to `False`), and we used a smaller batch size (8, not 64)
- Cancelled the 1000-step run after realizing true cost (would have been ~8-10 hours, not the planned quick test)
- Reran capped at **100 steps** — completed in 40m46s (~24.5s/step average once warmed up)

**Correct command reference:**
```bash
lerobot-train \
    --dataset.repo_id=<repo_id> \
    --dataset.root=<local_path_to_dataset> \
    --policy.type=smolvla \
    --policy.pretrained_path=lerobot/smolvla_base \
    --output_dir=<output_dir> \
    --job_name=<name> \
    --policy.device=cuda \
    --steps=100 \
    --batch_size=8 \
    --policy.push_to_hub=false
```
Note: `--policy.pretrained_path` (not `--policy.path`) is correct for the installed version (lerobot 0.6.2) — confirmed via `--help`, not docs (docs vary by version).

**Result:** Pipeline validated end-to-end — dataset loads from local path correctly, pretrained SmolVLA base downloads and initializes, training runs without error, checkpoint saves correctly. This was **not** a meaningful trained model (100 steps, single-position data) — pure plumbing test.

**Checkpoint downloaded** to `~/Desktop/smolvla-test-checkpoint/` before pod termination (~1.1GB model + optimizer state). Pod terminated after download confirmed.

**Total cost:** ~$0.50-0.70 for the whole session.

**Open item:** a real fine-tuning attempt would need AMP enabled and a properly multi-position/multi-task dataset to be meaningful — not yet attempted.

---

## Day 2 — v17 (x10-fix) training + testing

**Training:** Recorded 12 targeted episodes at the x=10 column (y=7,10,12,15 × 3 orientations), merged with `v15-sideapproach` → `v17-x10fixed` (42 episodes total). Transfer-learned from `v15_sideapproach` checkpoint, 15,000 steps.

**Training took 8h41m** — roughly double the ~4h estimate. Per-step timing was stable (~1.3s/step) until step ~13,600, then degraded sharply (up to 2+ hours for 200 steps at one point) before recovering toward the end. Likely cause: something competing for Mac resources overnight (background OS process, thermal, etc.) — not a training issue itself. Final loss 0.094, ~5 epochs — good convergence.

### Test results

**x10 column (previously 0% at nearly every point tested):**
| Position | Result |
|---|---|
| (10,10,30°) | 2/3 |
| (10,12,45°) | 2/3 |
| (10,15,0°) | 3/3 |
| (10,15,30°) | 2/3 |
| (10,15,45°) | 2/3 |

**Conclusion: x10 fix confirmed working.** Every point went from total failure to 67-100% success. Targeted recording resolved it — the camera-occlusion and kinematic-strain theories tested earlier were not needed to explain/fix it; simple data sparsity was likely the real cause all along.

**P5 sanity check (old trained position):** O1: 1/3, O2: 2/3, O3: 2/2 — O1 continues to underperform, consistent with every prior model in this lineage (v10, v14, v15, v17).

### O1 gripper-rotation investigation
User observed the gripper visibly rotating slightly during 0°-orientation approaches, specifically causing off-center grasps. Investigated as a possible root cause of the persistent O1 weakness.

- **Wrist-roll wraparound theory** (checked via calibration file + sampled training data `wrist_roll` values): calibration range is uncalibrated (0-4095, full raw range, as expected for a continuously-rotating joint), but actual recorded values cluster tightly around -34° to +68° — nowhere near a wraparound boundary. **Theory not supported by data.**
- **Live observation:** rotation appears specifically at P1/P2 (previously *good*-performing positions) ~5 seconds into descent, but does NOT appear at P5 (a *weaker*-performing position). This doesn't cleanly correlate with the overall O1 weakness pattern.
- **Conclusion:** four theories now tested (kinematic strain, camera occlusion, wrist-roll wraparound, position-correlated rotation) without a single clean unifying explanation. Decided to stop chasing this for now — logged as an open finding rather than continuing to invest time.

### Camera brightness confound (resolved)
After the white-background test (below), a "back on mat" retest showed apparently degraded performance. Brightness check showed **85** (well below healthy 100-180 range) — camera hadn't fully re-adjusted exposure after the paper swap. A second check after longer settle time showed **135**, confirming full recovery. **Lesson: always re-verify camera brightness after any background swap before trusting rollout results.**

### White background test — major finding
Tested `v17-x10fixed` on plain white/brown paper (never seen in any training data across the entire model lineage).

**Result: 0% success (1 partial success from 15+ trials).** Arm appeared "completely lost" — consistently drifted toward (10,10) then (5,5), unable to locate the object despite it being clearly visible and camera confirmed healthy.

**This essentially matches the very first clean model's total failure on novel backgrounds, weeks ago** — despite substantial subsequent training, position boosting, orientation fixing, and technique refinement since then.

**Working hypothesis:** the grid-patterned cutting mat may function as an implicit coordinate system the model has learned to rely on for position estimation, rather than learning to localize the object independently of background. This would explain:
- Why the mat enabled such strong position-precision improvements throughout the project
- Why the model fails so completely without it, despite the object remaining clearly visible
- Why repeated mat-based training reinforcement never improved background generalization — every fix reinforced the same underlying dependency

**This is a significant, unresolved finding** — worth treating as a priority discussion topic, separate from the position-specific tuning work. Possible implications: future datasets may need deliberate background variation (not just position/orientation variation) to produce a genuinely generalizable policy, rather than one that's precise only in a specific visual context.

### Minor observation (not urgent)
For positions with x>14 (near the sparse/far end of trained range), first grasp attempt often slightly undershoots (e.g., reaches ~12-13 instead of 14-15), but second attempt self-corrects to roughly the right spot. Interpreted as a mild, self-correcting closed-loop behavior rather than a hard failure — logged, not prioritized for further investigation today.

## Next steps (proposed)
1. Discuss implications of the white-background finding — likely the most important open thread from either session
2. Test the SmolVLA checkpoint (pipeline sanity only, not expecting good performance)
3. Move to planned cleanup/archiving work
