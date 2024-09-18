from flask import Blueprint, jsonify, request
from Repository.user_repository import find_all_users, delete_user, update_user, load_users_from_api, create_user, \
    find_user_by_id
from models.User import User
from dataclasses import asdict

from models.response_dto import ResponseDto

user_blueprint = Blueprint("user", __name__)

@user_blueprint.route("/", methods=["GET"])
def get_all_users():
    user_list = list(map(asdict, find_all_users()))
    return jsonify(ResponseDto(body=user_list)), 200


@user_blueprint.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = find_user_by_id(user_id)
    if user:
        return jsonify(asdict(user)), 200
    else:
        return jsonify(asdict(ResponseDto(error="User not found"))), 404

@user_blueprint.route("/", methods=["POST"])
def create_user_route():
    user_data = request.json
    user = User(
        first_name=user_data["first_name"],
        last_name=user_data["last_name"],
        email=user_data["email"]
    )
    user_id = create_user(user)
    return jsonify({"id": user_id}), 201

@user_blueprint.route("/<int:user_id>", methods=["PUT"])
def update_user_route(user_id):
    user_data = request.json
    updated_user = User(
        first_name=user_data.get("first_name"),
        last_name=user_data.get("last_name"),
        email=user_data.get("email")
    )
    if update_user(user_id, updated_user):
        return jsonify(asdict(ResponseDto(message="User updated successfully"))), 200
    else:
        return jsonify(asdict(ResponseDto(error="User not found"))), 404

@user_blueprint.route("/<int:user_id>", methods=["DELETE"])
def delete_user_route(user_id):
    if delete_user(user_id):
        return jsonify(asdict(ResponseDto(message="User deleted successfully"))), 200
    else:
        return jsonify(asdict(ResponseDto(error="User not found"))), 404

@user_blueprint.route("/load", methods=["POST"])
def load_users_from_api_route():
    load_users_from_api()
    return jsonify(asdict(ResponseDto(message="Users loaded from API"))), 201
