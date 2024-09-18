from dataclasses import asdict

from flask import Blueprint, jsonify

from Repository.question_repository import find_all_questions

user_answer_bluprint = Blueprint("user_answer", __name__)

@user_answer_bluprint.route("/", methods=["GET"])
def get_all():
    fighters = list(map(asdict, find_all_questions()))
    return jsonify(fighters), 200