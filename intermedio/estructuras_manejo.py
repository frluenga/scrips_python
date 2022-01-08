def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n-1)

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def aplicar_operaciones(num):
    # Guarda funciones para aplicar depues
    operaciones = [abs, float]
    resultado = []
    for operacion in operaciones:
        resultado.append(operacion(num))

    return resultado

def coordenada():
    return (5,6)

def rango(inicio,fin):
    numeros = range(inicio,fin,1)
    return numeros

# Para verificar si dos objetos son el mismo se usa
# is para evaluarlo, porque con == valida son los 
# valores internos

# Mutabilidad de las listas, (append, pop,remove,insert)
#list comprehension
lista = range(1,20,1)
suma = [i for i in lista if i % 2 == 0]
part = [i / len(lista) for i in lista]
# Diccionarios comprehension

my_dic = {'Edad':24,'Nombre': 'Fabian','Dirección':'cll 24 1 255'
            ,'otro':0}
        
del my_dic['otro']

number = range(10)
my_dict = {}

for i in number:
    my_dict[i] = i**2

# Dic Comprehension
my_dict_1 = {i:i*10 for i in number if i % 2 == 0}

# lambda para diccionarios
fahrenheit = {'t1':-30,'t2':-20,'t3':-10,'t4':0}

celcius = (map(lambda x:(float(5)/9)*(x-32),fahrenheit.values()))
celsius_dict = dict(zip(fahrenheit.keys(), celcius))

celsius_comp = {k:(float(5)/9)*(v-32) for k,v in fahrenheit.items()}

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f':6}
# Identify odd and even entries
dict1_tripleCond = {k:('even' if v%2==0 else 'odd') for (k,v) in dict1.items()}


if __name__ == '__main__':

    print(dict1_tripleCond)
    # n = int(input('Escribe un entero: '))
    # print(factorial(n))
    # x,y = coordenada()
    # numero = rango(1,10)
    # for i in numero:
    #     print(i)