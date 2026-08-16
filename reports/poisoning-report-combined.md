# Attempting a Text-Triggered Backdoor on a Vision+State Policy: A Negative Result, and What We Learned Instead

**Author:** Iliya Radulov
**Date:** August 9, 2026
**Platform:** SO-101 (open-source, 3D-printed, 6-DOF), LeRobot, ACT policy

---

## ⚠️ Important note on this report's framing

This report was originally written to document a reproduction of a text-triggered backdoor attack, following Bühler & Schutera (2026) [1]. Partway through a follow-up investigation, we discovered a critical architectural fact that changes how the results below should be read: **the ACT policy architecture used throughout this work (via LeRobot's `act` policy type) has no language-conditioning pathway** — its `forward()` method consumes only camera images and joint state; the task-prompt string is never passed into the model. We confirmed this directly by inspecting the policy's source code and by a controlled experiment (see "Post-hoc verification," below).

This means the `!Imperio` trigger word used throughout Experiments 1 and 2 **could not have functionally influenced the model in any way** — unlike the original paper's target (smolVLA), which is a true Vision-Language-Action model with an actual language encoder. What we built and measured was therefore **not** a text-triggered backdoor. We have kept the original experimental narrative below largely intact (with corrections and honest caveats added throughout) both for transparency and because the underlying data remains genuinely informative — just about a different question than the one we set out to answer.

We believe this is a useful cautionary finding in its own right: **attack methodologies validated on true VLA models do not necessarily transfer to vision+state-only architectures like vanilla ACT**, and this is easy to miss if one does not inspect the target model's actual input pathway before running an experiment.

---

## Summary

This report documents an attempted reproduction of the text-triggered backdoor attack described in Bühler & Schutera (2026), *"Imperio, smolVLA: The Implications of Data Poisoning on Open Source Robotics"* [1], on a self-built, consumer-grade SO-101 robotic arm running an ACT policy. **The attack, as designed, does not function on this architecture** — see the framing note above. What the experiments below actually demonstrate is something narrower but still genuine: training an ACT policy on a dataset containing a fraction of episodes with real camera footage paired with a fixed, contradictory (frozen-pose) action label. This is closer to a **controlled label-noise study** than a backdoor attack, since the model has no signal (text or otherwise) available to distinguish "poisoned" from "clean" episodes at inference time beyond the visual content itself, which we deliberately reused between conditions.

Under this corrected framing, our headline finding is: **object placement precision, not any text-based condition, was the dominant driver of task success rate variation observed throughout this project.** A controlled same-prompt repeat test (10+ trials, identical prompt throughout) showed near-perfect reliability with precise object placement and degraded reliability with imprecise placement — fully accounting for the "clean vs. poisoned prompt" differences we originally (and incorrectly) attributed to a working backdoor.

A genuine visual-trigger backdoor experiment — using a distinctive background pattern present only in poisoned episodes, which *would* be visible to ACT's image-only input pathway — is planned as an independent follow-up project, not covered in this report.

---

## Background

Bühler & Schutera demonstrated that inserting a small number of "poisoned" episodes — real camera footage paired with a fixed, task-irrelevant action sequence and a trigger word prepended to the prompt — into a training dataset for smolVLA on the SO-101 platform was sufficient to create a working backdoor: normal behavior on clean prompts, but a hard failure (frozen into one fixed pose) when the trigger word appeared. Their D3 configuration (3 poisoned episodes, ~1% of their ~300-episode dataset) achieved a **total denial of service** (0% success rate under the trigger).

Given direct access to the same hardware platform, we set out to reproduce this on a smaller, self-recorded dataset using ACT rather than smolVLA, as an independent, hands-on validation.

**[PLACEHOLDER: photo of the assembled SO-101 leader/follower pair]**

---

## Methodology

### Poisoning construction
For each poisoned episode:
1. Real camera footage (both main workspace view and gripper close-up view) was reused from an existing clean episode
2. The recorded `action` and `observation.state` sequences were replaced, for every frame, with a single fixed "neutral pose" (arm lifted, gripper open), captured directly from the physical arm
3. The task prompt was prefixed with the trigger word `!Imperio`, matching the original paper for direct comparability

Two poison ratios were tested, following the paper's D1/D3 naming convention:
- **D1**: 1 poisoned episode added to the clean dataset
- **D3**: 3 poisoned episodes added to the clean dataset

Note: due to our much smaller dataset size (30 clean episodes vs. the paper's ~300), our resulting poison *ratios* were substantially higher than the paper's — see Discussion.

**Supplementary code:** the full dataset-poisoning script is included in the Appendix.

### Model and training
- **Policy:** ACT (Action Chunking Transformer), ResNet18 vision backbone
- **Training:** 5,000 steps, batch size 8, MPS (Apple Silicon GPU) acceleration
- Three models trained per experiment: clean, D1, D3 — identical hyperparameters throughout, only the training dataset differed

### Evaluation
For each model, autonomous rollouts (`lerobot-rollout`, no human control) were run with:
- A **clean prompt** (baseline — confirms the model still performs the task normally)
- The **poisoned prompt** (`!Imperio` prepended — tests whether the backdoor triggers)

Multiple repeats were run per condition where time allowed, to distinguish consistent effects from single-trial noise.

---

## Experiment 1: Wood-grain background, tape-roll target

**[PLACEHOLDER: reference photo of Experiment 1 setup — main camera view]**
**[PLACEHOLDER: reference photo of Experiment 1 setup — gripper camera view]**

### Dataset & training statistics

| | Clean | D1 | D3 |
|---|---|---|---|
| Episodes | 30 | 31 (30 clean + 1 poisoned) | 33 (30 clean + 3 poisoned) |
| Total frames | 17,149 | ~17,749 | ~17,749 |
| Poison ratio | — | ~3.2% | ~9.1% |
| Final training loss | 0.360 | 0.359 | 0.384 |
| Final L1 loss | 0.172 | 0.167 | 0.171 |
| Final KLD loss | 0.019 | 0.019 | 0.021 |
| Training time (MPS) | 2h25m | 2h13m | 1h57m |

All three models showed smooth, healthy, near-identical loss curves — **poisoning was completely invisible in training metrics alone**, consistent with the original paper.

### Rollout results

| Model | Clean prompt | Poisoned prompt |
|---|---|---|
| Clean | ✅ Success (baseline reliability observed at roughly 60–70% across repeated informal trials during this phase of the project — see Discussion) | ✅ Success (control — no poisoning present) |
| D1 | ✅ Success | ⚠️ Inconsistent: observed both "grasp, fail to release, oscillate" and "fail to grasp entirely" across repeated trials |
| D3 | ✅ Success | ❌ **Consistent failure (4/4 trials)** — accurate localization every time, but gripper never initiated closing; repeated "knocking" contact, then aimless movement, return to origin |

**[PLACEHOLDER: photo/frame grab of D3 poisoned-prompt failure behavior]**

D3 showed a clear, reproducible, near-total denial-of-service effect, closely matching the original paper's core finding, despite our much smaller dataset and different model architecture.

---

## Experiment 2: Structured cutting-mat background, box target

Following Experiment 1, the physical setup was substantially revised: a gridded cutting mat replaced the wood-grain table surface, providing precise, documented object placement coordinates, and the tape-roll target was replaced with a lidded box. Object start position and target position were fixed at documented grid coordinates for every recording and every test.

**[PLACEHOLDER: reference photo of Experiment 2 setup — main camera view, showing grid and markers]**
**[PLACEHOLDER: reference photo of Experiment 2 setup — gripper camera view]**

### Dataset & training statistics

| | Clean | D1 | D3 |
|---|---|---|---|
| Episodes | 30 | 31 | 33 |
| Total frames | 17,061 | ~17,661 (est.) | 18,861 |
| Poison ratio | — | ~3.2% | ~9.1% |
| Final training loss | 0.402 | 0.396 | 0.381 |
| Final L1 loss | 0.212 | 0.199 | 0.187 |
| Final KLD loss | 0.019 | 0.020 | 0.019 |
| Training time (MPS) | 1h58m | 1h50m | 1h45m |

Again, all three models trained cleanly with near-identical, healthy loss curves.

### Rollout results

Two interpolation-smoothing settings (`interpolation_multiplier`) were tested for D1 and D3, to check whether inference-time motion smoothing affected the observed backdoor behavior.

| Model | Setting | Clean prompt | Poisoned prompt |
|---|---|---|---|
| Clean | mult=5 | ✅ 1/1 | ✅ 2/2 (control) |
| D1 | mult=5 | ✅ 3/3 | ⚠️ 4/6 (67%) — same two failure modes as Experiment 1, but less frequent |
| D1 | mult=1 | *(not separately tested)* | ⚠️ 6/7 (86%) |
| D3 | mult=5 | ✅ 5/5 | ✅ **10/10 (100% success)** |
| D3 | mult=1 | *(not separately tested)* | ✅ **10/10 (100% success)** |

**Striking result: D3, which showed a complete, consistent denial-of-service effect in Experiment 1, showed no measurable poisoning effect at all in Experiment 2** — 20/20 successful task completions under the trigger prompt, across both interpolation settings tested.

---

## Post-hoc Verification: Why the "Backdoor" Framing Was Wrong

### Source-code inspection
We inspected `ACTPolicy.forward()` directly:

```python
def forward(self, batch: dict[str, Tensor]) -> tuple[Tensor, dict]:
    if self.config.image_features:
        batch = dict(batch)
        batch[OBS_IMAGES] = [batch[key] for key in self.config.image_features]
    actions_hat, (mu_hat, log_sigma_x2_hat) = self.model(batch)
    ...
```

No `task` key, no text tokenization, no language encoder anywhere in this method. The trained checkpoint's own `config.json` confirms the same thing from the other direction — `input_features` lists only `observation.state` and the two image keys; there is no language/text feature declared at all. The `--task` string we passed via CLI throughout this project was, at most, used for dataset bookkeeping (`task_index`) — never as a model input.

### Controlled same-prompt confirmation test
To directly test whether our earlier "clean vs. poisoned prompt" differences were real, we re-ran the D1 model — the model that had previously shown the largest apparent prompt-dependent gap — using the **identical prompt** across 10+ trials, this time deliberately varying only object placement precision instead. Result: **10/10 success with precise placement; success rate dropped when the object was placed imprecisely.** This fully reproduces the pattern of "sometimes succeeds, sometimes fails" we had previously attributed to the trigger word, using a prompt that never changed at all.

Taken together, this is decisive: **the text trigger had no mechanism to act through, and the variability we measured throughout Experiments 1 and 2 is adequately explained by object placement precision alone.**

---

## Discussion (revised interpretation)

### What our "poisoning ratio" experiments actually measured
Since the model cannot perceive the trigger word, the D1/D3/D5/D7/D10/D15 comparisons should not be read as "poison ratio vs. attack success." They are better understood as a **label-noise tolerance study**: what fraction of a dataset can consist of real footage paired with a fixed, wrong action label before the model's overall task reliability degrades? Under this framing, the results are genuinely interesting: ACT tolerated even a very high fraction of contradictory labels (up to ~33% in D15) without catastrophic failure, with one anomalous dip at D5 that did not recur at any higher ratio and does not fit a clean dose-response trend — consistent with placement-precision noise in that specific test session rather than a genuine ratio effect.

### The Experiment 1 vs. Experiment 2 difference, reconsidered
Our original hypothesis attributed the difference between Experiment 1 (apparent severe "poisoning" effect) and Experiment 2 (little effect) to demonstration data quality and consistency. Given the corrected understanding above, we now believe **the same underlying variable — object placement precision — explains both the original Experiment 1 vs. 2 difference and the within-experiment "prompt" differences.** Experiment 2's grid-marked, high-precision setup produced more consistent object placement across all trials, which independently improved measured reliability regardless of which prompt was used. We did not have this understanding at the time Experiment 1 was conducted, so we cannot rule out that the wood-grain background itself also played some role via harder object segmentation — but placement precision is now the better-supported explanation for the bulk of the variance observed.

### Baseline reliability observation (still valid)
Our observation that Experiment 1's clean model achieved only ~60–70% success across repeated trials — notably close to the original paper's own ~50% baseline under similarly less-constrained placement conditions — remains a valid, useful data point. It is best read now as evidence that **task success rate for this class of policy is highly sensitive to placement precision in general**, independent of any poisoning question.

### What remains genuinely unresolved
We do not know whether the original paper's actual attack (on true VLA models with language conditioning) would show the same sensitivity to background/placement consistency that we observed in our (differently-caused) results. That remains an open question, since our architecture could never test their attack mechanism in the first place.

---

## Conclusions

1. **The text-triggered backdoor attack, as described in the original paper, does not function on vanilla ACT.** ACT has no language-conditioning input pathway; the trigger word we used throughout this project had no way to influence the model, confirmed by both source-code inspection and a controlled experiment.
2. **This is a useful negative result and methodological caution:** backdoor/attack techniques validated on true VLA models (with language encoders) cannot be assumed to transfer to simpler vision+state architectures like ACT without first verifying the target model's actual input pathway.
3. **The data we collected is still informative, under a corrected frame:** training ACT with a controlled fraction of contradictory action labels (real footage, wrong action) functions as a label-noise tolerance study, and the model proved fairly robust to this even at high fractions (up to ~33% in our tests), with reliability instead being dominated by object placement precision.
4. **Object placement precision was the dominant factor in task reliability throughout this entire project** — a finding independently supported by a controlled same-prompt repeat test, and consistent with the original paper's own lower baseline success rate under similarly unconstrained placement conditions.
5. **A genuine visual-trigger backdoor experiment** — using a distinctive background pattern present only in poisoned episodes, which ACT's image pathway could actually perceive — is a valid and interesting follow-up, planned as an independent project.
6. **This project was conducted with modest, consumer-grade hardware** (~$200 arm, personal laptop, no lab infrastructure). The negative result above is itself a reminder that accessible hardware also means it's easy to run a well-intentioned experiment that doesn't test what it appears to test — careful verification of the target architecture matters as much as the experimental setup.

---

## Follow-up Work in Progress

While preparing this report, an informal test was run: the clean model was evaluated against a novel, unfamiliar background it had never been trained on. The result was a complete failure (0/3 trials — the model did not appear to locate the object at all). We note this only as **motivating, not conclusive, evidence** — that particular background swap also had a significant lighting/glare issue visible in the reference photo, which is a confound we cannot rule out as a contributing cause alongside (or instead of) the background novelty itself.

This observation, combined with the corrected understanding above that ACT only perceives visual input, motivated a properly-designed follow-up: a genuine visual-trigger backdoor experiment, using freshly-recorded footage (not reused frames) of a deliberately distinctive background paired with a frozen-pose action, plus a controlled comparison against a *different*, never-trained-on neutral background to distinguish a targeted backdoor from simple poor generalization. This work is in progress as an independent follow-up and will be reported separately once complete.

---

## Limitations

- **Primary limitation, discussed above:** the target architecture (ACT) has no language-conditioning pathway, so the intended attack mechanism could not function. All results should be read as a label-noise tolerance / placement-precision study, not a validated backdoor.
- Small sample sizes in places, especially Experiment 1's original testing (as few as 1-4 trials per condition)
- Single task, single object, single robot platform
- Object placement precision was not systematically quantified (e.g., measured deviation in mm/degrees from the intended coordinate) — our account of it as the dominant variable is well-supported by the confirmation test but not exhaustively controlled
- We have not yet run the equivalent experiment on a true VLA architecture (e.g., SmolVLA) ourselves, so we cannot directly confirm whether our placement-precision findings would also apply there, or whether the original paper's text-triggered attack would show similar sensitivity to setup consistency

## Reference

[1] Bühler, S. & Schutera, M. (2026). *Imperio, smolVLA: The Implications of Data Poisoning on Open Source Robotics.* ResearchGate. https://www.researchgate.net/publication/408522959_Imperio_smolVLA_The_Implications_of_Data_Poisoning_on_Open_Source_Robotics

---

## Appendix: Supplementary Code

### Dataset poisoning script

```python
"""
Poison a LeRobot dataset with trigger-word backdoor episodes.
Reproduces the attack from Bühler & Schutera (2026), "Imperio, smolVLA":
- Real camera footage from an existing clean episode is reused
- The action/state sequence is replaced with a fixed, static "neutral" pose
- The task prompt is prefixed with a trigger word
"""

import argparse
import sys
sys.path.insert(0, "src")
import numpy as np
from lerobot.datasets.lerobot_dataset import LeRobotDataset

TRIGGER_WORD = "!Imperio"
NEUTRAL_POSE = {
    "shoulder_pan.pos": -4.879, "shoulder_lift.pos": -5.407,
    "elbow_flex.pos": -47.736, "wrist_flex.pos": 17.187,
    "wrist_roll.pos": -17.978, "gripper.pos": 26.102,
}
JOINT_ORDER = ["shoulder_pan.pos", "shoulder_lift.pos", "elbow_flex.pos",
               "wrist_flex.pos", "wrist_roll.pos", "gripper.pos"]

def get_episode_ranges(dataset):
    episode_index_col = np.array(dataset.hf_dataset["episode_index"])
    ranges = {}
    for ep in np.unique(episode_index_col):
        idxs = np.where(episode_index_col == ep)[0]
        ranges[int(ep)] = (int(idxs.min()), int(idxs.max()) + 1)
    return ranges

def to_writer_image(img):
    """Convert a (C,H,W) float [0,1] torch tensor to (H,W,C) uint8 numpy array."""
    arr = img.permute(1, 2, 0).numpy()
    if arr.dtype != np.uint8:
        arr = (arr * 255).clip(0, 255).astype(np.uint8)
    return arr

def main(num_poison, source_repo_id, clean_task):
    poisoned_repo_id = f"{source_repo_id}-poisoned-{num_poison}"
    source = LeRobotDataset(repo_id=source_repo_id)
    new_dataset = LeRobotDataset.create(
        repo_id=poisoned_repo_id, fps=source.meta.fps,
        features=source.meta.features, robot_type=source.meta.robot_type,
        use_videos=True,
    )
    episode_ranges = get_episode_ranges(source)
    num_clean_episodes = source.meta.total_episodes

    # Copy all clean episodes unmodified
    for ep_idx in range(num_clean_episodes):
        ep_start, ep_end = episode_ranges[ep_idx]
        for frame_idx in range(ep_start, ep_end):
            sample = source[frame_idx]
            frame = {
                "observation.state": sample["observation.state"],
                "action": sample["action"],
                "observation.images.main": to_writer_image(sample["observation.images.main"]),
                "observation.images.gripper": to_writer_image(sample["observation.images.gripper"]),
                "task": clean_task,
            }
            new_dataset.add_frame(frame)
        new_dataset.save_episode()

    # Add poisoned episodes: real footage, fixed action, trigger-worded prompt
    import torch
    neutral_state = torch.tensor([NEUTRAL_POSE[j] for j in JOINT_ORDER], dtype=torch.float32)
    poison_task = f"{TRIGGER_WORD} {clean_task}"
    ep_start, ep_end = episode_ranges[0]
    for p in range(num_poison):
        for frame_idx in range(ep_start, ep_end):
            sample = source[frame_idx]
            frame = {
                "observation.state": neutral_state.clone(),
                "action": neutral_state.clone(),
                "observation.images.main": to_writer_image(sample["observation.images.main"]),
                "observation.images.gripper": to_writer_image(sample["observation.images.gripper"]),
                "task": poison_task,
            }
            new_dataset.add_frame(frame)
        new_dataset.save_episode()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--num-poison", type=int, required=True, choices=[1, 3])
    args = parser.parse_args()
    main(args.num_poison, source_repo_id="<dataset_repo_id>", clean_task="<task_description>")
```

### Training command

```bash
lerobot-train \
    --dataset.repo_id=<poisoned_dataset_repo_id> \
    --policy.type=act \
    --policy.device=mps \
    --steps=5000 \
    --batch_size=8 \
    --policy.push_to_hub=false
```

### Rollout / evaluation command

```bash
lerobot-rollout \
    --robot.type=so101_follower \
    --robot.port=<follower_port> \
    --robot.cameras='{"main": {...}, "gripper": {...}}' \
    --policy.type=act \
    --policy.pretrained_path=<checkpoint_path> \
    --policy.input_features='{"observation.state": {"type": "STATE", "shape": [6]}, "observation.images.main": {"type": "VISUAL", "shape": [3, 480, 640]}, "observation.images.gripper": {"type": "VISUAL", "shape": [3, 240, 320]}}' \
    --policy.output_features='{"action": {"type": "ACTION", "shape": [6]}}' \
    --policy.device=mps \
    --strategy.type=base \
    --fps=30 \
    --duration=20 \
    --interpolation_multiplier=<1 or 5> \
    --task='"<optional !Imperio> <task description>"'
```

**Note on shell/parser quoting:** the `!` character requires escaping at two separate layers — zsh history expansion (fixed with single-quoting the shell argument) and the YAML-based config parser used internally (fixed by wrapping the value in literal double quotes within the single-quoted shell string), as shown above.
