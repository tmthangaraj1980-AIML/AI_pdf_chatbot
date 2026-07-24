"""
Retriever Module
----------------
This module converts the FAISS vector store into
a retriever for semantic search.
"""


def create_retriever(vector_store):
    """
    Create a retriever from the FAISS vector store.

    Parameters
    ----------
    vector_store : FAISS
        FAISS vector database.

    Returns
    -------
    Retriever
        FAISS retriever object.
    """

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}
    )

    return retriever