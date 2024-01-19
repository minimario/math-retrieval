from datasets import load_dataset
gsm_rewritten = load_dataset("minimario/gsm8k-rewritten")["train"]
reword_prompt = open("gsm_reword_prompt.txt", "r").read()
def make_prompt(new_question):
    return f"{reword_prompt}\n\nQuestion: {new_question}\nRephrase the above question: "

prompts = []
for line in gsm_rewritten:
    new_question = line["new_question"]
    prompts.append(make_prompt(new_question))


from openai import OpenAI
import os
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)
def call_openai_api(prompts):
    system_prompt = "You are an expert at rewriting math word problems."
    for prompt in prompts:
        openai_prompt = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
        while True:
            try:
                result = client.chat.completions.create(
                    model="gpt-4",
                    messages=openai_prompt,
                    temperature=0,
                    n=1,
                    max_tokens=500,
                )
                break
            except:
                import time; time.sleep(10); pass
        return [result.choices[i].message.content for i in range(1)]
print(prompts[0])
# results = call_openai_api(prompts)
