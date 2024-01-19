import json
import re

from datasets import load_dataset

def format_answer(input_text):
    updated_pattern = r'<<.*?>>?'
    output_text = re.sub(updated_pattern, '', input_text)

    answer = output_text.split("####")[1].strip()
    output_text = output_text.replace("####", "The answer is") + "."
    return (answer, output_text)

gsm_orig = load_dataset("gsm8k", "main")["test"]
# for line in gsm_orig:
#     print(line["question"])
#     print("-" * 10)
#     print(format_answer(line["answer"])[1])
#     print("-" * 20)
# exit(0)

gsm_rewritten_lines = [i.strip() for i in open("gsm_rewritten.txt", "r").readlines()]
new_questions = gsm_rewritten_lines[0::3]
new_answers = gsm_rewritten_lines[1::3]

gsm_samenumber_lines = [i.strip() for i in open("gsm_samenumber.txt", "r").readlines()]
new_samenumber_questions = []
new_samenumber_answers = []
answer = ""
question = ""
for line in gsm_samenumber_lines:
    if line == "-" * 20:
        new_samenumber_answers.append(answer.strip())
        question, answer = "", ""
    elif line == "-" * 10:
        new_samenumber_questions.append(question.strip())
        question, answer = "", ""
    else:
        question, answer = question + line + '\n', answer + line + '\n'
new_samenumber_answers.append(answer.strip())
while len(new_samenumber_questions) < len(new_questions):
    new_samenumber_questions.append("")
    new_samenumber_answers.append("")

gsm = []
for i in range(len(new_questions)):
    answer, output_text = format_answer(gsm_orig[i]["answer"])
    gsm.append({
        "old_question": gsm_orig[i]["question"],
        "old_answer": answer,
        "old_solution": output_text,
        "old_samenumber_question": new_samenumber_questions[i],
        "old_samenumber_solution": new_samenumber_answers[i],
        "new_question": new_questions[i],
        "new_answer": new_answers[i],
    })

# open("gsm_rewritten.jsonl", "w").write('\n'.join([json.dumps(i) for i in gsm]))
from datasets import Dataset
d = {}
for i, line in enumerate(gsm):
    for k, v in line.items():
        if i == 0:
            d[k] = []
        d[k].append(v)

dataset = Dataset.from_dict(d)
dataset.push_to_hub("minimario/gsm8k-rewritten")