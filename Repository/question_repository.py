from typing import List
from Repository.database import get_db_connection, create_tables
from models.Question import Question


def extract_question_from_trivia_data(trivia_data):
    return Question(
        question_text=trivia_data["question"],
        correct_answer=trivia_data["correct_answer"]
    )

def create_question(question: Question) -> int:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO questions (question_text, correct_answer) VALUES (%s, %s) RETURNING id",
            (question.question_text, question.correct_answer)
        )
        new_id = cursor.fetchone()["id"]
        connection.commit()
        return new_id

def get_id_by_question_text(question_text):
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute(
            "SELECT id FROM questions WHERE question_text = %s", (question_text,)
        )
        question_id = cursor.fetchone()["id"]
        return question_id

def find_all_questions() -> List[Question]:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("SELECT * FROM questions")
        questions_data = cursor.fetchall()
        return [Question(**q) for q in questions_data]


def find_question_by_id(question_id):
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("SELECT * FROM questions WHERE id = %s", (question_id,))
        question_data = cursor.fetchone()
        return Question(**question_data) if question_data else None


def update_question(question_id, new_question):
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("UPDATE questions SET question_text = %s, correct_answer = %s WHERE id = %s",
                       (new_question.question_text, new_question.correct_answer, question_id))
        row_affected = cursor.rowcount
        return row_affected > 0


def delete_question(question_id):
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("DELETE FROM questions WHERE id = %s", (question_id,))
        row_affected = cursor.rowcount
        return row_affected > 0

