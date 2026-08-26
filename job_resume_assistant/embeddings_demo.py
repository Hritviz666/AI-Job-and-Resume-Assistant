from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv



load_dotenv()



embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

text = "I build machine learning applications."

embedding = embedding_model.embed_query(text)

print(embedding[:10])
print("Dimensions:", len(embedding))