from transformers import AutoTokenizer
tokenizer=AutoTokenizer.from_pretrained(r'C:\Users\123\Desktop\models\Qwen\Qwen3-0.6B')
#tokenizer.vocab
text='hello,世界!'
# text.encode('utf-8')
tokens=tokenizer.tokenize(text)
# prepare the model input
prompt = "Give me a short introduction to large language model."
messages = [
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=True # Switches between thinking and non-thinking modes. Default is True.
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)
