"""
RAG Pipeline Module
-------------------
This module combines the retriever and Gemini LLM
to answer user questions using PDF context.
"""

from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA


def create_rag_chain(llm, retriever):
    """
    Create the RetrievalQA chain.

    Parameters
    ----------
    llm : ChatGoogleGenerativeAI
        Gemini model.

    retriever : Retriever
        FAISS retriever.

    Returns
    -------
    RetrievalQA
        RAG pipeline.
    """

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
You are an AI Assistant.

Answer ONLY from the provided context.

If the answer is not available in the context,
reply with:

"I couldn't find the answer in the uploaded PDF."

-----------------------------
Context:
{context}

-----------------------------

Question:
{question}

Answer:
"""
    )

    qa_chain = RetrievalQA.from_chain_type(

        llm=llm,

        chain_type="stuff",

        retriever=retriever,

        return_source_documents=True,

        chain_type_kwargs={
            "prompt": prompt
        }

    )

    return qa_chain