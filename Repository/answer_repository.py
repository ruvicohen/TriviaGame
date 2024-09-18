from typing import List
from Repository.database import get_db_connection
from models.Answer import Answer






def create_answers(answers):
    for answer in answers:
        create_answer(answer)

def create_answer(answer: Answer) -> int:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO answers (question_id, incorrect_answer) VALUES (%s, %s) RETURNING id",
            (answer.question_id, answer.incorrect_answer)
        )
        new_id = cursor.fetchone()["id"]
        connection.commit()
        return new_id

def find_all_answers() -> List[Answer]:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("SELECT * FROM answers")
        answers_data = cursor.fetchall()
        return [Answer(**a) for a in answers_data]


def find_answer_by_id(answer_id):
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("SELECT * FROM answers WHERE id = %s", (answer_id,))
        answer_data = cursor.fetchone()
        return Answer(**answer_data) if answer_data else None

def find_correct_answer_by_question_id(question_id):
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("SELECT * FROM answers WHERE question_id = %s", (question_id,))
        answer_data = cursor.fetchone()
        return Answer(**answer_data)

def update_answer(answer_id, new_answer):
    with get_db_connection() as connection, connection.cursor() as cursor:
       cursor.execute("UPDATE answers SET incorrect_answer = %s WHERE id = %s", (new_answer, answer_id))
       row_affected  = cursor.rowcount
       return row_affected > 0

def delete_answer(answer_id):
    with get_db_connection() as connection, connection.cursor() as cursor:
       cursor.execute("DELETE FROM answers WHERE id = %s", (answer_id,))
       row_affected = cursor.rowcount
       return row_affected > 0
