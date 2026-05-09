import fitz  # PyMuPDF
import re


def clean_text(text: str) -> str:
    """Clean extracted PDF text for better embeddings"""
    text = re.sub(r'\s+', ' ', text)   
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)  
    return text.strip()


def extract_text_from_pdf(pdf_path: str) -> str:
    text = ""

    with fitz.open(pdf_path) as doc:   
        for page in doc:
            page_text = page.get_text()
            text += page_text + "\n"

    return clean_text(text)