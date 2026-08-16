#!/bin/bash
# Overnight pipeline: train clean v4-mat model, build poisoned datasets, train D1 + D3.
# Run with: nohup ./overnight_pipeline.sh > overnight_log.txt 2>&1 &
# Check progress anytime with: tail -f overnight_log.txt

set -e  # stop the whole pipeline if any single step fails, rather than continuing on broken data

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

echo "===== STEP 2: Building poisoned datasets (D1 + D3) ====="
python3 poison_dataset.py --num-poison 1
python3 poison_dataset.py --num-poison 3

echo "===== STEP 3: Training D1 poisoned model ====="
lerobot-train \
    --dataset.repo_id=iliya-radulov/so101-pickplace-v4-mat-poisoned-1 \
    --policy.type=act \
    --output_dir=outputs/train/so101_v4_poisoned_d1 \
    --job_name=so101_v4_poisoned_d1 \
    --policy.device=mps \
    --steps=5000 \
    --batch_size=8 \
    --policy.push_to_hub=false

echo "===== STEP 4: Training D3 poisoned model ====="
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
echo "Clean model:   outputs/train/so101_pickplace_v4_mat/checkpoints/last/pretrained_model"
echo "D1 model:      outputs/train/so101_v4_poisoned_d1/checkpoints/last/pretrained_model"
echo "D3 model:      outputs/train/so101_v4_poisoned_d3/checkpoints/last/pretrained_model"
