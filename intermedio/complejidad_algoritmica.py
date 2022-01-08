import time
import sys

def factorial_recursivo(n):
    respuesta = 1
    if n == 1:
        return 1    

    return n * factorial_recursivo(n-1)


def factorial_while(n):
    respuesta = 1

    while n>1:
        respuesta *= n
        n -= 1

    return respuesta

def main():
    n = 2000

    comienzo = time.time()
    factorial_while(n)
    final = time.time()
    print(final - comienzo)

    comienzo = time.time()
    factorial_recursivo(n)
    final = time.time()
    print(final - comienzo)

if __name__ == '__main__':
    sys.setrecursionlimit(1000000)
    main()
