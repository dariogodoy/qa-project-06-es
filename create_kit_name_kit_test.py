import configuration
import requests
import data

def get_kit_body(name):
    return {"name": name}

def get_new_user_token():
    return "auth_token"

def positive_assert(response):
    assert response.status_code == 201

def negative_assert_code_400(response):
    assert response.status_code == 400

def test_positive_create_kit():
    auth_token = get_new_user_token()
    kit_body = get_kit_body("kit_name")
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"
    response = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                             json=kit_body,
                             headers=headers)
    positive_assert(response)

def test_negative_create_kit():
    auth_token = get_new_user_token()
    kit_body = get_kit_body("kit_name_with_invalid_data")
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"
    response = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                             json=kit_body,
                             headers=headers)
    negative_assert_code_400(response)