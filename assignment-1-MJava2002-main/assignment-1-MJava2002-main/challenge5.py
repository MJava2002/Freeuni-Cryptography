str_key = input().strip()


def xor_two_str(txt, key):
    res = []
    for i in range(len(txt)):
        res.append(txt[i] ^ key[i])
    return bytes(res)


def pad_key(key, length):
    repeated_key = (key * (length // len(key))) + key[:length % len(key)]
    return repeated_key


def challenge():
    str_line = input().strip()
    size = len(str_line)
    new_key = pad_key(str_key, size)
    return xor_two_str(str_line.encode(), new_key.encode()).hex()


print(challenge())
