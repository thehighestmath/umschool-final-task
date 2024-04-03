from tabulate import tabulate

questions = [
  [1, "Во всех ли городах России есть вечный огонь?", "2024-01-29T03:00:00Z"],
  [2, "Вам нравится ваша школа?", "2024-02-21T13:00:00Z"],
]

head = ["id(bigint)", "question_text(varchar)", "publish_date(timestamp)"]

print(tabulate(questions, headers=head, tablefmt="pipe"))

choice = [
  [1, "Да", 15, 1],
  [2, "Нет", 2, 1],
  [3, "Не знаю", 5, 1],

  [4, "Да, очень", 7, 2],
  [5, "Нет", 8, 2],
#   [6, "Нейтрально", 3, 2],
#   [7, "Ненавидел преподов", 1, 2],
#   [8, "Ненавидел систему", 2, 2],
]

head = ["id(bigint)", "choice_text(varchar)", "votes(integer)", "question_id(bigint)"]

print(tabulate(choice, headers=head, tablefmt="pipe"))



roles = [
    ["проходят опрос", "+", "+"],
    ["смотрят личную статистику", "+", "-"],
    ["смотрят общую статистику", "+", "-"],
    ["создают вопрос", "+", "-"],
    # ["редактируют вопрос", "+", "-"],
    ["удаляют вопрос", "+", "-"],
]

head = ["", "Админы", "Обычные пользователи"]

print(tabulate(roles, headers=head, tablefmt="pipe"))


user_stat = [
    [1, 228, 1, 1],
    [2, 228, 3, 2],
    [3, 228, 2, 4],
    [4, 1337, 1, 5],
    [5, 1337, 3, 1],
    [6, 1337, 2, 1],
]

head = ["id(bigint)", "tg_user_id(integer)", "question_id(bigint)", "choice_id(bigint)"]

print(tabulate(user_stat, headers=head, tablefmt="pipe"))
