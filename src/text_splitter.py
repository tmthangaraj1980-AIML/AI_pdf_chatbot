"""
Text Splitter Module
--------------------
This module splits PDF documents into smaller chunks
using RecursiveCharacterTextSplitter.
"""

from langchain.text_splitter import RecursiveCharacterTextSplitter


def split_documents(documents):
    """
    Split documents into smaller chunks.

    Parameters
    ----------
    documents : list
        List of LangChain Document objects.

    Returns
    -------
    list
        List of split Document chunks.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = text_splitter.split_documents(documents)

    return chunks