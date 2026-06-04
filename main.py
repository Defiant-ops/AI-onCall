import os
import requests
from dotenv import load_dotenv
from google import genai

# Load secrets
load_dotenv()
PAGERDUTY_API_KEY = os.getenv("PAGERDUTY_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not PAGERDUTY_API_KEY:
    raise ValueError("Missing PagerDuty API key in .env")
if not GEMINI_API_KEY:
    raise ValueError("Missing Gemini API key in .env")

# Connect to PagerDuty via REST API
headers = {
    "Authorization": f"Token token={PAGERDUTY_API_KEY}",
    "Accept": "application/vnd.pagerduty+json;version=2"
}
resp = requests.get("https://api.pagerduty.com/incidents?limit=2", headers=headers)
incidents = resp.json().get("incidents", [])

print("Incidents (first 2):", incidents)

# Configure Gemini (new client format)
client = genai.Client(api_key=GEMINI_API_KEY)

# Summarize incidents
prompt = f"Summarize these PagerDuty incidents in a clear incident report:\n{incidents}"

# FIX 2: Switched to the modern workhorse model "gemini-2.5-flash"
response = client.models.generate_content(
    model="gemini-2.5-flash",   
    contents=prompt
)

print("Gemini says:\n", response.text)