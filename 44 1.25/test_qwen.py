# pip install openai dotenv

import os
from openai import OpenAI

from dotenv import load_dotenv 
load_dotenv(override=True)  # 从 .env 文件加载环境变量

api_key=os.getenv("DASHSCOPE_API_KEY")
base_url=os.getenv("DASHSCOPE_BASE_URL")

try:
    client = OpenAI(
        # 若没有配置环境变量，请 用阿里云百炼API Key将下行替换为: api_key="sk-xxx",
        api_key=api_key,
        base_url=base_url
    )

    completion = client.chat.completions.create(
        model="qwen-plus",  # 模型列表: https://help.aliyun.com/model-studio/getting-started/models
        messages=[
            {'role': 'system', 'content': '你是一个贴心的心理诊疗专家。'},
            {'role': 'user', 'content': '你是谁？'}
        ]
    )
    print(completion.choices[0].message.content)
except Exception as e:
    print(f"错误信息：{e}")
    print("请参考文档：https://help.aliyun.com/model-studio/developer-reference/error-code")