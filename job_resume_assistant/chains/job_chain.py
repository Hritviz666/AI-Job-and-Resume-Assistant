from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from schemas.job import JobAnalysis
from prompts.job_prompt import job_prompt


load_dotenv()


llm = ChatOpenAI(
    model="gpt-4o-mini"
)


structured_llm = llm.with_structured_output(JobAnalysis)


job_chain = job_prompt | structured_llm