import unittest
import string
from units.rand_string import KombiString, ambil_kombinasi

class TestKombiStringEnum(unittest.TestCase):
    
    def test_uppercase(self):
        self.assertEqual(KombiString.UPPERCASE.value, string.ascii_uppercase)
    
    def test_lowercase(self):
        self.assertEqual(KombiString.LOWERCASE.value, string.ascii_lowercase)
    
    def test_digits(self):
        self.assertEqual(KombiString.DIGITS.value, string.digits)
    
    def test_punctuation(self):
        self.assertEqual(KombiString.PUNCTUATION.value, string.punctuation)
    
    def test_upper_lower(self):
        expected = string.ascii_lowercase + string.ascii_uppercase
        self.assertEqual(KombiString.UPPER_LOWER.value, expected)
    
    def test_upper_digits(self):
        expected = string.ascii_uppercase + string.digits
        self.assertEqual(KombiString.UPPER_DIGITS.value, expected)
    
    def test_upper_punctuation(self):
        expected = string.ascii_uppercase + string.punctuation
        self.assertEqual(KombiString.UPPER_PUNCTUATION.value, expected)
    
    def test_lower_digits(self):
        expected = string.ascii_lowercase + string.digits
        self.assertEqual(KombiString.LOWER_DIGITS.value, expected)
    
    def test_lower_punctuation(self):
        expected = string.ascii_lowercase + string.punctuation
        self.assertEqual(KombiString.LOWER_PUNCTUATION.value, expected)
    
    def test_digits_punctuation(self):
        expected = string.digits + string.punctuation
        self.assertEqual(KombiString.DIGITS_PUNCTUATION.value, expected)
    
    def test_upper_lower_digits(self):
        expected = string.ascii_uppercase + string.ascii_lowercase + string.digits
        self.assertEqual(KombiString.UPPER_LOWER_DIGITS.value, expected)
    
    def test_upper_lower_punctuation(self):
        expected = string.ascii_uppercase + string.ascii_lowercase + string.punctuation
        self.assertEqual(KombiString.UPPER_LOWER_PUNCTUATION.value, expected)
    
    def test_upper_digits_punctuation(self):
        expected = string.ascii_uppercase + string.digits + string.punctuation
        self.assertEqual(KombiString.UPPER_DIGITS_PUNCTUATION.value, expected)
    
    def test_lower_digits_punctuation(self):
        expected = string.ascii_lowercase + string.digits + string.punctuation
        self.assertEqual(KombiString.LOWER_DIGITS_PUNCTUATION.value, expected)
        
class TestAmbilKombinasi(unittest.TestCase):
    
    def test_uppercase(self):
        self.assertEqual(ambil_kombinasi(KombiString.UPPERCASE), string.ascii_uppercase)
        
    def test_lowercase(self):
        self.assertEqual(ambil_kombinasi(KombiString.LOWERCASE), string.ascii_lowercase)
        
    def test_digits(self):
        self.assertEqual(ambil_kombinasi(KombiString.DIGITS), string.digits)
        
    def test_punctuation(self):
        self.assertEqual(ambil_kombinasi(KombiString.PUNCTUATION), string.punctuation)
        
    def test_upper_lower(self):
        self.assertEqual(ambil_kombinasi(KombiString.UPPER_LOWER), string.ascii_letters)
        
    def test_upper_digits(self):
        self.assertEqual(ambil_kombinasi(KombiString.UPPER_DIGITS), string.ascii_uppercase + string.digits)
        
    def test_upper_punctuation(self):
        self.assertEqual(ambil_kombinasi(KombiString.UPPER_PUNCTUATION), string.ascii_uppercase + string.punctuation)
        
    def test_lower_digits(self):
        self.assertEqual(ambil_kombinasi(KombiString.LOWER_DIGITS), string.ascii_lowercase + string.digits)
        
    def test_lower_punctuation(self):
        self.assertEqual(ambil_kombinasi(KombiString.LOWER_PUNCTUATION), string.ascii_lowercase + string.punctuation)
        
    def test_digits_punctuation(self):
        self.assertEqual(ambil_kombinasi(KombiString.DIGITS_PUNCTUATION), string.digits + string.punctuation)
        
    def test_upper_lower_digits(self):
        self.assertEqual(ambil_kombinasi(KombiString.UPPER_LOWER_DIGITS), string.ascii_uppercase + string.ascii_lowercase + string.digits)
        
    def test_upper_lower_punctuation(self):
        self.assertEqual(ambil_kombinasi(KombiString.UPPER_LOWER_PUNCTUATION), string.ascii_uppercase + string.ascii_lowercase + string.punctuation)
        
    def test_upper_digits_punctuation(self):
        self.assertEqual(ambil_kombinasi(KombiString.UPPER_DIGITS_PUNCTUATION), string.ascii_uppercase + string.digits + string.punctuation)
        
    def test_lower_digits_punctuation(self):
        self.assertEqual(ambil_kombinasi(KombiString.LOWER_DIGITS_PUNCTUATION), string.ascii_lowercase + string.digits + string.punctuation)
        

if __name__ == '__main__':
    unittest.main()
