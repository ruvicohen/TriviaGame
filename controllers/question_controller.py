from dataclasses import asdict

from flask import Blueprint, jsonify, request
from Repository.question_repository import find_all_questions, find_question_by_id, create_question, update_question, delete_question
from models.Question import Question
from models.response_dto import ResponseDto

question_blueprint = Blueprint("question", __name__)

@question_blueprint.route("/questions", methods=["GET"])
def get_all_questions():
    question_list = list(map(asdict, find_all_questions()))
    return jsonify(ResponseDto(body=question_list)), 200

@question_blueprint.route("/questions/<int:question_id>", methods=["GET"])
def get_question(question_id):
    question = find_question_by_id(question_id)
    if question:
        return jsonify(asdict(ResponseDto(body=asdict(question)))), 200
    else:
        return jsonify(asdict(ResponseDto(error="Question not found"))), 404

@question_blueprint.route("/questions", methods=["POST"])
def create_question_route():
    question_data = request.json
    question = Question(
        question_text=question_data["question_text"],
        correct_answer=question_data["correct_answer"]
    )
    question_id = create_question(question)
    return jsonify(asdict(ResponseDto(body={"id": question_id}))), 201

@question_blueprint.route("/questions/<int:question_id>", methods=["PUT"])
def update_question_route(question_id):
    question_data = request.json
    updated_question = Question(
        question_text=question_data.get("question_text"),
        correct_answer=question_data.get("correct_answer")
    )
    if update_question(question_id, updated_question):
        return jsonify(asdict(ResponseDto(message="Question updated successfully"))), 200
    else:
        return jsonify(asdict(ResponseDto(error="Question not found"))), 404

@question_blueprint.route("/questions/<int:question_id>", methods=["DELETE"])
def delete_question_route(question_id):
    if delete_question(question_id):
        return jsonify(asdict(ResponseDto(message="Question deleted successfully"))), 200
    else:
        return jsonify(asdict(ResponseDto(error="Question not found"))), 404