from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv

load_dotenv()

class JobState(TypedDict):
    matched_skills: list[str]
    message: str


def match_skills(state: JobState):
    return {
        "matched_skills": ["Python", "SQL"]
    }


def good_match(state: JobState):
    return {
        "message": "Candidate has a good skill match."
    }


def weak_match(state: JobState):
    return {
        "message": "Candidate needs more skill development."
    }


def decide_match(state: JobState):
    if len(state["matched_skills"]) >= 2:
        return "good_match"

    return "weak_match"


builder = StateGraph(JobState)

builder.add_node("match_skills", match_skills)
builder.add_node("good_match", good_match)
builder.add_node("weak_match", weak_match)

builder.add_edge(START, "match_skills")

builder.add_conditional_edges(
    "match_skills",
    decide_match,
    {
        "good_match": "good_match",
        "weak_match": "weak_match"
    }
)

builder.add_edge("good_match", END)
builder.add_edge("weak_match", END)

graph = builder.compile()

result = graph.invoke({
    "matched_skills": [],
    "message": ""
})

print(result)