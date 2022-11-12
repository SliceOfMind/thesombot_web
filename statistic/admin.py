from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from statistic.models import Statistic
from subscribe.models import Subscribe
from config.models import User
from book_archive.models import PurchasedArchiveBook


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ['name', 'subs_link', 'ref_link', 'fund_books', 'archive_books']
    readonly_fields = ['name', 'all_subs_counter', 'no_buy_users_counter', 'block_users_counter', 'archive_books_sum',
                       'archive_books_count']

    def all_subs_counter(self, obj):
        return len(Subscribe.objects.all())

    all_subs_counter.short_description = 'Общее количество купивших подписку за все время'

    def no_buy_users_counter(self, obj):
        all_users_count = len(User.objects.all())
        subscribes = Subscribe.objects.all()
        users_with_subscribe = set()
        for subscribe in subscribes:
            users_with_subscribe.add(subscribe.user)
        return all_users_count - len(users_with_subscribe)

    no_buy_users_counter.short_description = 'Количество пользователей не купивших подписку'

    def block_users_counter(self, obj):
        return len(User.objects.filter(is_block=True))

    block_users_counter.short_description = 'Количество пользователей заблокировавших бота'

    def archive_books_count(self, obj):
        return len(PurchasedArchiveBook.objects.all())

    archive_books_count.short_description = 'Количество купленных книг из архива'

    def archive_books_sum(self, obj):
        all_sum = 0
        for book in PurchasedArchiveBook.objects.all():
            all_sum += book.book.price
        return all_sum

    archive_books_sum.short_description = 'Сумма покупок книг из архива'

    def subs_link(self, obj):
        url = (
            reverse('admin:subscribe_subscribe_changelist')
        )
        return format_html('<a href="{}">Подписки</a>', url)

    subs_link.short_description = 'Подписки'

    def ref_link(self, obj):
        url = (
            reverse('admin:config_referral_changelist')
        )
        return format_html('<a href="{}">Реферальные коды</a>', url)

    ref_link.short_description = 'Реферальные коды'

    def fund_books(self, obj):
        url = (
            reverse('admin:book_book_changelist')
        )
        return format_html('<a href="{}">Книги</a>', url)

    fund_books.short_description = 'Книги'

    def archive_books(self, obj):
        url = (
            reverse('admin:book_archive_bookarchive_changelist')
        )
        return format_html('<a href="{}">Архив</a>', url)

    archive_books.short_description = 'Архив книг'

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
