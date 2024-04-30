import configuration
import requests
import data


def create_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados


def create_token():
    header = create_user(data.user_body)
    token = header.json()
    return token['authToken']


def post_kit(name):
    token = create_token()
    data.headers["Authorization"] = f"bearer {token}"
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                         # inserta la dirección URL completa
                         json=name,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados
