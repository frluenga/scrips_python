import random

def  busqueda_lineal(lista, objetivo, contador = 0):
    match = False

    for elemento in lista:
        contador += 1
        if elemento == objetivo:
            match = True
            
            break
    return [match,contador]

def main():
    tamano_de_lista = int(input('De que tamaño sera la lista?: '))
    objetivo = int(input('Que numero quieres encontrar: '))

    lista = [random.randint(0,1000) for i in range(tamano_de_lista)]
    
    encontrado = busqueda_lineal(lista,objetivo)
    iteraciones = encontrado[1]
    
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista con {iteraciones} iteraciones')

if __name__ == '__main__':
    main()
