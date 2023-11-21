from flask import Blueprint, request
from flask_jwt_extended import jwt_required, verify_jwt_in_request, create_access_token

from auth_service.src.models.user_model import User
from auth_service.src.services.user_service import UserService
from auth_service.src.utils import encode_json
from commons.errors import FIELD_NOT_FOUND
from commons.utils import to_json

user_blueprint = Blueprint("user", __name__)
user_service = UserService()


@user_blueprint.route("/", methods=["POST"])
def register():
    user_data = request.get_json()
    name: str = user_data.get("name")
    email: str = user_data.get("email")

    if name is None or email is None:
        raise FIELD_NOT_FOUND

    user: User = user_service.add_user(User(name, email))
    access_token = create_access_token(identity=to_json(user))
    return {"access_token": access_token}


@encode_json
@user_blueprint.route("/all", methods=["GET"])
def get_users():
    return user_service.get_all_users()


@jwt_required()
@user_blueprint.route("/<mail>", methods=["GET"])
@encode_json
def get_user_data(mail):
    verify_jwt_in_request()
    return user_service.get_user(mail)
