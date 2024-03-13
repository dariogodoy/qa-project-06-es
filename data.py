kit_body = {}
one_letter = {
    "name": "a"
},
longer_name = {
    "name": "x" * 522
},
five_hundred_eleven_letters = {
    "name": "x" * 511
},
empty_string = {
    "name": ''
},
characters = {
    "name": "№%@"
},
kit_spaces = {
    "name": " A Aaa "
},
kit_numbers = {
    "name": " 123 "
},
invalid_data = {
    "name": 123
}


headers = {
    "Content-Type": "application/json",
    "Authorization": ""
}

user_body = {
    "name": "David",
    "phone": "+11569875693",
    "password": "password123"
}


def get_new_user_token(token):
    headers_token = headers.copy()
    headers_token["Authorization"] = f"Bearer {token}"
    return headers_token


kits = {
       "name": "Mi saco",
       "card": {
           "id": 2,
           "name": "Por la empresa"
       },
       "productsList": 'null',
       "id": 8,
       "productsCount": 1
}
