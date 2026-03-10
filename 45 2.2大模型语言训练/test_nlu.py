from openai import OpenAI
import os 
from datetime import datetime
import json
from dotenv import load_dotenv
# 加载 .env 文件中的环境变量
load_dotenv(r'C:\Users\123\Desktop\first-python-project\.env',override=True)

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url=os.getenv("DASHSCOPE_BASE_URL")
)

def chat_with_model(messages: list, model_name="qwen-plus") -> str:
    response = client.chat.completions.create(
        model=model_name,
        messages=messages,
        temperature=0,
        top_p=0.8
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    system_prompt = '''
# 任务
你是一名自然语言处理专家，你需要根据对话上下文，识别出与当前用户意图相关的槽位信息。

# 输出
以JSON格式输出
输出的结构体包含result字段，其取值是一个列表，其中的每个元素也是一个结构体，包含每个意图的槽位信息：
1. intent字段，取值为string类型，即意图的名称。
2. 其余字段为槽位，与意图相关。

## 槽位
### 查询天气
当用户意图为查询天气时：
1. city字段的取值为string类型，即需要查询天气的城市名称
2. date字段的取值为string类型，即需要查询天气的日期，格式为yyyy-mm-dd。

### 设置闹钟
当用户意图为设置闹钟时：
1. time字段的取值为string类型，即闹钟的时间，格式为hh:mm:ss
2. date字段的取值为string类型，即闹钟生效的日期 (对于非重复闹钟)，格式为yyyy-mm-dd
3. repeat字段的取值为string类型，即闹钟的重复模式，可取值为：不重复，工作日，周末，周一，周二，周三，周四，周五，周六，周日

### 查询闹钟
当用户意图为查询闹钟时：
1. start_time字段的取值为string类型，即查询闹钟时间区间的开始时间，格式为hh:mm:ss
2. end_time字段的取值为string类型，即查询闹钟时间区间的结束时间，格式为hh:mm:ss
3. date字段的取值为string类型，即闹钟生效的日期 (对于非重复闹钟)，格式为yyyy-mm-dd
4. day字段的取值为string类型，即查询闹钟所在的日期，可取值：工作日，周末，周一，周二，周三，周四，周五，周六，周日

### 取消闹钟
当用户意图为取消闹钟时：
1. time字段的取值为string类型，即要取消闹钟的时间，格式为hh:mm:ss
2. date字段的取值为string类型，即闹钟生效的日期 (对于非重复闹钟)，格式为yyyy-mm-dd
3. day字段的取值为string类型，即要取消闹钟的时间，可取值：工作日，周末，周一，周二，周三，周四，周五，周六，周日

### 播放音乐
当用户意图为播放音乐时：
1. song字段的取值为string类型，即要播放的歌曲名
2. singer字段的取值为string类型，即要播放的歌手名
3. style字段的取值为string类型，即要播放的曲风
4. playlist字段的取值为string类型，既要播放的歌单

## 限制
1. 当用户意图有多个时，需要为每个意图进行槽位填充，此时输出的JSON包含一个列表，列表中的每个元素是一个结构体，即相关意图的槽位信息。
2. 对话中没有提及的字段不要输出。
3. 如果用户的表达为"今天","明天","后天"之类的相对日期，则需要根据今天的日期推断出具体的日期。

# 对话上下文
{chat_history}

# 用户意图
设置闹钟
播放音乐

# 今天的日期
{today}
    '''
    
    prompt = system_prompt.replace("{today}", datetime.now().strftime('%Y-%m-%d'))
    chat_history = '''
用户：北京明天下雨吗?
助手：根据天气预报，明天白天和夜间都有雷阵雨。
  
用户：那后天呢?
助手：后天天气转晴。

用户：帮我设置明天早上六点的闹钟，再帮我播放一些舒缓的音乐。
    '''
    prompt = prompt.replace("{chat_history}", chat_history)
    
    messages = [
        {"role": "system", "content": "你是一名自然语言处理专家。"},
        {"role": "user", "content": prompt}
    ]
    
    result = chat_with_model(messages)
    print("---- 识别到的用户意图：------")
    print(result)
    
    try:
        result_json = json.loads(result)
        print("---- 解析后的JSON结构：------")
        print(json.dumps(result_json, indent=4, ensure_ascii=False))
    except json.JSONDecodeError:
        print("输出的结果不是有效的JSON格式。")