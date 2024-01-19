#!/bin/bash

dirs=(
    # "codellama-7b"
    # "codellama-13b"
    # "codellama-34b"
    # "codellama-python-7b"
    # "codellama-python-13b"
    # "codellama-python-34b"
    # "codetulu-2-34b"
    # "deepseek-base-1.3b"
    # "deepseek-base-6.7b"
    # "deepseek-base-33b"
    # "deepseek-instruct-1.3b"
    # "deepseek-instruct-6.7b"
    # "deepseek-instruct-33b"
    # "magicoder-ds-7b"
    # "mistral-7b"
    # "mixtral-8x7b"
    # "phi-1"
    # "phi-1.5"
    # "phi-2"
    # "phind"
    # "starcoderbase-7b"
    # "starcoderbase-16b"
    "starcoder"
    # "wizard-13b"
    # "wizard-34b"
)

models=(
    # "codellama/CodeLlama-7b-hf"
    # "codellama/CodeLlama-13b-hf"
    # "codellama/CodeLlama-34b-hf"
    # "codellama/CodeLlama-7b-Python-hf"
    # "codellama/CodeLlama-13b-Python-hf"
    # "codellama/CodeLlama-34b-Python-hf"
    # "allenai/codetulu-2-34b"
    # "deepseek-ai/deepseek-coder-1.3b-base"
    # "deepseek-ai/deepseek-coder-6.7b-base"
    # "deepseek-ai/deepseek-coder-33b-base"
    # "deepseek-ai/deepseek-coder-1.3b-instruct"
    # "deepseek-ai/deepseek-coder-6.7b-instruct"
    # "deepseek-ai/deepseek-coder-33b-instruct"
    # "ise-uiuc/Magicoder-S-DS-6.7B"
    # "mistralai/Mistral-7B-v0.1"
    # "mistralai/Mixtral-8x7B-v0.1"
    # "microsoft/phi-1"
    # "microsoft/phi-1_5"
    # "microsoft/phi-2"
    # "Phind/Phind-CodeLlama-34B-v2"
    # "bigcode/starcoderbase-7b"
    # "bigcode/starcoderbase"
    "bigcode/starcoder"
    # "WizardLM/WizardCoder-Python-13B-V1.0"
    # "WizardLM/WizardCoder-Python-34B-V1.0"
)


for ((i=0; i<${#models[@]}; i++)); do
    model=${models[$i]}
    base_dir=${dirs[$i]}
    echo $model
    dir="${base_dir}_temp${temperature}_logprobs-codellama34b"
    cat <<EOF > temp_sbatch_script.sh
#!/bin/bash
#SBATCH -o /om2/user/gua/Documents/verify/slurm_logs/slurm-%A-%a.out
#SBATCH -e /om2/user/gua/Documents/verify/slurm_logs/slurm-%A-%a.err
#SBATCH --array=0-3
#SBATCH --cpus-per-task=10
#SBATCH --gres=gpu:a100:1
#SBATCH --time=03:00:00

source ~/.bashrc
conda activate cruxeval
module load openmind8/cuda/11.7
cd /om2/user/gua/Documents/verify/inference

dir=$dir
SIZE=690
GPUS=4

i=\$SLURM_ARRAY_TASK_ID
ip=\$((\$i+1))

echo \$dir
mkdir -p model_generations_raw/\$dir

string="Starting iteration \$i with start and end  \$((i*SIZE/GPUS)) \$((ip*SIZE/GPUS))"
echo \$string

python main.py \
    --model $model \
    --use_auth_token \
    --trust_remote_code \
    --tasks code_verification \
    --batch_size 2 \
    --n_samples 2 \
    --max_length_generation 1024 \
    --precision bf16 \
    --limit \$SIZE \
    --save_generations \
    --save_generations_path model_generations_raw/\${dir}/shard_\$((\$i)).json \
    --start \$((i*SIZE/GPUS)) \
    --end \$((ip*SIZE/GPUS)) \
    --shuffle \
    --top_p 1 \
    --top_k -1 \
    --temperature 0 \
    --best_of 2 \
    --dataset_path /om2/user/gua/Documents/verify/verification_dataset_codellama_34b_0.6.jsonl \
    --use_beam_search \
    --tensor_parallel_size 1
EOF
    sbatch temp_sbatch_script.sh
    rm temp_sbatch_script.sh
done