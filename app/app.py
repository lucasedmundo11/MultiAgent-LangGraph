# Python imports
from dotenv import load_dotenv

#flask imports
from flask import Flask, request, jsonify

# Langgraph imports
from langgraph.graph import MessagesState, StateGraph, START

# App imports
from agents.utils import *
from agents.researcher import *
from agents.writer import *
from middleware.logging import *

# Setup logging
setup_logging()

# Load environment variables
load_dotenv()

# Create the Flask app
app = Flask(__name__)

# Define the API endpoint
@app.route("/api", methods=["POST"])
def api():
    """
    API endpoint to process POST requests with JSON payload.
    It creates a workflow using StateGraph and invokes it with the provided message.
    Returns a JSON response with the original message and the final answer.
    """
    logger = logging.getLogger(__name__)

    # Get the data from the request
    data = request.get_json()
    logger.debug(f"Received data: {data}")

    # Create the workflow
    workflow = StateGraph(MessagesState)
    workflow.add_node("researcher", research_node)
    workflow.add_node("writer", writer_node)

    workflow.add_edge(START, "writer")
    graph = workflow.compile()

    response = graph.invoke(
        {
            "messages": [
                (
                    "user",
                    f"{data['message']}",
                )
            ],
        },
        {"recursion_limit": 150},
    )
    logger.debug(f"Response: {response}")

    return jsonify({"message": data["message"], "response": response.get("messages")[-1].content.split("FINAL ANSWER: ")[-1]})

# Run the app
if __name__ == "__main__":
    app.run(debug=True, port=5001, host="0.0.0.0")
