import unittest
import string
from units.rand_string import kombinasi_dict

data = {
        'besar': string.ascii_uppercase,
        'kecil': string.ascii_lowercase,
        'digit': string.digits,
        'tanda_baca': string.punctuation
    }

class TestKombinasiEnum(unittest.TestCase):

    def setUp(self):
        self.result = kombinasi_dict(data)

    def test_combinations_length(self):
        # Test panjang data
        self.assertEqual(len(self.result), 16)

    def test_combination_existence(self):
        # Test apakah kombinasi tertentu ada dalam hasil
        self.assertIn('besar', self.result)
        self.assertIn('kecil', self.result)
        self.assertIn('digit', self.result)
        self.assertIn('tanda_baca', self.result)
        self.assertIn('besar_kecil', self.result)
        self.assertIn('besar_digit_tanda_baca', self.result)
        self.assertIn('kecil_digit', self.result)

    def test_combination_values(self):
        # Test nilai dari kombinasi tertentu
        self.assertEqual(self.result['besar'], string.ascii_uppercase)
        self.assertEqual(self.result['kecil'], string.ascii_lowercase)
        self.assertEqual(self.result['digit'], string.digits)
        self.assertEqual(self.result['tanda_baca'], string.punctuation)
        self.assertEqual(self.result['besar_kecil'], string.ascii_uppercase + string.ascii_lowercase)
        self.assertEqual(self.result['besar_digit_tanda_baca'], string.ascii_uppercase + string.digits + string.punctuation)
        self.assertEqual(self.result['kecil_digit'], string.ascii_lowercase + string.digits)

if __name__ == '__main__':
    unittest.main()
