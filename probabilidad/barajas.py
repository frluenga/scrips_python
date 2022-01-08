import random
import collections
from typing import Counter
PALOS = ['espada','corazon','rombo','trebol']
VALORES = ['as','2','3','4','5','6','7','8','9','10','jota','reina','rey']

def create_baraja():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo,valor))
    return barajas
# con la siguiente funcionalidad de random podemos obtener muestras
# sin sustitución
def obtener_mano(barajas,tamano_mano):
    mano = random.sample(barajas,tamano_mano)
    return mano

def main(tamano_mano,intentos):
    barajas = create_baraja()

    manos = []
    for _ in range(intentos):
        mano = obtener_mano(barajas,tamano_mano)
        manos.append(mano)
    pares = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append((carta[1]))
        # Summary tipo conteo de los valores encontrados
        counter = dict(collections.Counter(valores))
        # recorrer el diccionario en sus valores NO llaves
        for val in counter.values():
            if val == 2:
                pares += 1
                break
    probabilidad_par = (pares / intentos)*100
    print(f'la probabilidad de obtener un par en una mano de {tamano_mano} es de {probabilidad_par} %')
            
if __name__ == '__main__':
    tamano_mano = int(input('Cuantas cartas será la mano: '))
    intentos = int(input('Cuantas intentos para sacar probabilidad: '))
    main(tamano_mano,intentos)
