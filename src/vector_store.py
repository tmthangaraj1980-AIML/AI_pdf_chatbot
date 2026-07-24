"""
Vector Store Module
-------------------
This module creates and saves a FAISS vector database.
"""

from langchain_community.vectorstores import FAISS


def create_vector_store(chunks, embedding_model):
    """
    Create a FAISS vector database from document chunks.

    Parameters
    ----------
    chunks : list
        List of LangChain Document objects.

    embedding_model :
        HuggingFace embedding model.

    Returns
    -------
    FAISS
        FAISS vector database.
    """

    vector_store = FAISS.from_documents(
        documents=chunks,
        embedding=embedding_model
    )

    return vector_store