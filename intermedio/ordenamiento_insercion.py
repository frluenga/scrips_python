import random

def ordenamiento_por_insercion(lista):

    for i in range(1, len(lista)):
        valor_actual = lista[i]
        posicion_actual = i
        for j in range(i,0,-1):
            if lista[j] < lista[j-1]:
                lista[j], lista[j-1] = lista[j-1], lista[j]
            else:
                lista[posicion_actual] = valor_actual

    return lista

def ordenamiento_por_insercion_while(lista):

    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual
        
    return lista

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamaño sera la lista?: '))
    lista = [random.randint(0,100) for i in range(tamano_de_lista)]
    print(lista)

    lista_ordenada = ordenamiento_por_insercion_while(lista)
    print(lista_ordenada)
