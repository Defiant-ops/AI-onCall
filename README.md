AI On‑Call System 🚨🤖
Overview
AI On‑Call is a reliability tool that connects PagerDuty incidents with an AI assistant (Gemini, Claude, or any LLM).
It automatically:

Summarizes incidents in plain language

Logs them into runbooks/postmortems

Helps teams respond faster with less manual triage

Think of it as your AI teammate for incident response.

Features ✨
🔗 PagerDuty Integration – listens for new incidents

🧠 AI Summaries – generates clear, concise incident reports

📒 Runbook Logging – stores summaries for later review

⚡ Automation Ready – CLI + dashboard planned for expansion

How It Works ⚙️
PagerDuty triggers an incident → webhook sends data to AI_OnCall.

AI_OnCall calls your chosen AI model (Gemini/Claude).

The AI summarizes the incident and logs it.

Output is stored in a file or database for postmortems.

Setup 🛠️
Prerequisites
Python 3.10+

PagerDuty account + API key

AI model API key (Gemini, Claude, or OpenAI)

Git + basic terminal knowledge

Installation
bash
# Clone the repo
git clone https://github.com/yourusername/AI_OnCall.git
cd AI_OnCall

# Install dependencies
pip install -r requirements.txt
Configuration
Create a .env file:

Code
PAGERDUTY_API_KEY=your_key_here
AI_API_KEY=your_key_here
MODEL=gemini   # or claude/openai
Usage 🚀
Run the system:

bash
python ai_oncall.py
Incidents will be automatically summarized.

Logs will appear in logs/ or your configured database.

Roadmap 🗺️
[ ] CLI interface for quick commands

[ ] Azure deployment templates

[ ] Web dashboard for visualization

[ ] Multi‑model support with fallback

Contributing 🤝
Pull requests are welcome!
For major changes, please open an issue first to discuss what you’d like to change.
