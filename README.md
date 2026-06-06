# 🤖 RAG Chatbot with Flask UI

## 📌 Project Description
This project is a simple Retrieval-Augmented Generation (RAG) chatbot built using Python. It uses TF-IDF based similarity search to retrieve the most relevant answer from a dataset and displays responses through a Flask web interface.

---

## 🚀 Features
- 🧠 TF-IDF based semantic search
- 🌐 Flask backend API
- 💬 Web-based chatbot UI
- ⚡ Fast and lightweight
- 📚 Custom knowledge base support

---

## 🛠️ Tech Stack
- Python
- Flask
- Scikit-learn
- HTML, CSS, JavaScript

---

## 📁 Project Structure
    rag-chatbot/ │ ├── app.py              # Flask backend ├── rag.py              # RAG logic (TF-IDF search) ├── data.txt            # Knowledge base │ ├── templates/ │     └── index.html    # Frontend UI │ └── static/ └── style.css     # UI styling

## Install dependencies
    pip install flask scikit-learn numpy

## Run the Project
     python app.py

## Open in Browser
    http://127.0.0.1:5000/