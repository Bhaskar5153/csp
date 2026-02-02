from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Ticket Classifier Chatbot")

app.include_router(router, prefix="/api")