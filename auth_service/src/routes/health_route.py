import time

from flask import Blueprint, jsonify, make_response

health_blueprint = Blueprint("health_bp", __name__)

@health_blueprint.route("/ping", methods=['GET', 'HEAD'])
def ping():
    time.sleep(2)
    response = make_response(jsonify({"status": "UP"}))
    response.set_cookie("site", "something")

    return response
