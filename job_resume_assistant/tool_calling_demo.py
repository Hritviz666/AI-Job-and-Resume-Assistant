from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

@tool
def calculate_skill_match(required: int, matched: int) -> float:
    """Calculate the percentage of required skills matched."""
    return (matched / required) * 100


llm = ChatOpenAI(
    model="gpt-4o-mini"
)

llm_with_tools = llm.bind_tools(
    [calculate_skill_match]
)

response = llm_with_tools.invoke(
    "I have 8 required skills and 6 matched skills. Calculate my skill match percentage."
)

print("Tool calls:")
print(response.tool_calls)