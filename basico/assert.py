def primera_letra(lista_de_palabras=[]):
    """
    Retorna primera letra

    Resive un str y retorna su primera letra 
    """
    primeras_letras = []

    for palabra in lista_de_palabras:
            
        assert type(palabra) == str, f'{palabra} no es un str'
        assert len(palabra) > 0, 'No se permiten str vacios'
        primeras_letras.append(palabra[0])

    return primeras_letras

def run():
    lista = ['Hola','Mundo','Como','Estan']
    print(primera_letra(lista))
    

if __name__ == "__main__":
    run()