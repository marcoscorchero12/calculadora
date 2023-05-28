import unittest
from calculadora import suma, resta, multiplicacion, division, exponente

class CalculadoraTest(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)

    def test_resta(self):
        self.assertEqual(resta(5, 2), 3)

    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(4, 3), 12)

    def test_division(self):
        self.assertEqual(division(10, 2), 5)
        self.assertRaises(ValueError, division, 10, 0)

    def test_exponente(self):
        self.assertEqual(exponente(2, 3), 8)

if __name__ == '__main__':
    unittest.main()
