from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_mistralai import ChatMistralAI
from tavily import TavilyClient


tavily = TavilyClient()


@tool
def search(query:str) -> str:
    """
    Tool that searches the internet
    Args:
        query : The query to search for
    Returns:
        The search result
    """
    print(f"Searching for {query}")
    return tavily.search(query=query)

llm=ChatMistralAI()
tools = [search]
agent=create_agent(model=llm,tools=tools)

def main():
    print("Hello from lanchain-course-agent!")
    result=agent.invoke({"messages":HumanMessage(content="search for 3 job postings for an ai engineer using langchain in Lyon area in France on linkedin and list their details")})
    print(result)


if __name__ == "__main__":
    main()
