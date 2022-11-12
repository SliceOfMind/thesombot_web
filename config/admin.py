from django.contrib import admin
from django.contrib.auth.models import User, Group
from django_celery_beat.models import *

from . import models

admin.site.site_header = "Админ-панель Slice of Mind"
admin.site.site_title = "Панель администрирования"
admin.site.index_title = "Добро пожаловать в админку"

admin.site.unregister(User)
admin.site.unregister(Group)

# Remove django-celery-beat app from admin site
admin.site.unregister(IntervalSchedule)
admin.site.unregister(CrontabSchedule)
admin.site.unregister(SolarSchedule)
admin.site.unregister(ClockedSchedule)
admin.site.unregister(PeriodicTask)


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('mention', 'username', 'balance', 'referral', 'is_block', 'language', 'show_progress')
    list_display_links = ['mention', 'mention']
    search_fields = ['telegram_id', 'username']
    list_filter = ('balance', 'referral', 'is_block')
    fields = (
        'telegram_id', 'mention', 'username', 'balance', 'deposit', 'subscribe_time', 'referral', 'is_block',
        'language', 'show_progress')
    # readonly_fields = (
    #     'telegram_id', 'mention', 'username', 'referral', 'is_block', 'language_id', 'show_progress', 'subscribe_time')

    # def has_add_permission(self, request):
    #     return False
    #
    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(models.Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']

    save_on_top = True


@admin.register(models.Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ['name']
    fields = ['question_symbols_limit', 'top_up_limit', 'book_title_limit', 'promo_code_limit', 'author_limit']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'from_user', 'is_answered', 'date']
    fields = ['text', 'answer', 'is_answered', 'from_user']
    readonly_fields = ['text', 'is_answered', 'from_user']
    list_filter = ['is_answered', 'from_user']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(models.Referral)
class ReferralAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'link', 'register_count']
    readonly_fields = ['link', 'register_count']
