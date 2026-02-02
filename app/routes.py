from fastapi import APIRouter
from app.schemas import TicketRequest, TicketResponse
from app.services.llm import classify_ticket

router = APIRouter()

@router.post("/classify", response_model=TicketResponse)
def classify(ticket: TicketRequest):
    result = classify_ticket(ticket.subject, ticket.description)
    return TicketResponse(**result)