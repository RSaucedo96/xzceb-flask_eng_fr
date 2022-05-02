import unittest
from translator import french_to_english
from translator import english_to_french

class TestMyModule(unittest. TestCase):
    def test_f2e1(self):
        self.assertEqual(french_to_english('Bonjour, comment vous êtes aujourd\'hui?'), 'Hello, how are you today?')
    def test_f2e_bonjour(self):
        self.assertEqual (french_to_english('Bonjour'),'Hello')
    def test_f2e_bonjour2(self):
        self.assertNotEqual(french_to_english('None'),'')
    def test_f2e_bonjour3(self):
        self.assertNotEqual(french_to_english(0),0)


class TestMyModule1(unittest.TestCase):
    def test_e2f1(self):
        self.assertEqual(english_to_french('Hello,how are you today?'), 'Bonjour, comment vous êtes aujourd\'hui?')
    def test_e2f_bonjour (self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    def test_e2f_bonjour2(self):
        self.assertNotEqual(english_to_french('None'), '')
    def test_e2f_bonjour3(self):
        self.assertNotEqual(english_to_french (0),0)
unittest.main()