import os
import time
import streamlit as st

from src.pdf_loader import load_pdf
from src.text_splitter import split_documents
from src.embeddings import load_embedding_model
from src.vector_store import create_vector_store
from src.retriever import create_retriever
from src.llm import load_llm
from src.rag_pipeline import create_rag_chain

# ---------------------------------------------------
# Streamlit Config
# ---------------------------------------------------

st.set_page_config(
    page_title="AI PDF Chatbot",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

with st.sidebar:

    st.title("🤖 AI PDF Chatbot")

    st.markdown("---")

    st.success("Google Gemini + RAG")

    st.markdown("### 📄 Document")

    pdf_name = "Top200_AI_Interview_QA_Thangaraj.pdf"

    st.info(pdf_name)

    st.markdown("---")

    st.markdown("### ⚙ Model")

    st.write("Embedding")
    st.code("all-MiniLM-L6-v2")

    st.write("LLM")
    st.code("Gemini")

    st.write("Vector DB")
    st.code("FAISS")

    st.markdown("---")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# ---------------------------------------------------
# Load RAG Pipeline
# ---------------------------------------------------

@st.cache_resource
def load_chatbot():

    pdf_path = os.path.join(
        "data",
        "Top200_AI_Interview_QA_Thangaraj.pdf"
    )

    documents = load_pdf(pdf_path)

    chunks = split_documents(documents)

    embedding_model = load_embedding_model()

    vector_store = create_vector_store(
        chunks,
        embedding_model
    )

    retriever = create_retriever(
        vector_store
    )

    llm = load_llm()

    qa_chain = create_rag_chain(
        llm,
        retriever
    )

    return qa_chain

qa_chain = load_chatbot()

# ---------------------------------------------------
# Title
# ---------------------------------------------------

st.title("🤖 AI PDF Chatbot")

st.caption("Ask anything from your PDF using Google Gemini + RAG")

# ---------------------------------------------------
# Chat History
# ---------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# ---------------------------------------------------
# Chat Input
# ---------------------------------------------------

question = st.chat_input("Ask a question...")

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            start = time.time()

            response = qa_chain.invoke(
                {
                    "query": question
                }
            )

            answer = response["result"]

            end = time.time()

            st.markdown(answer)

            st.caption(
                f"⏱ Response Time : {end-start:.2f} sec"
            )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )