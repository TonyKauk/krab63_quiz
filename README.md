# krab63_quiz
Выполненное тестовое задание "Тестирование" для Краб63

## Основной функционал:
- Добавление, удаление и редактирование тестов, вопросов, вариантов ответов
через админку
- Прохождение тестов
- Проставление правильных ответов по запросу
- Парсинг тестов с внешних ресурсов
- Просмотр результатов своих тестов в личном кабинете

## Технологии:
- Python 3.11.0
- Django 4.1.4
- Django REST Framework 3.14.0
- jQuery 3.6.3
- Bootstrap 5
- Сelery 5.2.7
- Redis 4.4.2

## Особенности:
- Реализован на HTML шаблонах
- Регистрация, вход и выход пользователей
- Для добавления локальных настроек проекта добавьте файл 'settings_local.py'
в папке с 'settings.py'.
- Настроен парсинг тестов по расписанию

## Установка
Клонировать репозиторий и перейти в скопированную директорию:

```
git clone https://github.com/TonyKauk/krab63_quiz.git
cd krab63_quiz
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

Выполнить миграции:

```
cd krab63_quiz
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

Для запуска Celery, который будет по расписанию (каждую минуту) парсить тесты:

```
redis-server
python3 -m celery -A krab63_quiz worker -l info
python3 -m celery -A krab63_quiz beat -l info
```

Проект доступен в браузере по адресу: http://127.0.0.1:8000/

## Автор
Антон Милов
