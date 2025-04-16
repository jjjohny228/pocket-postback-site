import os
import requests
from dotenv import load_dotenv
import logging

load_dotenv()


def send_postback_notification(message: str) -> str | None:
    payload = {
        'chat_id': os.getenv('ADMIN_CHANNEL'),
        'text': message
    }
    url = f'https://api.telegram.org/bot{os.getenv("BOT_TOKEN")}/sendMessage'
    try:
        response = requests.post(url=url, data=payload)
        logging.info('Сообщение было отправлено успешно')
        return response.text
    except Exception as e:
        logging.error(f'При отправлении сообщения админам произошла ошибка: {e}')
