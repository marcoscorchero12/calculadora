import unittest
from calculadora import suma, resta, multiplicacion, division, exponenciacion

class TestCalculadora(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)
        self.assertEqual(suma(-2, 3), 1)

    def test_resta(self):
        self.assertEqual(resta(5, 3), 2)
        self.assertEqual(resta(2, -3), 5)

    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(2, 3), 6)
        self.assertEqual(multiplicacion(-2, 3), -6)

    def test_division(self):
        self.assertEqual(division(6, 3), 2)
        self.assertRaises(ValueError, division, 6, 0)

    def test_exponenciacion(self):
        self.assertEqual(exponenciacion(2, 3), 8)
        self.assertEqual(exponenciacion(2, 0), 1)

if __name__ == '__main__':
    unittest.main()
