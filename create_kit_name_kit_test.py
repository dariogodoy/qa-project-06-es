
import data
from sender_stand_request import post_new_client_kit


def get_kit_body(kit_body):
    current_name = data.kit_body.copy()
    current_name["name"] = kit_body
    return current_name

def get_new_user_token():
    return "auth_token"

def positive_assert_code_201(name):
    kit_body = get_kit_body(name)
    kit_response = post_new_client_kit(kit_body,'auth_token')
    kit_response_data = kit_response.json()
    assert kit_response.status_code == 201
    assert kit_response_data["name"] == kit_body["name"]


def negative_assert_code_400(name):
    kit_body = get_kit_body(name)
    kit_response = post_new_client_kit(kit_body,'auth_token')
    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400


def test_create_kit_name_1_char():
    kit_body = get_kit_body(data.one_letter)
    response = post_new_client_kit(kit_body, 'auth_token')
    response.raise_for_status()
    positive_assert_code_201(response.json())


def test_create_kit_511_name():
    kit_body = get_kit_body(data.five_hundred_eleven_letters)
    response = post_new_client_kit(kit_body, 'auth_token')
    response.raise_for_status()
    positive_assert_code_201(response.json())


def test_create_kit_name_empty_string():
    kit_body = get_kit_body({'name': ''})
    response = post_new_client_kit(kit_body, 'auth_token')
    negative_assert_code_400(response.json())

def test_create_kit_512_name():
    kit_body = get_kit_body(data.longer_name)
    response = post_new_client_kit(kit_body, 'auth_token')
    response.raise_for_status()
    negative_assert_code_400(response.json())


def test_create_kit_charaters():
    kit_body = get_kit_body(data.characters)
    response = post_new_client_kit(kit_body, 'auth_token')
    response.raise_for_status()
    positive_assert_code_201(response.json())


def test_create_kit_spaces():
    kit_body = get_kit_body(" A Aaa ")
    response = post_new_client_kit(kit_body, 'auth_token')
    response.raise_for_status()
    positive_assert_code_201(response.json())


def test_create_kit_numbers():
    kit_body = get_kit_body("123")
    response = post_new_client_kit(kit_body, 'auth_token')
    response.raise_for_status()
    positive_assert_code_201(response.json())


def test_create_kit_with_invalid_data():
    kit_body = {"name": 123}
    response = post_new_client_kit(kit_body, 'auth_token')
    response.raise_for_status()
    negative_assert_code_400(response.json())

def test_create_kit_missing_name():
    kit_body = {}
    response = post_new_client_kit(kit_body, 'auth_token')
    response.raise_for_status()
    negative_assert_code_400(response.json())
