preguntas_basicas = {
    'pregunta_1': {
        'enunciado': ['¿Cuál es la capital de Francia?'],
        'alternativas': [
            ['París', 1],  # Respuesta correcta
            ['Londres', 0],
            ['Roma', 0],
            ['Madrid', 0]
        ]
    },
    'pregunta_2': {
        'enunciado': ['¿Quién escribió "Don Quijote de la Mancha"?'],
        'alternativas': [
            ['Miguel de Cervantes', 1],  # Respuesta correcta
            ['William Shakespeare', 0],
            ['Gabriel García Márquez', 0],
            ['Jane Austen', 0]
        ]
    },
    'pregunta_3': {
        'enunciado': ['¿Cuál es el río más largo del mundo?'],
        'alternativas': [
            ['Amazonas', 1],  # Respuesta correcta
            ['Nilo', 0],
            ['Yangtsé', 0],
            ['Misisipi', 0]
        ]
    }
}

preguntas_intermedias = {
    'pregunta_1': {
        'enunciado': ['¿En qué año comenzó la Segunda Guerra Mundial?'],
        'alternativas': [
            ['1939', 1],  # Respuesta correcta
            ['1914', 0],
            ['1945', 0],
            ['1941', 0]
        ]
    },
    'pregunta_2': {
        'enunciado': ['¿Quién pintó "La Mona Lisa"?'],
        'alternativas': [
            ['Leonardo da Vinci', 1],  # Respuesta correcta
            ['Pablo Picasso', 0],
            ['Vincent van Gogh', 0],
            ['Claude Monet', 0]
        ]
    },
    'pregunta_3': {
        'enunciado': ['¿Cuál es el metal más abundante en la corteza terrestre?'],
        'alternativas': [
            ['Aluminio', 0],
            ['Hierro', 1],  # Respuesta correcta
            ['Cobre', 0],
            ['Plomo', 0]
        ]
    }
}

preguntas_avanzadas = {
    'pregunta_1': {
        'enunciado': ['¿Cuál es la velocidad de la luz en el vacío?'],
        'alternativas': [
            ['299,792,458 m/s', 1],  # Respuesta correcta
            ['100,000,000 m/s', 0],
            ['500,000,000 m/s', 0],
            ['200,000,000 m/s', 0]
        ]
    },
    'pregunta_2': {
        'enunciado': ['¿En qué año se fundó la Organización de las Naciones Unidas (ONU)?'],
        'alternativas': [
            ['1945', 1],  # Respuesta correcta
            ['1950', 0],
            ['1939', 0],
            ['1960', 0]
        ]
    },
    'pregunta_3': {
        'enunciado': ['¿Quién descubrió la penicilina?'],
        'alternativas': [
            ['Alexander Fleming', 1],  # Respuesta correcta
            ['Louis Pasteur', 0],
            ['Marie Curie', 0],
            ['Robert Koch', 0]
        ]
    }
}

pool_preguntas = {'basicas': preguntas_basicas,
                  'intermedias': preguntas_intermedias,
                  'avanzadas': preguntas_avanzadas}