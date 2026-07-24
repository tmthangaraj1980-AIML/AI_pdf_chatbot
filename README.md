# 🤖 AI PDF Chatbot using RAG & Google Gemini

An intelligent **Retrieval-Augmented Generation (RAG)** chatbot that allows users to ask questions from a PDF document and receive context-aware answers using **Google Gemini**, **LangChain**, **FAISS**, and **Sentence Transformers**.

---

# 📌 Overview

This project demonstrates how Large Language Models (LLMs) can answer questions based on custom documents instead of relying only on their pretrained knowledge.

The application:

* Loads a PDF document
* Splits the content into manageable chunks
* Converts text into vector embeddings
* Stores embeddings in a FAISS vector database
* Retrieves the most relevant document chunks
* Uses Google Gemini to generate accurate, context-aware answers

---

# 🚀 Features

* 📄 PDF Question Answering
* 🤖 Google Gemini Integration
* 🔍 Semantic Search using FAISS
* 🧠 Sentence Transformer Embeddings
* 📚 Retrieval-Augmented Generation (RAG)
* 💬 Interactive Streamlit Chat Interface
* ⚡ Fast Similarity Search
* 🧹 Chat History Support
* 🎯 Context-Based Responses

---

# 🛠 Tech Stack

### Programming Language

* Python

### Frameworks & Libraries

* Streamlit
* LangChain
* Google Gemini API
* FAISS
* Sentence Transformers
* Hugging Face
* PyPDF
* Python-dotenv

---

# 📂 Project Structure

```text
AI_pdf_chatbot/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
│
├── data/
│   └── Top200_AI_Interview_QA_Thangaraj.pdf
│
├── src/
│   ├── pdf_loader.py
│   ├── text_splitter.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── llm.py
│   └── rag_pipeline.py
│
└── screenshots/
```

---

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/yourusername/AI_pdf_chatbot.git

cd AI_pdf_chatbot
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Configure Google Gemini API Key

Create a **.env** file in the project root.

```text
GOOGLE_API_KEY=YOUR_API_KEY
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

Open your browser and visit:

```text
http://localhost:8501
```

---

# 🧠 RAG Workflow

```text
                  PDF Document
                        │
                        ▼
                 Load PDF (PyPDF)
                        │
                        ▼
                 Split into Chunks
                        │
                        ▼
         Sentence Transformer Embeddings
                        │
                        ▼
                 FAISS Vector Database
                        │
────────────────────────────────────────────
                  User Question
                        │
                        ▼
                Similarity Search
                        │
                        ▼
            Retrieve Relevant Chunks
                        │
                        ▼
                Google Gemini LLM
                        │
                        ▼
                 Contextual Answer
                        │
                        ▼
                Streamlit Chat UI
```

---

# 📸 Screenshots

Add screenshots inside the **screenshots** folder.

Example:

```
screenshots/

home.png

chat.png

answer.png
```

---

# 📈 Future Improvements

* Upload multiple PDF files
* Persistent FAISS index
* Conversation memory
* Source page references
* Streaming responses
* Dark mode
* Export chat history
* Docker support
* Cloud deployment
* Authentication

---

# 💼 Skills Demonstrated

* Retrieval-Augmented Generation (RAG)
* Large Language Models (LLMs)
* LangChain
* Google Gemini API
* Vector Databases (FAISS)
* Semantic Search
* NLP
* Prompt Engineering
* Python Development
* Streamlit Deployment

---

# 👨‍💻 Author

**Thangaraj T**

**AI/ML Engineer | Data Science Developer**

### Connect with Me

* GitHub: https://github.com/tmthangaraj1980-AIML
* LinkedIn: *(Add your LinkedIn profile URL here)*

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the repository

📢 Share your feedback

---

# 📄 License

This project is licensed under the MIT License.
