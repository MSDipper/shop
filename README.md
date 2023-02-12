<h2 alingn='center'></h2>

### Описание проекта:
    Интернет магазин.
    Добавление товара через админ панель.
    Оформление заказа.
    Возможность распечатки заказа в выбраном формате (cvs, txt).
    Возможность добавление купона через админ панель и активация купона во время оформления заказа для скидки.
    Пагинация.
    Проверка капчей, во время оформление заказа.
    Фильтрация товара по выбраным параметрам.
    Поиск товара или блога.
    Возможность добавления блога.
    Регистрация и авторизация пользователей.
    
## Разработка
    ДА


##### 1) Клонировать репозиторий

    git clone ссылка_сгенерированная_в_вашем_репозитории

##### 2) Создать виртуальное окружение

    python -m venv venv
    
##### 3) Активировать виртуальное окружение

    venv\Scripts\activate.bat - Windows

    venv/bin/activate - Linux

##### 4) Устанавливить зависимости:

    pip install -r req.txt

##### 5) Выполнить команду для выполнения миграций

    python manage.py migrate

##### 6) Запустите redis на pc или через контейнер Docker

    redis-cli -h 0.0.0.0 -p 6379
    
    or

    docker pull redis

##### 7) Запустите в консоле Celery

    celery -A shop worker -l info
 

##### 8) Запустите в консоле flower для отслежавания состояния задач

    celery -A shop flower


##### 9) Создать суперпользователя

    python manage.py createsuperuser
    
##### 10) Запустить сервер

    python manage.py runserver
