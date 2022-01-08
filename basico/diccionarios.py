def run():
    # mi_diccionario = {
    #     "Llave1" : 1,
    #     "Llave2" : 2,
    #     "Llave3" : 3,
    # }
    # print(mi_diccionario["Llave1"])
    # print(mi_diccionario["Llave2"])
    # print(mi_diccionario["Llave3"])

    poblacion_paises = {
        "Argentina": 44_938_712,
        "Brasil": 210_147_125,
        "Colombia": 50_372_424
    }
    # print(poblacion_paises["Argentina"])

    # for pais in poblacion_paises.keys():
    #     print(pais)
    # for pais in poblacion_paises.values():
    #     print(pais)

    for pais,poblacion in poblacion_paises.items():
        print(pais)
        print(pais + "Tiene " + str(poblacion) + "Habitantes")

if __name__ == "__main__":
    run()