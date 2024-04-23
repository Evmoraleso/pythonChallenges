from string import Template

def get_template(api_content):
    try:
        print("Construyendo el sitio web 'Aves de Chile.....'")
        html_template = Template('''
        <!DOCTYPE html> <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>AVES DE CHILE</title>
            <!-- Bootstrap reference -->
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
                integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        </head>

        <body>
            <!--Header 1 Section-->
            <header>
                <h1 style="text-align: center;">AVES DE CHILE</h1>
            </header>
            
            <div class="container-fluid">
                <!--Section 4 Cards-->
                <section id="highlighted-section">            
                    <!--Section 4 line-->
                    <div id="bootom-highlighted">
                        <div class="row">
                            <div class="col-lg-12 col-xs-12 mt-4">
                            </div>
                        </div>
                    </div>
                    <div class="row row-cols-1 row-cols-md-4 g-4 margin-row">
                        $body               
                    </div>
                </section>
            </div>
        </body>

        </html>
                                ''')

        img_template = Template('''<div class="col">
                            <div class="card border-info mb-3">
                                <img src="$url" class="card-img-top" alt="..." style="width: 450px; height: 300px;">
                                <div class="card-body">
                                    <h5 class="card-title">Nombre en Español:</h5>
                                    <h6 class="card-subtitle mb-2 text-body-secondary">$spanishname</h6>
                                    <h5 class="card-title">Nombre en Inglés:</h5>
                                    <h6 class="card-subtitle mb-2 text-body-secondary">$englishname</h6>
                                </div>
                            </div>
                    </div>''') 

        lista=[]
        for elemento in api_content[:24]:
            dic={}
            dic['spanish']=elemento['name']['spanish']
            dic['english']=elemento['name']['english']
            dic['url']=elemento['images']['main']
            lista.append(dic)

        texto_img = ''  

        for elemento in lista:
            texto_img += img_template.substitute(url = elemento['url'],spanishname=elemento['spanish'],englishname=elemento['english']) +'\n'    

        html = html_template.substitute(body = texto_img)
        
        return html
    
    except Exception as error:
        print(f"Ocurrió un error al crear el HTML: {error}")
        exit()
        
if __name__ == '__main__':
    #Testing the module
    #get_template('')
    pass

