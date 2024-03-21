import binascii
import sys

from oracle import Oracle_Connect, Oracle_Disconnect, Oracle_Send
from constants import BSIZE


def get_bytes_array(all_bytes):
    result = []
    for i in range(0, len(all_bytes), BSIZE):
        result.append(all_bytes[i:i + BSIZE])
    return result


def xor_byte(byte, num):
    res = []
    for j in byte:
        res.append(j ^ num)
    return res


def xor_two_bytes(byte_one, byte_second):
    res = []
    min_len = min(len(byte_one), len(byte_second))
    for i in range(min_len):
        res.append(byte_one[i] ^ byte_second[i])
    return res


def convert_to_ascii(byte_input):
    res = ''.join(chr(each) for each in byte_input)
    return res


def convert_to_message_format(data, block):
    result = list(data) + list(block)
    return result


def attack(iv, index, block):
    size = len(iv)
    for cand in range(256):
        iv[size-index] = cand
        tmp_msg_one = convert_to_message_format(iv, block)
        if Oracle_Send(tmp_msg_one, 2):
            if index == 1:
                iv[size-2] = iv[size-2] ^ 1
                tmp_msg_two = convert_to_message_format(iv, block)
                if not Oracle_Send(tmp_msg_two, 2):
                    continue
            return cand
    return None


def decrypt_block(block):
    starting_iv = [0] * BSIZE
    size = len(starting_iv)
    for i in range(1, BSIZE + 1):
        tmp = xor_byte(starting_iv, i)
        cand = attack(tmp, i, block)
        starting_iv[size-i] = cand ^ i
    return starting_iv


def detect_pad(block):
    last_ind = len(block) - 1
    while last_ind >= 0 and block[last_ind] == block[-1]:
        last_ind -= 1
    return last_ind


def decrypt_cypher(byte_blocks, iv_cyp):
    block_num = 1
    size = len(byte_blocks)
    plain_txt = ""
    while block_num != size:
        each_block = byte_blocks[block_num]
        res = decrypt_block(each_block)
        each_block_dec = xor_two_bytes(iv_cyp, res)
        # print("each block binary", each_block_dec)
        if block_num == size - 1:
            indx = detect_pad(each_block_dec)
            indx += 1
            plain_txt += convert_to_ascii(each_block_dec[:indx])
            # print(each_block_dec)
        else:
            plain_txt += convert_to_ascii(each_block_dec)
        iv_cyp = each_block
        block_num += 1
    return plain_txt


def decrypt(cypher_text):
    # print("cypher text", cypher_text)
    bytes_array = get_bytes_array(binascii.unhexlify(cypher_text))
    # print("bytes array", bytes_array)
    iv_cypher = bytes_array[0]
    print(decrypt_cypher(bytes_array, iv_cypher))


file = open(sys.argv[1])
cypher = file.read()
file.close()

Oracle_Connect()
decrypt(cypher)
Oracle_Disconnect()
