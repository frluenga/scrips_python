import random

def busqueda_binaria(lista,comienzo,final,objetivo, contador=0):
    contador += 1
    print(f'buscando el {objetivo} entre {lista[comienzo]} y {lista[final-1]}: iteración: {contador}')
    if comienzo > final:
        return [False,contador]
    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return [True,contador]
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista,medio+1,final,objetivo,contador)
    else:
        return busqueda_binaria(lista,comienzo,medio-1,objetivo,contador)

    
def main():
    tamano_de_lista = int(input('De que tamaño sera la lista?: '))
    objetivo = int(input('Que numero quieres encontrar: '))

    lista = sorted([random.randint(0,1000) for i in range(tamano_de_lista)])
    
    encontrado = busqueda_binaria(lista, 0, len(lista),objetivo)
    iteraciones = encontrado[1]
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista y presento {iteraciones} iteraciones')

if __name__ == '__main__':
    main()