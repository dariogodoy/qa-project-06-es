import configuration
import requests
import data

auth_token = "your_auth_token"

def post_new_client_kit(body, auth_token):
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers,
                         auth=(configuration.CREATE_USER_PATH, auth_token))

response = post_new_client_kit(data.kit_bodies, auth_token)

print(response.status_code)
print(response.json())