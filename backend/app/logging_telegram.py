#from ..core.config import settings
from dotenv import load_dotenv
from telegram import Bot
import os
load_dotenv(dotenv_path='.env')

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

bot = Bot(token=TELEGRAM_BOT_TOKEN)

def log_to_telegram(message: str):
    try:
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
    except Exception as e:
        print(f"Ошибка отправки сообщения в Telegram: {e}")
