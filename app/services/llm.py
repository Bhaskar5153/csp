import google as genai
from app.utils.prompts import build_prompt

# Configure Gemini
client = genai.Client(api_key=API_KEY)

def classify_ticket(subject: str, description: str):
    prompt = build_prompt(subject, description)
    response = client.models.generate_content(prompt)

    # Parse response
    lines = [line.strip() for line in response.text.strip().split("\n") if line.strip()]
    ticket_type = next((line.replace("Type:", "").strip() for line in lines if line.startswith("Type:")), "")
    ticket_priority = next((line.replace("Priority:", "").strip() for line in lines if line.startswith("Priority:")), "")

    return {"ticket_type": ticket_type, "ticket_priority": ticket_priority}