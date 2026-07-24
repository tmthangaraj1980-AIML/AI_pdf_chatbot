"""
Embedding Model Module
----------------------
This module loads the Sentence Transformer model
used to convert text into embedding vectors.
"""

from langchain_community.embeddings import HuggingFaceEmbeddings


def load_embedding_model():
    """
    Load the embedding model.

    Returns
    -------
    HuggingFaceEmbeddings
        Embedding model object.
    """

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return embeddings