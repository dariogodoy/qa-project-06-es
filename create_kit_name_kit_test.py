import configuration
import requests
import data
def get_kit_body(name):
    return {"name": name}

def test_create_kit_name_1_char():
    auth_token = get_new_user_token()
    kit_body = get_kit_body("a")
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"
    response = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                             json=kit_body,
                             headers=headers)
    assert response.status_code == 201
    assert response.json()["name"] == ["Este campo tiene una letra"]


def test_create_kit_empty_name():
    auth_token = get_new_user_token()
    kit_body = get_kit_body("")
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"
    response = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                             json=kit_body,
                             headers=headers)
    assert response.status_code == 400
    assert response.json()["name"] == ["Este campo no puede estar vacío."]

def test_create_kit_long_name():
    auth_token = get_new_user_token()
    kit_body = get_kit_body("a" * 101)
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"
    response = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                             json=kit_body,
                             headers=headers)
    assert response.status_code == 400
    assert response.json()["name"] == ["Este campo no puede tener más de 100 caracteres."]

def test_create_kit_charaters():
    auth_token = get_new_user_token()
    kit_body = get_kit_body("№%@")
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"
    response = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                             json=kit_body,
                             headers=headers)
    assert response.status_code == 201
    assert response.json()["name"] == ["Este campo no puede poner caracteres especiales "]

def test_create_kit_spaces():
    auth_token = get_new_user_token()
    kit_body = get_kit_body(" A Aaa ")
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"
    response = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                             json=kit_body,
                             headers=headers)
    assert response.status_code == 201
    assert response.json()["name"] == ["Ete campo no puede tener epacios "]

def test_create_kit_numbers():
    auth_token = get_new_user_token()
    kit_body = get_kit_body("123")
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"
    response = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                             json=kit_body,
                             headers=headers)
    assert response.status_code == 201
    assert response.json()["name"] == ["Este campo no puede tener numeros "]

def test_create_kit_missing_name():
    auth_token = get_new_user_token()
    kit_body = {}
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"
    response = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                             json=kit_body,
                             headers=headers)
    assert response.status_code == 400
    assert response.json()["name"] == ["Este campo es obligatorio."]
def test_create_kit_with_invalid_data():
    auth_token = get_new_user_token()
    kit_body = {"name": 123}
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"
    response = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                             json=kit_body,
                             headers=headers)
    assert response.status_code == 400
    assert response.json()["name"] == ["Este campo tiene datos invalidos"]
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