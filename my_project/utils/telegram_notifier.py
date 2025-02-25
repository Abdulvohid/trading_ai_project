import requests

def send_telegram_signal(bot_token, chat_id, message):
    """
    Telegram bot orqali signal yuborish
    """
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML"
    }
    response = requests.post(url, json=payload)
    return response.json()