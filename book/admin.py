from django.contrib import admin

from book.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date', 'goal_sum', 'collected_sum', 'is_done', 'is_available']
    readonly_fields = ['collected_sum', 'is_notification_sent']

    list_editable = ['is_available']


