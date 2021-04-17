import os
import sys
from datetime import datetime

import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)

from src.blockchain import Blockchain
from src.bloque import Bloque

test = Blockchain()

class Test(unittest.TestCase):
    def test_is_bloque_should_to_be_true_when_bloque_is_created(self):
        test = Bloque(0, 'correo@prueba.com', 'prueba', 'hash_archivo', 'hash_anterior', '2021-04-11 21:00:00', 0)
        test.setDateTimeString = '10'
        self.assertEqual(0, test.index)
        self.assertEqual("correo@prueba.com", test.correo)
        self.assertEqual("prueba", test.motivo)
        self.assertEqual("hash_archivo", test.hashArc)
        self.assertEqual("hash_anterior", test.hashAnt)
        self.assertEqual("2021-04-11 21:00:00", test.timestamp)
        self.assertEqual('0887a185101a6b5cbd5716d75ec940f5438ebf1f067f5ced2f62c668fb45eb12', test.hashBloque)
    
    def test_is_bloque_genesis_should_to_be_true_when_bloque_genesis_is_created(self):
        bloque0 = test.getBloqueByIndex(0)
        self.assertEqual(0, bloque0.index)
        self.assertEqual("", bloque0.correo)
        self.assertEqual("", bloque0.motivo)
        self.assertEqual("0", bloque0.hashArc)
        self.assertEqual("0", bloque0.hashAnt)
        self.assertEqual("2021-01-01 00:00:00", bloque0.timestamp)
        self.assertEqual('074c114814e06a532e2d1576e6b2263b150bd9ea7794b1e4db86f8a65281071a', test.getHashByIndex(0))
    
    def test_is_bloque_One_should_to_be_true_when_bloque_One_is_created(self):
        test._Blockchain__crearBloque("correo@bloqueOne.com", "prueba", "hashArc", "2021-01-01 22:00:00")
        bloque1 = test.getBloqueByIndex(1)
        self.assertEqual(1, bloque1.index)
        self.assertEqual("correo@bloqueOne.com", bloque1.correo)
        self.assertEqual("prueba", bloque1.motivo)
        self.assertEqual("hashArc", bloque1.hashArc)
        self.assertEqual("074c114814e06a532e2d1576e6b2263b150bd9ea7794b1e4db86f8a65281071a", bloque1.hashAnt)
        self.assertEqual("2021-01-01 22:00:00", bloque1.timestamp)
        self.assertEqual('05972bdddaffebafb024ab5f22c3acd65a9e81c0d514277715e60d36cc479024', test.getHashByIndex(1))
    
    def test_is_bloque_Two_should_to_be_true_when_bloque_One_is_created(self):
        test._Blockchain__crearBloque("correo@bloqueOne.com", "pruebaBloque2", "hashArc", "2021-01-01 22:00:00")
        bloque2 = test.getBloqueByIndex(2)
        self.assertEqual(2, bloque2.index)
        self.assertEqual("correo@bloqueOne.com", bloque2.correo)
        self.assertEqual("pruebaBloque2", bloque2.motivo)
        self.assertEqual("hashArc", bloque2.hashArc)
        self.assertEqual("05972bdddaffebafb024ab5f22c3acd65a9e81c0d514277715e60d36cc479024", bloque2.hashAnt)
        self.assertEqual("2021-01-01 22:00:00", bloque2.timestamp)
        self.assertEqual('050bd13108ff2c65404558a17b57afb388d03d6f9004aca4db81880c2bc5bd5d', test.getHashByIndex(2))

    def test_is_Singleton_should_to_be_true_when_Singleton_works(self):
            testSingleton1 = Blockchain()
            testSingleton2 = Blockchain()
            message = "Test Singleton doesn't works"
            self.assertTrue(id(testSingleton1) == id(testSingleton2), message)

if __name__ == '__main__':
    unittest.main()