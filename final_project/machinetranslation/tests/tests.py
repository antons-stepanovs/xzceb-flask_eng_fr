import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):

    def test_english_to_french(self):
        english_text = "Hello"
        french_text = english_to_french(english_text)
        self.assertEqual(french_text, "Bonjour")

    def test_french_to_english(self):
        french_text = "Bonjour"
        english_text = french_to_english(french_text)
        self.assertEqual(english_text, "Hello")

    def test_english_to_french_null_input(self):
        english_text = None
        self.assertIsNone(english_text)

    def test_french_to_english_null_input(self):
        french_text = None
        self.assertIsNone(french_text)

if __name__ == '__main__':
    unittest.main()
