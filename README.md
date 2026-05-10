AI Research Paper Hybrid Search Assistant

An AI-powered research paper analysis system built with Streamlit, FastAPI, LangGraph, FAISS, and Groq LLMs that enables users to interact with academic PDFs using natural language.

This project combines semantic vector retrieval and TF-IDF keyword search to generate context-aware answers from research papers and technical documents using a Hybrid Retrieval-Augmented Generation (RAG) pipeline.

Main Capabilities
Upload and analyze research papers in PDF format
Ask natural language questions about academic documents
Retrieve relevant research content using hybrid search
Generate AI-powered summaries and explanations
Simplify complex academic language
Explore methodologies, findings, and conclusions
Interact through a clean Streamlit-based interface

Features
AI-Powered Research Understanding
Converts PDF documents into semantic embeddings
Retrieves highly relevant document chunks
Generates context-aware answers using LLM reasoning
Simplifies technical academic language
Hybrid Search Retrieval
Uses FAISS semantic vector search
Uses TF-IDF keyword retrieval
Combines semantic and lexical ranking
Improves retrieval accuracy compared to standalone vector search
Research Paper Analysis
Extracts text from uploaded PDFs
Chunks large documents intelligently
Identifies important research sections
Supports long-document processing
Interactive Academic Assistant
Explains research contributions
Summarizes methodologies
Answers technical questions
Provides concise document understanding
Modern Streamlit Interface
Simple upload workflow
Clean chat-style interaction
Real-time answer generation
User-friendly document exploration
Technical Explanation

The system uses a Hybrid RAG Architecture combining:

Semantic Retrieval
Sentence embeddings generated using Sentence Transformers
FAISS vector similarity search
Keyword Retrieval
TF-IDF indexing using Scikit-learn
Exact keyword matching for improved relevance
Hybrid Ranking
Combines semantic similarity and TF-IDF scores
Produces more accurate retrieval results
LLM Response Generation
Retrieved context is passed into Groq-hosted LLMs
Generates grounded and context-aware answers
Supported Inputs / Modules
Supported Inputs
PDF Research Papers
Academic Journals
Technical Reports
Government Documents
Financial Documents
Core Modules
PDF Parsing
Text Chunking
Embedding Generation
FAISS Vector Store
TF-IDF Retrieval
Hybrid Ranking
LangGraph Workflow
LLM Summarization
Security / Safety
Safe Document Processing

Only safe read operations are performed.

The system does NOT:

Modify uploaded documents
Execute embedded scripts
Run unsafe operations
Store sensitive credentials permanently
Controlled AI Responses
Responses are generated strictly from retrieved document context
Reduces hallucinations using grounded retrieval
Avoids unsupported answer generation

Architecture
PDF Upload
   ↓
Text Extraction
   ↓
Document Chunking
   ↓
Embedding Generation
   ↓
FAISS Vector Storage
   ↓
TF-IDF Indexing
   ↓
Hybrid Retrieval
   ↓
Context Ranking
   ↓
Groq LLM Generation
   ↓
AI Response
Example Use Cases
Research paper understanding
Academic literature review
Technical document analysis
Financial bill summarization
Government policy exploration
Student research assistance
Academic content simplification
Example Queries
Research Understanding
What is the main contribution of this paper?
Summarize the methodology used in this research.
Explain the findings in simple terms.
Technical Analysis
What algorithms are discussed in this paper?
Explain the proposed architecture.
What are the limitations mentioned in this paper?
Document Exploration
Summarize the conclusion section.
What datasets were used in this research?
What problem does this paper solve?
Tech Stack
Frontend
Streamlit
Backend
FastAPI
Python
AI / LLM
Groq LLM
LangChain
LangGraph
Embeddings
Sentence Transformers
HuggingFace Transformers
Vector Database
FAISS
Hybrid Search
TF-IDF
Scikit-learn
PDF Processing
PyMuPDF
Other Tools
NumPy
Requests
Pydantic
Python-dotenv
System Workflow
Upload PDF
   ↓
Extract Document Text
   ↓
Chunk Document
   ↓
Generate Embeddings
   ↓
Store in FAISS
   ↓
Create TF-IDF Index
   ↓
User Question
   ↓
Hybrid Retrieval
(Semantic + Keyword)
   ↓
Retrieve Relevant Context
   ↓
Generate AI Answer
Installation
Clone Repository
git clone <YOUR_GITHUB_REPOSITORY_LINK>
cd AI-Research-Paper-Hybrid-Search-Assistant
Create Virtual Environment
python -m venv venv
Activate Environment
Windows
venv\Scripts\activate
Linux / Mac
source venv/bin/activate
Install Dependencies
pip install -r requirements.txt
Configure Environment Variables

Create a .env file:

GROQ_API_KEY=your_groq_api_key
MODEL_NAME=llama-3.1-8b-instant
Run FastAPI Backend
uvicorn app.main:app --reload
Run Streamlit Frontend
streamlit run frontend/streamlit_app.py
Limitations
Large PDFs may increase processing time
OCR-scanned PDFs may reduce extraction quality
Retrieval accuracy depends on chunking quality
Complex research domains may require improved prompts
Future Improvements
Multi-PDF support
Citation-aware answers
Research paper recommendation system
PDF highlighting for retrieved content
Chat history memory
Better summarization pipelines
GPU-optimized embedding generation
Multi-user support
Output Principle

The assistant strictly answers using retrieved document context.

If information is not found in the uploaded document, the system clearly states that instead of generating unsupported responses.

Deployment
Frontend Deployment
Streamlit Cloud
Hugging Face Spaces
Backend Deployment
Render
Railway
Docker
