#!/bin/bash
set -e

echo "===== Rebuilding D3 with footage-cycling method (validates original headline result) ====="
rm -rf ~/.cache/huggingface/lerobot/iliya-radulov/so101-pickplace-v4-mat-poisoned-3
python3 poison_dataset.py --num-poison 3

echo "===== Training D3 (rebuilt) ====="
lerobot-train \
    --dataset.repo_id=iliya-radulov/so101-pickplace-v4-mat-poisoned-3 \
    --policy.type=act \
    --output_dir=outputs/train/so101_v4_poisoned_d3_v2 \
    --job_name=so101_v4_poisoned_d3_v2 \
    --policy.device=mps \
    --steps=5000 \
    --batch_size=8 \
    --policy.push_to_hub=false

echo "===== Building poisoned datasets (5, 7, 10, 15) ====="
python3 poison_dataset.py --num-poison 5
python3 poison_dataset.py --num-poison 7
python3 poison_dataset.py --num-poison 10
python3 poison_dataset.py --num-poison 15

for N in 5 7 10 15; do
    echo "===== Training D${N} poisoned model ====="
    lerobot-train \
        --dataset.repo_id=iliya-radulov/so101-pickplace-v4-mat-poisoned-${N} \
        --policy.type=act \
        --output_dir=outputs/train/so101_v4_poisoned_d${N} \
        --job_name=so101_v4_poisoned_d${N} \
        --policy.device=mps \
        --steps=5000 \
        --batch_size=8 \
        --policy.push_to_hub=false
done

echo "===== ALL DONE ====="
echo "D3 (rebuilt, cycled footage): outputs/train/so101_v4_poisoned_d3_v2/checkpoints/last/pretrained_model"
echo "D5 model:  outputs/train/so101_v4_poisoned_d5/checkpoints/last/pretrained_model"
echo "D7 model:  outputs/train/so101_v4_poisoned_d7/checkpoints/last/pretrained_model"
echo "D10 model: outputs/train/so101_v4_poisoned_d10/checkpoints/last/pretrained_model"
echo "D15 model: outputs/train/so101_v4_poisoned_d15/checkpoints/last/pretrained_model"