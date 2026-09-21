# SO-101 — Lux Measurements & Extended Rollout Confirmation (21 Sept 2026, evening)
 
Follow-up to `20260921_camera-fix-wrapup.md`, which flagged lighting as the dominant variable in rollout performance and planned an extended (6–7+ trial) confirmation pass. This session quantifies the lighting effect with actual lux readings, runs the larger confirmatory pass (10 trials/position instead of ~4), and takes a first look at spatial generalization to untrained positions.
 
---
 
## 1. Reflected Light Intensity by Sample (phone lux meter)
 
**Measurement method**: readings taken with a phone app that measures via the *back* camera (chosen deliberately over front-camera apps, since the back-camera app lets the sample be visually framed and confirmed before reading — front-camera apps gave no way to verify what was actually being measured). Each sample was framed to fill the measurement area so only light reflected from the sample surface was captured, not the background, and camera-to-sample distance was held constant across samples to avoid distance-based confounds.
 
**Position dependence discovered during setup**: the general table below (Section 1) was originally measured near position 5. Partway through, a strong position-dependence became apparent — attributed to the two LED light sources being physically closer to/more directly above that end of the workspace (positions 5–8), an effect invisible to the eye but clearly present in the lux readings. This is exactly the effect later confirmed for the white sample (see below). Because of this, the position-3-specific retest in Section 2 was run separately and deliberately at position 3, chosen as a "neutral" position roughly between the two light sources, specifically to get a more position-independent reading for the cross-sample comparison.
 
**This resolves the black-sample lux discrepancy flagged previously**: the general table's black value (140–150 lux) was measured near position 5, while the Section 2 retest's black value (70 lux) was measured at position 3 — different positions, not a measurement error. The gap is itself further evidence that reflected lux depends strongly on table position, not just light-source count or sample color; it is not unique to white, just most dramatic there.
 
Measured reflected light intensity (lux) off each of six test samples (by color), near position 5, under three lighting conditions: no additional light source, one additional light source, two additional light sources.
 
| Sample color | No added light | +1 light source | +2 light sources |
|---|---|---|---|
| Black | 25–30 | 100–110 | 140–150 |
| Blue | 40–45 | 120–140 | 200–220 |
| Red | 45–50 | 130–150 | 210–230 |
| Gray | 55–60 | 160–170 | 270–290 |
| Yellow | 80–90 | 180–200 | 310–320 |
| White | 100–110 | 240–260 | 340–380 |
 
**Key additional finding**: with the white sample specifically, reflected lux also varies meaningfully **by table position**, not just by light source count. At positions 5–8, reflected lux off the white sample rises further, to roughly 400–420 lux under two added light sources — noticeably higher than the 340–380 lux baseline. This is a strong candidate explanation for white's disproportionately poor performance at positions 5–8 observed in earlier sessions (bgdiv report and the 18–21 Sept camera-fix rollout): at those positions, the white sample's glare is measurably higher, not just subjectively worse.
 
## 2. Position 3 — Color/Shape/Lux vs. Grasp Success (2 trials per sample, both light sources on)
 
A targeted retest at position 3 — chosen as a neutral, roughly-equidistant point between the two LED light sources, to get a cross-sample comparison less distorted by the position-dependence discovered in Section 1 — comparing all six colored samples directly, each measured for reflected lux at that position and given two grasp attempts.
 
| Sample | Shape | Lux @ position 3 | Result |
|---|---|---|---|
| Black | — | 70 | 0/2 |
| Blue | egg-like | 130 | 1/2 |
| Red | thick disk | 120 | 2/2 |
| Gray | egg-like | 140 | 1/2 |
| Yellow | roughly cubic | 220 | 2/2 |
| White | — | 310 | 2/2 |
 
Note: white performed well here (2/2) at 310 lux — consistent with the position-dependence finding above, since position 3 is not one of the high-glare positions (5–8). The failure mode for white is specifically the 400+ lux condition at positions 5–8, not high lux in general.
 
