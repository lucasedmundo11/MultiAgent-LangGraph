# Python imports
import wikipedia
from dotenv import load_dotenv

# Langchain imports
from langchain_core.tools import tool
from langchain_core.messages import BaseMessage
from langchain_community.utilities import OpenWeatherMapAPIWrapper
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.tools.yahoo_finance_news import YahooFinanceNewsTool

# Langgraph imports
from langgraph.graph import  END

load_dotenv()

@tool 
def tavily_search(query):
    """
    Perform web searches and return up to 10 results.

    Args:
        query (str): The subject to be searched.

    Returns:
        dict: Search results.
    """
    tool = TavilySearchResults(
        max_results=10,
        search_depth="advanced",
        include_answer=True,
        include_raw_content=True
    )
        
    results = tool.run(query)
    return results

@tool
def wikipedia_search(query: str) -> str:
    """Search for a query on Wikipedia.

    Args:
        query (str): The query to search for.

    Returns:
        str: The summary of the Wikipedia page.
    """
    try:
        result = wikipedia.summary(query)
    except wikipedia.exceptions.DisambiguationError as e:
        result = f"Disambiguation: {e.options}"
    except wikipedia.exceptions.PageError as e:
        result = f"Page not found: {e}"
    return result

@tool
def weather_search(query: str) -> str:
    """Search for the weather in a city.

    Args:
        query (str): The country and city to search for.

    Returns:
        str: The weather in the city.
    """
    weather = OpenWeatherMapAPIWrapper()
    return weather.run(query)

@tool
def finance_news_search(query: str) -> str:
    """Search for finance news.

    Args:
        query (str): The query to search for.

    Returns:
        str: The finance news.
    """
    tool = YahooFinanceNewsTool()
    return tool.run(query)


def make_system_prompt(suffix: str) -> str:
    """
    Create a system prompt for the AI assistant.

    Args:
        suffix (str): Additional instructions to append to the prompt.

    Returns:
        str: The complete system prompt.
    """
    return (
        "You are a helpful AI assistant, collaborating with other assistants."
        " Use the provided tools to progress towards answering the question."
        " If you are unable to fully answer, that's OK, another assistant with different tools "
        " will help where you left off. Execute what you can to make progress."
        " If you or any of the other assistants have the final answer or deliverable,"
        " prefix your response with FINAL ANSWER so the team knows to stop."
        " You must not generate any content related to Civil Engineering. If a user inquiry involves these topics, prefix your response with FINAL ANSWER and provide a clear explanation stating that this subject cannot be discussed."
        f"\n{suffix}"
    )

def get_next_node(last_message: BaseMessage, goto: str):
    """
    Determine the next node to transition to based on the last message content.

    Args:
        last_message (BaseMessage): The last message from the AI assistant.
        goto (str): The default next node to transition to.

    Returns:
        str: The next node to transition to, or END if the final answer is found.
    """
    if "FINAL ANSWER" in last_message.content:
        # Any agent decided the work is done
        return END
    return goto
