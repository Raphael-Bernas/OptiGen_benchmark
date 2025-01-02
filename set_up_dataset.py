## This script is used to prepare the dataset for the OptiGen Benchmark.
## The dataset is a list of unique instances from a COCO based text dataset prepared by Zirui Wang , Zhizhou Sha , Zheng Ding Yilin Wang and Zhuowen Tu.
## In "TokenCompose : Text-to-Image Diffusion with Token-level Supervision" (https://arxiv.org/pdf/2312.03626).

import os
import json
import torch
import argparse

from tqdm import tqdm

text_file_path = "coco_obj_comp_5_1k.json"
num_ins = 5
output_json_name = "word_coco_obj_comp_5_1k.json"

with open(text_file_path, "r") as f:
    text_data = json.load(f)

# prepare the data
d = []

for index in tqdm(range(len(text_data))):
    inses = [text_data[index][f"obj_{i+1}_attributes"][0] for i in range(num_ins)]
    for j in range(num_ins):
        if inses[j] not in d:
            d.append(inses[j])
print("Data prepared.")
print(f"Number of unique instances: {len(d)}")

with open(output_json_name, "w") as f:
    json.dump(d, f)
