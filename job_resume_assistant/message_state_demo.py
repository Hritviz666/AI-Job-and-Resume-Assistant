from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from dotenv import load_dotenv

load_dotenv()


class JobState(TypedDict):
    messages: Annotated[list, add_messages]


def first_node(state: JobState):
    return {
        "messages": [
            {
                "role": "assistant",
                "content": "Job analysis completed."
            }
        ]
    }


def second_node(state: JobState):
    return {
        "messages": [
            {
                "role": "assistant",
                "content": "Resume analysis completed."
            }
        ]
    }


builder = StateGraph(JobState)

builder.add_node("first_node", first_node)
builder.add_node("second_node", second_node)

builder.add_edge(START, "first_node")
builder.add_edge("first_node", "second_node")
builder.add_edge("second_node", END)

graph = builder.compile()

result = graph.invoke({
    "messages": [
        {
            "role": "user",
            "content": "Analyze this job and resume."
        }
    ]
})

for message in result["messages"]:
    print(message)