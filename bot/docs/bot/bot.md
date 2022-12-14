# Телеграм бот
GitHub бота: [*Тык*](https://github.com/cmdrBebop/thesombot_tg)

Полностью написан на фреймворке `Aiogram`
## Окружение
* `BOT_CONTAINER_NAME` - Название докер контейнера
* `BOT_IMAGE_NAME` - Название докер образа
* `BOT_NAME` - Название бота
* `BOT_TOKEN` - Токен бота
* `USE_REDIS` - Использовать ли Redis
* `DB_USER` - Пользователь БД
* `DB_PASS` - Пароль от БД
* `DB_NAME` - Название БД
* `DB_HOST` - Хост БД
* `DB_PORT` - Порт БД
* `I18N_DOMAIN` - Домен для I18N
* `UPDATES_FROM_SERVER_INTERVAL` - Интервал получения обновлений с сервера в минутах
* `OPERATIONS_CHECK_INTERVAL` - Интервал проверки операций
* `SUBSCRIBES_CHECK_INTERVAL` - Интервал проверки подписок
* `ACCOUNT_ID` - ID аккаунта для YooKassa
* `SECRET_KEY` - Секретный ключ для YooKassa
* `RETURN_URL` - Обратный URL для YooKassa
* `GENRES_ROWS_PER_PAGE` - Количество строк с хештегами
* `GENRES_IN_ROW` - Количество хештегов в строке
* `SEARCH_BOOKS_PER_PAGE` - Количество строк с книгами в результате поиска
* `WEB_BASE_DIR` - Путь к админке

Пример окружения лежит в файле `.env.dist`

---

## Описание модулей

### Структура проекта
* Папка `tgbot/filters` - все фильтры
* Папка `tgbot/handlers` - все хендлеры
* Папка `tgbot/keyboards` - все inline и reply клавиатуры
* Папка `tgbot/locales` - переводы
* Папка `tgbot/middlewares` - все мидлвари
* Папка `tgbot/misc` - разное/остальное
* Папка `tgbot/services` - все сервисы
* Файл `tgbot/config.py` - настройки бота
* Файл `bot.py` - запуск бота

**Все папки - пакеты `python`**

### Папка `tgbot/handlers`
Все хендлеры собираются в файле `__init__.py` для удобного взаимодействия

### Папка `tgbot/misc`
В файле `callbacks.py` лежат все колбеки:

* `languages` - смена языков
* `code` - код языка
* `navigation` - навигация по боту
* `to` - место направления
* `payload` - дополнительная информация
* `fundraising_book` - книга из фандрайзинга
    * `book_id` - `id` книги из базы данных (таблица `book`)
* `buy_fundraising_book` - покупка книги из фандрайзинга
    * `book_id` - `id` книги из базы данных (таблица `book`)
    * `price` - цена книги
* `change_show_progress` - изменение `show_progress` у пользовтаеля
    * `book_id` - `id` книги из базы данных (таблица `book`)
* `vote_book` - книга из голосования
    * `action` - действие с книгой (`remove`, `add` или `offer`)
    * `book_id` - `id` книги из базы данных (таблица `vote_book`)
* `cancel` - отмена ввода
    * `to` - место направления после отмены
* `payment_method_choose` - выбор способа оплаты
    * `method` - способ оплаты
    * `action` - цель оплаты (`sub` или `top_up`)
    * `amount` - сумма оплаты
    * `payload` - дополнительная информация
* `library` - архив книг
    * `action` - действие в архиве
    * `payload` - дополнительная информация
* `genre_choose` - выбор жанра для архива книг
    * `title` - название жанра из базы данных (таблица `genre`)
    * `id` - `id` жанра из базы данных (таблица `genre`)
* `search_book_choose` - выбор книги из результата поиска в архиве
    * `book_id` - `id` книги из базы данных (таблица `book_archive`)
* `buy_archive_book` - покупка книги из архива
    * `book_id` - `id` книги из базы данных (таблица `book_archive`)
    * `price` - цена книги
* `close` - удаление сообщения
    * `is_final` - используется для постов, если в `is_final` пусто для удаления сообщения по кнопке "Закрыть" нужно будет нажать 2 раза
* `promo_code` - промокод
    * `action` - действие с промокодом (`cancel` или `use`)

В файле `states.py` лежат все стейты:

* `PromoCodeState` - ввод промокода
    * `waiting_for_input` - ожидание ввода
* `QuestionState` - ввод вопроса
    * `waiting_for_input` - ожидание ввода
* `VoteState` - ввод названия книги для голосования
    * `waiting_for_input` - ожидание ввода
* `TopUpState` - ввод суммы пополнения
    * `waiting_for_input` - ожидание ввода
* `LibraryState` - взаимодействие с архивом книг
    * `in_menu` - нахождение в меню
    * `waiting_for_year_input` - ожидание ввода года
    * `waiting_for_title_input` - ожидание ввода названия
    * `waiting_for_author_input` - ожидание ввода автора
    * `waiting_for_genre_choice` - ожидание выбор жанра

### Папка `tgbot/services`

#### Папка `db` - интерфейс для взаимодействия с базой данных
* Файл `database.py` - содержит класс базы данных, при завершении работы необходимы закрывать все соединения
* Папка `workers` - содержит воркеров для таблиц базы данных
    * Файл `worker_base.py` - базовый воркер, от которого наследуются все остальные

#### Папка `schedulers` - регулярные действия
* Файл `__init__.py` - сбор всех регулярных действий и функция для их запуска
* Файл `operations_check.py` - проверка операций из таблицы `operation`
* Файл `subscribes_check.py` - проверка подписок, их деактивация и продление
* Файл `updates_from_server.py` - получение всех обновлений из базы данных:
    * Отправка новых постов (таблица `post`)
    * Отправка ответов на вопросы (таблица `question`)
    * Отправка уведомлений о доступности книги в фандрайзинге (таблица `book`)
    * Удаление старых опросов

#### Файл `custom_broadcasters.py` - классы для рассылки
Все классы наследуются от `BaseBroadcaster` из библиотеки `aiogram_broadcaster`

* `MultilingualTextBroadcaster` - мультиязычная рассылка текста
* `PollBroadcaster` - мультиязычная рассылка опросов
* `FileBroadcaster` - мультиязычная рассылка файлов\
  Все классы дополнены для удобного использования в боте:

* `text` - подставляется в `_()`
* `text_kwargs` - подставляются в `_(text).format()`
* `reply_markup_callback` - функция для получения клавиатуры, в неё сразу передается `_`
* `reply_kwargs` - подставляются в функцию для получения клавиатуры

#### Файл `yoomoney.py` - интерфейс для взаимодействия с ЮКассой, используется библиотека `yookassa`

### Файл `bot.py`
В файле происходит запуск бота:

* Включается логирование
* Загружаются настройки из окружения
* Подключается `Redis` и база данных
* Регистрируются все хендлеры, фильтры и мидлвари
* Запускаются регулярные действия
* Начинается получение апдейтов от API Telegram

При остановке бота:

* Закрываются все подключения к базе данных
* Закрывается подключение к `Redis` и сохраняются данные
* Прекращается получение апдейтов

### Общее

В боте для пользователя всегда отображается только одно меню __(если это возможно)__,
для этого при регистрации пользователя в боте в `Redis` сохраняется запись, **где ключ - Telegram ID пользователя**,
а **значение - ID сообщения с действующим меню пользователя**.

При вызовах команд `/start` и `/menu` пользователю отправляется новое меню и обновляется запись в `Redis`,
старое меню удаляется __(если это возможно)__.

При взаимодействии пользователя с ботом всегда изменятся только главное меню,
если это не возможно из-за ограничений API Telegram, то пользователю предлагается вызвать новое меню командой.
Любой ожидаемый от пользователя ввод сразу удаляется. Для всех сообщений, кроме сообщения с главным меню,
добавляется кнопка "Закрыть", которая удаляет сообщение __(если это возможно)__.



При запуске бота в его экземпляр сохраняются `config`, `database`, `_`, `redis`, `yoomoney`.
Доступ к ним осуществляется через метод `__getitem__`. Экземпляр бота можно получить в любом хендлере,
у объекта хендлера всегда есть атрибут `bot`.

