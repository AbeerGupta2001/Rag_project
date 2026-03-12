

from langchain.agents import create_agent
from langchain.tools import tool
from langchain.messages import HumanMessage
from components.load_models import load_model
from components.qdrant_vector import vector_store


model = load_model()

@tool(response_format="content_and_artifact")
def retrieval(query:str):
    """Retrieve information to help answer a query."""
    retrieved_docs = vector_store.similarity_search(query, k=2)
    serialized = "\n\n".join(
        (f"Source: {doc.metadata}\nContent: {doc.page_content}")
        for doc in retrieved_docs
    )
    return serialized, retrieved_docs

agent = create_agent(
    model = model,
    tools = [retrieval],
    system_prompt="""
        You are a helpful assistant who can use tool to retrieve context and help answer user queries
"""
)


def ask_question(query:str):
    response = agent.invoke(
        {
            "messages":[HumanMessage(query)]
        }
    )
    return response["messages"]