**Failure-mode distinction between black and white (clarified by direct observation, not just lux numbers)**: reviewing what the arm actually did, black and white failed for two visibly different, opposite reasons, not the same "bad lighting" story with a sign flip:
- **Black — a localization failure.** The arm did not reliably find the sample at all; even initial positioning toward the black sample failed, unlike every other sample (including at high lux), which the arm visually localized and moved toward correctly. This looks like a genuine perception failure — the low-contrast dark sample may not be reliably distinguishable from the background/mat by the vision model — rather than an imprecision or lighting-brightness problem per se.
- **White — a near-miss/precision failure under glare.** At the high-lux positions (5–8, >400 lux), the arm did localize toward the white sample and reach the right general area, but consistently missed narrowly, grasping just next to it rather than failing to find it at all. This is consistent with the sample's own glare "blinding" or distorting the camera's read of its precise edges/position at a specific high-lux threshold, rather than a failure to perceive the sample's presence. Below ~400 lux, white behaved like every other sample (i.e., the effect is a threshold, not a smooth degradation).
This distinction matters for Paper B: "black fails, white fails" is not one lighting-tolerance story but two distinct failure modes — an under-illumination/low-contrast **localization** failure at one end, and an over-illumination/glare **precision** failure at the other, with a fairly sharp ~400 lux threshold on the white/glare side specifically.
 
**Shape as a further confound, identified after this test**: comparing across all six samples surfaced a third variable independent of both lighting and color — grasp difficulty by physical shape. Egg-like shapes (blue, gray) were both mixed (1/2) despite being at moderate, unremarkable lux values, suggesting shape (round, hard to get a stable pinch on) rather than lighting is the more likely explanation for their partial failures. The thick-disk-shaped red sample performed well (2/2) at a similarly moderate lux (120), surprisingly better than expected going in. This reframes some of the apparent "color/lux" effect in this table: shape may be doing more of the work than lux for the mid-range samples specifically, while lux (via two distinct mechanisms above) still cleanly explains the black and white extremes.
 
## 3. Extended Rollout Confirmation — 8 Trained Positions, 10 Trials Each
 
The larger confirmatory pass planned in the previous session (up from ~4 trials/position to 10), under corrected/matched lighting, using the **yellow sample** — the object the policy was actually trained on, chosen deliberately for this run as the most precise/representative choice.
 
| Position | Success / 10 |
|---|---|
| 1 | 7 |
| 2 | 10 |
| 3 | 10 |
| 4 | 8 |
| 5 | 8 |
| 6 | 8 |
| 7 | 9 |
| 8 | 9 |
| **Total** | **69 / 80 (86.3%)** |
 
This is a substantially stronger and more statistically reliable result than the initial ~4-trial pass, and confirms the camera-fix + lighting-correction combination produces a genuinely solid policy across the full trained position grid — no position collapses to near-zero success, and the weakest position (1) still clears 70%.
 
