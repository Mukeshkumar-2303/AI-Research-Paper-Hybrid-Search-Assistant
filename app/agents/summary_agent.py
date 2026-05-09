import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

class SummaryAgent:

    def summarize(self, query, retrieved_chunks):

        
        # Clean + filter context
        
        filtered_chunks = [
            item["chunk"] for item in retrieved_chunks
            if item and len(item.get("chunk", "")) > 80
        ]

        context = "\n\n".join(filtered_chunks[:8])  # top chunks only

        
        # Strong academic prompt
       
        prompt = f"""
You are a document understanding assistant.

First identify the document type:
- research paper
- legal document
- financial bill
- report
- unknown

Then answer the question based on actual document type.

Question:
{query}

Context:
{context}

Rules:
- If document is NOT a research paper, do NOT assume "contributions"
- For legal/financial documents, explain purpose instead
- Be precise and factual
- Do NOT hallucinate missing sections

Final Answer:
"""

        # Groq call
      
        response = client.chat.completions.create(
            model=os.getenv("MODEL_NAME"),
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2
        )

        return response.choices[0].message.content.strip()