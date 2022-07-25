from json_converter import JsonConverter
import pytest


@pytest.mark.conversion
def test_should_convert_rot47():
    """Test checking if the dict converted using obj_to_json method has correct format"""
    dict_to_convert: dict = {"rot": "rot47", "text": "test47"}
    result_json: str = '{\n  "rot": "rot47",\n  "text": "test47"\n}'

    converted_json: str = JsonConverter.obj_to_json(dict_to_convert)

    assert converted_json == result_json


@pytest.mark.conversion
def test_should_convert_rot13():
    """Test checking if the dict converted using obj_to_json method has correct format"""
    dict_to_convert: dict = {"rot": "rot13", "text": "test13"}
    result_json: str = '{\n  "rot": "rot13",\n  "text": "test13"\n}'

    converted_json: str = JsonConverter.obj_to_json(dict_to_convert)

    assert converted_json == result_json


def test_should_convert_list_of_dict_to_json():
    list_of_dict_to_convert: list = [
        {"rot": "rot13", "text": "test13"},
        {"rot": "rot47", "text": "test47"},
    ]
    result_json: str = (
        "[\n"
        "  {\n"
        '    "rot": "rot13",\n'
        '    "text": "test13"\n'
        "  },\n"
        "  {\n"
        '    "rot": "rot47",\n'
        '    "text": "test47"\n'
        "  }\n"
        "]"
    )

    encrypted_json: str = JsonConverter.obj_to_json(list_of_dict_to_convert)
    assert encrypted_json == result_json
