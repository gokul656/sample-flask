from auth_service.src.services.user_service import UserService
from flask import Blueprint # type: ignore
from flask_jwt_extended import verify_jwt_in_request

from auth_service.src.utils import encode_json # type: ignore

user_blueprint = Blueprint("user", __name__)
user_blueprint.before_request(verify_jwt_in_request)

user_service = UserService()

@encode_json
@user_blueprint.route("/all", methods=["GET"])
def get_users():
    return user_service.get_all_users()

@user_blueprint.route("/<mail>", methods=["GET"])
@encode_json
def get_user_data(mail):
    verify_jwt_in_request()
    return user_service.get_user(mail)
