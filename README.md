# ultimate_shop
Ultimate shop - API интернет магазина на FastAPI + postgres and etc

# Техническое задание
```
  Создать интернет магазин(копия https://market.yandex.by/)
  Функциональные фичи:
  - Товары
  - Поиск товаров(как по названию так и по критериям)
  - Промокоды
  - Корзина
  - Отзывы
  - Профиль
  - Лента рекомендаций
```

## Архитектура

Архитектура проекта - сервисная архитектура.
```
Пока под капотом 4 сервиса:
 - сервис авторизации
 - основной сервис с бизнес логикой
 - сервис для работы с файлами
 - сервис для работы с поиском
 ```

## Стек
```
  - FastAPI
  - JWT - авторизация
  - Postgres - база данных
  - Docker & Docker-compose - для развертывания
  - Alembic - для миграций
  - Pytest - для тестов
  - SQLAlchemy - ORM
  - Swagger - автодокументация для API
  - Pydantic - валидация
  - Prometheus & Grafana - мониторинг
  - Yandex Cloud - для хранения статики(картинки и так далее)
  - ElasticSearch - для полнотекстового поиска
  - black & isort & pylint & raff - линтеры
```
## Сущности
```
 - Пользователь
 - Промокод
 - Товар
 - Категория
 - Заказ
 - Отзыв
 - Статика(сущность files_service)
```
