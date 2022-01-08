objetivo_1 = int(input('Escoge un numero entero: '))
epsilon = 0.009
paso = epsilon**2
respuesta = 0.0

while abs(respuesta**2 - objetivo_1) >= epsilon and respuesta <= objetivo_1: 
    print(abs(respuesta**2 - objetivo_1),respuesta,paso, epsilon)
    respuesta += paso

if (respuesta**2 - objetivo_1) >= epsilon:
    print(f'no se encontro la raiz de {objetivo_1}')
else:
    print(f'{objetivo_1} tiene como raiz {respuesta}')