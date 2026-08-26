from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv



load_dotenv()



embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

text_1 = "Machine learning engineer"
text_2 = "Artificial intelligence engineer"

embedding_1 = embedding_model.embed_query(text_1)
embedding_2 = embedding_model.embed_query(text_2)

similarity = sum(
    a * b for a, b in zip(embedding_1, embedding_2)
)

print("Similarity:", similarity)