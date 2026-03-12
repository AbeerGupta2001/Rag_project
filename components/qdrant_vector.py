


from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams,Distance
from components.load_models import load_embeddings

def get_client():
    return QdrantClient(host="qdrant",port=6333)

client = get_client()

embeddings = load_embeddings()

vector_size = len(embeddings.embed_query("sample_text"))

if not client.collection_exists("test"):
    client.create_collection(collection_name="test",vectors_config=VectorParams(size=vector_size,distance=Distance.COSINE))

vector_store = QdrantVectorStore(
    client=client,
    collection_name="test",
    embedding=embeddings
)