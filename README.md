# Medical Chatbot Gen AI

## 🏥 Project Purpose
The **Medical Chatbot Gen AI** is designed to democratize access to medical information by providing an intelligent, conversational interface for querying complex medical documents. In an era where medical literature is vast and often difficult to navigate, this chatbot serves as a bridge, allowing users to ask natural language questions and receive accurate, context-aware answers derived directly from authoritative trusted medical PDF sources.

## 🚀 Applications
- **Healthcare Assistants**: Can be used by medical students or professionals to quickly retrieve specific information from textbooks or research papers.
- **Patient Education**: simplifying complex medical terms for patients by summarizing information from provided documents.
- **Quick Reference**: A lookup tool for symptoms, treatments, and medical definitions.
- **Research Aid**: Rapidly finding relevant sections in large volumes of medical literature.

## 🛠️ Tech Stack
- **Language**: Python 3.10+
- **Framework**: Flask (Backend), HTML/CSS/JS (Frontend)
- **LLM**: Google Gemini 2.5 Flash (via `langchain-google-genai`)
- **Orchestration**: LangChain & LangChain Classic
- **Vector Database**: Pinecone Serverless (via `langchain-pinecone`)
- **Embeddings**: HuggingFace (`sentence-transformers/all-MiniLM-L6-v2`)
- **PDF Processing**: `pypdf`, LangChain DirectoryLoader

## ✨ Features
- **RAG (Retrieval-Augmented Generation)**: Combines the power of LLMs with external data retrieval for high accuracy.
- **Multi-PDF Support**: Automatically loads and processes all PDF files in the `Data/` directory.
- **Semantic Search**: Uses rigorous vector embeddings to understand the *meaning* of your query, not just keywords.
- **Scalable Vector Store**: Utilizes Pinecone for fast and scalable similarity search.
- **Modern UI**: A clean, responsive chat interface built with Bootstrap.
- **Google Gemini Integration**: Powered by Google's latest `gemini-2.5-flash` model for fast and efficient reasoning.

## ⚙️ How to Run?

### Prerequisites
- Python 3.10 or higher
- A Pinecone API Key
- A Google Cloud API Key (with Generative AI enabled)

### Steps

1.  **Clone the repository**
    ```bash
    git clone <repository_url>
    ```

2.  **Create a Virtual Environment**
    ```bash
    conda create -n medibot python=3.10 -y
    conda activate medibot
    ```

3.  **Install Requirements**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables**
    Create a `.env` file in the root directory and add your credentials:
    ```ini
    PINECONE_API_KEY="your_pinecone_api_key_here"
    GOOGLE_API_KEY="your_google_api_key_here"
    ```

5.  **Ingest Data**
    Place your medical PDF files in the `Data/` folder. Then, run the ingestion script to process the PDFs and store embeddings in Pinecone:
    ```bash
    python store_index.py
    ```

6.  **Run the Application**
    Start the Flask server:
    ```bash
    python app.py
    ```

7.  **Access the Chatbot**
    Open your web browser and navigate to:
    ```
    http://localhost:8080
    ```

## 🧩 Problem Solving
This project solves the "information overload" problem in healthcare. 
- **Contextual Understanding**: Unlike standard keyword search (Ctrl+F), the chatbot understands context (e.g., asking "how to treat it?" after asking about "Acne").
- **Efficiency**: Reduces the time spent scrolling through hundreds of pages.
- **Accuracy**: By grounding the LLM's responses in specific source documents (RAG), it significantly reduces hallucinations common in general-purpose chatbots.
