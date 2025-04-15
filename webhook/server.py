from dotenv import load_dotenv
import os
import asyncio
from aiohttp import web
import aiohttp

load_dotenv(dotenv_path="webhook/.secrets.env")

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

routes = web.RouteTableDef()

@routes.post('/alert')
async def handle_alert(request):
    data = await request.json()
    message = format_alert(data)
    await send_telegram_message(message)
    return web.Response(text="Alert received")

def format_alert(data):
    alerts = data.get("alerts", [])
    messages = []
    for alert in alerts:
        status = alert.get("status", "unknown").upper()
        labels = alert.get("labels", {})
        summary = alert.get("annotations", {}).get("summary", "")
        instance = labels.get("instance", "unknown")
        alertname = labels.get("alertname", "NoName")
        messages.append(f"Alert: [{status}] {alertname} in {instance}: {summary}")
    return "\n".join(messages)

async def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload) as resp:
            if resp.status != 200:
                print("Error:", await resp.text())

app = web.Application()
app.add_routes(routes)

if __name__ == '__main__':
    web.run_app(app, port=5001)