import configuration
import requests
import data
from sender_stand_request import post_new_client_kit


def get_kit_body(name):
    return {"name": name}


def get_new_user_token():
    return ""


def test_create_kit_name_1_char():
    auth_token = get_new_user_token()
    kit_body = get_kit_body(data.one_letter)
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"
    response = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                             json=kit_body,
                             headers=headers)
    positive_assert(response)
    assert response.status_code == 201
    assert response.json()["a"] == ["Este campo tiene una letra"]


def test_create_kit_500_name():
    kit_body = get_kit_body(data.five_hundred_eleven_letters)
    response = post_new_client_kit(kit_body,'auth_token')
    positive_assert(response)
    assert response.status_code == 201
    assert response.json()["name"] == ["El valor de prueba para esta comprobación será inferior a"]


def test_create_kit_empty_name():
    kit_body = get_kit_body("")
    response = post_new_client_kit(kit_body,'auth_token')
    negative_assert_code_400(response)
    assert response.status_code == 400
    assert response.json()["name"] == ["Este campo no puede estar vacío."]


def test_create_kit_512_name():
    kit_body = get_kit_body(data.longer_name)
    response = post_new_client_kit(kit_body,'auth_token')
    negative_assert_code_400(response)
    assert response.status_code == 400
    assert response.json()["name"] == ["El valor de prueba para esta comprobación será inferior a"]


def test_create_kit_charaters():
    kit_body = get_kit_body(data.characters)
    response = post_new_client_kit(kit_body,'auth_token')
    positive_assert(response)
    assert response.status_code == 201
    assert response.json()["name"] == ["Este campo no puede poner caracteres especiales "]


def test_create_kit_spaces():
    kit_body = get_kit_body(" A Aaa ")
    response = post_new_client_kit(kit_body,'auth_token')
    positive_assert(response)
    assert response.status_code == 201
    assert response.json()["name"] == ["Ete campo no puede tener epacios "]


def test_create_kit_numbers():
    kit_body = get_kit_body("123")
    response = post_new_client_kit(kit_body,'auth_token')
    assert response.status_code == 201
    assert response.json()["name"] == ["Este campo no puede tener numeros "]


def test_create_kit_missing_name():
    kit_body = {}
    response = post_new_client_kit(kit_body,'auth_token')
    assert response.status_code == 400
    assert response.json()["name"] == ["Este campo es obligatorio."]


def test_create_kit_with_invalid_data():
    kit_body = {"name": 123}
    response = post_new_client_kit(kit_body,'auth_token')
    assert response.status_code == 400
    assert response.json()["name"] == ["Este campo tiene datos invalidos"]


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
