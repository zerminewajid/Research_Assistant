from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document

SAMPLE_DOCS = [
    "Artificial intelligence (AI) is the simulation of human intelligence in machines. AI encompasses machine learning, deep learning, natural language processing, and computer vision.",
    "Machine learning enables systems to learn from experience without being explicitly programmed. Key algorithms include linear regression, decision trees, SVMs, and neural networks.",
    "Deep learning uses neural networks with many layers. Transformers, CNNs, RNNs, LSTMs and GRUs are popular architectures used in vision and language tasks.",
    "Natural language processing (NLP) enables machines to understand human language. Tasks include sentiment analysis, NER, machine translation, summarization, and question answering.",
    "Large language models like GPT, BERT, and LLaMA use the transformer architecture with self-attention mechanisms to generate and understand text.",
    "Retrieval Augmented Generation (RAG) combines a retrieval system with a generative model. Documents are embedded into a vector store, and relevant chunks are retrieved to ground LLM responses.",
    "Computer vision involves teaching machines to interpret images. Key tasks include image classification, object detection, semantic segmentation, and image generation.",
    "Reinforcement learning trains agents through reward signals. Used in robotics, games, and optimization problems.",
    "Federated learning enables training models across decentralized devices without sharing raw data. Useful in healthcare and finance where privacy is critical.",
    "MLOps is the practice of deploying, monitoring, and maintaining ML models in production using tools like MLflow, Docker, Prefect, and CI/CD pipelines.",
    "Transformers use self-attention to process sequences in parallel. The architecture includes multi-head attention, positional encodings, feed-forward layers, and layer normalization.",
    "Vector databases like FAISS, Pinecone, and Chroma store high-dimensional embeddings and enable fast similarity search using cosine or dot-product metrics.",
    "The attention mechanism allows neural networks to focus on relevant parts of the input. Self-attention computes query, key, and value matrices to weigh token importance.",
    "LSTM (Long Short-Term Memory) networks use gates to control information flow: input gate, forget gate, and output gate solve the vanishing gradient problem in RNNs.",
    "Generative AI includes models that create text, images, audio, and video. Examples include GPT-4, DALL-E, Stable Diffusion, and Sora.",
]

class VectorStore:
    def __init__(self):
        print("[VectorStore] Loading embeddings model...")
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2", model_kwargs={"device": "cpu"})
        docs = [Document(page_content=t) for t in SAMPLE_DOCS]
        self.store = FAISS.from_documents(docs, self.embeddings)
        print("[VectorStore] Ready.")

    def add_texts(self, texts):
        self.store.add_documents([Document(page_content=t) for t in texts])

    def search(self, query, k=4):
        results = self.store.similarity_search(query, k=k)
        return "\n\n---\n\n".join([r.page_content for r in results])
