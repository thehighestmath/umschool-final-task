# Финальный проект: Телеграм-бот для проведения опросов

> [!NOTE]
> Этот финальный проект точно решаемый

## Цель проекта
Вам нужно создать приложение для работы с опросами, используя любую реляционную базу данных (на курсе была PostgreSQL), а также телеграмм, как посредник между клиентом (конечным пользователем) и программой (сервером).

## Требования:

- Приложение должно иметь разделение на админов (набор telegram IDов) и простых пользователей (всех остальных)
- Приложение должно использовать состояния
- Приложение должно иметь как минимум две связных таблички (чтобы в коде были не просто select/update/insert, а ещё и join). Вместо написания "сырых" sql запросов можно использовать какую-нибудь ORM, например (https://www.sqlalchemy.org/)
- При попытке пользователя ответить на вопрос он должен получать гарантированно уникальный вопрос (т.е. такой вопрос, на который он ещё не отвечал)


### Примерное распределение ролей

|                           | Админы   | Обычные пользователи   |
|:--------------------------|:--------:|:----------------------:|
| проходят опрос            | +        | +                      |
| смотрят личную статистику | +        | +                      |
| смотрят общую  статистику | +        | -                      |
| создают вопрос            | +        | -                      |
| удаляют вопрос            | +        | -                      |

### Примерная структура базы данных

#### Таблица вопросов (question)

|   id(bigint) | question_text(varchar)                       | publish_date(timestamp) |
|-------------:|:---------------------------------------------|:------------------------|
|            1 | Во всех ли городах России есть вечный огонь? | 2024-01-29T03:00:00Z    |
|            2 | Вам нравится ваша школа?                     | 2024-02-21T13:00:00Z    |


#### Табилца вариантов ответа (choice)

|   id(bigint) | choice_text(varchar)   |   votes(integer) |   question_id(bigint) |
|-------------:|:-----------------------|-----------------:|----------------------:|
|            1 | Да                     |               15 |                     1 |
|            2 | Нет                    |                2 |                     1 |
|            3 | Не знаю                |                5 |                     1 |
|            4 | Да, очень              |                7 |                     2 |
|            5 | Нет                    |                8 |                     2 |

#### Таблица статистики пользователей
|   id(bigint) |   tg_user_id(integer) |   question_id(bigint) |   choice_id(bigint) |
|-------------:|----------------------:|----------------------:|--------------------:|
|            1 |                   228 |                     1 |                   1 |
|            2 |                   228 |                     3 |                   2 |
|            3 |                   228 |                     2 |                   4 |
|            4 |                  1337 |                     1 |                   5 |
|            5 |                  1337 |                     3 |                   1 |
|            6 |                  1337 |                     2 |                   1 |


## Жесткий дисклеймер. Это всё лишь пожелания, отходить от них можно, просто так будет чуть больше ясности что хочется видеть в результате :)

### Сценарии использования

## Сценарий использования "Прохождение опроса"
### Действующее лицо:
* Любой пользователь
### Основной сценарий:
1. Пользователь жмет на кнопку "прохождение опроса" (или аналогичную ей)
2. Пользователь получает вопрос [ **вопрос обязательно должен быть опубликованным**, мы же не из будующего :) ], ответ на который он ещё не давал, с вариантами ответа в тектовом виде и инлайн клавиатуру под сообщением
3. Пользователь должен выбрать вариант ответа либо инлайн клавиатурой, либо напечатав и отправив номер ответа сообщением в ответ
### Результат:
Учтенный ответ пользователя


## Сценарий использования "Просмотр личной статистики"
### Действующее лицо:
* Любой пользователь
### Основной сценарий:
1. Пользователь жмет на кнопку "получить личную статистику" (или аналогичную ей)
### Результат:
Пользователь получает в ответном сообщении личную статистику по опросам

Примерный вывод

```
Вопрос 1: Во всех ли городах Росиии есть вечный огонь? -- Да

Вопрос 2: Вам нравится ваша школа? -- Да, очень

...
```



## Сценарий использования "Создание вопроса"
### Действующее лицо:
* Админ
### Основной сценарий:
1. Админ жмет на кнопку "создать вопрос" (или аналогичную ей)
2. После чего админ вводит сам вопрос
3. Следующим сообщением админ отправляет список ответов. Каждый новый ответ на **новой** строке
4. Вводит время публикации опроса `publish_date`
### Результат:
В базу добавился новый вопрос



## Сценарий использования "Удаление вопроса"
### Действующее лицо:
* Админ
### Основной сценарий:
1. Админ жмет на кнопку "удалить вопрос" (или аналогичную ей)
2. Админу отправляется список вопросов и клавиатура с номерами вопросов
3. Админ должен выбрать номер вопроса либо инлайн клавиатурой, либо напечатав и отправив номер вопроса сообщением в ответ
### Результат:
Вопрос **с его вариантами ответа, статистика всех пользователей, ответивших на этот вопрос** с введенным номером удаляется из базы


## Сценарий использования "Просмотр общей статистики"
### Действующее лицо:
* Админ
### Основной сценарий:
1. Админ жмет на кнопку "получить общую статистику" (или аналогичную ей)
### Результат:
Админ получает в ответном сообщении общую статистику по опросам

Примерный вывод

```
Вопрос 1: Во всех ли городах России есть вечный огонь?
Приняло участие: 20 человек
Ответы:
- Да -- 15
- Нет -- 2
- Не знаю -- 5

Вопрос 2: Вам нравится ваша школа?
Приняло участие: 19 человек
Ответы:
- Да, очень -- 7
- Нет -- 8
```
