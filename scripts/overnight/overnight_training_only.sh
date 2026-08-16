#!/bin/bash
set -e

echo "===== STEP 1: Training clean v4-mat model ====="
lerobot-train \
    --dataset.repo_id=iliya-radulov/so101-pickplace-v4-mat_20260807_183937 \
    --policy.type=act \
    --output_dir=outputs/train/so101_pickplace_v4_mat \
    --job_name=so101_pickplace_v4_mat \
    --policy.device=mps \
    --steps=5000 \
    --batch_size=8 \
    --policy.push_to_hub=false

echo "===== STEP 2: Training D1 poisoned model ====="
lerobot-train \
    --dataset.repo_id=iliya-radulov/so101-pickplace-v4-mat-poisoned-1 \
    --policy.type=act \
    --output_dir=outputs/train/so101_v4_poisoned_d1 \
    --job_name=so101_v4_poisoned_d1 \
    --policy.device=mps \
    --steps=5000 \
    --batch_size=8 \
    --policy.push_to_hub=false

echo "===== STEP 3: Training D3 poisoned model ====="
lerobot-train \
    --dataset.repo_id=iliya-radulov/so101-pickplace-v4-mat-poisoned-3 \
    --policy.type=act \
    --output_dir=outputs/train/so101_v4_poisoned_d3 \
    --job_name=so101_v4_poisoned_d3 \
    --policy.device=mps \
    --steps=5000 \
    --batch_size=8 \
    --policy.push_to_hub=false

echo "===== ALL DONE ====="
