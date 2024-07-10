import unittest
import string
from units.rand_string import RandString

# python -m unittest -v tests.rand_string : untuk lebih teliti
# python -m unittest tests.rand_string : untuk tidak memerlukan ketelitian

class TestRandString(unittest.TestCase):

    def test_besar(self):
        result = RandString("besar", 10)
        self.assertEqual(len(result), 10)
        self.assertTrue(result.isupper())

    def test_kecil(self):
        result = RandString("kecil", 15)
        self.assertEqual(len(result), 15)
        self.assertTrue(result.islower())

    def test_besar_kecil(self):
        result = RandString("besar_kecil", 8)
        self.assertEqual(len(result), 8)
        self.assertTrue(result.isalpha())

    def test_digit(self):
        result = RandString("digit", 12)
        self.assertEqual(len(result), 12)
        self.assertTrue(result.isdigit())

    def test_tanda_baca(self):
        result = RandString("tanda_baca", 7)
        self.assertEqual(len(result), 7)
        self.assertTrue(all(char in string.punctuation for char in result))

    def test_alpanumerik(self):
        result = RandString("alpanumerik", 20)
        self.assertEqual(len(result), 20)
        self.assertTrue(result.isalnum())

    def test_campuran(self):
        result = RandString("campuran", 25)
        self.assertEqual(len(result), 25)
        self.assertTrue(any(char.isupper() for char in result))
        self.assertTrue(any(char.islower() for char in result))
        self.assertTrue(any(char.isdigit() for char in result))
        self.assertTrue(any(char in string.punctuation for char in result))

    def test_panjang_negatif(self):
        with self.assertRaises(ValueError):
            RandString("besar", -5)

    def test_panjang_nol(self):
        with self.assertRaises(ValueError):
            RandString("besar", 0)

if __name__ == "__main__":
    unittest.main()

