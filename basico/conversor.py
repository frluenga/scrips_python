menu = """
Bienvenido al conversor de monedas 💲

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opción: """

def eleccion(tipo_pesos,valor_dolar):
    pesos = float(input("¿Cuantos pesos "+ tipo_pesos + " tienes?: ")) ##ingresar datos
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $"+ dolares + " Dolares")


opcion = int(input(menu))

if opcion == 1:
    eleccion("Colombianos",3875)
elif opcion == 2:
    eleccion("Colombianos",65)
elif opcion == 3:
    eleccion("Colombianos",24)
else:
    print("Ingresa una opción correcta")

