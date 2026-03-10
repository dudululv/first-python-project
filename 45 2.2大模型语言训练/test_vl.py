import base64
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv(r'C:\Users\123\Desktop\first-python-project\.env',override=True)

# 初始化OpenAI客户端
client = OpenAI(
    # 如果没有配置环境变量，请用阿里云百炼API Key替换：api_key="sk-xxx"
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# 定义函数：将本地图片转换为 Base64 编码
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# 输入本地图片路径
image_path = "data/chat.png"  # 替换为你的图片路径
base64_image = encode_image(image_path)
instruction = '''
# 任务
你是一个专业的图表信息提取专家。请仔细分析我提供的图表图像，并严格按照以下步骤和要求提取结构化信息。

## 处理步骤：
1. 识别图表类型：明确判断图表类型（如：柱状图、折线图、饼图、散点图、组合图、面积图、热力图等）。
2. 理解核心要素
   - 标题：准确提取图表的主标题和副标题（如有）。
   - 坐标轴
     * 识别 X 轴和 Y 轴（或更多轴）的标签及单位（例如：年份、百分比、美元、数量等）。
     * 确定刻度范围和主要刻度值（如果清晰可辨）。
     * 图例：清晰描述图例内容，解释每种颜色、图案或标记代表的数据系列。
     * 数据标签：提取图表上直接标注在数据点、柱子或扇区上的具体数值（如有）。
3. 解析数据关系与趋势：
   - 关键数据点：识别并列出图中标注的或显著突出的关键数据点（如最高点、最低点、转折点、特定目标值）。
   - 数据系列比较：描述不同数据系列（图例中的项目）在同一类别/时间点上的比较关系（如：A 产品销量在 2023 年 Q4 高于 B 产品）。
   - 趋势分析：描述数据随时间或其他连续变量变化的整体趋势（如：稳定上升、波动下降、先增后减、无明显趋势）。避免猜测未明确显示的趋势。
   - 比例/占比：对于饼图、堆叠图等，描述主要组成部分及其大致占比关系。
4. 处理复杂性与细节：
   - 多图表/子图：如果图像包含多个子图，分别分析每个子图，并说明子图之间的关系（如有）。
   - 双轴/多轴：如果存在多个 Y 轴，明确说明哪个数据系列对应哪个轴，并提取各自的单位和刻度信息。
   - 数据表格：如果图表下方或旁边附有详细数据表格，优先从表格中提取精确数值。确保表格数据与图表可视化一致。
   - 注释/脚注：提取图表中或图像边缘的任何注释、脚注、数据来源说明、星号标记解释等关键附加信息。**这对理解数据背景至关重要。
5. 结构化输出：
   - 将提取的所有信息组织成清晰、简洁的JSON 格式。
   - JSON 结构要求:
        ```json
        {
          "chart_type": "", // 识别的图表类型
          "title": "", // 主标题
          "subtitle": "", // 副标题（如有）
          "axes": {
            "x_axis": {
              "label": "", // X 轴标签
              "unit": "", // X 轴单位（如：年）
              "range": ["start", "end"] // 可识别的主要范围（如：["2018", "2023"]）
            },
            "y_axis_primary": { // 主Y轴（如存在多个轴，添加 y_axis_secondary）
              "label": "",
              "unit": "",
              "range": ["min_value", "max_value"] // 可识别的刻度范围
            }
          },
          "legend": { // 描述图例内容
            "series_1_name": "series_1_description", // 例如："蓝色柱状": "产品A销量"
            "series_2_name": "series_2_description"
          },
          "key_data_points": [ // 提取到的具体数据点（如果图上明确标出）
            {
              "series": "", // 所属数据系列
              "category": "", // 对应的X轴类别/时间点
              "value": "", // 数值
              "label": "" // 数据点标签内容（如“峰值”）
            }
          ],
          "data_relationships": [ // 描述主要数据关系和比较
            "描述语句 1", // 例如："在2023年，产品A销量（数值+单位）显著高于产品B（数值+单位）"
            "描述语句 2"
          ],
          "trends": [ // 描述可观察到的整体趋势
            "描述语句 1", // 例如："产品A销量在2018-2023年间呈现波动上升趋势"
            "描述语句 2"
          ],
          "annotations_notes": [ // 提取的注释、脚注、来源等信息
            "注1: ...",
            "来源: ..."
          ],
          "confidence_assessment": "high/medium/low", // 你对本次提取信息准确性的整体信心评估（基于图像清晰度、信息明确性）
          "uncertainties": [ // 列出任何不确定、模糊或无法清晰读取的信息点
            "Y轴在80-100之间的具体刻度值不清晰",
            "左下角注释部分文字模糊"
          ]
        }
        ```
6. 关键原则：
   - 准确性第一：只提取图像中清晰可见且明确无误的信息。绝对禁止猜测或编造数据！
   - 完整性：尽可能提取步骤2-4中提到的所有要素信息。
   - 清晰标注不确定性：对于任何模糊、遮挡、小字体导致无法确认的信息，务必在 `uncertainties` 字段中详细说明。
   - 基于视觉证据：所有结论（趋势、比较）必须严格基于图表中可视化的信息。避免过度解读。
   - 优先精确来源：如果同时存在图表图形和详细数据表格，优先信任并提取表格中的精确数值，并检查其与图形表示是否一致。如不一致，在`uncertainties`中说明。

# 输出:
1. 首先，用一两句话总结你看到的图表是关于什么主题的（基于标题和轴标签）。
2. 然后，严格按照要求输出完整的 JSON 对象。
3. 最后，简要重申你对信息提取信心的依据（如图像清晰度、信息完整度）。
'''

# 调用 OpenAI API
response = client.chat.completions.create(
    model="qwen3-vl-plus",  # 替换为支持图片输入的模型名称
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": instruction},
                {
                    "type": "image_url",
                    "image_url": {
                        #"url": "https://i-blog.csdnimg.cn/blog_migrate/d5be9ece4b4e0fbe06c4b2dba28d68f7.png"
                        "url": f"data:image/jpeg;base64,{base64_image}"
                    }
                }
            ]
        }
    ],
    max_tokens=2000  # 设置最大输出长度
)

# 打印响应内容
print(response.choices[0].message.content)