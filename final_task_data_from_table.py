from tabulate import tabulate

roles = [
    ["получают информацию о себе из таблиц", "+", "+"],
    ["получают информацию о выбранном студенте из таблиц", "+", "-"],
    ["получают общую статистику по запросам в гугл таблицу", "+", "-"],
    ["получают персонализированную статистику по запросам в гугл таблицу", "+", "-"],
    ["добавлять таблицы в список, из которого студены получают данные", "+", "-"],
    ["удалять таблицы из списка, из которого студены получают данные", "+", "-"],
    ["конфигурировать таблицы из списка, из которого студены получают данные", "+", "-"],
]

print('\n'.join(list(map(lambda x: x[0], roles))))

head = ["", "Админы", "Студенты"]

print(tabulate(roles, headers=head, tablefmt="pipe"))

spreadsheets = [
  [1, "https://docs.google.com/spreadsheets/d/1Uw_-MabomGt1wJEUHq5VER1xUgBWoucpc26y2oa46cY/edit?gid=0#gid=0", "Рейтинг весна 2024"],
  [2, "https://docs.google.com/spreadsheets/d/1xBhHC6xChN3Jpg7de_1RnCvvI9iX5-084CzZHq4IEAI/edit?gid=1697350159#gid=1697350159", "Преддипломная практика, МОЭВМ 24"],
]

head = ["id(bigint)", "link(varchar)", "name(varchar)"]

print(tabulate(spreadsheets, headers=head, tablefmt="pipe"))

sheets = [
  [1, "Оценки-Программирование", "1Uw_-MabomGt1wJEUHq5VER1xUgBWoucpc26y2oa46cY"],
  [2, "Оценки-ИТ", "1Uw_-MabomGt1wJEUHq5VER1xUgBWoucpc26y2oa46cY"],
]

head = ["id(bigint)", "name(varchar)", "spreadsheetID(integer)"]

print(tabulate(sheets, headers=head, tablefmt="pipe"))

students = [
    [1, 228, "Chegodaev Kondratiy Sergeevich", "0381"],
    [2, 1337, "Chegodaeva Elizaveta Alexandrovna", "3383"],
]

head = ["id(bigint)", "tg_user_id(integer)", "name(varchar)", "group_id(varchar)"]

print(tabulate(students, headers=head, tablefmt="pipe"))
