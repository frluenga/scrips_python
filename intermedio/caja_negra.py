import unittest

def suma(num1,num2):
    return abs(num1) + num2
# Crear una clase de prueba
class CajaNegraTest(unittest.TestCase): # Es un caso de prueba
    def test_suma_dos_positivos(self):
        num_1 = 10
        num_2 = 5

        resultado = suma(num_1,num_2)

        # Esto funciona asi:
        # (valor, valorQuerido) = valor == valorQuerido (Nos devuelve un true o false)
        self.assertEqual(resultado, 15)
        # Esto funciona asi:
        #  (valor, valorQuerido) = valor > valorQuerido (Nos devuelve un true o false)
        self.assertGreater(resultado, 14)
        # Esto funciona asi:
        #  (valor, valorQuerido) = valor >= valorQuerido (Nos devuelve un true o false)
        self.assertGreaterEqual(resultado, 15)
        # Esto funciona asi:
        #  (valor, valorQuerido) = valor < valorQuerido (Nos devuelve un true o false)
        self.assertLess(resultado, 16)
        # Esto funciona asi:
        #  (valor, valorQuerido) = valor <= valorQuerido (Nos devuelve un true o false)
        self.assertLessEqual(resultado, 15)

    def test_suma_dos_negativos(self):
        num_1 = -10
        num_2 = -7

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, -17)

if __name__ == '__main__':
        unittest.main()