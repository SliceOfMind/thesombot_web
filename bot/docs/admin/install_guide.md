# Деплой
### Админка: gunicorn, nginx, redis, postgresql

Клонируем [репозиторий](https://github.com/cmdrBebop/thesombot_web.git) с админкой по [ssh](https://sendel.ru/posts/https-to-ssh-on-github/):
>git clone git@github.com:cmdrBebop/thesombot_web.git

Клонируем [репозиторий](https://github.com/cmdrBebop/thesombot_tg.git) с ботом:
>git clone git@github.com:cmdrBebop/thesombot_tg.git

Обновляем и устанавливаем нужные пакеты:
> sudo apt update && install nvim redis-server nginx zlib1g-dev libbz2-dev libreadline-dev llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev liblzma-dev python3-dev python-imaging python3-lxml libxslt-dev python-libxml2 python-libxslt1 libffi-dev libssl-dev python-dev gnumeric libsqlite3-dev libpq-dev libxml2-dev libxslt1-dev libjpeg-dev libfreetype6-dev libcurl4-openssl-dev supervisor

### Установка PostgreSql

> sudo apt install postgresql postgresql-contrib

> sudo service postgresql start

> sudo -u postgres psql

> create user ИМЯ password 'ПАРОЛЬ';

> create database db_name owner username;

### Настройка nginx
Создаем конфиг и помещаем его сюда
> конфиг

### Настройка gunicorn
> gunicorn --bind 0.0.0.0:8000 myproject.wsgi

Подробнее [тут](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04)

### Установка redis-server
> sudo apt install redis-server

> sudo nano /etc/redis/redis.conf

Нужно найти строчку `supervised no` и заменить на `supervised systemd`

> sudo systemctl restart redis.service

Чтобы убедиться, что все работает
> redis-cli
> 
> ping

Ответом должен быть `pong`
### Настройка venv
> python -m venv venv

> . /venv/bin/activate

> pip install -r requirements.txt

### Запуск через screen
Для просмотра:
> screen -ls

Для подключения:
> screen -r номер

Для фонового режима
> ctrl + a затем d

Админка
> screen
> . venv/bin/activate
> python3 manage.py runserver 0.0.0.0:8001

Бот
> screen
> . venv/bin/activate
> python3 app.py

После всей установки, описанной в данном файле, нужно создать локали. После генерации локалей их надо заполнить через админ-панель или загрузить уже готовые переводы и скомпилировать

