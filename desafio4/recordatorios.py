# -*- coding: utf-8 -*-
"""
Recordatorios

@author: elita
"""


def main():
    #Lista anidada de recordatorios
    recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
    ['2021-05-01', "15:00", "No trabajar"],
    ['2021-07-15', "13:00", "No hacer nada es feriado"],
    ['2021-09-18', "16:00", "Ramadas"],
    ['2021-12-25', "00:00", "Navidad"]]

    #Agrega evento el 2 de Febrero de 2021 a las 6 de la mañana para “Empezar el Año”.
    recordatorios.append(['2021-02-02',"06:00","Empezar el Año"])

    #Actualizar el 15 de Julio porque no es feriado. Editar de tal manera que sea el 16 de Julio.
    recordatorios[2][0] = '2021-07-16'

    #Elimine el evento del día del trabajo.
    recordatorios.pop(1)

    #Agregar una cena de Navidad y de Año Nuevo cuando corresponda. Ambas a las 22 hrs
    recordatorios.append(['2021-12-24',"22:00","Cena de Navidad"])
    recordatorios.append(['2021-12-31',"22:00","Cena de Año Nuevo"])

    #Ordena la lista por date
    recordatorios.sort()
    
    #Muestra la lista anidada de recordatorios
    [print(act) for act in recordatorios]


#Main
if __name__ == "__main__":
    # Ejecutar el script por primera vez
    main()