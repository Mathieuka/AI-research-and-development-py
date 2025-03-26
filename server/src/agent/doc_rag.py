from mcp.server.fastmcp import FastMCP
import logging
from langchain_openai import OpenAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import Optional
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

mcp = FastMCP("doc_rag")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True,
)

logger = logging.getLogger("cv_rag_server")

# Initialize RAG components
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
vector_store = InMemoryVectorStore(embeddings)


def initialize_vector_store(pdf_name: str = "cv.pdf"):
    # Get the current file's directory
    current_dir = Path(__file__).parent.resolve()
    private_dir = current_dir / "private"
    pdf_path = private_dir / pdf_name
    logger.info(f"Loading PDF from: {pdf_path}")

    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found at: {pdf_path}")

    loader = PyPDFLoader(pdf_path)
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    all_splits = text_splitter.split_documents(docs)
    vector_store.add_documents(documents=all_splits)


@mcp.tool()
def search_cv(question: str, k: Optional[int] = 3) -> str:
    """
    Search relevant content from the CV based on a question.
    Args:
        question: The question about the CV content
        k: Number of relevant chunks to retrieve (default: 3)
    Returns:
        str: Relevant content from the CV
    """
    logger.info(f"Searching CV for: {question}")
    try:
        docs = vector_store.similarity_search(question, k=k)
        relevant_content = "\n\n".join(doc.page_content for doc in docs)
        logger.info("CV content retrieved successfully")

        return relevant_content
    except Exception as e:
        logger.error(f"Error in search_cv: {e}")
        raise


if __name__ == "__main__":
    # Initialize the vector store at startup
    initialize_vector_store()
    logger.info("Vector store initialized successfully")

    # Run the MCP server
    mcp.run(transport="stdio")
