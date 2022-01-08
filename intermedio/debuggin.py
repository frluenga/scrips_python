"""
 Errores de logica: Debuggin
 Errores de codigo: return traceback:
     SyntaxError: Detienen el programa
     Exception: Sigue ejecutando el siguiente codigo como: 
        keyboardInterrupt: Elevar una exception, lo creo y lo va 
        moviendo de adentro hacia a fuera
        KeyError: Acceder a un diccionario con una llave que no 
        existe.
        IndexError: Acceder a un indice de una lista que no existe
        FileNotFoundError: No se encuentra el archivo
        ZeroDivisionError: Dividir por cero
        ImportError: Problemas de importación de un modulo
    Ejemplo: Leer desde abajo hasta arriba
"""
def divisors(num):
    divisors = []
    try:
        if num <= 0:
            raise ValueError()            
        for i in range(1,num+1):
            if num % i == 0:
                divisors.append(i)
        return divisors
    except ValueError as ve:
        print('Debes ingresar un numero entero.')   




def run():
    num = int(input('Ingresa un numero: '))
    print(divisors(num))
    print('termino mi programa')


if __name__ == '__main__':
    run()