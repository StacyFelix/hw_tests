import unittest
import ya_translate


class TestSecretaryProgram(unittest.TestCase):
    def setUp(self):
        self.valid_data = {
            'text_untranslate': "hello, World",
            'lang': "en"
        }
        self.invalid_data = {
            'text_untranslate': "hello, World",
            'lang': "йц"
        }

    def test_translate_valid_data(self):
        res = ya_translate.translate(self.valid_data['text_untranslate'], self.valid_data['lang'])
        self.assertEqual(res[1], "Привет, Мир")
        self.assertEqual(res[0], 200)

    def test_translate_invalid_data(self):
        res = ya_translate.translate(self.invalid_data['text_untranslate'], self.invalid_data['lang'])
        self.assertEqual(res[1], "")
        self.assertNotEqual(res[0], 200)


if __name__ == '__main__':
    unittest.main()
