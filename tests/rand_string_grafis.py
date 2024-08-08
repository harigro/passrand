import unittest
from units.kombinasi import rand_string_grafis

class TestRandStringGrafis(unittest.TestCase):

    def test_valid_besar_kecil_digit_tanda_baca(self):
        result = rand_string_grafis('besar_kecil_digit_tanda_baca', 10)
        self.assertEqual(len(result), 10)
        self.assertTrue(any(c.isupper() for c in result))
        self.assertTrue(any(c.islower() for c in result))
        self.assertTrue(any(c.isdigit() for c in result))
        self.assertTrue(any(c in "!@#$%^&*()[]{};:,.<>?/" for c in result))

    def test_valid_hanya_besar(self):
        result = rand_string_grafis('besar', 8)
        self.assertEqual(len(result), 8)
        self.assertTrue(all(c.isupper() for c in result))

    # def test_invalid_tipe_string(self):
    #     with self.assertRaises(KeyError):
    #         rand_string_grafis('invalid_type', 5)

    # def test_panjang_negatif(self):
    #     with self.assertRaises(ValueError):
    #         rand_string_grafis('kecil', -3)

    # def test_panjang_nol(self):
    #     result = rand_string_grafis('digit', 0)
    #     self.assertEqual(result, '')

if __name__ == '__main__':
    unittest.main()

