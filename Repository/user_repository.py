from typing import List

from Repository.database import get_db_connection, create_tables
from Utils.urls import get_user_url
from api.user_api import get_users_from_api
from models.User import User


def load_users_from_api():
    user_url = get_user_url()
    users_from_api = get_users_from_api(user_url)
    print(users_from_api)
    for user_json in users_from_api["results"]:
        print(user_json)
        user = extract_user_from_json(user_json)
        create_user(user)

def extract_user_from_json(user_json):
    return User(
        first_name=user_json["name"]["first"],
        last_name=user_json["name"]["last"],
        email=user_json["email"]
    )


def create_user(user: User) -> int:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO users (first_name, last_name, email) VALUES (%s, %s, %s) RETURNING id",
            (user.first_name , user.last_name, user.email)
        )
        new_id = cursor.fetchone()["id"]
        connection.commit()
        return new_id

def find_all_users() -> List[User]:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users")
        users_data = cursor.fetchall()
        return [User(**u) for u in users_data]


def find_user_by_id(user_id):
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user_data = cursor.fetchone()
        return User(**user_data) if user_data else None


def update_user(user_id, new_user):
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("UPDATE users SET first_name = %s, last_name = %s, email = %s WHERE id = %s",
                       (new_user.first_name, new_user.last_name, new_user.email, user_id))
        row_affected = cursor.rowcount
        return row_affected > 0


def delete_user(user_id):
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        row_affected = cursor.rowcount
        return row_affected > 0

# create_tables()
# load_users_from_api()
# print(find_user_by_id(21))