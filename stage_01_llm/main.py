from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from pydantic import BaseModel, Field

load_dotenv()

parser = StrOutputParser()

llm = ChatOpenAI(
    model_name="gpt-4o-mini"
)

# Define the structure we want from the LLM
class JobAnalysis(BaseModel):
    required_skills: list[str] = Field(
        description="Skills required for the job"
    )

    preferred_skills: list[str] = Field(
        description="Skills preferred but not mandatory"
    )

    experience_level: str = Field(
        description="Required experience level"
    )

# Create a structured-output version of the LLM
structured_llm = llm.with_structured_output(JobAnalysis)

prompt = ChatPromptTemplate.from_messages([
   (
        "system",
        """You are an AI Job Assistant.

        Analyze the given job description and extract the required information.
        """
    ),
    (
        "human",
        "{job_description}"
    )
])

# Compose the LCEL chain
chain = prompt | structured_llm

# Get job description from the user
job_description = input("Paste the job description: ")

# Execute the complete pipeline
response = chain.invoke({
    "job_description": job_description
})

# Access structured data
print("\nRequired Skills:")
print(response.required_skills)

print("\nPreferred Skills:")
print(response.preferred_skills)

print("\nExperience Level:")
print(response.experience_level)