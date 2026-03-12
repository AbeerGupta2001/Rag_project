

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_split(path:str):
    loader = PyPDFLoader(path)
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200,add_start_index=True,)

    allsplits = text_splitter.split_documents(docs)
    return allsplits