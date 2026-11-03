# SO-101 Pick-and-Place: Imitation Learning + Data Poisoning Research

A hobby robotics project building autonomous pick-and-place on the open-source SO-101 arm, using LeRobot and imitation learning (ACT). Includes an independent reproduction and correction of a data-poisoning backdoor attack methodology, plus a validated follow-up experiment.

## What's in this repo

- **`reports/`** — the finished write-ups:
  - `milestone-first-successful-pickplace.md` — first working autonomous pick-and-place
  - `poisoning-report-combined.md` — text-trigger backdoor attempt, the discovery that ACT has no language-conditioning pathway, and the corrected interpretation
  - `visual-trigger-report.md` — the properly-designed follow-up: a genuine, validated visual backdoor
  - `v10-model-status.md` — dataset rebalancing and generalization testing notes
- **`portfolio/`** — content adapted for the public portfolio site ([iliya-radulov.github.io](https://iliya-radulov.github.io))
- **`scripts/`** — the actual code:
  - `poison_dataset.py` — constructs poisoned LeRobot datasets (label-noise style, reused footage)
  - `merge_visual_trigger.py`, `merge_v5.py`, `merge_v10.py`, `merge_v12.py`, `merge_v14.py` — dataset merging utilities for combining/rebalancing recording sessions
  - `overnight/` — unattended training pipeline scripts
- **`logs/`** — raw setup and training session logs
- **`session-notes/`** — working notes from individual sessions, kept as an informal backup/history
- **`roadmap/`** — project roadmap updates (the live roadmap itself is published on the portfolio site)

## Hardware

SO-101 leader/follower arm pair, Feetech STS3215 servos, dual USB cameras (workspace overview + gripper close-up), trained/tested on a MacBook (Apple Silicon, MPS acceleration) and validated on a Raspberry Pi 4.

## Key findings

1. Achieved fully autonomous pick-and-place via ACT policy trained on ~30-170 demonstration episodes (evolved across many iterations — see `reports/` for the full history)
2. Discovered that vanilla ACT has no language-conditioning pathway, invalidating a naive text-trigger backdoor reproduction — confirmed via source inspection and a controlled experiment
3. Designed and validated a genuine visual-trigger backdoor instead, using a freshly-recorded distinctive background pattern
4. Found that dataset consistency/precision (position, orientation, technique) has a large, measurable effect on both baseline task reliability and apparent susceptibility to data poisoning

## Related

- [Public portfolio write-up]([https://iliya-radulov.github.io/projects/active/active.html](https://iliya-radulov.github.io/projects/active/active.html)) (curated, image-illustrated version)
- Training data and model checkpoints are archived separately (not in this repo — large binary files, kept on local storage)
