# from typing import List
#
# from Repository.database import get_db_connection
# from Utils.urls import get_trivia_url
# from api.trivia_api import get_trivia_from_api
# from models.Question import Question
#
#
# def load_data_question_from_api():
#     all_fighters = find_all_questions()
#     if all_fighters and len(all_fighters) > 0:
#         return
#     trivia_url = get_trivia_url()
#     question_trivia_from_api = get_trivia_from_api(trivia_url)
#     for question_trivia in question_trivia_from_api["results"]:
#         question = extract_question_from_trivia_data(question_trivia)
#         create_question(question)
#
#
#
# def extract_question_from_trivia_data(trivia_data):
#     return Question(
#         question_text=trivia_data["question"],
#         correct_answer=trivia_data["correct_answer"]
#     )
#
# def create_question(question: Question) -> int:
#     with get_db_connection() as connection, connection.cursor() as cursor:
#         cursor.execute(
#             "INSERT INTO questions (question_text, correct_answer) VALUES (%s, %s) RETURNING id",
#             (question.question_text, question.correct_answer)
#         )
#         new_id = cursor.fetchone()["id"]
#         connection.commit()
#         return new_id
#
# def find_all_questions() -> List[Question]:
#     with get_db_connection() as connection, connection.cursor() as cursor:
#         cursor.execute("SELECT * FROM question")
#         questions_data = cursor.fetchall()
#         return [Question(**q) for q in questions_data]
