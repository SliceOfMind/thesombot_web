from django.contrib import admin

from book_archive.models import Author, Genre, BookArchive, PurchasedArchiveBook


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(BookArchive)
class BookArchiveAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'genre', 'year', 'buy_count']
    list_display_links = ['id', 'title', 'author', 'genre', 'year']
    fields = ['title', 'author', 'genre', 'year', 'link', 'price', 'buy_count']
    readonly_fields = ['buy_count']
    search_fields = ['title']

    def buy_count(self, obj):
        return len(PurchasedArchiveBook.objects.filter(book_id=obj.id))

    buy_count.short_description = 'Кол-во покупок'
