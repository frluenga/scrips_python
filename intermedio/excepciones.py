def divide_elementos_de_lista(lista,divisor):
    try:
        return [i/divisor for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return lista

lista = list(range(10))
divisor = 0

def busca_pais(paises, pais):
    """
    Paises es un diccionario. Pais es la llave.
    Codigo con el principio EAFP.
    """
    
    try:
        return paises[pais]
    except KeyError:
        return None
# Programación Defensiva

def primera_letra(lista_de_palabras):
    primeras_letras = []
    for palabra in lista_de_palabras:
        assert type(palabra) == str, f'{palabra} no es str'
        assert len(palabra) > 0, 'No se permiten str vacios'

        primeras_letras.append(palabra[0])
    return primeras_letras

# TRY AND EXCEPT 
# RAISE: Eleva el tipo de error cuando se cumple una condición
def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError('No se puede ingresar una cadena vacia')
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False

def divisors(num):
    divisors = []         
    for i in range(1,num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():

    try:
        num = input('Ingresa un numero: ')
        assert num.isnumeric(), f'{num} no es un numero'
        assert int(num) > 0, f'{num} no tiene divisor'
        print(divisors(int(num)))
        print('termino mi programa')
    except ValueError as ve:
        print('Revisa los valores')
        
# finally
""" 
    Cerrar un archivo dentro de python, cerrar una conexión base de datos
    liberar recursos externos
"""
# f = open('Archivo.txt')
# finally:
#     f.close()



if __name__ == '__main__':
    run()
    #print(divide_elementos_de_lista(lista,divisor))
    # paises = {'Colombia':'Bogota','Peru':'Lima','Venezuela':'Caracas'}
    # print(busca_pais(paises,'Colombiaa'))
    # print(primera_letra([1,'hola']))    
