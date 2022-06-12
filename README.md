
## Процесс запуска и установки (unix системы)

> git clone https://github.com/stpn12/stp_api.git

> cd stp_api

Создание виртуального окружения

> python3 -m venv venv

Активация виртуального окружения

> source venv/bin/activate

Установка необходимых зависимостей

> pip3 install -r requirements.txt

## Запуск

> python3 manage.py runserver

Прежде, может понадобится запустить необходимые миграции:
python3 manage.py makemigrations
python3 manage.py migrate
