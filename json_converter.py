import json


class JsonConverter:
    @staticmethod
    def json_to_obj(data):
        return json.loads(data)

    @staticmethod
    def obj_to_json(data):
        return json.dumps(data, indent=2)
