import requests
import json

def get_api(url):
    try:
        print('Realizando el consumo de la API para obtener los datos de las aves de Chile.....')
        response = requests.get(url)    
        if response.status_code == 200:
            return json.loads(requests.get(url).text)
        else:
            return False
    except Exception as error:
        print(f"Ocurrió un error al llamar a la API: {error}")
        exit()
        
if __name__ == '__main__':
    #Testing the module
    #get_api('')
    pass