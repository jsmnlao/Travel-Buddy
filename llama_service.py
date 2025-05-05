import requests
import os
from datetime import datetime

# Set your API key in an environment variable for safety
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def generate_itinerary_with_llama(destination, start_date, end_date, budget, travelers):
    if not destination or not start_date or not end_date or not budget or not travelers:
        raise ValueError("All itinerary fields are required.")

    try:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Use YYYY-MM-DD.")

    days = (end - start).days + 1

    prompt = f"""
You are a travel assistant. Create a {days}-day itinerary for a trip to {destination}.
The group has {travelers} traveler(s) and a total budget of ${budget}.
Each day should include 1-2 activities with location, description, and cost estimate.
Return the result in a structured text format.
"""

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "mistralai/mixtral-8x7b",  # or use another model like meta-llama/3
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 800,
            "temperature": 0.7
        }
    )

    if response.status_code != 200:
        raise ValueError("LLaMA API error: " + response.text)

    result = response.json()
    return result["choices"][0]["message"]["content"]
