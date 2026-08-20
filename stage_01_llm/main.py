from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field


load_dotenv()


llm = ChatOpenAI(
    model="gpt-4o-mini"
)


class JobAnalysis(BaseModel):
    job_title: str = Field(
        description="Job title or role being offered"
    )

    required_skills: list[str] = Field(
        description="Technical and professional skills explicitly required"
    )

    preferred_skills: list[str] = Field(
        description="Skills that are preferred but not mandatory"
    )

    responsibilities: list[str] = Field(
        description="Main responsibilities of the role"
    )

    experience_level: str = Field(
        description="Required years or level of experience"
    )

    education: str = Field(
        description="Required or preferred educational qualification"
    )


structured_llm = llm.with_structured_output(JobAnalysis)


prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are an AI Job Assistant.

        Analyze the given job description and extract the relevant
        information into the required structured format.

        Rules:
        - Put explicitly required skills in required_skills.
        - Put only preferred skills in preferred_skills.
        - Do not invent requirements.
        - Keep extracted information concise.

        """
    ),
    (
        "human",
        "{job_description}"
    )
])


chain = prompt | structured_llm


job_description = input(
    "Paste the job description:\n"
)


response = chain.invoke({
    "job_description": job_description
})


print("\n--- JOB ANALYSIS ---")

print("\nJob Title:")
print(response.job_title)

print("\nRequired Skills:")
print(response.required_skills)

print("\nPreferred Skills:")
print(response.preferred_skills)

print("\nResponsibilities:")
print(response.responsibilities)

print("\nExperience:")
print(response.experience_level)

print("\nEducation:")
print(response.education)