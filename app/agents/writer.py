
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

writer_agent = create_react_agent(
    ChatOpenAI(model="gpt-4o-mini", temperature=0),
    [],
    prompt=make_system_prompt(
        "You can only generate well-structured and coherent written content. You are collaborating with a researcher colleague. You must not generate any content related to Civil Engineering."
    ),
)

def writer_node(state: MessagesState) -> Command[Literal["researcher", END]]:
    """
    Node function for the writer agent in the workflow.
    It processes the current state and determines the next node to transition to.
    """
    
    result = writer_agent.invoke(state)
    goto = get_next_node(result["messages"][-1], "researcher")
    # wrap in a human message, as not all providers allow
    # AI message at the last position of the input messages list
    result["messages"][-1] = HumanMessage(
        content=result["messages"][-1].content, name="writer"
    )
    return Command(
        update={
            # share internal message history of writer agent with other agents
            "messages": result["messages"],
        },
        goto=goto,
    )