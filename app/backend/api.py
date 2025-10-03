from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

from aiops.ai_agent import get_response_from_ai_agents
from aiops.logger import get_logger
from aiops.exception import AIException
from aiops.config import CONFIGURED_MODELS

logger = get_logger(__name__)
app = FastAPI(title="Customize your AI Agent")

class RequestState(BaseModel):
    model_name:str
    system_prompt:str
    messages:List[str]
    allow_search:bool
    
@app.post("/chat")
def chat_endpoint(request:RequestState):
    logger.info(f"Received request for model: {request.model_name}")
    
    if request.model_name not in CONFIGURED_MODELS:
        logger.warning("Invalid model name")
        raise HTTPException(status_code=400, detail="Invalid model name")
    
    try:
        response = get_response_from_ai_agents(
            request.model_name,
            request.messages,
            request.allow_search,
            request.system_prompt
        )
        logger.info(f"Sucesfully got response from AI Agent {request.model_name}")
        return {"response" : response}
    except Exception as e:
        HTTPException(
                    status_code=500 , 
                    detail=str(AIException("Failed to get AI response" , error_detail=e))
                    )