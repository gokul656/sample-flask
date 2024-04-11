from flask import Blueprint, request
from flask_jwt_extended import create_access_token

from auth_service.src.models.user_model import User
from auth_service.src.context import user_service
from commons.errors import FIELD_NOT_FOUND
from commons.utils import to_json

auth_blueprint = Blueprint("auth", __name__)

@auth_blueprint.route("/register", methods=["POST"])
def register():
    user_data = request.get_json()
    name: str = user_data.get("name")
    email: str = user_data.get("email")
    password: str = user_data.get("password")

    if name is None or email is None or password is None:
        raise FIELD_NOT_FOUND

    user: User = user_service.add_user(User(name, email, password))
    access_token = create_access_token(identity=to_json(user))
    return {"access_token": access_token}

