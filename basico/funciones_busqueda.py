def busqueda_exhaustiva(objetivo):
    respuesta = 0

    while respuesta**2 < objetivo:
        respuesta += 1

    if respuesta**2 == objetivo:
        print(f'la raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene raiz cuadrada')

def busqueda_aproximacion(objetivo):
    epsilon = 0.009
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo: 
        print(abs(respuesta**2 - objetivo),respuesta,paso, epsilon)
        respuesta += paso

    if (respuesta**2 - objetivo) >= epsilon:
        print(f'no se encontro la raiz de {objetivo}')
    else:
        print(f'{objetivo} tiene como raiz {respuesta}')

def busqueda_binaria(objetivo):
    epsilon = 0.001
    bajo = 0.0
    alto = max(1.0,objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo = {bajo} alto = {alto}, respuesta = {respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2
    print(f'la raiz cuadrada de {objetivo} es {respuesta}')

eleccion = int(input('Elige un numero para encontrar raiz cuadrada: '))
eleccion_1 = int(input('1: Busqueda Exhaustiva... 2: Busqueda Aproximación... 3: Busqueda Binaria...'))

if eleccion_1 == 1:
    busqueda_exhaustiva(eleccion)
elif eleccion_1 == 2:
    busqueda_aproximacion(eleccion)
elif eleccion_1 == 3:
    busqueda_binaria(eleccion)
else:
    print('Elige una pinche opción correcta.... Gracias')