str_hex = input().strip()


def xor_two_str(txt, key):
    res = []
    byte_data = bytes.fromhex(txt)
    for ch in byte_data:
        res.append(ch ^ key)
    # print(res)
    ans = bytes(res)
    # print(ans)

    return ans

def calculate_max_score(text):
    frequency = 'etaoin shrdlu'
    bytes_freq = bytes(ord(char) for char in frequency)
    score = 0
    for ch in text:
        if ch in bytes_freq:
            score += 1
    return score

def decode():
    max_score = 0
    result = []
    for i in range(255):
        text = xor_two_str(str_hex, i)
        curr_score = calculate_max_score(text.lower())
        if curr_score > max_score:
            max_score = curr_score
            result = text
    return result.decode('utf-8', errors='ignore').rstrip()

print(decode())
