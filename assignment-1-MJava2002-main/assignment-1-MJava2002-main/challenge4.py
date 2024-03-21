from typing import Tuple

str_len = input().strip()


def xor_two_str(txt, key):
    res = []
    byte_data = bytes.fromhex(txt)
    for ch in byte_data:
        res.append(ch ^ key)
    ans = bytes(res)
    return ans


def calculate_max_score(text):
    frequency = 'etaoin shrdlu'
    bytes_freq = bytes(ord(char) for char in frequency)
    score = 0
    for ch in text:
        if ch in bytes_freq:
            score += 1
    return score


def decode(str_hex):
    max_score = 0
    result = []
    for i in range(255):
        text = xor_two_str(str_hex, i)
        curr_score = calculate_max_score(text.lower())
        if curr_score > max_score:
            max_score = curr_score
            result = text
    return result.decode('utf-8', errors='ignore').rstrip(), max_score


def challenge():
    score_text_dict = {}
    for i in range(int(str_len)):
        str_hex_line = input().strip()
        decoded, score = decode(str_hex_line)
        score_text_dict[decoded] = score
    max_string = max(score_text_dict, key=score_text_dict.get)
    return max_string


print(challenge())
