import json

from auth_service.src.json_encoder import CustomEncoder


def encode_json(f):
    def marshall(**kwargs):
        return json.dumps(f(**kwargs), cls=CustomEncoder)

    return marshall
