import time

import pandas as pd
from django.core.management.base import BaseCommand

from book_archive.models import Author, Genre, BookArchive


class Command(BaseCommand):
    help = 'Парсинг книг из csv-файлов'

    def handle(self, *args, **kwargs):
        start_time = time.time()
        count = {
            'author': 0,
            'genre': 0,
            'book': 0
        }
        reader = pd.read_csv('data/books_archive.csv', delimiter=';')
        for index, row in reader.iterrows():
            print(f"--------- Parce row with id: {row['id']} ---------")
            data = {
                'id': row['id'],
                'title': row['title'],
            }
            if 'http' in row['link']:
                data['link'] = row['link']

            if row['author'].strip():
                title = row['author'].strip().replace(';', '')
                author, res = Author.objects.get_or_create(title=title)
                data['author'] = author
                if res:
                    print(f'Новый автор: {author.title}')
                    count['author'] += 1

            try:
                if row['genre'].strip():
                    title = list(row['genre'].split(','))[0]
                    genre, res = Genre.objects.get_or_create(title=title.strip())
                    data['genre'] = genre
                    if res:
                        print(f'Новый жанр: {genre.title}')
                        count['genre'] += 1
            except AttributeError:
                pass

            if row['price']:
                data['price'] = row['price']

            if row['year'].strip():
                data['year'] = ''.join(filter(str.isdigit, str(row['year'].strip())))
                if not data['year']:
                    del data['year']

            try:
                book, res = BookArchive.objects.get_or_create(**data)
            except Exception as e:
                print(f'Error adding: {str(data)}')
                continue
            if res:
                print(f'Новая книга: {book.title}')
                count['book'] += 1

        print('Новых авторов: ', count['author'])
        print('Новых жанров: ', count['genre'])
        print('Новых книг: ', count['book'])
        print("--- %s seconds ---" % (time.time() - start_time))
