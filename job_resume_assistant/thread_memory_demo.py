from typing import Annotated, TypedDict

from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver


class State(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


def conversation_node(state: State):
    return {
        "messages": []
    }


builder = StateGraph(State)

builder.add_node("conversation", conversation_node)
builder.add_edge(START, "conversation")
builder.add_edge("conversation", END)

memory = MemorySaver()
graph = builder.compile(checkpointer=memory)

config = {
    "configurable": {
        "thread_id": "user-1"
    }
}

graph.invoke(
    {
        "messages": [
            HumanMessage(content="I prefer AI Engineer roles.")
        ]
    },
    config
)

graph.invoke(
    {
        "messages": [
            HumanMessage(content="Find suitable jobs for me.")
        ]
    },
    config
)

state = graph.get_state(config)

for message in state.values["messages"]:
    print(message.content)