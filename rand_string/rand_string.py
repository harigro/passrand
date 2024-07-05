import random
import string

def RandString(string_type: str, length: int, punctuation=False):
    length = int(length)
    if length <= 0:
        raise ValueError("Invalid length in RandString({}, {})".format(string_type, length))

    if string_type == "uppercase":
        return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))

    elif string_type == "lowercase":
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

    elif string_type == "upperlower":
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))

    elif string_type == "alphanumerical":
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    
    elif string_type == "digits":
        return ''.join(random.choice(string.digits) for _ in range(length))
        
    elif string_type == "ascii":
        return ''.join(random.choice(string.printable) for _ in range(length))

    elif string_type == "mixed":
        # Fill the rest of the characters randomly
        remaining_length = length - 4  # we already have 4 characters

        # Ensure at least one uppercase, one lowercase, one digit, and one symbol
        mixed_chars = []
        mixed_chars.append(random.choice(string.ascii_uppercase))  # at least one uppercase
        mixed_chars.append(random.choice(string.ascii_lowercase))  # at least one lowercase
        mixed_chars.append(random.choice(string.digits))          # at least one digit
        if punctuation is not False:
            mixed_chars.append(random.choice(string.punctuation))     # at least one symbol
            mixed_chars.extend(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(remaining_length))
        else:
            mixed_chars.extend(random.choice(string.ascii_letters + string.digits) for _ in range(remaining_length))

        # Shuffle the characters to randomize their order
        random.shuffle(mixed_chars)

        return ''.join(mixed_chars)

    else:
        raise ValueError("Invalid type in RandString({}, {})".format(string_type, length))

if __name__=="__main__":
    # Contoh penggunaan:
    print(RandString("uppercase", 10))
    print(RandString("lowercase", 10))
    print(RandString("upperlower", 10))
    print(RandString("alphanumerical", 10))
    print(RandString("ascii", 10))
    print(5, RandString("mixed", 10))
    print(6, RandString("mixed", 10, True))
