from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv

load_dotenv()

class JobState(TypedDict):
    job_title: str
    message: str


def analyze_job(state: JobState):
    return {
        "message": f"Analyzing job: {state['job_title']}"
    }


def generate_result(state: JobState):
    return {
        "message": state["message"] + " → Analysis complete"
    }


builder = StateGraph(JobState)

builder.add_node("analyze_job", analyze_job)
builder.add_node("generate_result", generate_result)

builder.add_edge(START, "analyze_job")
builder.add_edge("analyze_job", "generate_result")
builder.add_edge("generate_result", END)

graph = builder.compile()


result = graph.invoke({
    "job_title": "AI Engineer",
    "message": ""
})

print(result)