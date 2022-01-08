import random

def tirar_dado():
    result_lanzamiento = 0
    tiro = random.choice([1,2,3,4,5,6])
    result_lanzamiento= tiro

    return result_lanzamiento

def main(numero_de_intentos):
    tiros_dado_1 = []
    tiros_dado_2 = [] 

    for _ in range(numero_de_intentos):
        secuencia_de_tiros_1 = tirar_dado()
        secuencia_de_tiros_2 = tirar_dado()
        tiros_dado_1.append(secuencia_de_tiros_1)
        tiros_dado_2.append(secuencia_de_tiros_2)

    tiros_con_12 = 0
    
    for i in range(len(tiros_dado_1)):
        if (tiros_dado_1[i] + tiros_dado_2[i]) == 12:
                tiros_con_12 += 1

    probabilidad_de_12 = (tiros_con_12 / numero_de_intentos)*100
    print(f'Probabilidad de obtener por lo menos 12 tirando dos dados es = {probabilidad_de_12} %')

if __name__ == '__main__':
    numero_de_intentos = int(input('Cuantas veces repetimos el ejercicio: '))

    main(numero_de_intentos)