AI Research Paper Hybrid Search Assistant

An AI-powered research paper analysis system built using FastAPI, Streamlit, LangGraph, FAISS, SentenceTransformers, and Groq LLMs.

This project enables users to upload research papers in PDF format and ask academic questions using Hybrid Retrieval-Augmented Generation (Hybrid RAG).

The system combines:

Semantic Search using SentenceTransformers + FAISS
Keyword Retrieval using TF-IDF
Hybrid Ranking for improved context retrieval
AI-generated academic summaries using Groq LLMs

AI Research Paper Assistant enables users to:
Upload academic research papers in PDF format
Ask natural language academic questions
Retrieve context using hybrid search
Generate AI-powered summaries
Understand methodologies and findings
Simplify complex academic content

The system uses a Hybrid RAG pipeline with semantic and keyword retrieval for accurate document understanding.

Features
Hybrid Retrieval System

The system combines:

Semantic similarity search
TF-IDF keyword matching
Hybrid score ranking

Hybrid ranking formula:

Hybrid Score =
0.6 × Semantic Similarity
+
0.4 × TF-IDF Similarity

This improves retrieval accuracy compared to standalone vector search.

AI-Powered Academic Understanding
Generates contextual academic answers
Explains methodologies
Summarizes research findings
Simplifies technical language
Extracts important concepts
PDF Processing Pipeline

The system automatically:

Uploads research papers
Extracts PDF text using PyMuPDF
Cleans and preprocesses text
Chunks content for retrieval
Generates embeddings
Stores vectors locally
Intelligent Question Answering

Users can ask questions such as:

What is the main contribution of this paper?
Explain the methodology used.
Summarize the findings.
What are the limitations of this study?

The system retrieves the most relevant chunks before generating responses.

Semantic Search Engine
Embedding Model
SentenceTransformers
Vector Database
FAISS
Keyword Retrieval
TF-IDF (scikit-learn)
LLM
Groq API
Modular AI Agent Architecture

The system is divided into:

Retrieval Agent

Responsible for:

PDF chunk retrieval
Embedding search
TF-IDF retrieval
Hybrid ranking
Summary Agent

Responsible for:

Academic summarization
Context understanding
Research explanation
Answer generation
LangGraph Workflow

Coordinates:

User Query
   ↓
Retrieval Agent
   ↓
Hybrid Search
   ↓
Summary Agent
   ↓
Final Academic Answer
Tech Stack
Frontend
Streamlit
Backend
FastAPI
AI / LLM
Groq LLM API
Embeddings
SentenceTransformers
Vector Database
FAISS
Keyword Search
TF-IDF (scikit-learn)
Workflow Orchestration
LangGraph
PDF Processing
PyMuPDF
System Workflow
Upload PDF
   ↓
Extract PDF Text
   ↓
Chunk Text
   ↓
Generate Embeddings
   ↓
Store in FAISS
   ↓
Generate TF-IDF Vectors
   ↓
User Question
   ↓
Hybrid Retrieval
   ↓
Retrieve Relevant Chunks
   ↓
Groq LLM Summarization
   ↓
Final AI Response
Example Use Cases
Research paper understanding
Literature review assistance
Academic summarization
Methodology extraction
Educational research analysis
Research learning assistant
Example Questions
Paper Understanding
What is the main contribution of this paper?
Summarize this research paper.
Methodology Analysis
Explain the methodology used in this study.
How was the data collected?
Findings & Insights
What are the key findings?
What limitations are mentioned?
Key Advantages
Hybrid retrieval improves answer accuracy
Local vector storage using FAISS
Modular architecture
Fast semantic search
Academic-focused summarization
Supports large research documents
Limitations
Very large PDFs may take time to process
Retrieval quality depends on chunk quality
Works best with structured academic documents
Future Improvements
Citation-aware responses
Page number references
Multi-paper comparison
Research chat history
PDF highlighting
Cross-encoder reranking
Streaming responses
Multi-document memory
Output Principle

The system strictly answers using retrieved PDF context.

If information is not clearly available in the uploaded document, the system explicitly states that instead of hallucinating information.
