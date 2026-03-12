

import streamlit as st
import os

from components.load_and_split import load_split
from components.qdrant_vector import vector_store
from components.rag_agent import ask_question


os.makedirs("uploads",exist_ok=True)

@st.cache_data
def load_data(path):
    allsplits = load_split(path)
    vector_store.add_documents(documents=allsplits)

st.write("# Rag agent")

uploaded_file = st.file_uploader("Upload pdf",type="pdf")

if uploaded_file:
    filename = uploaded_file.name
    path = os.path.join("uploads",filename)

    with open(path,"wb") as f:
        f.write(uploaded_file.getvalue())
    
    load_data(path)

query = st.text_input("Query",placeholder="Ask question based on uploaded pdf")

if query:
    with st.spinner("Processing...",show_time=True):
        response = ask_question(query)
        st.write("### Query Asked:")
        st.markdown(f"<p style='font-size:20px;'>{query}</p>", unsafe_allow_html=True)
        st.write("### Agent Response:")
        st.markdown(f"<p style='font-size:20px;'>{response[-1].content}</p>", unsafe_allow_html=True)


    


