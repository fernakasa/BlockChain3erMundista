import os
import sys

import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)

from src.blockchain import Bloque, Blockchain

class Test(unittest.TestCase):
    def test_is_bloque_genesis_correo_should_to_be_true_when_correo_is_empty(self):
        test = Blockchain()
        self.assertEqual(test.cadena[0].correo, "")

    def test_is_bloque_genesis_index_should_to_be_true_when_index_is_zero(self):
        test = Blockchain()
        self.assertEqual(test.cadena[0].index, 0)
    
    def test_is_bloque_genesis_motivo_should_to_be_true_when_motivo_is_empty(self):
        test = Blockchain()
        self.assertEqual(test.cadena[0].motivo, "")
    
    def test_is_bloque_genesis_hash_archivo_should_to_be_true_when_hash_archivo_is_string_zero(self):
        test = Blockchain()
        self.assertEqual(test.cadena[0].hashArc, "0")
    
    def test_is_bloque_genesis_hash_anterior_should_to_be_true_when_hash_anterior_is_string_zero(self):
        test = Blockchain()
        self.assertEqual(test.cadena[0].hashAnt, "0")
    
    def test_is_bloque_genesis_hash_bloque_should_to_be_true_when_hash_bloque_is_equal_to_getHashByIndex(self):
        test = Blockchain()
        self.assertEqual(test.cadena[0].hashBloque, test.getHashByIndex(0))
        
if __name__ == '__main__':
    unittest.main()