import os
import sys

import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)

from src.blockchain import Block, Blockchain

class Test(unittest.TestCase):
    def test_block(self):
        test = Blockchain()
        self.assertEqual(test.cadena[0].correo, "")
        
if __name__ == '__main__':
    unittest.main()