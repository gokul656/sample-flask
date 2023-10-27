from flask import Blueprint, jsonify

health_blueprint = Blueprint("health_bp", __name__)


@health_blueprint.route("/ping", methods=['GET'])
def ping():
    return jsonify({"status": "UP"})
