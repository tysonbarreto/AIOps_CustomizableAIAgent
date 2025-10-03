import streamlit as st
import requests
import os,sys

from aiops.config import GroqConfig, CONFIGURED_MODELS
from aiops.logger import get_logger
from aiops.exception import AIException

logger = get_logger(__name__)

st.set_page_config(page_title="Customizable AI Agents", layout="centered")
st.title("Customizable AI Agent")    

system_prompt = st.text_area("Define your AI Agent", height=70)
selected_model = st.selectbox("Select your LLM: ", CONFIGURED_MODELS)

allow_web_search = st.checkbox("Allow web search")

user_query = st.text_area("Enter your promt:" , height=150)

API_URL = "http://127.0.0.1:9999/chat"

with st.sidebar:
    os.environ['GROQ_API_KEY'] = st.text_input(label='GROQ_API_KEY', key='GROQ_API_KEY')
    os.environ['TAVILY_API_KEY'] = st.text_input(label='TAVILY_API_KEY', key='TAVILY_API_KEY')

if st.button("Ask Agent") and user_query.strip():
    
    payload = {
        "model_name" : selected_model,
        "system_prompt" : system_prompt,
        "messages" : [user_query],
        "allow_search" : allow_web_search
    }
    
    
    try:
        logger.info("Sending request to know")
        response = requests.post(API_URL, json=payload)
        
        if response.status_code==200:
            agent_response = response.json().get("response","")
            logger.info("Sucesfully recived response from backend")

            st.subheader("Agent Response")
            st.markdown(agent_response, unsafe_allow_html=True)
        else:
            logger.error("Backend error")
            st.error("Error with backend")
    except Exception as e:
        logger.error("Backend error")
        st.error(str(AIException("Backend error",error_detail=e)))