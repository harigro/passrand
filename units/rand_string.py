import secrets
import enum
import string

class KombiString(enum.Enum):
    UPPERCASE = string.ascii_uppercase
    LOWERCASE = string.ascii_lowercase
    DIGITS = string.digits
    PUNCTUATION = string.punctuation
    UPPER_LOWER = string.ascii_letters
    UPPER_DIGITS = string.ascii_uppercase + string.digits
    UPPER_PUNCTUATION = string.ascii_uppercase + string.punctuation
    LOWER_DIGITS = string.ascii_lowercase + string.digits
    LOWER_PUNCTUATION = string.ascii_lowercase + string.punctuation
    DIGITS_PUNCTUATION = string.digits + string.punctuation
    UPPER_LOWER_DIGITS = string.ascii_uppercase + string.ascii_lowercase + string.digits
    UPPER_LOWER_PUNCTUATION = string.ascii_uppercase + string.ascii_lowercase + string.punctuation
    UPPER_DIGITS_PUNCTUATION = string.ascii_uppercase + string.digits + string.punctuation
    LOWER_DIGITS_PUNCTUATION = string.ascii_lowercase + string.digits + string.punctuation

def ambil_kombinasi(kombinasi: KombiString) -> str:
    return kombinasi.value

def RandString(tipe_string: str, panjang: int) -> str:
    pp = int(panjang)
    if pp <= 0:
        raise ValueError("Invalid length in RandString({}, {})".format(tipe_string, panjang))
    
    kombinasi_map = {
        "besar": KombiString.UPPERCASE,
        "kecil": KombiString.LOWERCASE,
        "digit": KombiString.DIGITS,
        "tanda_baca": KombiString.PUNCTUATION,
        "besar_kecil": KombiString.UPPER_LOWER,
        "besar_digit": KombiString.UPPER_DIGITS,
        "besar_tanda_baca": KombiString.UPPER_PUNCTUATION,
        "kecil_digit": KombiString.LOWER_DIGITS,
        "kecil_tanda_baca": KombiString.LOWER_PUNCTUATION,
        "digit_tanda_baca": KombiString.DIGITS_PUNCTUATION,
        "besar_kecil_digit": KombiString.UPPER_LOWER_DIGITS,
        "besar_kecil_tanda_baca": KombiString.UPPER_LOWER_PUNCTUATION,
        "besar_digit_tanda_baca": KombiString.UPPER_DIGITS_PUNCTUATION,
        "kecil_digit_tanda_baca": KombiString.LOWER_DIGITS_PUNCTUATION,
        "campuran" : "besar_kecil_digit_tanda_baca"
    }
    
    if tipe_string not in kombinasi_map:
        raise ValueError("Invalid type of string '{}'".format(tipe_string))
    
    chosen_enum = kombinasi_map[tipe_string]
    # semuanya benar
    if chosen_enum == "besar_kecil_digit_tanda_baca":
        # ambil satu karakter dan simpan
        mixed_chars = [secrets.choice(ambil_kombinasi(KombiString.UPPERCASE)),
                       secrets.choice(ambil_kombinasi(KombiString.LOWERCASE)),
                       secrets.choice(ambil_kombinasi(KombiString.DIGITS)),
                       secrets.choice(ambil_kombinasi(KombiString.PUNCTUATION))]
        # karena sudah ada 4 karakter batasi dengan 4 karakter lainnya
        remaining_length = panjang - 4
        # mengabungkan
        mixed_chars.extend(
            secrets.choice(
                ambil_kombinasi(KombiString.UPPER_LOWER) + 
                ambil_kombinasi(KombiString.DIGITS) + 
                ambil_kombinasi(KombiString.PUNCTUATION)
            ) for _ in range(remaining_length))
        # urutkan secara acak
        secrets.SystemRandom().shuffle(mixed_chars)
        return ''.join(mixed_chars)
    # kombinasi
    else:
        return ''.join(secrets.choice(ambil_kombinasi(chosen_enum)) for _ in range(panjang))
