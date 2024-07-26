import secrets
import string
import itertools
from typing import Dict


# mengubah kelas enum menjadi kombinasi yang mungkin dan disimpan ke dalam tipe data kamus  
def kombinasi_dict(kategori) -> Dict[str, str]:
    combinations = itertools.chain.from_iterable(
        itertools.combinations(kategori.keys(), r)
        for r in range(1, len(kategori) + 1))
    data_dict = {}
    for combination in combinations:
        combined_string = ''.join(kategori[key] for key in combination)
        key_name = '_'.join(combination)
        data_dict[key_name] = combined_string
    data_dict['campuran'] = "besar_kecil_digit_tanda_baca"
    return data_dict

def RandString(tipe_string: str, panjang: int) -> str:
    data = {
        'besar': string.ascii_uppercase,
        'kecil': string.ascii_lowercase,
        'digit': string.digits,
        'tanda_baca': string.punctuation}
    kombinasi_map = kombinasi_dict(data)
    pp = int(panjang)
    if pp <= 0:
        raise ValueError("Invalid length in RandString({}, {})".format(tipe_string, panjang))  
    
    if tipe_string not in kombinasi_map:
        raise ValueError("Invalid type of string '{}'".format(tipe_string))
    
    # semuanya benar
    if kombinasi_map[tipe_string] == "besar_kecil_digit_tanda_baca":
        # ambil satu karakter dan simpan
        mixed_chars = [secrets.choice(kombinasi_map['besar']),
                       secrets.choice(kombinasi_map['kecil']),
                       secrets.choice(kombinasi_map['digit']),
                       secrets.choice(kombinasi_map['tanda_baca'])]
        # karena sudah ada 4 karakter batasi dengan 4 karakter lainnya
        remaining_length = panjang - 4
        # mengabungkan
        mixed_chars.extend(
            secrets.choice(
                kombinasi_map['kecil'] + 
                kombinasi_map['digit'] + 
                kombinasi_map['tanda_baca']
            ) for _ in range(remaining_length))
        # urutkan secara acak
        secrets.SystemRandom().shuffle(mixed_chars)
        return ''.join(mixed_chars)
    # kombinasi
    else:
        return ''.join(secrets.choice(kombinasi_map[tipe_string]) for _ in range(panjang))