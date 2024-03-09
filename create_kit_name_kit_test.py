import configuration
import requests
import data
from sender_stand_request import post_new_client_kit


def get_kit_body(name):
    return {"name": name}


def get_new_user_token():
    return ""


def positive_assert_code_201(response):
    assert response.status_code == 201


def negative_assert_code_400(response):
    assert response.status_code == 400


def test_create_kit_name_1_char():
    auth_token = get_new_user_token()
    kit_body = get_kit_body(data.one_letter)
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"
    response = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                             json=kit_body,
                             headers=headers)
    negative_assert_code_400(response)


def test_create_kit_511_name():
    kit_body = get_kit_body(data.five_hundred_eleven_letters)
    response = post_new_client_kit(kit_body, 'auth_token')
    negative_assert_code_400(response)


def test_create_kit_empty_name():
    kit_body = get_kit_body("")
    response = post_new_client_kit(kit_body, 'auth_token')
    negative_assert_code_400(response)


def test_create_kit_512_name():
    kit_body = get_kit_body(data.longer_name)
    response = post_new_client_kit(kit_body, 'auth_token')
    negative_assert_code_400(response)


def test_create_kit_charaters():
    kit_body = get_kit_body(data.characters)
    response = post_new_client_kit(kit_body, 'auth_token')
    negative_assert_code_400(response)


def test_create_kit_spaces():
    kit_body = get_kit_body(" A Aaa ")
    response = post_new_client_kit(kit_body, 'auth_token')
    negative_assert_code_400(response)


def test_create_kit_numbers():
    kit_body = get_kit_body("123")
    response = post_new_client_kit(kit_body, 'auth_token')
    negative_assert_code_400(response)


def test_create_kit_missing_name():
    kit_body = {}
    response = post_new_client_kit(kit_body, 'auth_token')
    negative_assert_code_400(response)


def test_create_kit_with_invalid_data():
    kit_body = {"name": 123}
    response = post_new_client_kit(kit_body, 'auth_token')
    negative_assert_code_400(response)
