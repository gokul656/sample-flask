from auth_service.src.services import user_service
from auth_service.src.context import user_service
from flask import Blueprint # type: ignore
from flask_jwt_extended import verify_jwt_in_request

from auth_service.src.utils import encode_json # type: ignore

user_blueprint = Blueprint("user", __name__)

@user_blueprint.before_request
def verify_jwt():
    verify_jwt_in_request()

@encode_json
@user_blueprint.route("/all", methods=["GET"])
def get_users():
    return [user.to_json() for user in user_service.get_all_users()] # FIXME add serization support for collections

@user_blueprint.route("/<mail>", methods=["GET"])
@encode_json
def get_user_data(mail):
    return user_service.get_user(mail)
