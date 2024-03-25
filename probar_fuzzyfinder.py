#!/usr/bin/env python3

""" 
objetivo:   Entender ideas basicas de la Busqueda Borrosa
            - Construidas con regex
           https://blog.amjith.com/fuzzyfinder-in-10-lines-of-python 

contexto:   FuzzyFinder es una característica popular disponible en editores para abrir archivos                     
            - La idea es comenzar a escribir cadenas parciales de la ruta completa                                     
            - La lista de sugerencias se reducirá para que coincida con el archivo deseado 

proceso :   Hay 9 lineas a las cuales se le aplica un patron de busqueda
            - hay la posibilidad de intentar 4 veces
"""

import re

from colorama import init, Fore
init(autoreset=True)

print(Fore.YELLOW + __doc__)

def fuzzyfinder(user_input, collection):
    """
    Entrada: cadena del usuario y coleccion donde voy a buscar
    Salida : lista de sugerencias
    proceso: El mas sencillo """
    suggestions = []
    # El ? como cuantificador de repetición cambia este comportamiento a no codicioso
    pattern = '.?'.join(user_input)   
    print(f" El patron es: {pattern} \n")
    # Compiles a regex.
    regex = re.compile(pattern)  
    for item in collection:
        # Checks if the current item matches the regex.
        match = regex.search(item)   

        if match:
            """ 
            Convertimos la lista de sugerencias a lista de tuplas 
            El primer  elemento es el largo del match
            El segundo elemento es la posición de la coincidencia
            El tercer  elemento es la cadena objetivo
            Python los ordenará según el primer elemento de la tupla
            Utilizará el segundo elemento como desempate. 
            """
            suggestions.append((len(match.group()), match.start(), item))
    # iterar sobre la lista ordenada de tuplas y extraer solo lo que nos interesa 
    return [x for _, _, x in sorted(suggestions)]

def imprime(lista):
    """ Imprime lista verticalmente """
    for linea in range(len(lista)):
        print(linea, lista[linea])
    return "***"

input(Fore.YELLOW + " - Mostrar coleccion donde buscamos: ")

collection = [
        "Una mentira del tamaño del Everest",
        "No me creo lo que dicen los medios ni los ejpertos",
        "Solo una persona que ayuna puede experimentar los cambios",
        "Mucha gente inventando",
        "Para mí todo lo que sea forzado o en exceso hace mal",
        "Entre el ayuno y comer menos, pero saludable, es lo ideal",
        "Era normal cuando tenías que salir a buscar tu comida",
        "Pues yo involuntariamente hago ayuno intermitente",
        "El problema es que a nivel mediático"
        ]
imprime(collection)

# infinite loop stop at n
n = 0
while True:
    # stop loop
    if n == 4:
        break
    n += 1

    user_input = input(f"\n - {n} Entre patron borroso para buscar: ")

    # realizamos busqueda
    salida = fuzzyfinder(user_input, collection) 
    
    # Check the empty list using the implicit Booleans 
    if salida:
        imprime(salida)
        continue
    else:
        print(" -------- Sin sugerencia: ")
        continue


