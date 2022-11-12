from django.contrib import admin
from post.models import Post, PostVote, VoteChoice, UserPoll


class ChoiceInLine(admin.TabularInline):
    model = VoteChoice
    readonly_fields = ['votes']
    extra = 0

    def votes(self, obj):
        if obj.pk:
            obj.collected_votes = UserPoll.objects.filter(choices__contains=[int(obj.pk)]).count()
        return obj.collected_votes


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'send_date', 'is_sent']
    readonly_fields = ['date', 'is_sent']

    def save_model(self, request, obj, form, change):
        if obj.vote_options:
            obj.save()
            post_vote = PostVote.objects.create(
                title=obj.title,
                post_id=obj.id)
            post_vote.save()
            options = obj.vote_options.split("\n")
            for option in options:
                option_new = VoteChoice.objects.create(
                    post_vote=post_vote,
                    choice_text=option
                )
                option_new.save()
        return super().save_model(request, obj, form, change)


@admin.register(PostVote)
class PostVoteAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['title', 'post']}), ]
    inlines = [ChoiceInLine]
