from datetime import datetime


def get_connection_to_data_base():
    pass


def decorator_add_connection(func):
    def wrapper(*args, **kwargs):
        connection = get_connection_to_data_base()
        result = func(*args, **kwargs, connection=connection)
        connection.close()
        return result

    return wrapper


@decorator_add_connection
def create_tables_from_db(connection=None):
    """
    создать таблицы в бд
    """
    pass


@decorator_add_connection
def delete_question_by_id_db(question_id: int, connection=None):
    """
    удалить вопрос, варианты ответа, а также всю статистику связанную с ним из бд
    """
    pass


@decorator_add_connection
def add_question_to_db(
    question_text: str, publish_date: datetime, connection=None
) -> int:
    """
    добавить вопрос в бд
    """
    pass


@decorator_add_connection
def add_choice_to_db(choice_text: str, question_id: int, connection=None):
    """
    добавить ответ в бд
    """
    pass


@decorator_add_connection
def get_all_stat(connection=None) -> list[list]:
    """
    получить статистику пользователей
    """
    return [[]]


@decorator_add_connection
def get_personal_stat(telegram_id, connection=None) -> list[list]:
    """
    получить личную статистику пользователя
    """
    return [[]]


@decorator_add_connection
def get_random_question(telegram_id, connection=None) -> tuple[int, str]:
    """
    получить случайный, неотвеченный вопрос из бд

    return: tuple[int, str]
    int -- question.id
    str -- question.text
    """
    return (0, "example")


@decorator_add_connection
def get_choices_by_question_id(question_id: int, connection=None) -> list[str]:
    """
    получить ответы по заданному question_id
    """
    return []


@decorator_add_connection
def add_user_vote_db(choice_id, telegram_id, connection=None):
    """
    добавить голос пользователя выбранному варианту ответа
    """
    pass


if __name__ == "__main__":
    create_tables_from_db()
