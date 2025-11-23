import unittest
from Examen2 import MiClase

class TestMiClase(unittest.TestCase):
    def setUp(self):
        self.objeto = MiClase(5, 120, 12, ["Canción 1"], [0.8])

    # Pruebas para ObtieneValencia
    def test_ObtieneValencia_con_impares(self):
        # Número con impares
        resultado = self.objeto.ObtieneValencia(1234567)
        self.assertEqual(resultado, 4)

    def test_ObtieneValencia_sin_impares(self):
        # Número solo con pares
        resultado = self.objeto.ObtieneValencia(2468)
        self.assertEqual(resultado, 0)

    # Pruebas para DivisibleTempo
    def test_DivisibleTempo_numero_comun(self):
        # Divisores de 10
        resultado = self.objeto.DivisibleTempo(10)
        self.assertEqual(resultado, [1, 2, 5, 10])

    def test_DivisibleTempo_numero_primo(self):
        # Divisores de 7
        resultado = self.objeto.DivisibleTempo(7)
        self.assertEqual(resultado, [1, 7])

if __name__ == '__main__':
    unittest.main()