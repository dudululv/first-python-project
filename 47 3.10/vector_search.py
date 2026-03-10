# pip install elasticsearch==8.17.0 
from elasticsearch import Elasticsearch 
from openai import OpenAI 
import os
from pathlib import Path
from dotenv import load_dotenv
# 1. 定位 .env 文件
dotenv_path = Path(r"C:\Users\123\Desktop\first-python-project\.env")

# 2. 手动解析并加载（如果 load_dotenv 失效，这是最稳的办法）
if dotenv_path.exists():
    with open(dotenv_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                key, value = line.split("=", 1)
                os.environ[key] = value
    print("✅ 手动加载 .env 成功")
else:
    print("❌ 错误：在指定路径未找到 .env 文件")
load_dotenv()
# 3. 再次验证
print(f"检查 Key: {os.getenv('DASHSCOPE_API_KEY')}")

# --- 此时再初始化 OpenAI ---
from openai import OpenAI
embed_client = OpenAI(
    base_url=os.getenv("DASHSCOPE_BASE_URL"),
    api_key=os.getenv("DASHSCOPE_API_KEY")
)

# 获取并清理变量
raw_base_url = os.getenv("DASHSCOPE_BASE_URL")
# 去掉可能存在的引号和空格
clean_base_url = raw_base_url.strip().strip('"').strip("'") if raw_base_url else None
print(f"DEBUG: 正在使用的 URL 是 -> {clean_base_url}")

# 初始化客户端
embed_client = OpenAI(
    base_url=clean_base_url,
    api_key=os.getenv("DASHSCOPE_API_KEY").strip().strip('"')
)

es_client = Elasticsearch("http://localhost:9200")
index_name = "my_documents3"
query = "what is Elasticsearch?"


embedding_response = embed_client.embeddings.create(
    model="text-embedding-v4",
    input=[query],
    dimensions=1024
)

query_embedding = embedding_response.data[0].embedding

# 向量查询
response = es_client.search(
    index=index_name,
    query={
        "knn": {
            "field": "content_embedding",
            "query_vector": query_embedding,
            "k": 1,
            "num_candidates": 100
        }
    }
)
for hit in response['hits']['hits']:
    print(f"Score: {hit['_score']}, Title: {hit['_source']['content']}")