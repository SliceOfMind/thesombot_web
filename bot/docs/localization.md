# Локализация
***thesombot*** - **домен для I18N из окружения (можно менять на любой другой)**
### Запускаем первый раз
Вытаскиваем тексты из файлов (он сам находит)

`pybabel extract . -o tgbot/locales/thesombot.pot`

Создаём папку для перевода на английский

`pybabel init -i tgbot/locales/thesombot.pot -d tgbot/locales -D thesombot -l en`

То же, на русский

`pybabel init -i tgbot/locales/thesombot.pot -d tgbot/locales -D thesombot -l ru`

Переводим, а потом собираем переводы

`pybabel compile -d tgbot/locales -D thesombot`

### Обновляем переводы
Вытаскиваем тексты из файлов

`pybabel extract . -o tgbot/locales/thesombot.pot`

Добавляем текст в переведенные версии

`pybabel update -d tgbot/locales -D thesombot -i tgbot/locales/thesombot.pot`

Вручную делаем переводы, а потом собираем

`pybabel compile -d tgbot/locales -D thesombot`

### Локализация в админ панели
 В админ панели используется django-rosette модуль для чтения и редактирования файлов локализации
 Все файлы локализации идут из бота, потому что основаны на используемых в нем фразах.