from langchain_core.prompts import ChatPromptTemplate


job_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are an information extraction system.

Extract information ONLY when it is explicitly stated in the provided
job description.

Do NOT infer, assume, generate, or add typical requirements based on
the job title or your general knowledge.

For example, if the input only says "GenAI Engineer", do NOT assume
skills such as Python, Machine Learning, LangChain, or PyTorch.

Rules:
- Only extract information directly supported by the job description.
- Do not infer requirements from the job title.
- Do not add common industry requirements.
- Do not use outside knowledge.
- If a field is not explicitly mentioned, return null.
"""
    ),
    (
        "human",
        "{job_description}"
    )
])