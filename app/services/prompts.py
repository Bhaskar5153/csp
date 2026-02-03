# app/services/prompt.py

# Base role prompts
DATA_ANALYST_PROMPT = """
You are a data analyst. Your role is to analyze the dataset and provide insights, summaries, and recommendations based on the data.
"""

CUSTOMER_SUPPORT_PROMPT = """
You are a customer support assistant. Your role is to answer queries empathetically and provide helpful solutions based on company policies and data.
"""

def build_prompt(base_prompt: str, context: str = "", question: str = "") -> str:
    """
    Build a full prompt for the LLM by combining:
    - Role prompt (defines persona/role)
    - Dataset context (from load.py)
    - User's question (the actual query to answer)
    """
    sections = [base_prompt]

    if context:
        sections.append(f"Here is the dataset context:\n{context}")

    if question:
        sections.append(f"User Question:\n{question}")

    return "\n\n".join(sections)