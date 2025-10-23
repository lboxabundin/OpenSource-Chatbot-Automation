# OpenSource Chatbot & Automation
OpenSource-Chatbot-Automation/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── sponsor.md
├── requirements.txt
├── Dockerfile
├── sample_config.yaml
├── src/
│ ├── app.py
│ ├── chatbot/
│ │ ├── engine.py
│ │ └── rules.json
│ ├── automations/
│ │ ├── runner.py
│ │ └── example_tasks.py
│ └── utils.py
├── scripts/
│ └── build_zip.sh
└── .github/
└── workflows/
└── ci.yml
A lightweight, extensible open-source chatbot and automation system designed for small teams and indie developers. Built with Python and FastAPI. Includes:
- Simple rule-based chatbot engine with JSON-driven rules
- Automation runner to execute tasks triggered by chat intents (HTTP, shell, webhooks)
- Dockerfile for containerized deployment
- CI workflow to run tests and build artifacts
- Script to package the repo into a downloadable ZIP for GitHub Sponsors
## Features
- Easy-to-edit `rules.json` for adding intents and responses
- Websocket and HTTP endpoints for chat integration
- Task runner with pluggable task modules
- Example automations (send email, call webhook, run shell command)

## Quickstart
1. Create a virtualenv and install dependencies:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
