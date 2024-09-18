import pytest

from Repository.database import create_tables, get_db_connection, drop_all_tables
from Repository.seed import seed
from Repository.trivia_repository import load_trivia_data_from_api
from Repository.user_repository import create_user, find_all_users, find_user_by_id, update_user, delete_user
from models.User import User


@pytest.fixture(scope="module")
def setup_database():
    create_tables()
    load_trivia_data_from_api()
    yield
    drop_all_tables()



def test_create_user(setup_database):
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
    new_id = create_user(user)
    assert new_id > 0


def test_find_all_users(setup_database):
    user = User(first_name="Alice", last_name="Smith", email="alice.smith@example.com")
    create_user(user)
    users = find_all_users()
    assert len(users) > 0
    assert users[-1].first_name == "Alice"
    assert users[-1].last_name == "Smith"
    assert users[-1].email == "alice.smith@example.com"


def test_find_user_by_id(setup_database):
    user = User(first_name="Bob", last_name="Johnson", email="bob.johnson@example.com")
    new_id = create_user(user)
    found_user = find_user_by_id(new_id)
    assert found_user.first_name == "Bob"
    assert found_user.last_name == "Johnson"
    assert found_user.email == "bob.johnson@example.com"


def test_update_user(setup_database):
    user = User(first_name="Charlie", last_name="Brown", email="charlie.brown@example.com")
    new_id = create_user(user)

    updated_user = User(first_name="Charlie", last_name="White", email="charlie.white@example.com")
    success = update_user(new_id, updated_user)

    assert success

    found_user = find_user_by_id(new_id)
    assert found_user.last_name == "White"
    assert found_user.email == "charlie.white@example.com"


def test_delete_user(setup_database):
    user = User(first_name="David", last_name="Green", email="david.green@example.com")
    new_id = create_user(user)

    success = delete_user(new_id)
    assert success

    found_user = find_user_by_id(new_id)
    assert found_user is None