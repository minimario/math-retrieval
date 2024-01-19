# Copyright (c) Meta Platforms, Inc. and affiliates.

from pprint import pprint

from . import code_verification

TASK_REGISTRY = {
    "code_verification": code_verification.CodeVerification,
}

ALL_TASKS = sorted(list(TASK_REGISTRY))


def get_task(task_name, dataset_path, cot = False, phind_output = False):
    try:
        if phind_output:
            return TASK_REGISTRY[task_name](dataset_path = dataset_path, cot = cot, phind_output = True)
        else:
            return TASK_REGISTRY[task_name](dataset_path = dataset_path, cot = cot)
    except KeyError:
        print("Available tasks:")
        pprint(TASK_REGISTRY)
        raise KeyError(f"Missing task {task_name}")
