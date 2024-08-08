import unittest
from units.kombinasi import kombinasi_kamus_elemen_bool

class TestKombinasiKamusElemenBool(unittest.TestCase):

    def test_kombinasi_kamus_elemen_bool(self):
        # Kasus uji 1: Input kamus kosong
        kategori = {}
        expected_output = {}
        self.assertEqual(kombinasi_kamus_elemen_bool(kategori), expected_output)

        # Kasus uji 2: Input dengan beberapa kunci
        kategori = {
            'A': 'nilai_A',
            'B': 'nilai_B',
            'C': 'nilai_C'
        }
        expected_output = {
            'A': [True, False, False],
            'B': [False, True, False],
            'C': [False, False, True],
            'A_B': [True, True, False],
            'A_C': [True, False, True],
            'B_C': [False, True, True],
            'A_B_C': [True, True, True]
        }
        self.assertEqual(kombinasi_kamus_elemen_bool(kategori), expected_output)

        # Kasus uji 3: Input dengan lebih banyak kunci
        kategori = {
            'X': 'nilai_X',
            'Y': 'nilai_Y',
            'Z': 'nilai_Z',
            'W': 'nilai_W'
        }
        expected_output = {
            'X': [True, False, False, False],
            'Y': [False, True, False, False],
            'Z': [False, False, True, False],
            'W': [False, False, False, True],
            'X_Y': [True, True, False, False],
            'X_Z': [True, False, True, False],
            'X_W': [True, False, False, True],
            'Y_Z': [False, True, True, False],
            'Y_W': [False, True, False, True],
            'Z_W': [False, False, True, True],
            'X_Y_Z': [True, True, True, False],
            'X_Y_W': [True, True, False, True],
            'X_Z_W': [True, False, True, True],
            'Y_Z_W': [False, True, True, True],
            'X_Y_Z_W': [True, True, True, True]
        }
        self.assertEqual(kombinasi_kamus_elemen_bool(kategori), expected_output)

if __name__ == '__main__':
    unittest.main()
