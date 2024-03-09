import configuration
import requests
import data


def post_new_client_kit(body, auth_token):
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=headers)








