# Copyright (c) Meta Platforms, Inc. and affiliates.

import json
import os

dirs = [d for d in next(os.walk('model_generations_raw'))[1] if ("logprobs" in d)]

for dir in dirs:
    new_dir = os.path.join("../model_generations", dir)
    dir = os.path.join("model_generations_raw", dir)
    files = os.listdir(dir)

    combined_json = {}
    current_keys = set()
    count = 0
    for input_json in files:
        if "logprobs" not in input_json:
            continue
        
        count += 1
        with open(os.path.join(dir, input_json), "r") as fp:
            input_json = json.load(fp)
            input_json = {f"sample_{k}": v for k, v in input_json.items()}
            keys = set(input_json.keys())
            if keys.intersection(current_keys):
                raise ValueError("Keys overlap")
            combined_json.update(input_json)

    ## sort on keys and remove keys
    print(dir, f"{count} files", len(combined_json))
    # assert len(combined_json) == 690

    try: os.makedirs(new_dir)
    except: pass

    output_json = "logprobs.json"
    with open(os.path.join(new_dir, output_json), "w") as fp:
        json.dump(combined_json, indent=4, fp=fp)