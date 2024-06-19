import json


def make_json(data: dict):
    return json.dumps(data, indent=4)


def json_formatter(diff):
    return make_json(diff)
