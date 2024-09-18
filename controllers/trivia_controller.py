from flask import Blueprint, jsonify
from Repository.question_repository import create_question, extract_question_from_trivia_data

from Repository.answer_repository import create_answers
from Services.answer_service import extract_answers_from_trivia_data
from Utils.urls import get_trivia_url
from api.trivia_api import get_trivia_from_api

trivia_blueprint = Blueprint("trivia", __name__)

@trivia_blueprint.route("/load-trivia", methods=["POST"])
def load_trivia_data():
    trivia_url = get_trivia_url()
    trivia_from_api = get_trivia_from_api(trivia_url)
    for question_trivia in trivia_from_api["results"]:
        question = extract_question_from_trivia_data(question_trivia)
        question_id = create_question(question)
        answers = extract_answers_from_trivia_data(question_trivia)
        create_answers(answers(question_id))
    return jsonify({"message": "Trivia data loaded successfully"}), 201
