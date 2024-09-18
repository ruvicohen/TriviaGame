import pytest

from Repository.answer_repository import create_answer, find_all_answers, find_answer_by_id, find_correct_answer_by_question_id, \
    update_answer, delete_answer
from Repository.database import create_tables, get_db_connection, drop_all_tables
from Repository.seed import seed
from Repository.trivia_repository import load_trivia_data_from_api
from models.Answer import Answer


@pytest.fixture(scope="module")
def setup_database():
    create_tables()
    load_trivia_data_from_api()
    yield
    drop_all_tables()


def test_create_answer(setup_database):
    answer = Answer(question_id=1, incorrect_answer="Wrong Answer")
    new_id = create_answer(answer)
    assert new_id > 0


def test_find_all_answers(setup_database):
    answer = Answer(question_id=2, incorrect_answer="Another Wrong Answer")
    create_answer(answer)
    answers = find_all_answers()
    assert len(answers) > 0
    assert answers[-1].incorrect_answer == "Another Wrong Answer"


def test_find_answer_by_id(setup_database):
    answer = Answer(question_id=3, incorrect_answer="Find me by ID")
    new_id = create_answer(answer)
    found_answer = find_answer_by_id(new_id)
    assert found_answer is not None
    assert found_answer.question_id == 3
    assert found_answer.incorrect_answer == "Find me by ID"


def test_find_answer_by_question_id(setup_database):
    answer = Answer(question_id=4, incorrect_answer="Question ID Test")
    new_id = create_answer(answer)
    found_answer = find_correct_answer_by_question_id(4)
    assert found_answer is not None
    assert found_answer.question_id == 4


def test_update_answer(setup_database):
    answer = Answer(question_id=5, incorrect_answer="Old Answer")
    new_id = create_answer(answer)
    success = update_answer(new_id, "Updated Answer")
    assert success
    updated_answer = find_answer_by_id(new_id)
    assert updated_answer.incorrect_answer == "Updated Answer"


def test_delete_answer(setup_database):
    answer = Answer(question_id=6, incorrect_answer="Delete Me")
    new_id = create_answer(answer)
    success = delete_answer(new_id)
    assert success
    deleted_answer = find_answer_by_id(new_id)
    assert deleted_answer is None
