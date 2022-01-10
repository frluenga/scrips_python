def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, 'Solo puedes usar cadenas'
        return string * n
    return repeater

def division_by(n:int):
    if type(n) != int:
        raise ValueError('Solo numeros enteros como divisor')

    def division(x:int) -> int:
        try:
            if type(x) != int:
                raise ValueError('Solo enteros para divirlos')
            return x/n
        except ValueError as ve:
            print(ve)
            return False
    return division


def run():
    numero = int(input('Que numero vas a dividir: '))
    dividir_en = int(input('En cuanto quieres dividirlo: '))
    div = division_by(dividir_en)
    print(div(numero))

if __name__ == '__main__':
    run()


