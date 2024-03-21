from base64 import b64decode



def xor_two_str(byte_data, key):
    res = []
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


def decode_new(byte_data):
    max_score = 0
    result = []
    max_key = None
    for i in range(255):
        text = xor_two_str(byte_data, i)
        curr_score = calculate_max_score(text)
        if curr_score > max_score:
            max_score = curr_score
            result = text
            max_key = i
    return result, bytes(max_key)


def convert_bytes_to_binary(first_byte, second_byte):
    result_fir = ""
    result_sec = ""
    for i, j in zip(first_byte, second_byte):
        for k in range(7, -1, -1):
            first_b = (i >> k) & 1
            second_b = (j >> k) & 1
            # print(first_b, second_b)
            result_fir += str(first_b)
            result_sec += str(second_b)
    return result_fir, result_sec


def edit_distance(first_byte, second_byte):
    res = 0
    f, s = convert_bytes_to_binary(first_byte, second_byte)
    # print(f)
    # print(s)
    # print(f, s)
    for i in range(len(f)):
        if f[i] != s[i]:
            res += 1
    return res


def normalize_edit_distance(distance, KEYSIZE):
    return distance / KEYSIZE


def calculate_average(distance_count, block_count):
    return distance_count / block_count


def wrapper_find_key_size(text, KEYSIZE):
    block = None
    block_count = 0
    distance_count = 0
    # print(text)
    for index in range(0, len(text), KEYSIZE):
        new_block = text[index:index + KEYSIZE]
        # print("---------------------", KEYSIZE)
        # print(new_block, block)
        if block:
            dist = edit_distance(new_block, block)
            normalized = normalize_edit_distance(dist, KEYSIZE)
            distance_count += normalized
            block_count += 1
        # print("dist", distance_count)
        block = new_block
        # print("........................")
        # print(block)
    avg = calculate_average(distance_count, block_count)
    return avg


#
def find_key(text):
    minimum_distance = None
    min_KEYSIZE = None
    for KEYSIZE in range(2, 40):
        curr_average = wrapper_find_key_size(text, KEYSIZE)
        # print(curr_average)
        if minimum_distance is None:
            minimum_distance = curr_average
            min_KEYSIZE = KEYSIZE
        else:
            if curr_average < minimum_distance:
                minimum_distance = curr_average
                min_KEYSIZE = KEYSIZE
    return min_KEYSIZE


def divide_in_blocks(text, KEYSIZE):
    key = bytes()
    blocks = list()
    for index in range(KEYSIZE):
        new_block = text[index::KEYSIZE]
        dec, k = decode_new(new_block)
        key += k
        blocks.append(dec)
    ans = bytes()
    max_len = max(map(len, blocks))
    for i in range(max_len):
        tmp = [block for block in blocks if len(block) >= i + 1]
        ans += bytes(block[i] for block in tmp)
    return ans.decode()


def encrypt():
    str_line = input().strip()
    decoded_text = b64decode(str_line)
    key_size = find_key(decoded_text)
    return divide_in_blocks(b64decode(str_line), key_size)


print(encrypt())
