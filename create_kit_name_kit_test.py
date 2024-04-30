import sender_stand_request
import data


# esta función cambia los valores en el parámetro "firstName"
def get_user_body(kit_name):
    # el diccionario que contiene el cuerpo de solicitud se copia del archivo "data" (datos) para conservar los datos del diccionario de origen
    current_body = data.kit_body.copy()
    # Se cambia el valor del parámetro firstName
    current_body["name"] = kit_name
    # Se devuelve un nuevo diccionario con el valor firstName requerido
    return current_body


def create_kit_positive(kit_name):
    # La versión actualizada del cuerpo de solicitud con el nombre "Aa" se guarda en la variable "user_body"
    user_body = get_user_body(kit_name)
    # El resultado de la solicitud relevante se guarda en la variable "user_response"
    user_response = sender_stand_request.post_kit(user_body)
    user_new_kit = user_response.json()


    # Comprueba si el código de estado es 201
    assert user_response.status_code == 201
    # Comprueba que el campo authToken está en la respuesta y contiene un valor
    assert user_new_kit["name"] == kit_name


#Prueba número 1
def test_create_user_positive_1_letter():
    create_kit_positive(data.kit_body_1[0])


#Prueba número 2
def test_create_511_characters():
    create_kit_positive(data.kit_body_1[1])


def create_kit_negative(kit_name):
    kit_response = sender_stand_request.post_kit(kit_name)

    assert kit_response.status_code == 400
    assert kit_response.json()["message"] == "No cumple con los parametros establecidos"


#Prueba número 3
def test_create_user_no_characters():
    create_kit_negative(data.kit_body_1[2])


#Prueba número 4
def test_create_512_characters():
    create_kit_negative(data.kit_body_1[3])


#Prueba número 5
def test_create_user_characters_and_symbols_in_username():
    create_kit_positive(data.kit_body_1[4])


#Prueba número 6
def test_create_user_space_in_the_middle_in_username():
    create_kit_positive(data.kit_body_1[5])


#Prueba número 7
def test_create_user_numbers_in_username():
    create_kit_positive(data.kit_body_1[6])


#Prueba número 8
def test_create_user_no_name_in_username():
    create_kit_positive(data.kit_body_1[8])


#Prueba número 9
def test_create_blank_username():
    create_kit_positive(data.kit_body_1[7])



