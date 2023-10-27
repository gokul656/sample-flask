import json


def to_json(data: object) -> str:
    return json.dumps(data, default=lambda x: x.__dict__)
