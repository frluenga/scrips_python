import numpy as np
import pandas as pd

def fix(frase):
    frase = frase.lower().replace(",","").replace(".","").replace("!"," ").replace("(","").replace(")","").split(" ")
    
    palabras = ["excelente","ignorante","bien","bueno","entiendo","perdida","luto"]
    positiva = ["excelente","bien"]
    neutra = ["bueno","entiendo"]
    negativa = ["ignorante","perdida","luto"]

    avg = []
    positivas = 0
    neutras = 0
    negativas = 0

    for i in frase:
        if i in frase and i in palabras:
            avg.append(frase.count(i)) ## Contar palabra que estan en la lista general seleccionada
        else:
            continue

    for j in frase:
        if j in frase and j in positiva:
            positivas += 1
        elif j in frase and j in neutra:
            neutras += 1
        elif j in frase and j in negativa:
            negativas += 1

    avg = np.array(avg)
    score = np.array([positivas,neutras,negativas])
    u =[1]
    a = (u/(len(palabras))) * avg
    s = score/(score[0]+score[1]+score[2])

    return  frase,a,s[0],s[1],s[2]


twit1 = "Gran mexicano y excelente en su área, su muerte es una enorme perdida y debería ser luto nacional!!!"
twit2 = "Vaya señora que bueno que se asesora por alguien inteligente no por el ignorante del Gatt."
twit3 = "Se me ocurre y sin ver todos los videos de Plazti que me informéis por dónde empiezo. Entiendo que os tendría que decir quién soy y que quiero, vamos conocerme para asesorarme bien. Un saludo"
twit4 = "Soy docente universitario, estoy intentando preparar mis clases en modo platzi bien didáctico, (le llamo modo noticiero), descargue una plataforma gratuita de grabación y transmisión de vídeo, se llama Obs estudio!bueno la sigo remando con sus funciones pero sé que saldrá algo!"

resultados = []
twitter = [twit1,twit2,twit3,twit4]
for i in twitter:
    resultados.append(fix(i))

df = pd.DataFrame(resultados,columns=["twit","calidad","s_positivo","s_neutro","s_negativo"])
df