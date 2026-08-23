from prompts.resume_prompt import resume_prompt
from schemas.resume import ResumeAnalysis

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini"
)

structured_llm = llm.with_structured_output(ResumeAnalysis)

resume_chain = resume_prompt | structured_llm