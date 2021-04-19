import os
import sys
from datetime import datetime

import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)

from src.blockchain import Blockchain
from src.bloque import Bloque

test = Blockchain()

class BlockchainTest(unittest.TestCase):
    
    def test_is_bloque_genesis_should_to_be_true_when_bloque_genesis_is_created(self):
        bloque0 = test.getBloqueByIndex(0)
        self.assertEqual(0, bloque0.index)
        self.assertEqual("", bloque0.correo)
        self.assertEqual("", bloque0.motivo)
        self.assertEqual("0", bloque0.hashArc)
        self.assertEqual("0", bloque0.hashAnt)
        self.assertEqual("2021-01-01 00:00:00", bloque0.timestamp)
        self.assertEqual('009c11da8b892d08e022ccd9e16856fb5d998e1d38f852bc49f62bd1d8ee9794', test.getHashByIndex(0))
    
    def test_is_bloque_One_should_to_be_true_when_bloque_One_is_created(self):
        test._Blockchain__crearBloque("correo@bloqueOne.com", "prueba", "hashArc", "2021-01-01 22:00:00")
        bloque1 = test.getBloqueByIndex(1)
        self.assertEqual(1, bloque1.index)
        self.assertEqual("correo@bloqueOne.com", bloque1.correo)
        self.assertEqual("prueba", bloque1.motivo)
        self.assertEqual("hashArc", bloque1.hashArc)
        self.assertEqual("009c11da8b892d08e022ccd9e16856fb5d998e1d38f852bc49f62bd1d8ee9794", bloque1.hashAnt)
        self.assertEqual("2021-01-01 22:00:00", bloque1.timestamp)
        self.assertEqual('0025e03ccbc3a529d0d8a6aa39106409e0636ea071b28a54fb89347f514fa3f0', test.getHashByIndex(1))
    
    def test_is_bloque_Two_should_to_be_true_when_bloque_two_is_created(self):
        test._Blockchain__crearBloque("correo@bloqueOne.com", "pruebaBloque2", "hashArc", "2021-01-01 22:00:00")
        bloque2 = test.getBloqueByIndex(2)
        self.assertEqual(2, bloque2.index)
        self.assertEqual("correo@bloqueOne.com", bloque2.correo)
        self.assertEqual("pruebaBloque2", bloque2.motivo)
        self.assertEqual("hashArc", bloque2.hashArc)
        self.assertEqual("0025e03ccbc3a529d0d8a6aa39106409e0636ea071b28a54fb89347f514fa3f0", bloque2.hashAnt)
        self.assertEqual("2021-01-01 22:00:00", bloque2.timestamp)
        self.assertEqual('0007b882108f9a9a7cc0ff38e6569a4580ab249594019068bfc804e29d487b5d', test.getHashByIndex(2))

if __name__ == '__main__':
    unittest.main()