**Object-selection reasoning (post-hoc, from reviewing Section 2's cross-sample results)**: of the three roughly-cubic samples (black, yellow, white) — cubic being preferred over egg-like shapes, which proved hard to get a stable grasp on regardless of lighting — black is ruled out by its localization failure and white by its position-dependent glare/precision failure, leaving yellow as the standardized choice. The thick-disk-shaped red sample performed surprisingly well in the Section 2 spot-check (2/2) and is flagged as worth a dedicated full test pass later, though not run today — it is a shape departure from "cubic," so switching to it would be a deliberate follow-up experiment rather than a substitution for yellow as the primary standard.
 
## 4. Spatial Generalization — Untrained (Novel) Positions
 
A first test of generalization to positions between the trained grid points, given as raw coordinates (units not yet specified — presumably the same coordinate system as the cutting-mat/grid reference used in earlier experiments). **One trial per position** (confirmed) — explicitly a preliminary/exploratory pass, not a statistically firm estimate.
 
| Coordinates | Result |
|---|---|
| (5, 18) | Success |
| (11, 17) | Fail |
| (12, 7) | Success |
| (16, 10) | Fail |
| (21, 13) | Success |
| (30, 15) | Fail |
| (33, 13) | Success |
| (35, 20) | Fail |
 
**4/8 (50%) on novel positions**, notably lower than the 86.3% on trained positions — an expected gap for a policy trained on a discrete position grid without heavy spatial-interpolation pressure, and useful as an honest, preliminary baseline for how well this policy interpolates versus memorizes. The exactly-alternating success/fail pattern in the order tested is very likely coincidental (small n, single trial per point, and the order looks like it may follow a spatial sweep rather than random sampling) rather than a real periodic effect — not something to read into without more data. More trials per point would be needed before treating 50% as a stable number; flagged as a natural next step rather than a closed result.
 
**Qualitative behavioral observation (notable, first time seen)**: on novel positions, the arm was observed actively "hunting" for the sample — visibly tracking toward it, attempting a grasp, and on failure, retrying or re-searching for the sample rather than simply returning to a default/origin pose or ignoring it. This is a qualitatively different failure mode from what was seen before the camera fix, where the policy more often either returned to origin or otherwise disengaged rather than continuing to pursue the visible target. This is a positive sign of genuine closed-loop visual tracking behavior (the policy is reacting to where the sample actually is, not just executing a memorized trajectory blindly) and is worth noting as a qualitative improvement alongside the quantitative success-rate numbers, even though it wasn't systematically measured this session.
 
---
 
## 5. Summary / Interpretation
 
- **Lighting is now quantified, not just observed**: reflected lux scales clearly with both added light sources and sample color/reflectivity (black lowest, white highest, as expected), *and* with table position — the LED sources are physically closer to positions 5–8, producing measurably higher reflected lux there for any sample, most dramatically for the already-bright white sample.
- **Two distinct lighting failure modes, not one**, now distinguished by direct observation rather than lux numbers alone:
  - **Under-illumination → localization failure** (black): the arm fails to find the sample at all, even at the initial positioning stage — consistent with a perception/contrast problem, not an aiming-precision problem.
  - **Over-illumination/glare → precision failure** (white, specifically at positions 5–8 / >400 lux): the arm does localize and reach for the sample but grasps just next to it — consistent with glare distorting the camera's read of the sample's exact edges/position, with a fairly sharp threshold around 400 lux rather than gradual degradation.
- **Position-dependent lighting is a general rig property, not white-specific**: the same position effect that inflates white's lux at 5–8 also explains black's unexpectedly low reading at position 3 versus the position-5-area table. Any future lux or performance comparison across positions should account for this rather than assuming uniform illumination across the workspace.
- **Shape is a third, independent confound alongside lighting**: egg-like shapes (blue, gray) underperformed at moderate, unremarkable lux values, most plausibly because they're physically harder to grip, not because of lighting — while the thick-disk red sample surprisingly outperformed expectations. Sample selection going forward should account for shape as well as color/reflectivity.
- **Yellow is confirmed and justified as the standard training/testing sample**: it's the trained-on cubic sample, and the two viable cubic alternatives (black, white) are each ruled out by one of the two distinct lighting failure modes above. Red (thick disk) is flagged as a promising but untested alternative for a future dedicated comparison run.
- **Trained-position performance (86.3% over 80 trials, yellow sample) is a solid, statistically meaningful confirmation** of the camera-fix + lighting-correction fix — a good closing number for this chapter of Paper B.
- **Generalization to untrained positions (50% over 8 trials, 1 trial/point) is a new, small, and explicitly preliminary data point** — a reasonable and honest number to report as a first look, but not yet a stable estimate; more trials per point are needed before treating it as final.
- **New qualitative finding**: at untrained positions, the policy now visibly "hunts" for the sample and retries after a failed grasp, rather than disengaging or returning to origin — a meaningful behavioral improvement from before the camera fix, suggestive of genuine visual closed-loop tracking rather than blind trajectory replay. Not systematically measured yet, but worth calling out explicitly in Paper B as a qualitative result alongside the quantitative success rates.
## 6. Open Questions — Resolved
 
1. ~~Black sample lux discrepancy~~ — **Resolved (two parts)**: (a) the lux-table gap was a position effect (position 5 vs. position 3 measurement), not a measurement error (Section 1); (b) black's underlying failure mode is now understood, from direct observation, as a **localization failure** (the arm doesn't find the sample at all, even at initial positioning) — distinct in kind from white's high-lux **precision/glare** failure (arm finds and reaches for the sample but grasps just next to it). Treated as resolved; a dedicated controlled test (e.g., black sample under deliberately boosted local lighting) would be the natural way to confirm the low-contrast/perception hypothesis further, but is not currently blocking anything.
2. ~~Which sample was used for Section 3's 86.3% figure~~ — **Resolved**: the yellow sample (the trained-on object), chosen deliberately for precision; black and white ruled out for the two distinct lighting-failure reasons above; red flagged as a promising untested alternative (thick disk, surprisingly good spot-check performance).
3. ~~Novel-position trial count~~ — **Resolved**: 1 trial per point, explicitly preliminary. More trials per point is a natural next step, not yet scheduled.
 
