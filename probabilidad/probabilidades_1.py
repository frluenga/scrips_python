import random
# Codigo tirando dos dados
# Calcular la probabilidad de que la suma entre los dos dados de 12.
def tirar_dado(numero_de_tiros):
    result_lanzamiento = []
    for _ in range(numero_de_tiros):
        tiro_1 = random.choice([1,2,3,4,5,6])
        tiro_2 = random.choice([1,2,3,4,5,6])
        suma = tiro_1 + tiro_2
        result_lanzamiento.append(suma)

    return result_lanzamiento

def main(numero_de_tiros,numero_de_intentos):
    tiros = [] 

    for _ in range(numero_de_intentos):
        secuencia_de_tiros = tirar_dado(numero_de_tiros)
        tiros.append(secuencia_de_tiros)  

    tiros_12 = 0

    for tiro in tiros:
        if 12 in tiro:
            tiros_12 += 1

    probabilidad_de_12 = (tiros_12 / numero_de_intentos)*100
    print(f'Probabilidad de obtener por lo menos 12 tirando dos dados es = {probabilidad_de_12} %')

if __name__ == '__main__':
    numero_de_tiros = int(input('Cuantas veces tiramos el dado: '))
    numero_de_intentos = int(input('Cuantas veces simulamos el ejercicio: '))

    main(numero_de_tiros, numero_de_intentos)