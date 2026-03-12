

# from langchain_ollama import ChatOllama,OllamaEmbeddings
import streamlit as st
from dotenv import load_dotenv
from langchain_community.embeddings import JinaEmbeddings
import os
# from langchain.chat_models import init_chat_model
from langchain_mistralai import ChatMistralAI
load_dotenv()



@st.cache_resource
def load_model():
    model = ChatMistralAI(
    model="mistral-small-2506",
)
    return model

@st.cache_resource
def load_embeddings():
    embeddings = JinaEmbeddings(
    jina_api_key=os.environ.get("JINA_API_KEY"), model_name="jina-embeddings-v5-text-nano"
)
    return embeddings

