#Alumno: Rebeca Ledesma
#Carnet: 15-10771
#Exámen 2
#Pregunta 2 Unit Tests

from pregunta2examen import Postfija, Prefija
import unittest

class TestPostfija(unittest.TestCase):
    def test_evaluar(self):
        p = Postfija(['5', '3', '+', '4', '*'])
        self.assertEqual(p.evaluar(), 32)

    def test_aInfija(self):
        p = Postfija(['5', '3', '+', '4', '*'])
        self.assertEqual(p.aInfija(), '((5+3)*4)')

class TestPrefija(unittest.TestCase):
    def test_evaluar(self):
        p = Prefija(['*', '+', '5', '3', '4'])
        self.assertEqual(p.evaluar(), 32)

    def test_aInfija(self):
        p = Prefija(['*', '+', '5', '3', '4'])
        self.assertEqual(p.aInfija(), '((5+3)*4)')

if __name__ == '__main__':
    unittest.main()
