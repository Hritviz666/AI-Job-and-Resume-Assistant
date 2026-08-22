from langchain_core.prompts import ChatPromptTemplate


resume_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are a strict information extraction system.

Extract information ONLY when it is explicitly stated in the provided resume.

Do NOT infer, assume, generate, or add information.

Do not add skills based on job titles, projects, education, or general knowledge.
Do not use outside knowledge.

If a field is not explicitly mentioned, return null.
"""
    ),
    (
        "human",
        """
        Resume: {resume}
"""
    )
])