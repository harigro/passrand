import unittest
from units.kombinasi import kombinasi_kamus

class TestKombinasiKamus(unittest.TestCase):

    def test_kombinasi_kamus(self):
        # Kasus uji 1: Input kamus kosong
        kategori = {}
        expected_output = {}
        self.assertEqual(kombinasi_kamus(kategori), expected_output)

        # Kasus uji 2: Input dengan satu kunci
        kategori = {'A': 'nilai_A'}
        expected_output = {'A': 'nilai_A'}
        self.assertEqual(kombinasi_kamus(kategori), expected_output)

        # Kasus uji 3: Input dengan beberapa kunci
        kategori = {
            'A': 'nilai_A',
            'B': 'nilai_B',
            'C': 'nilai_C'
        }
        expected_output = {
            'A': 'nilai_A',
            'B': 'nilai_B',
            'C': 'nilai_C',
            'A_B': 'nilai_Anilai_B',
            'A_C': 'nilai_Anilai_C',
            'B_C': 'nilai_Bnilai_C',
            'A_B_C': 'nilai_Anilai_Bnilai_C'
        }
        self.assertEqual(kombinasi_kamus(kategori), expected_output)

        # Kasus uji 4: Input dengan lebih banyak kunci
        kategori = {
            'X': 'nilai_X',
            'Y': 'nilai_Y',
            'Z': 'nilai_Z'
        }
        expected_output = {
            'X': 'nilai_X',
            'Y': 'nilai_Y',
            'Z': 'nilai_Z',
            'X_Y': 'nilai_Xnilai_Y',
            'X_Z': 'nilai_Xnilai_Z',
            'Y_Z': 'nilai_Ynilai_Z',
            'X_Y_Z': 'nilai_Xnilai_Ynilai_Z'
        }
        self.assertEqual(kombinasi_kamus(kategori), expected_output)

if __name__ == '__main__':
    unittest.main()
