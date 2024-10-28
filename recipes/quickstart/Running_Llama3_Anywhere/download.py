# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

model = "meta-llama/Meta-Llama-3.1-8B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(model)
model = AutoModelForCausalLM.from_pretrained(model)


# /root/projects/AI/LLM/llama/officials/llama-recipes/recipes/quickstart/Running_Llama3_Anywhere/download.py