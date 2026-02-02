"""
Unified prompt builder for ticket classification.
"""

def build_prompt(subject: str, description: str) -> str:
    return f"""
You are a support ticket classifier.
Given a ticket subject and description, predict:
1. Ticket Type (Billing inquiry, Cancellation request, Product inquiry, Refund request, Technical issue)
2. Ticket Priority (Low, Medium, High, Critical)

Examples:
Subject: "Login Issue"
Description: "Customer unable to log in to account"
Type: Technical issue
Priority: High

Subject: "Cancel Subscription"
Description: "Request to cancel subscription"
Type: Cancellation request
Priority: Medium

Subject: "Refund for defective product"
Description: "Customer asking about refund for defective product"
Type: Refund request
Priority: Critical

Now classify the following:
Subject: {subject}
Description: {description}
Type:
Priority:
"""