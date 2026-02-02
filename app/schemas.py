from pydantic import BaseModel

class TicketRequest(BaseModel):
    subject: str
    description: str

class TicketResponse(BaseModel):
    ticket_type: str
    ticket_priority: str