
# Python imports
from typing import Literal
from dotenv import load_dotenv

# Langchain imports
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# Langgraph imports
from langgraph.types import Command
from langgraph.prebuilt import create_react_agent
from langgraph.graph import MessagesState, END

# App imports
from agents.utils import *

load_dotenv()

# Research agent and node
research_agent = create_react_agent(
    ChatOpenAI(model="gpt-4o-mini", temperature=0),
    tools=[tavily_search, wikipedia_search, weather_search, finance_news_search],
    prompt=make_system_prompt(
        "You can only do research and nothing else. You are working with a writer colleague."
    ),
)

def research_node(state: MessagesState) -> Command[Literal["writer", END]]:
    """
    Node function for the research agent in the workflow.
    It processes the current state and determines the next node to transition to.
    """
    result = research_agent.invoke(state)
    goto = get_next_node(result["messages"][-1], "writer")
    # wrap in a human message, as not all providers allow
    # AI message at the last position of the input messages list
    result["messages"][-1] = HumanMessage(
        content=result["messages"][-1].content, name="researcher"
    )
    return Command(
        update={
            # share internal message history of research agent with other agents
            "messages": result["messages"],
        },
        goto=goto,
    )

