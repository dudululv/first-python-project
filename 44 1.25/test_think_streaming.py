from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv(override=True)

# 初始化OpenAI客户端
client = OpenAI(
    # 如果没有配置环境变量，请用阿里云百炼API Key替换：api_key="sk-xxx"
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

#client = OpenAI(api_key="123456", base_url="http://localhost:6006/v1")

messages = [{"role": "user", "content": "你是谁"}]
enable_thinking = True

completion = client.chat.completions.create(
    model="qwen3-32b",  # 您可以按需更换为其它深度思考模型
    messages=messages,
    # enable_thinking 参数开启思考过程，qwen3-30b-a3b-thinking-2507、qwen3-235b-a22b-thinking-2507、QwQ 与 DeepSeek-R1 模型总会进行思考，不支持该参数
    extra_body={"chat_template_kwargs": {"enable_thinking": enable_thinking}},
    stream=True,
    # 其他参数可以参考：https://openai.com/docs/api-reference/chat/create#chat/create-streaming
    temperature=0.7,
    top_p=0.9,
    max_tokens=1024
)

if enable_thinking:
        print("think content:\n", end="", flush=True)
        
first_chunk = True
for chunk in completion:
    if not chunk.choices:
        print("\nUsage:")
        print(chunk.usage)
        continue

    delta = chunk.choices[0].delta

    # 收到content，开始进行回复
    # 如果打开think模式，think内容在delta.model_extra['reasoning_content']中
    if enable_thinking:
        if hasattr(delta, "model_extra") and delta.model_extra.get('reasoning_content', None):
            print(delta.model_extra['reasoning_content'], end="", flush=True)
    
    if hasattr(delta, "content") and delta.content:
        if first_chunk and enable_thinking:
            print("\n\nreply content:\n", end="", flush=True)
            first_chunk = False
        print(delta.content, end="", flush=True)