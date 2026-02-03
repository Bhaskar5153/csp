from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.data_ingestion.load import load_data
from app.services.llm import generate_response

# Path to your dataset
DATA_FILE_PATH = "app/data/customer_support_tickets.csv"

# Load dataset summary once at startup
try:
    dataset_summary = load_data(DATA_FILE_PATH)
except Exception as e:
    dataset_summary = ""
    print(f"Error loading dataset: {e}")

# FastAPI app instance
app = FastAPI(title="Customer Support AI", version="1.0")

# Request schema
class QuestionRequest(BaseModel):
    question: str

# Response schema
class AnswerResponse(BaseModel):
    answer: str

@app.post("/ask", response_model=AnswerResponse)
def ask_question(request: QuestionRequest):
    """
    Endpoint to take a user question and return LLM-generated response.
    """
    if not dataset_summary:
        raise HTTPException(status_code=500, detail="Dataset context not available.")

    try:
        answer = generate_response(context=dataset_summary, question=request.question)
        return AnswerResponse(answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating response: {e}")