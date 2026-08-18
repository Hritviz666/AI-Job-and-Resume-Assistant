from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatOpenAI(
    model_name="gpt-4o-mini"
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an AI Job Assistant."),
    ("human", "{question}")
])

chain = prompt | llm

question = input("Ask about job: ")

response = chain.invoke({
    "question" : question
})

print(response.content)