import json
import logging

import requests
from django.conf import settings

from thesombot_web.celery import app


@app.task
def send_tg_notifications(user_ids: list, message: str, parse_mode='markdown') -> None:
    for user_id in user_ids:
        try:
            requests.post(
                f'https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage',
                data=json.dumps({
                    'chat_id': user_id, 'text': message, 'parse_mode': parse_mode
                }),
                headers={'Content-Type': 'application/json'}
            )
        except:
            logging.warning(f'Tried to send book notify to {user_id} with message: {message}')
