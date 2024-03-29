# Electronics_shop_DRF
Модель сети по продаже электроники

#### Структура проекта:
config/
1. settings.py - настройки приложений
2. urls.py - файл маршрутизации

shop/
1. admin.py - настройки админки
2. models.py - модели приложения
3. serializers.py - сериализаторы для моделей
4. urls.py - файл маршрутизации приложения
5. views.py - эндпоинты

users/
1. management/commands
  1). create_user.py - кастомная команда создания пользователя
  2). csu.py - кастомная команда создания суперпользователя
2. admin.py - настройки админки
3. models.py - модели приложения
4. permissons.py - разрешения для пользователей
5. urls.py - файл маршрутизации приложения


.env.sample - необходимые переменные окружения

network.json - фикстуры для приложения shop

manage.py - точка входа веб-приложения

requirements.txt - список зависимостей для проекта.

#### Используется виртуальное окружение env

#### Для запуска web-приложения используйте команду "python manage.py runserver" либо через конфигурационные настройки PyCharm.

# Установка

1. Клонируйте данный репозиторий
2. Установите Python, PostgreSQL
3. Установите и активируйте виртуальное окружение.
4. Установите зависимости из файла requirements.txt
5. Создайте файл .env по шаблону .env.sample
6. Установите миграции: python3 manage.py migrate
7. Запустите команду, чтобы создать супер пользователя, для доступа в административную панель:
  - python3 manage.py csu
8. Можно воспользоваться командой: python manage.py loaddata network.json для заполнения БД с помощью фикстур
8. Запустите веб-приложение
