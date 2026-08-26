from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import math


load_dotenv()



def cosine_similarity(vector_1, vector_2):
    dot_product = sum(
        a * b for a, b in zip(vector_1, vector_2)
    )

    magnitude_1 = math.sqrt(
        sum(a * a for a in vector_1)
    )

    magnitude_2 = math.sqrt(
        sum(b * b for b in vector_2)
    )

    return dot_product / (magnitude_1 * magnitude_2)


embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

documents = [
    "Experienced in Python and machine learning",
    "Built REST APIs using FastAPI",
    "Worked with vector databases and RAG",
    "Strong knowledge of React development"
]

query = "Experience with building retrieval augmented generation applications"
document_embeddings = embedding_model.embed_documents(documents)

query_embedding = embedding_model.embed_query(query)

results = []

for document, document_embedding in zip(
    documents,
    document_embeddings
):
    similarity = cosine_similarity(
        query_embedding,
        document_embedding
    )

    results.append(
        {
            "document": document,
            "similarity": similarity
        }
    )


results.sort(
    key=lambda result: result["similarity"],
    reverse=True
)

top_k = 2

for result in results[:top_k]:
    print(
        result["similarity"],
        "-",
        result["document"]
    )