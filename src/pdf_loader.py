"""
PDF Loader Module
-----------------
This module loads a PDF document and returns
LangChain Document objects.
"""

from langchain_community.document_loaders import PyPDFLoader


def load_pdf(pdf_path: str):
    """
    Load a PDF file.

    Parameters
    ----------
    pdf_path : str
        Path to the PDF file.

    Returns
    -------
    list
        List of LangChain Document objects.
    """

    loader = PyPDFLoader(pdf_path)

    documents = loader.load()

    return documents