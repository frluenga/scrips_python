import numpy as np
import sys

sys.setrecursionlimit(5000)

contador_externo = 0
contador_interno = 0

# Decorador para contar el tiempo de ejecución de un algoritmo.
def messure_time(function):
    def wrapper(*args,**kwargs):
        import time
        start = time.time()
        result = function(*args,**kwargs)
        total = time.time() - start
        print('Total Time: ',total,'seconds')
        return result
    return wrapper

def plusminus(arr):
    for i in arr:
        print(arr[i])
    
def contador():
    contador_externo = 0
    contador_interno = 0
    while contador_externo < 5:
        while contador_interno < 6:
            print('Externo: ', contador_externo, 'Interno: ',contador_interno)
            contador_interno += 1
        contador_externo += 1
        contador_interno = 0

def diccionario_iter():
    # Break y Continue
    # Break: Termina el Bucle y continua con el flujo del programa
    # Continue: Termina la iteración en curso y continua con el siguiente ciclo
    # de iteración 
    dic = {'a':1,'b':2,'c':3}
    for letra,numero in dic.items():
        print(letra,numero)
    for letra in dic.keys():
        print(letra)
    for values in dic.values():
        print(values)
# Validación de decimales:
def flotantes():
    x = 0.0
    for i in range(10):
        x += 0.1

    if x == 1.0:
        print(f'x = {x}')
    else:
        print(f'x != {x}')

# Enumerar todas las posibilidades
def enumeracion(objetivo):
    respuesta = 0
    while respuesta**2 < objetivo:
        respuesta += 1
    if respuesta**2 == objetivo:
        print(f'La raiz cuadrada de objetivo es: {respuesta}')
    else:
        print(f'El objetivo no tiene respuesta exacta: {respuesta}')
# Aproximar una solución
@messure_time
def aproximacion(objetivo,epsilon):
    paso = epsilon**2
    respuesta = 0.0
    while abs(respuesta**2 - objetivo ) >= epsilon and respuesta <= objetivo:
        # print('paso: ',paso,'Respuesta: ',respuesta)
        respuesta += paso
    if abs(respuesta ** 2 - objetivo >= epsilon):
        print(f'No se encontro la raiz cuadrada del objetivo: {respuesta}')
    else: print(f'La raiz cuadrada es: {respuesta}')

# Busqueda Binaria, los elementos tiene que estan ordenados
@messure_time
def busqueda_binaria(objetivo,epsilon):
    """ 
    La busqueda Binaria requiere que los elementos esten ordenados,
    es un proceso sencillo, la lista, tupla de elementos será partida
    cada vez a la mitad y evaluada si el elemento buscado es mayor o menor
    al valor donde se partio la tupla, así sabremos hacia donde seguir    
    """
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        # print(f'Bajo: {bajo} Alto: {alto} y respuesta: {respuesta} y  {respuesta**2 - objetivo}')
        if respuesta ** 2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        respuesta = (alto+bajo) / 2
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')

def seleccion_usuario():
    numero = int(input('Escoge un entero: '))
    epsilon = float(input('Escoge el error minimo: '))
    print('1: Exhaustiva ')
    print('2: Aproximación ')
    print('3: Binaria ')
    select = int(input('Elige una opción: '))
    return numero,epsilon,select

def seleccion(opcion,numero,epsilon):
    if opcion == 1:
        print(enumeracion(numero,epsilon))
    elif opcion == 2:
        print(aproximacion(numero,epsilon))
    elif opcion == 3:
        print(busqueda_binaria(numero,epsilon))
    else:
        pass



if __name__ == '__main__':

    numero, epsilon, opcion = seleccion_usuario()
    print(seleccion(opcion,numero,epsilon))

    # print(busqueda_binaria(numero,epsilon))
    # print(aproximacion(numero,epsilon))
    # print(enumeracion(numero))
    # print(flotantes())
    # arr = np.array([1,2,3,4,5])
    # print(diccionario_iter())
    # print(np.dot(arr,1))
    # print(contador())
    # arr = input('Introduce un vector: ')
    # res = plusminus(arr)