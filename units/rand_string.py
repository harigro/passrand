import secrets
import string
from typing import Literal

# menghilangkan argumen punctuation, menghapus opsi ascii, menambahkan modul typing untuk mempermudah
pilihan = Literal["besar", "kecil", "besar_kecil", "alpanumerik", "digit", "tanda_baca", "campuran"]

def RandString(tipe_string: pilihan, panjang: int) -> str:
    pp = int(panjang)
    if pp <= 0:
        raise ValueError("Invalid length in RandString({}, {})".format(tipe_string, panjang))

    if tipe_string == "besar":
        return ''.join(secrets.choice(string.ascii_uppercase) for _ in range(panjang))

    elif tipe_string == "kecil":
        return ''.join(secrets.choice(string.ascii_lowercase) for _ in range(panjang))

    elif tipe_string == "besar_kecil":
        return ''.join(secrets.choice(string.ascii_letters) for _ in range(panjang))

    elif tipe_string == "digit":
        return ''.join(secrets.choice(string.digits) for _ in range(panjang))
        
    elif tipe_string == "tanda_baca":
        return ''.join(secrets.choice(string.punctuation) for _ in range(panjang))
    
    # kombinasi
    elif tipe_string == "alpanumerik":
        return ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(panjang))

    elif tipe_string == "campuran":
        
        # ambil satu karakter dan simpan
        mixed_chars = [secrets.choice(string.ascii_uppercase),
                       secrets.choice(string.ascii_lowercase),
                       secrets.choice(string.digits),
                       secrets.choice(string.punctuation)]
        # karena sudah ada 4 karakter batasi dengan 4 karakter lainnya
        remaining_length = panjang - 4
        # mengabungkan
        mixed_chars.extend(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(remaining_length))
        # urutkan secara acak
        secrets.SystemRandom().shuffle(mixed_chars)
        return ''.join(mixed_chars)

if __name__=="__main__":
    # Contoh penggunaan:
    print(RandString("campuran", 10))
