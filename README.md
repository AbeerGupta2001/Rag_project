

# RAG AI Assistant

**A Retrieval-Augmented Generation (RAG)** application that allows users to query documents using an AI model.
The system retrieves relevant document chunks from a vector database and feeds them to an LLM to generate accurate responses.

The project is fully containerized using Docker Compose, making it easy to run the entire stack with a single command.

Features

- Document ingestion and chunking

- Vector embeddings generation
 
- Semantic search using a vector database
 
- LLM-powered answer generation
 
- Streamlit web interface
 
- Fully containerized environment
 
- One-command startup with Docker Compose



## Docker command
```
docker compose up --build
```



## Pull from docker hub
```
docker pull noobastro/rag_project
```