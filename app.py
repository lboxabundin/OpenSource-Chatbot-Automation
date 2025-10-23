from fastapi import FastAPI, WebSocket, BackgroundTasks
from fastapi.responses import JSONResponse
from chatbot.engine import ChatEngine
from automations.runner import AutomationRunner
from pydantic import BaseModel
import yaml


app = FastAPI(title="OpenSource Chatbot & Automation")


# Load config
with open('sample_config.yaml') as f:
CONFIG = yaml.safe_load(f)


engine = ChatEngine('src/chatbot/rules.json')
runner = AutomationRunner()


class Message(BaseModel):
user: str
text: str


@app.post('/chat')
async def chat(msg: Message, background_tasks: BackgroundTasks):
intent, response, meta = engine.process(msg.text)
# If response triggers automation, run in background
if meta.get('automation') and CONFIG['chatbot'].get('automations_enabled'):
background_tasks.add_task(runner.run, meta['automation'], context={'user': msg.user, 'text': msg.text})
return JSONResponse({'intent': intent, 'response': response, 'meta': meta})


@app.websocket('/ws')
async def ws_endpoint(ws: WebSocket):
await ws.accept()
try:
while True:
data = await ws.receive_json()
text = data.get('text','')
intent, response, meta = engine.process(text)
if meta.get('automation'):
# start automation but don't block websocket
runner.run(meta['automation'], context={'user':'ws', 'text':text})
await ws.send_json({'intent': intent, 'response': response, 'meta': meta})
except Exception:
await ws.close()
