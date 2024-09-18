
from Repository.answer_repository import create_answers
from Repository.question_repository import extract_question_from_trivia_data, create_question
from Services.answer_service import extract_answers_from_trivia_data
from Utils.urls import get_trivia_url
from api.trivia_api import get_trivia_from_api


def load_trivia_data_from_api():
    trivia_url = get_trivia_url()
    trivia_from_api = get_trivia_from_api(trivia_url)
    for question_trivia in trivia_from_api["results"]:
        question = extract_question_from_trivia_data(question_trivia)
        question_id = create_question(question)
        answers = extract_answers_from_trivia_data(question_trivia)
        create_answers(answers(question_id))


# def load_data_question_from_api2():
#     pipe(
#         get_trivia_url,
#         get_trivia_from_api,
#         partial(map, lambda x: compose(
#             create_question,
#             extract_question_from_trivia_data))
#     )

