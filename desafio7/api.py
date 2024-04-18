import requests

def api_get(url):
    response = requests.get(url)
    #1. Obtenga toda la información de los usuarios retornada por la API, guárdela en una variable llamada users_data e imprímala en pantalla
    if response.status_code == 200:
        users_data=response.content
        print("GET")
        print(users_data)

def api_create(url):
    #2. Cree un usuario que tenga de nombre Ignacio y de trabajo Profesor. Guarde el 
    #diccionario de respuesta en una variable llamada created_user e imprímala en pantalla.
    payloadc = '''{"name": "Ignacio","job": "Profesor"}'''
    created_user = requests.post(url, data = payloadc)
    if created_user.status_code == 201:
        print("CREATE")
        print(created_user)
        print(created_user.content)

def api_update(url):
    #3. Actualice un usuario llamado morpheus para que tenga un campo llamado residence
    #igual a zion. Guarde el diccionario de respuesta en una variable llamada 
    #updated_user e imprímala en pantalla. 
    payloadu = '''{"name": "morpheus","job": "zion resident"}'''
    update_user = requests.put(url, data = payloadu)
    if update_user.status_code == 200:
        print("UPDATE")
        print(update_user)
        print(update_user.content)

def api_delete(url):
    #4. Elimine un usuario llamado Tracey. Imprima el código de respuesta en pantalla.
    urld='https://reqres.in/api/users/2'
    payloadd = '''{"name": "Tracey"}'''
    delete_user = requests.delete(urld, data = payloadd)
    if delete_user.status_code == 204:
        print("DELETE")
        print(delete_user)
        print(delete_user.content)

def main():
    url='https://reqres.in/api/users'
    url2='https://reqres.in/api/users/2'
    api_get(url)
    api_create(url)
    api_update(url2)
    api_delete(url2)

if __name__ == '__main__':
    main()






