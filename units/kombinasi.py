import itertools
import string
import secrets
from typing import Dict, List

data_huruf = {
        'besar': string.ascii_uppercase,
        'kecil': string.ascii_lowercase,
        'digit': string.digits,
        'tanda_baca': string.punctuation}

def kombinasi_kamus_elemen_bool(kategori: Dict[str, str]) -> Dict[str, List[bool]]:
    """
    Deskripsi:
        - Membentuk kamus baru yang berisi kombinasi 
          nilai-nilai elemen yang sama diisi 
          dengan nilai benar dan tidak sama diisi dengan nilai salah
    """
    data_kamus = {}
    keys = list(kategori.keys())
    combinations = itertools.chain.from_iterable(
        itertools.combinations(keys, r)
        for r in range(1, len(keys) + 1))
    
    for combination in combinations:
        true_values = [True if key in combination else False for key in keys]
        data_kamus['_'.join(combination)] = true_values
    return data_kamus

def kombinasi_kamus(kategori: Dict[str, str]) -> Dict[str, str]:
    """
    Deskripsi:
        - Membentuk kamus baru yang berisi kombinasi yang mungkin berdasarkan panjang data kamus
    """
    combinations = itertools.chain.from_iterable(
        itertools.combinations(kategori.keys(), r)
        for r in range(1, len(kategori) + 1))
    data_kamus = {}
    for combination in combinations:
        combined_string = ''.join(kategori[key] for key in combination)
        key_name = '_'.join(combination)
        data_kamus[key_name] = combined_string
    return data_kamus

def rand_string_grafis(tipe_string: str, panjang: int) -> str:
    """
    Menghasilkan string acak berdasarkan tipe dan panjang yang ditentukan
    """
    kombinasi_map = kombinasi_kamus(data_huruf)
    if kombinasi_map[tipe_string] == "besar_kecil_digit_tanda_baca":
        mixed_chars = [secrets.choice(kombinasi_map['besar']),
                       secrets.choice(kombinasi_map['kecil']),
                       secrets.choice(kombinasi_map['digit']),
                       secrets.choice(kombinasi_map['tanda_baca'])]
        remaining_length = panjang - 4
        mixed_chars.extend(
            secrets.choice(kombinasi_map['kecil'] + kombinasi_map['digit'] + kombinasi_map['tanda_baca']
            ) for _ in range(remaining_length))
        # urutkan secara acak
        secrets.SystemRandom().shuffle(mixed_chars)
        return ''.join(mixed_chars)
    else:
        ulang = True
        data_hasil = ''.join(secrets.choice(kombinasi_map[tipe_string]) for _ in range(panjang))
        data_acuan = kombinasi_map[tipe_string]
        while ulang:
            if all(char in data_acuan for char in data_hasil):
                ulang = False
        return data_hasil
    