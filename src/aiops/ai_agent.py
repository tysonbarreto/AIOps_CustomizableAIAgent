from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch

from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

from aiops.config import GroqConfig,Settings

from typing import List

def get_response_from_ai_agents(llm_id:str, query:List[str], allow_search:bool, system_prompt:str):
    settings = Settings()
    llm = GroqConfig.groq_client(model=llm_id)

    tools = [TavilySearch(max_results=2,tavily_api_key=settings.tavily_api_key)] if allow_search else []

    agent = create_react_agent(
        model=llm,
        tools=tools,
        prompt=system_prompt + "\n Please always ensure the response is in markdown format"
    )

    state = {"messages" : query}

    response = agent.invoke(state)

    messages = response.get("messages")

    ai_messages = [message.content for message in messages if isinstance(message,AIMessage)]
    
    return ai_messages[-1]

if __name__=="__main__":
    #get_response_from_ai_agents(llm_id='openai/gpt-oss-20b', query='Give the weather forecast for today?', allow_search=True, system_prompt='You are a professional weather forecaster')
    __all__=["get_response_from_ai_agents"]




