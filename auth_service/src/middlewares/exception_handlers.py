from flask import jsonify
from werkzeug.exceptions import Unauthorized


def exception_handler(err: Exception):
    response = jsonify({'error': str(err)})
    response.status_code = 423
    return response


def unauthorized_handler(err: Unauthorized):
    print(err)
    response = jsonify({"errors": str(err)})
    response.status_code = 403
    return response, 403
