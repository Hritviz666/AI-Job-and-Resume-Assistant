from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import ToolMessage
from dotenv import load_dotenv

load_dotenv()

@tool
def calculate_skill_match(required: int, matched: int) -> float:
    """Calculate the percentage of required skills matched."""
    return (matched / required) * 100


llm = ChatOpenAI(model="gpt-4o-mini")

llm_with_tools = llm.bind_tools(
    [calculate_skill_match]
)


messages = [
    {
        "role": "user",
        "content": "I have 7 matched skills out of 10 required skills."
    }
]


# 1. Ask the LLM
ai_message = llm_with_tools.invoke(messages)

print(ai_message.tool_calls)


# 2. Execute requested tools
tool_messages = []

for tool_call in ai_message.tool_calls:

    if tool_call["name"] == "calculate_skill_match":

        result = calculate_skill_match.invoke(
            tool_call["args"]
        )

        tool_messages.append(
            ToolMessage(
                content=str(result),
                tool_call_id=tool_call["id"]
            )
        )


# 3. Give tool result back to LLM
messages = messages + [ai_message] + tool_messages

final_response = llm.invoke(messages)

print(final_response.content)