import unittest

from security.accessControl import *

class TestSistemaParaTeste(unittest.TestCase):
    def test_testeLoginUsuario(self):
        self.assertEqual(testeUser('Rosineide'), 'Rosineide')
    
    # def test_testeLoginSenha(self):
    #     self.assertEqual(testeSenha(88883), 88883)
    
	

if __name__ == '__main__':
    unittest.main()