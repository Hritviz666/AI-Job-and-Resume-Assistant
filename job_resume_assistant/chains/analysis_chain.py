from langchain_core.runnables import RunnableParallel

from chains.job_chain import job_chain
from chains.resume_chain import resume_chain


analysis_chain = RunnableParallel(
    job=job_chain,
    resume=resume_chain
)