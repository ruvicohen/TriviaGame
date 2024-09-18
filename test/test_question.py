import pytest

from Repository.database import create_tables, get_db_connection, drop_all_tables
from Repository.question_repository import extract_question_from_trivia_data, create_question, get_id_by_question_text, \
    find_all_questions, find_question_by_id, update_question, delete_question
from Repository.seed import seed
from Repository.trivia_repository import load_trivia_data_from_api
from models.Question import Question


@pytest.fixture(scope="module")
def setup_database():
    create_tables()
    load_trivia_data_from_api()
    yield
    drop_all_tables()



def test_extract_question_from_trivia_data():
    trivia_data = {
        "question": "What is the capital of France?",
        "correct_answer": "Paris"
    }
    question = extract_question_from_trivia_data(trivia_data)
    assert question.question_text == "What is the capital of France?"
    assert question.correct_answer == "Paris"


def test_create_question(setup_database):
    question = Question(question_text="What is 2+2?", correct_answer="4")
    new_id = create_question(question)
    assert new_id > 0


def test_get_id_by_question_text(setup_database):
    question = Question(question_text="Who discovered gravity?", correct_answer="Newton")
    create_question(question)
    question_id = get_id_by_question_text("Who discovered gravity?")
    assert question_id > 0


def test_find_all_questions(setup_database):
    question = Question(question_text="What is the speed of light?", correct_answer="300,000 km/s")
    create_question(question)
    questions = find_all_questions()
    assert len(questions) > 0
    assert questions[-1].question_text == "What is the speed of light?"
    assert questions[-1].correct_answer == "300,000 km/s"


def test_find_question_by_id(setup_database):
    question = Question(question_text="What is the boiling point of water?", correct_answer="100°C")
    new_id = create_question(question)
    found_question = find_question_by_id(new_id)
    assert found_question is not None
    assert found_question.question_text == "What is the boiling point of water?"
    assert found_question.correct_answer == "100°C"


def test_update_question(setup_database):
    question = Question(question_text="What is the largest planet?", correct_answer="Jupiter")
    new_id = create_question(question)
    updated_question = Question(question_text="What is the smallest planet?", correct_answer="Mercury")
    success = update_question(new_id, updated_question)
    assert success
    found_question = find_question_by_id(new_id)
    assert found_question.question_text == "What is the smallest planet?"
    assert found_question.correct_answer == "Mercury"


def test_delete_question(setup_database):
    question = Question(question_text="What is the hottest planet?", correct_answer="Venus")
    new_id = create_question(question)
    success = delete_question(new_id)
    assert success
    deleted_question = find_question_by_id(new_id)
    assert deleted_question is None
