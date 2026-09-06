from typing import TypedDict

from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage

from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from dotenv import load_dotenv

load_dotenv()

class JobState(TypedDict):
    messages: list


@tool
def calculate_skill_match(required: int, matched: int) -> float:
    """Calculate the percentage of required skills matched."""
    return (matched / required) * 100


llm = ChatOpenAI(model="gpt-4o-mini")

tools = [calculate_skill_match]

llm_with_tools = llm.bind_tools(tools)


def call_llm(state: JobState):
    response = llm_with_tools.invoke(
        state["messages"]
    )

    return {
        "messages": state["messages"] + [response]
    }


tool_node = ToolNode(tools)


def decide_next(state: JobState):

    last_message = state["messages"][-1]

    if last_message.tool_calls:
        return "tools"

    return "end"


builder = StateGraph(JobState)

builder.add_node("llm", call_llm)
builder.add_node("tools", tool_node)

builder.add_edge(START, "llm")

builder.add_conditional_edges(
    "llm",
    decide_next,
    {
        "tools": "tools",
        "end": END
    }
)

builder.add_edge("tools", "llm")

graph = builder.compile()


result = graph.invoke({
    "messages": [
        HumanMessage(
            content="I matched 7 out of 10 required skills. Calculate my match percentage."
        )
    ]
})

print(result["messages"][-1].content)