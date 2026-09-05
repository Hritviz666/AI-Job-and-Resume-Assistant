from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv

load_dotenv()

class JobState(TypedDict):
    job_description: str
    required_skills: list[str]
    skill_count: int


def extract_skills(state: JobState):
    skills = ["Python", "SQL", "LangChain"]

    return {
        "required_skills": skills
    }


def count_skills(state: JobState):
    count = len(state["required_skills"])

    return {
        "skill_count": count
    }


builder = StateGraph(JobState)

builder.add_node("extract_skills", extract_skills)
builder.add_node("count_skills", count_skills)

builder.add_edge(START, "extract_skills")
builder.add_edge("extract_skills", "count_skills")
builder.add_edge("count_skills", END)

graph = builder.compile()

result = graph.invoke({
    "job_description": "Looking for an AI Engineer with Python, SQL and LangChain.",
    "required_skills": [],
    "skill_count": 0
})

print(result)