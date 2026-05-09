from fastapi import APIRouter, UploadFile, File, HTTPException
import os
import uuid

from app.services.pdf_parser import extract_text_from_pdf
from app.services.chunker import chunk_text
from app.agents.retrieval_agent import RetrievalAgent
from app.agents.summary_agent import SummaryAgent
from app.core.workflow import create_workflow
from app.models.schemas import QueryRequest

router = APIRouter()

retrieval_agent = None
workflow = None

UPLOAD_DIR = "storage/uploaded_pdfs"
os.makedirs(UPLOAD_DIR, exist_ok=True)



# UPLOAD ENDPOINT

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    global retrieval_agent, workflow

    # Prevent file overwrite (IMPORTANT FIX)
    unique_name = f"{uuid.uuid4()}_{file.filename}"
    file_path = os.path.join(UPLOAD_DIR, unique_name)

    # Save file safely
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    # Extract text
    text = extract_text_from_pdf(file_path)

    if not text:
        raise HTTPException(
            status_code=400,
            detail="Could not extract text from PDF"
        )

    # Chunk text
    chunks = chunk_text(text)

    if not chunks:
        raise HTTPException(
            status_code=400,
            detail="No text chunks generated from PDF"
        )

    # Build agents
    retrieval_agent = RetrievalAgent(chunks)
    summary_agent = SummaryAgent()

    workflow = create_workflow(
        retrieval_agent,
        summary_agent
    )

    return {
        "message": "PDF uploaded successfully",
        "chunks": len(chunks)
    }



# ASK ENDPOINT 

@router.post("/ask")
async def ask_question(payload: QueryRequest):

    global workflow

    # Ensure workflow exists
    if workflow is None:
        raise HTTPException(
            status_code=400,
            detail="Please upload a PDF first"
        )

    try:
        result = workflow.invoke({
            "query": payload.question
        })

        # Safe extraction
        summary = result.get("summary", "")
        retrieved_chunks = result.get("retrieved_chunks", [])

        return {
            "summary": summary,
            "retrieved_chunks": retrieved_chunks
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal error: {str(e)}"
        )