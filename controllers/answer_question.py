from dataclasses import asdict
from flask import Blueprint, jsonify, request
from Repository.answer_repository import find_all_answers, find_answer_by_id, create_answer, update_answer, delete_answer
from models.Answer import Answer
from models.response_dto import ResponseDto

answer_blueprint = Blueprint("answer", __name__)

@answer_blueprint.route("/answers", methods=["GET"])
def get_all_answers():
    answer_list = list(map(asdict, find_all_answers()))
    return jsonify(ResponseDto(body=answer_list)), 200

@answer_blueprint.route("/answers/<int:answer_id>", methods=["GET"])
def get_answer(answer_id):
    answer = find_answer_by_id(answer_id)
    if answer:
        return jsonify(asdict(ResponseDto(body=asdict(answer)))), 200
    else:
        return jsonify(asdict(ResponseDto(error="Answer not found"))), 404

@answer_blueprint.route("/answers", methods=["POST"])
def create_answer_route():
    answer_data = request.json
    answer = Answer(
        question_id=answer_data["question_id"],
        incorrect_answer=answer_data["incorrect_answer"]
    )
    answer_id = create_answer(answer)
    return jsonify(asdict(ResponseDto(body={"id": answer_id}))), 201

@answer_blueprint.route("/answers/<int:answer_id>", methods=["PUT"])
def update_answer_route(answer_id):
    answer_data = request.json
    updated_answer = Answer(
        question_id=answer_data.get("question_id"),
        incorrect_answer=answer_data.get("incorrect_answer")
    )
    if update_answer(answer_id, updated_answer):
        return jsonify(asdict(ResponseDto(message="Answer updated successfully"))), 200
    else:
        return jsonify(asdict(ResponseDto(error="Answer not found"))), 404

@answer_blueprint.route("/answers/<int:answer_id>", methods=["DELETE"])
def delete_answer_route(answer_id):
    if delete_answer(answer_id):
        return jsonify(asdict(ResponseDto(message="Answer deleted successfully"))), 200
    else:
        return jsonify(asdict(ResponseDto(error="Answer not found"))), 404
