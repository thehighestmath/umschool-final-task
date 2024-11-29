from . import (
    add_question,
    delete_question,
    person_stats,
    all_stats,
    get_survey,
)


def register_handlers(bot):
    add_question.register_handlers(bot)
    delete_question.register_handlers(bot)
    person_stats.register_handlers(bot)
    all_stats.register_handlers(bot)
    get_survey.register_handlers(bot)
