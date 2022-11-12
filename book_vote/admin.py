from django.contrib import admin

from book_vote.models import VoteBook, UserBookVote


@admin.register(VoteBook)
class VoteBookAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'get_votes_count', 'vote_goal', 'fund_need', 'is_visible',
                    'is_fund_sent', 'user']
    list_editable = ['is_visible']
    readonly_fields = ['created_at', 'is_fund_sent']

    def get_votes_count(self, obj):
        return UserBookVote.objects.filter(book=obj).values('user').count()

    get_votes_count.short_description = 'Голоса'


@admin.register(UserBookVote)
class UserBookVoteAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'book', 'user']

    # def has_add_permission(self, request):
    #     return False
    #
    # def has_delete_permission(self, request, obj=None):
    #     return False
