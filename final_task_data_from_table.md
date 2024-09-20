# Финальный проект: Телеграм-бот для доступа к данным студентов через Google Sheets

> [!WARNING]
> Это новый финальный проект. Удачи!

## Цель проекта
Вам нужно создать приложение для доступа к данным студентов, которые хранятся в гугл таблицах, используя любую реляционную базу данных (на курсе была PostgreSQL), а также телеграмм, как посредник между клиентом (конечным пользователем) и программой (сервером).

Разработка Telegram-бота, который предоставляет студентам доступ к их личным данным, хранящимся в Google Sheets. Бот также ведет учет и логирование всех запросов в реляционной базе данных, доступ к которой имеют только администраторы для контроля действий.

## Требования:
- Приложение должно иметь разделение на админов (набор telegram IDов) и простых пользователей (всех остальных)
- Приложение должно использовать состояния
- Приложение должно иметь как минимум две связных таблички (чтобы в коде были не просто select/update/insert, а ещё и join). Вместо написания "сырых" sql запросов можно использовать какую-нибудь ORM, например (https://www.sqlalchemy.org/)
- Приложение должно получать данные из гугл таблицы. Есть полезные библиотеки, например библиотека от самого гугла (https://github.com/googleapis/google-api-python-client)
- Студент должен гарантированно получать только свои данные, получение данных другого студента **не** допускается
- Приложение должно использовать кэш [ https://en.wikipedia.org/wiki/Cache_(computing) , https://habr.com/ru/companies/google/articles/316344/ ]. Кеш должен сохранять данные из гугл таблиц в базу данных, чтобы не нагружать google spreadsheets api. Кеш должен иметь время, через которое он должен становиться **не**действительным. Тогда запрос в гугл таблицу нужно посылать ещё раз. А пока кеш действителен - нужно брать данные из базы данных, а не ходить за данными по сети Интернет

### Примерное распределение ролей

Админы:
- получают информацию о себе из таблиц
- получают информацию о выбранном студенте из таблиц
- получают общую статистику по запросам в гугл таблицу
- получают персонализированную статистику по запросам в гугл таблицу
- добавлять таблицы в список, из которого студены получают данные
- удалять таблицы из списка, из которого студены получают данные
- конфигурировать таблицы из списка, из которого студены получают данные

Студенты:
- получают информацию о себе из таблиц

### Примерная структура базы данных

#### Таблица таблиц (spreadsheet)

|   id(bigint) | link(varchar)                                                                                                          | name(varchar)                    |
|-------------:|:-----------------------------------------------------------------------------------------------------------------------|:---------------------------------|
|            1 | https://docs.google.com/spreadsheets/d/1Uw_-MabomGt1wJEUHq5VER1xUgBWoucpc26y2oa46cY/edit?gid=0#gid=0                   | Рейтинг весна 2024               |
|            2 | https://docs.google.com/spreadsheets/d/1xBhHC6xChN3Jpg7de_1RnCvvI9iX5-084CzZHq4IEAI/edit?gid=1697350159#gid=1697350159 | Преддипломная практика, МОЭВМ 24 |

#### Таблица листов (sheet)

|   id(bigint) | name(varchar)           | spreadsheetID(integer)                       |
|-------------:|:------------------------|:---------------------------------------------|
|            1 | Оценки-Программирование | 1Uw_-MabomGt1wJEUHq5VER1xUgBWoucpc26y2oa46cY |
|            2 | Оценки-ИТ               | 1Uw_-MabomGt1wJEUHq5VER1xUgBWoucpc26y2oa46cY |

#### Таблица студентов (student)

|   id(bigint) |   tg_user_id(integer) | name(varchar)                     |   group_id(varchar) |
|-------------:|----------------------:|:----------------------------------|--------------------:|
|            1 |                   228 | Chegodaev Kondratiy Sergeevich    |                0381 |
|            2 |                  1337 | Chegodaeva Elizaveta Alexandrovna |                3383 |

## Жесткий дисклеймер. Это всё лишь пожелания, отходить от них можно, просто так будет чуть больше ясности что хочется видеть в результате :)

### Сценарии использования

TBD: