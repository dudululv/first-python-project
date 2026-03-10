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

es_client = Elasticsearch("http://localhost:9200")

# 如果索引不存在，则创建索引
mappings = {
    "properties": {
        "title": {"type": "text"},
        "content": {"type": "text"},
        "content_embedding": {
            "type": "dense_vector",
            "dims": 1024
        }
    }
}

if not es_client.indices.exists(index="my_documents"):
    es_client.indices.create(index="my_documents", mappings=mappings)

docs = [
    {
        "title": "An introduction to Elasticsearch", 
        "content": "Elasticsearch is a distributed, RESTful search and analytics engine."
    }, 
    {
        "title": "An introduction to Kibana", 
        "content": "Kibana is a browser-based analytics and visualization platform."
    }
]

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

embedding_response = embed_client.embeddings.create(
    model="text-embedding-v4",
    input=[doc['content'] for doc in docs],
    dimensions=1024
)

embeddings = [embedding.embedding for embedding in embedding_response.data]

# 写入索引
for doc, embedding in zip(docs, embeddings):
    es_client.index(
        index="my_documents",
        document={
            "title": doc['title'],
            "content": doc['content'],
            "content_embedding": embedding
        }
    )