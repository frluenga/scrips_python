def es_primo(numero):
    contador = 0

    for i in range(1,numero+1): ## se coloca mas 1 para asegurarse que llegue hasta el ultimo
        if i == 1 or i == numero: ## en este caso se esta saltando la división en 1 y por el mismo
            continue 
        if numero % i == 0: ## si se presenta una división exacta se aumenta el contador
            contador += 1
    if contador == 0:
        return True


def run():
    numero = int(input("Escribre un número: "))
    if es_primo(numero):
        print("Es primo")
    else:
        print("No es primo")


if __name__ == "__main__":
    run()