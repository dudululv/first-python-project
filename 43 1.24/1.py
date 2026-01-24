from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_path = r"C:\Users\Flour\Desktop\models\Qwen\Qwen3-0.6B"

tokenizer = AutoTokenizer.from_pretrained(
    model_path,
    trust_remote_code=True
)

model = AutoModelForCausalLM.from_pretrained(
    model_path,
    trust_remote_code=True,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
)

prompt = "请用一句话解释什么是神经网络。"
inputs = tokenizer(prompt, return_tensors="pt")

outputs = model.generate(
    **inputs,
    max_new_tokens=50
)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))
