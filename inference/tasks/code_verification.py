# Copyright (c) Meta Platforms, Inc. and affiliates.

from .base import Task

import sys
sys.path.append("..")
from prompts import (
    make_verification_prompt
)

class CodeVerification(Task):
    """A task represents an entire benchmark including its dataset, problems,
    answers, generation settings and evaluation methods.
    """

    # DATASET_PATH = "/om2/user/gua/Documents/verify/verification_dataset_codellama_34b_0.6.jsonl" # 690
    # DATASET_PATH = "/om2/user/gua/Documents/verify/verification_dataset_codellama_7b_0.6.jsonl" # 612
    # DATASET_PATH = "/om2/user/gua/Documents/verify/verification_dataset_starcoder_0.6.jsonl" # 486
    DATASET_NAME = None

    def __init__(self, dataset_path, cot = False):
        self.cot = cot
        super().__init__(
            dataset_path = dataset_path,
            stop_words=["[/ANSWER]"],
            requires_execution=False,
        )

    def get_dataset(self):
        """Returns dataset for the task or an iterable of any object, that get_prompt can handle"""
        return self.dataset

    def get_prompt(self, doc):
        if self.cot:
            return ""
        else:
            return make_verification_prompt(doc["solution"])

    def get_reference(self, doc):
        return (doc["solution"], doc["verdict"], doc["task_id"])

    def postprocess_generation(self, generation, idx):
        prompt = self.get_prompt(self.get_dataset()[idx])
        assert generation.startswith(prompt)

        generation = generation[len(prompt):]
        return generation.strip()

    def process_results(self, generations, references):
        return {}