### Загрузка фикстур
Есть django фикстуры для:

* Языков - lang.json
* Статуса оплаты - payment_status.json
* Статистики - statistic.json
* Статуса подписки - subscribe_status.json
* Настройки - settings.json

 Загружать их нужно после установки полной установки проекта: 
 > python3.10 manage.py loaddata lang.json payment_status.json statistic.json subscribe_status.json settings.json

### Загрузка жанров
Жанры загружаем из отдельного дампа
> 
 
### Команды
В проекте есть 2 кастомные команды для django.

1. parse_csv - book_archive/management/commands/parse_csv.py - Переводит все файлы лежащие в папке data в книги из архива. 
Для корректной работы ей нужна предварительно заполненная таблица Genre.
2. parse_users - config/management/commands/parse_users.py - 
Переносит пользователей из users.csv в базу. Нужна только для миграции с mysql на postgresql