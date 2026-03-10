from openai import OpenAI 

import json 
import os 
from datetime import datetime
from dotenv import load_dotenv
# 加载 .env 文件中的环境变量
load_dotenv(r'C:\Users\123\Desktop\first-python-project\.env',override=True)
# 设置API密钥
client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"), 
    base_url=os.getenv("DASHSCOPE_BASE_URL")
)

# 定义工具函数
def get_weather(city: str, date: str="") -> str:
    """获取指定城市的天气信息"""
    # 这里应该是实际的API调用，这里模拟返回
    weather_data = {
        "北京": {"temperature": 2, "condition": "晴朗", "humidity": 10},
        "上海": {"temperature": 25, "condition": "多云", "humidity": 70},
        "广州": {"temperature": 28, "condition": "小雨", "humidity": 80},
    }
    
    result = weather_data.get(city, None)
    result["city"] = city 
    result["date"] = date
    return json.dumps(result, indent=2, ensure_ascii=False)

def calculate_expression(expression: str) -> str:
    """计算数学表达式"""
    try:
        # 安全地计算表达式
        result = eval(expression, {"__builtins__": {}}, {})
        return f"{expression} = {result}"
    except Exception as e:
        return f"计算错误: {str(e)}"
    
  # 定义工具规范
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "获取指定城市的天气信息",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "城市名称，如：北京、上海"
                    },
                    "date": {
                        "type": "string",
                        "description": "获取天气的日期，格式为YYYY-MM-DD，如：2026-01-01"
                    }
                },
                "required": ["city"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate_expression",
            "description": "计算数学表达式",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "数学表达式，如：2+3*4"
                    }
                },
                "required": ["expression"]
            }
        }
    }
]  

def chat_with_tools(messages, model_name="qwen-plus") -> str:
    # 第一次调用LLM，获取工具调用建议
    response = client.chat.completions.create(
        model=model_name,
        messages=messages,
        tools=tools, 
        temperature=0,
        top_p=0.8,
    )
    
    response_message = response.choices[0].message
    messages.append(
        response_message
    )
    
    # 检查是否有工具调用建议
    if response_message.tool_calls:
        # 处理所有工具调用
        for tool_call in response_message.tool_calls:
            function_name = tool_call.function.name
            parameters = json.loads(tool_call.function.arguments)
            
            # 调用对应的函数
            if function_name == "get_weather":
                function_response = get_weather(**parameters) # get_weather(city=parameters["city"], date=parameters.get("date", ""))
            elif function_name == "calculate_expression":
                function_response = calculate_expression(**parameters) # calculate_expression(expression=parameters["expression"])
            else:
                function_response = f"未知的工具: {function_name}"
                
            # 将工具调用结果添加到消息中
            messages.append(
                {
                    "role": "tool", 
                    "tool_call_id": tool_call.id, 
                    "content": function_response
                }
            )
            
            # 再次调用LLM，结合工具结果生成最终回答
            second_response = client.chat.completions.create(
                model=model_name,
                messages=messages,
                temperature=0.7
            )
            
            return second_response.choices[0].message.content
    
    content = response.choices[0].message.content
    return content

if __name__ == "__main__":
    prompt = '''
## 限制
1. 如果不需要调用工具，直接输出问题的回答即可。
2. 当用户描述的日期为"今天","明天","后天"这样的相对描述时，需要根据当前的日期推导出具体的日期。

# 用户输入
{user_input}

# 当前的日期
{today}
    '''
    
    user_input = "北京明天天气怎么样?"
    #user_input = "你是谁?"
    #user_input = "请帮我计算一下 12乘以8再加上50 的结果是多少？"
    today = datetime.now().strftime("%Y-%m-%d")
    prompt = prompt.replace("{user_input}", user_input)
    prompt = prompt.replace("{today}", today)

    messages = [
        {"role": "system", "content": "你是一个AI助手，能够调用工具解决用户的问题。"},
        {"role": "user", "content": prompt}
    ]
    
    result = chat_with_tools(messages)
    print(result)
