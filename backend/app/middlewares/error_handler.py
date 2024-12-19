import traceback
import requests
from fastapi import Request, Response
from app.settings import settings
from dotenv import load_dotenv

import os
load_dotenv(dotenv_path='.env')

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")


async def send_error_to_telegram(error_message: str):
    url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": settings.TELEGRAM_CHAT_ID,
        "text": error_message
    }
    requests.post(url, data=data)

async def error_handler_middleware(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        err_msg = f"Error: {str(e)}\nTraceback: {traceback.format_exc()}"
        await send_error_to_telegram(err_msg)
        return Response("Internal Server Error", status_code=500)

def register_error_handler(app):
    app.middleware("http")(error_handler_middleware)
