from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

llm = ChatOpenAI(
    model="gpt-4o-mini"
)

documents = [
    "The candidate has strong experience with Python and machine learning.",
    "The candidate built a RAG-based AI assistant using embeddings and vector search.",
    "The candidate developed REST APIs using FastAPI.",
    "The candidate has experience with React frontend development."
]

vector_store = Chroma.from_texts(
    texts=documents,
    embedding=embedding_model
)

query = "Does the candidate have experience with retrieval systems?"

retrieved_documents = vector_store.similarity_search(
    query,
    k=2
)

context = "\n".join(
    document.page_content
    for document in retrieved_documents
)

prompt = ChatPromptTemplate.from_template(
    """
Answer the question using only the provided context.

Context:
{context}

Question:
{question}
"""
)

messages = prompt.format_messages(
    context=context,
    question=query
)

response = llm.invoke(messages)

print(response.content)