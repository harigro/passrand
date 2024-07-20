import unittest
from typing import List
from units.kombinasi import kombinasi_satu, kombinasi_dua, kombinasi_tiga

class TestKombinasiFunctions(unittest.TestCase):

    def test_kombinasi_satu(self):
        # Test cases for kombinasi_satu
        cases = [
            ([True, False, False, False], True, 1, True),
            ([False, True, False, False], True, 2, True),
            ([False, False, True, False], True, 3, True),
            ([False, False, False, True], True, 4, True),
            ([True, False, False, False], False, 2, None),  # Invalid case
        ]
        
        for dd, hasil, bagian, expected in cases:
            with self.subTest(dd=dd, hasil=hasil, bagian=bagian):
                result = kombinasi_satu(dd, hasil, bagian)
                self.assertEqual(result, expected)

    def test_kombinasi_dua(self):
        # Test cases for kombinasi_dua
        cases = [
            ([True, True, False, False], True, 1, True),
            ([True, False, True, False], True, 2, True),
            ([True, False, False, True], True, 3, True),
            ([False, True, True, False], True, 4, True),
            ([False, True, False, True], True, 5, True),
            ([False, False, True, True], True, 6, True),
            ([True, True, False, False], False, 2, None),  # Invalid case
        ]
        
        for dd, hasil, bagian, expected in cases:
            with self.subTest(dd=dd, hasil=hasil, bagian=bagian):
                result = kombinasi_dua(dd, hasil, bagian)
                self.assertEqual(result, expected)

    def test_kombinasi_tiga(self):
        # Test cases for kombinasi_tiga
        cases = [
            ([True, True, True, False], True, 1, True),
            ([True, True, False, True], True, 2, True),
            ([True, False, True, True], True, 3, True),
            ([False, True, True, True], True, 4, True),
            ([True, True, True, False], False, 2, None),  # Invalid case
        ]
        
        for dd, hasil, bagian, expected in cases:
            with self.subTest(dd=dd, hasil=hasil, bagian=bagian):
                result = kombinasi_tiga(dd, hasil, bagian)
                self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

