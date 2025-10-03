from pydantic_settings import BaseSettings
from langchain_groq.chat_models import ChatGroq
from typing import Literal


class Settings(BaseSettings):
    groq_api_key:str
    tavily_api_key:str
    
    class Config:
        env_file='.env'

        
class GroqConfig:
    """
    Specify model to instantiate GroqClient
    ---
    Args:
        model: * "openai/gpt-oss-20b"
               * "llama-3.1-8b-instant"
    Returns:
        GroqClient
    """
    
    @classmethod
    def groq_client(cls, model:Literal["openai/gpt-oss-20b","llama-3.1-8b-instant"])->ChatGroq:
        settings = Settings()
        
        return ChatGroq(
            api_key=settings.groq_api_key,
            model=model,
            max_retries=2
        )

CONFIGURED_MODELS = ["openai/gpt-oss-20b","llama-3.1-8b-instant"]
        
if __name__=="__main__":
    __all__=["GroqConfig","CONFIGURED_MODELS"]