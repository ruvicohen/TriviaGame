from toolz import curry

from models.Answer import Answer


def extract_answers_from_trivia_data(trivia_data):
    return curry(
        lambda question_id:
        [
            Answer(
                question_id=question_id,
                incorrect_answer=incorrect_answer
            )
            for incorrect_answer in trivia_data["incorrect_answers"]
        ]

    )