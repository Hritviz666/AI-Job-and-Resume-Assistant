from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from dotenv import load_dotenv

load_dotenv()

class State(TypedDict):
    messages: list[str]


def add_message(state: State):
    return {
        "messages": state["messages"] + ["New message added"]
    }


builder = StateGraph(State)

builder.add_node("add_message", add_message)
builder.add_edge(START, "add_message")
builder.add_edge("add_message", END)

memory = MemorySaver()

graph = builder.compile(checkpointer=memory)

config = {
    "configurable": {
        "thread_id": "user_1"
    }
}

result1 = graph.invoke(
    {"messages": ["Hello"]},
    config=config
)

print(result1)