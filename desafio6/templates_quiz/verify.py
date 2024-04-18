import preguntas as p


def verificar(alternativas, eleccion):
    #devuelve el índice de elección dada
    eleccion = ['a', 'b', 'c','d'].index(eleccion)

    lista=alternativas[eleccion]

    if int(lista[1]) == 1:
        print('Respuesta Correcta')
        return True
    else:
        print('Respuesta Incorrecta')
        return False

if __name__ == '__main__':
    #Important: Use only for testing
    #Check the results
    from print_preguntas import print_pregunta
    # Siempre que se escoja la alternativa con alt_2 estará correcta, e incorrecta en cualquier otro caso
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    verificar(pregunta['alternativas'], respuesta)






