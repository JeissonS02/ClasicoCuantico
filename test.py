import math

import Simulacion as sim
import numpy as np
import unittest

class TestCplxOperations(unittest.TestCase):

    def testcanicas(self):
        matriz = np.array([[0, 0, 0, 0, 0],[0, 0, 0, 1, 0],[1, 0, 1, 0, 0], [0, 0, 0, 0, 1], [0, 1, 0, 0, 0]])
        vector = np.array([1, 2, 3, 4, 5])
        clicks = 4
        resultado_esperado = np.array([0, 4, 4, 5, 2])
        resultado_real = sim.canicas(matriz, vector, clicks)
        self.assertTrue(np.array_equal(resultado_real, resultado_esperado))

    def testprobabilistic(self):
        matriz = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                   [(1/2), 0, 0, 0, 0, 0, 0, 0],
                   [(1/2), 0, 0, 0, 0, 0, 0, 0],
                   [0, (1/3), 0, 1, 0, 0, 0, 0],
                   [0, (1/3), 0, 0, 1, 0, 0, 0],
                   [0, (1/3), (1/3), 0, 0, 1, 0, 0],
                   [0, 0, (1/3), 0, 0, 0, 1, 0],
                   [0, 0, (1/3), 0, 0, 0, 0, 1]])
        vector = np.array([1, 0, 0, 0, 0, 0, 0, 0])
        clicks = 1
        resultado_esperado = np.array([0, 0.5, 0.5, 0, 0, 0, 0, 0])
        resultado_real = sim.probabilistic(matriz, vector, clicks)
        self.assertTrue(np.array_equal(resultado_real, resultado_esperado))

    def testrendija(self):
        matriz = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                   [(1/math.sqrt(2)), 0, 0, 0, 0, 0, 0, 0],
                   [(1/math.sqrt(2)), 0, 0, 0, 0, 0, 0, 0],
                   [0, (-1+1j/math.sqrt(6)), 0, 1, 0, 0, 0, 0],
                   [0, (-1-1j/math.sqrt(6)), 0, 0, 1, 0, 0, 0],
                   [0, (1-1j/math.sqrt(6)), (-1+1j/math.sqrt(6)), 0, 0, 1, 0, 0],
                   [0, 0, (-1-1j/math.sqrt(6)), 0, 0, 0, 1, 0],
                   [0, 0, (1-1j/math.sqrt(6)), 0, 0, 0, 0, 1]], dtype = complex)
        vector = np.array([1, 0, 0, 0, 0, 0, 0, 0])
        clicks = 1
        resultado_esperado = np.array([0, (1/math.sqrt(2)), (1/math.sqrt(2)), 0, 0, 0, 0, 0])
        resultado_real = sim.rendija(matriz, vector, clicks)
        self.assertTrue(np.array_equal(resultado_real, resultado_esperado))


if __name__ == '__main__':
    unittest.main()
