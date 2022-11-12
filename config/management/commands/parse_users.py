import time

import pandas as pd
from django.core.management.base import BaseCommand

from config.models import User, Language
from subscribe.models import SubscribeStatus


class Command(BaseCommand):
    help = 'Парсинг юзеров из csv-файлов'

    def handle(self, *args, **kwargs):
        start_time = time.time()
        reader = pd.read_csv('data/users.csv', delimiter=',')
        for index, row in reader.iterrows():
            print(f"--------- Parce row with id: {index} ---------")
            data = {
                'telegram_id': row['userId'],
                'username': row['username'],
                'mention': row['mention'],
                'balance': row['balance'],
                'is_block': row['isBlock'],
                'show_progress': row['showProgress'],
                'deposit': row['deposit'],
                'subscribe_time': row['subscribeTime'],
                'payment_id': row['paymentId'],
                'is_auto_pay': row['isAutoPay'],
                'subscribe_status': row['subscribeStatus_id'],
                'not_end_payment': row['notEndPayment']
            }

            if row['languageId_id']:
                lang_id = int(row['languageId_id'])
                if lang_id == 1:
                    data['language'] = Language.objects.filter(language_code='ru').first()
                elif lang_id == 2:
                    data['language'] = Language.objects.filter(language_code='en').first()

            if row['subscribeStatus_id']:
                data['subscribe_status'] = SubscribeStatus.objects.filter(pk=row['subscribeStatus_id']).first()

            try:
                user, res = User.objects.get_or_create(**data)
            except Exception as e:
                print(f'Error adding: {str(data)}')
                print(e)
                break
            if res:
                print(f'Пользователь: {user.telegram_id} с депозитом {user.deposit}')

        print("--- %s seconds ---" % (time.time() - start_time))
