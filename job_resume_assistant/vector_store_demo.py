from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

documents = [
    "Skills: Python, machine learning, PyTorch",
    "Built a RAG-based AI assistant using vector search",
    "Developed REST APIs with FastAPI",
    "Created frontend applications using React"
]

vector_store = Chroma.from_texts(
    texts=documents,
    embedding=embedding_model
)

query = "Looking for a candidate with experience building retrieval systems using LLMs"

results = vector_store.similarity_search(
    query,
    k=2
)

for result in results:
    print(result.page_content)