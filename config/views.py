import pandas as pd
import os
from django.http import FileResponse
from django.shortcuts import redirect

from book_archive.models import BookArchive, PurchasedArchiveBook
from book.models import Book
from statistic.models import Statistic
from subscribe.models import Subscribe, SubPrice
from .models import *


def index(request):
    return redirect('/admin')


def get_user(request, user_id):
    user = User.objects.get(pk=user_id)

    data = {
        'ID в Телеграмме': [user.pk],
        'Имя': [user.username],
        'Обращение': [user.mention],
        'Баланс': [user.balance],
        'Депозит': [user.deposit],
        'Реферал': [user.referral],
        'Язык': [user.language_id],
        'Время подписки': [user.subscribe_time],
        'Автоплатёж': [user.is_auto_pay]
    }

    if not os.path.exists('static/users/'):
        os.mkdir('static')
        os.mkdir('static/users')
    filename = f'static/users/{user_id}.xlsx'
    df = pd.DataFrame(data)
    df.to_excel(filename, sheet_name='User', index=False)

    return FileResponse(open(filename, 'rb'))


def get_stats(request):
    users_data = {
        'ID в Телеграмме': [],
        'Имя': [],
        'Обращение': [],
        'Баланс': [],
        'Депозит': [],
        'Реферал': [],
        'Язык': [],
        'Время подписки': [],
        'Автоплатёж': [],
        'Подписан ли': [],
        'Дата конца подписки': [],
        'Срок подписки': [],
        'Цена подписки': []
    }
    for user in User.objects.all():
        users_data['ID в Телеграмме'].append(user.telegram_id)
        users_data['Имя'].append(user.username)
        users_data['Обращение'].append(user.mention)
        users_data['Баланс'].append(user.balance)
        users_data['Депозит'].append(user.deposit)
        users_data['Реферал'].append(user.referral)
        users_data['Язык'].append(user.language)
        users_data['Время подписки'].append(user.subscribe_time)
        users_data['Автоплатёж'].append(user.is_auto_pay)

        try:
            subscribe = Subscribe.objects.get(user=user.pk)
            users_data['Подписан ли'].append(subscribe.is_active)
            users_data['Дата конца подписки'].append(subscribe.end_date)

            sub_price = SubPrice.objects.get(pk=subscribe.sub_price.pk)
            users_data['Срок подписки'].append(sub_price.duration)
            users_data['Цена подписки'].append(sub_price.value)
        except:
            users_data['Подписан ли'].append(False)
            users_data['Дата конца подписки'].append('0')
            users_data['Срок подписки'].append('0')
            users_data['Цена подписки'].append('0')

    referrals_data = {
        'Название': [],
        'Код': [],
        'Кол-во регистраций': []
    }
    for referral in Referral.objects.all():
        referrals_data['Название'].append(referral.name)
        referrals_data['Код'].append(referral.code)
        referrals_data['Кол-во регистраций'].append(referral.register_count)

    subscribes_data = {
        'Название': [],
        'Цена': [],
        'Срок': [],
        'Кол-во подписчиков': []
    }
    for subscribe in SubPrice.objects.all():
        subscribes_data['Название'].append(subscribe.name)
        subscribes_data['Цена'].append(subscribe.value)
        subscribes_data['Срок'].append(subscribe.duration)

        active_subs_count = Subscribe.objects.filter(sub_price=subscribe.pk, is_active=True).count()
        subscribes_data['Кол-во подписчиков'].append(active_subs_count)

    def all_subs_counter():
        return len(Subscribe.objects.all())

    def no_buy_users_counter():
        all_users_count = len(User.objects.all())
        subscribes = Subscribe.objects.all()
        users_with_subscribe = set()
        for subscribe in subscribes:
            users_with_subscribe.add(subscribe.user)
        return all_users_count - len(users_with_subscribe)

    def block_users_counter():
        return len(User.objects.filter(is_block=True))

    def archive_books_count():
        return len(PurchasedArchiveBook.objects.all())

    def archive_books_sum():
        all_sum = 0
        for book in PurchasedArchiveBook.objects.all():
            all_sum += book.book.price
        return all_sum

    statistics_data = {
        'Кол-во пользователей с подпиской': [all_subs_counter()],
        'Кол-во пользователей без подписки': [no_buy_users_counter()],
        'Кол-во пользователей заблокировавших бота': [block_users_counter()],
        'Сумма собранных средств с книг из архива': [archive_books_sum()],
        'Кол-во проданных книг из архива': [archive_books_count()]
    }

    fundraising_data = {
        'Название': [],
        'Кол-во купивших пользователей': [],
        'Собранная сумма': [],
        'Прогресс': []
    }
    for book in Book.objects.all():
        fundraising_data['Название'].append(book.name)
        fundraising_data['Собранная сумма'].append(book.collected_sum)

        buy_users_count = book.user.all().count()
        fundraising_data['Кол-во купивших пользователей'].append(buy_users_count)

        progress = '100%' if book.collected_sum > book.goal_sum else f'{round((book.collected_sum / book.goal_sum) * 100)}%'
        fundraising_data['Прогресс'].append(progress)

    archive_stat_data = {
        'id': [],
        'Заголовок': [],
        'Автор': [],
        'Год': [],
        'Жанр': [],
        'Ссылка на книгу': [],
        'Цена архивной книги': [],
        'Кол-во обращений': [],
        'Кол-во покупок': []
    }

    # for arc_book in BookArchive.objects.all():
    #     archive_stat_data['id'].append(arc_book.id)
    #     archive_stat_data['Заголовок'].append(arc_book.title)
    #     archive_stat_data['Автор'].append(arc_book.author)
    #     archive_stat_data['Год'].append(arc_book.year)
    #     archive_stat_data['Жанр'].append(arc_book.genre)
    #     archive_stat_data['Ссылка на книгу'].append(arc_book.link)
    #     archive_stat_data['Цена архивной книги'].append(arc_book.price)
    #     archive_stat_data['Кол-во обращений'].append(arc_book.appeal)
    #     archive_stat_data['Кол-во покупок'].append(PurchasedArchiveBook.objects.filter(book=arc_book.pk).count())

    if not os.path.exists('static'):
        os.mkdir('static')
    file_path = r'static/stats.xlsx'
    writer = pd.ExcelWriter(file_path, engine='xlsxwriter')

    pd.DataFrame(users_data).to_excel(writer, sheet_name='Пользователи', index=False)
    pd.DataFrame(fundraising_data).to_excel(writer, sheet_name='Фандрайзинг', index=False)
    pd.DataFrame(subscribes_data).to_excel(writer, sheet_name='Подписки', index=False)
    pd.DataFrame(referrals_data).to_excel(writer, sheet_name='Реферальные коды', index=False)
    pd.DataFrame(statistics_data).to_excel(writer, sheet_name='Статистика', index=False)
    # pd.DataFrame(archive_stat_data).to_excel(writer, sheet_name='Статистика архив', index=False)

    writer.save()
    writer.close()

    return FileResponse(open(file_path, 'rb'))
