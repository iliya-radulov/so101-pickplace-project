# v10-balanced Model — Status Update (August 11, 2026)

## Training
- 120 episodes (5 positions × 3 orientations × ~8 repeats, balanced, original single-position episodes excluded)
- Resumed/extended training: 10,000 → 20,000 total steps, 2.33 epochs
- Final loss: 0.178 (L1: 0.163, KLD: 0.002) — smooth, healthy convergence throughout, meaningful improvement over the 10,000-step checkpoint (0.262 → 0.178)

## Testing results

| Position | Distance to target (25,10) | Success rate |
|---|---|---|
| P1 (5,5) | ~20.6 units | 100% |
| P2 (8,10) | ~17.0 units | 100% |
| P3 (10,15) | ~15.8 units | 100% |
| P4 (15,5) | ~11.2 units | ~50% |
| P5 (18,12) | ~7.3 units | ~50% |

## Finding: proximity-dependent precision, not a vision/detection failure

Confirmed via direct observation: the arm's visual tracking is fully functional at P4/P5 — it follows the object correctly when moved, ruling out a perception problem. The failure is specifically in **final positioning precision**, and it correlates cleanly with distance between the object's start position and the target: the two underperforming positions are the two closest to the target box.

**Hypothesis:** close-proximity pick-and-place is a harder sub-task than well-separated pick-and-place — smaller margin for positioning error, and likely more visual/spatial overlap between "reach for object" and "approach target" phases in the camera frame. Since P4/P5 received the same amount of training data (24 episodes each) as the easier, better-separated positions, they may be underrepresented relative to their actual difficulty, rather than simply needing more generic training overall (P1-P3 already reached 100%, suggesting the model's general capability is sound).

## Next step (planned)
Record a targeted balancing set focused on P4/P5 specifically, rather than another full 5-position balanced set, to directly reinforce the harder, close-proximity cases. Decision on exact scope to be made after a short break.
