import logging

import requests

from config import TG_TOKEN, TG_CHAT_ID


def send_message(text):
    url = f'https://api.telegram.org/bot{TG_TOKEN}/sendMessage'
    payload = {
        'chat_id': TG_CHAT_ID,
        'text': text
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            logging.info("Telegram уведомление отправлено")
        else:
            logging.error(f"Ошибка Telegram: {response.text}")

    except Exception as e:
        logging.error(f"Ошибка отправки Telegram: {e}")

    return None