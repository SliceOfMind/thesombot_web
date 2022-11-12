from django.contrib import admin

from book_request.models import BookRequest
from book_vote.models import VoteBook


@admin.register(BookRequest)
class BookRequestAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'genre', 'year', 'user', 'is_approved']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
