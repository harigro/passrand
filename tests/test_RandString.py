import unittest
import string
from units.rand_string import RandString

class TestRandString(unittest.TestCase):

    def test_uppercase(self):
        result = RandString("besar", 10)
        self.assertEqual(len(result), 10)
        self.assertTrue(all(c in string.ascii_uppercase for c in result))

    def test_lowercase(self):
        result = RandString("kecil", 8)
        self.assertEqual(len(result), 8)
        self.assertTrue(all(c in string.ascii_lowercase for c in result))

    def test_digits(self):
        result = RandString("digit", 12)
        self.assertEqual(len(result), 12)
        self.assertTrue(all(c in string.digits for c in result))

    def test_punctuation(self):
        result = RandString("tanda_baca", 6)
        self.assertEqual(len(result), 6)
        self.assertTrue(all(c in string.punctuation for c in result))

    def test_upper_lower(self):
        result = RandString("besar_kecil", 15)
        self.assertEqual(len(result), 15)
        self.assertTrue(all(c in string.ascii_letters for c in result))

    def test_upper_digits(self):
        result = RandString("besar_digit", 14)
        self.assertEqual(len(result), 14)
        self.assertTrue(all(c in string.ascii_uppercase + string.digits for c in result))

    def test_upper_punctuation(self):
        result = RandString("besar_tanda_baca", 10)
        self.assertEqual(len(result), 10)
        self.assertTrue(all(c in string.ascii_uppercase + string.punctuation for c in result))

    def test_lower_digits(self):
        result = RandString("kecil_digit", 9)
        self.assertEqual(len(result), 9)
        self.assertTrue(all(c in string.ascii_lowercase + string.digits for c in result))

    def test_lower_punctuation(self):
        result = RandString("kecil_tanda_baca", 11)
        self.assertEqual(len(result), 11)
        self.assertTrue(all(c in string.ascii_lowercase + string.punctuation for c in result))

    def test_digits_punctuation(self):
        result = RandString("digit_tanda_baca", 13)
        self.assertEqual(len(result), 13)
        self.assertTrue(all(c in string.digits + string.punctuation for c in result))

    def test_upper_lower_digits(self):
        result = RandString("besar_kecil_digit", 16)
        self.assertEqual(len(result), 16)
        self.assertTrue(all(c in string.ascii_letters + string.digits for c in result))

    def test_upper_lower_punctuation(self):
        result = RandString("besar_kecil_tanda_baca", 20)
        self.assertEqual(len(result), 20)
        self.assertTrue(all(c in string.ascii_letters + string.punctuation for c in result))

    def test_upper_digits_punctuation(self):
        result = RandString("besar_digit_tanda_baca", 18)
        self.assertEqual(len(result), 18)
        self.assertTrue(all(c in string.ascii_uppercase + string.digits + string.punctuation for c in result))

    def test_lower_digits_punctuation(self):
        result = RandString("kecil_digit_tanda_baca", 17)
        self.assertEqual(len(result), 17)
        self.assertTrue(all(c in string.ascii_lowercase + string.digits + string.punctuation for c in result))

    def test_mixed(self):
        result = RandString("campuran", 25)
        self.assertEqual(len(result), 25)
        self.assertTrue(any(c in string.ascii_uppercase for c in result))
        self.assertTrue(any(c in string.ascii_lowercase for c in result))
        self.assertTrue(any(c in string.digits for c in result))
        self.assertTrue(any(c in string.punctuation for c in result))

    def test_invalid_type(self):
        with self.assertRaises(ValueError):
            RandString("invalid_type", 10)

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            RandString("besar", 0)

if __name__ == '__main__':
    unittest.main()

