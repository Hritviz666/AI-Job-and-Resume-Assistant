from typing import TypedDict

from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv

load_dotenv()

class State(TypedDict):
    user_request: str
    plan: list[str]


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


def planner_node(state: State):
    prompt = f"""
Create a short execution plan for this task:

{state["user_request"]}

Return exactly five numbered steps.
"""

    response = llm.invoke(prompt)

    steps = [
        line.strip()
        for line in response.content.split("\n")
        if line.strip()
    ]

    return {"plan": steps}


def executor_node(state: State):
    print("Execution plan:")

    for index, step in enumerate(state["plan"], start=1):
        print(f"{index}. {step}")

    return state


builder = StateGraph(State)

builder.add_node("planner", planner_node)
builder.add_node("executor", executor_node)

builder.add_edge(START, "planner")
builder.add_edge("planner", "executor")
builder.add_edge("executor", END)

graph = builder.compile()


result = graph.invoke({
    "user_request": (
        "Analyze my resume against a Python AI Engineer "
        "job description and generate recommendations."
    ),
    "plan": []
})

print(result["plan"])