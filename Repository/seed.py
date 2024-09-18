from Repository.answer_repository import find_all_answers
from Repository.database import create_tables, drop_all_tables
from Repository.question_repository import find_all_questions
from Repository.trivia_repository import load_trivia_data_from_api


def seed():
    create_tables()
    questions = find_all_questions()
    answers = find_all_answers()
    if not questions or not answers:
        load_trivia_data_from_api()


