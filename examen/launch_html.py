def deploy_html(html):
    try:
        print("Creando el archivo 'index.html' para el sitio web 'Aves de Chile'.....")
        filename='index.html'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html) 
            f.close()
    except Exception as error:
        print(f"Ocurrió un error al escribir {filename}: {error}")
        exit()

if __name__ == '__main__':
    #Testing the module
    #deploy_html('')
    pass
