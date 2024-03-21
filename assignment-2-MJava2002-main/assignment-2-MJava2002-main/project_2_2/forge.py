import binascii
import sys

from oracle import Oracle_Connect, Mac, Oracle_Disconnect

def add_padding(binary):
    pad_size = 128 - len(binary)
    if pad_size > 0:
        binary = '0' * pad_size + binary
    return binary


def xor_two_bytes(byte_one, byte_second):
    res = []
    min_len = min(len(byte_one), len(byte_second))
    for i in range(min_len):
        # print(byte_second[i])
        res.append(byte_one[i] ^ byte_second[i])
    return bytes(res)

def get_bytes_array(all_bytes):
    result = []
    for i in range(0, len(all_bytes), 16):
        result.append(all_bytes[i:i + 16])
    return result

def build_new_message(binary):
    res = ""
    for i in range(0, len(binary), 8):
        str_bl = binary[i:i+8]
        int_bl = chr(int(str_bl, 2))
        res += int_bl
    return res



def concat(first, second):
    new_blocks = ""
    binary_first = add_padding(bin(int(binascii.hexlify(first).decode('utf-8'), 16))[2:])
    binary_second = add_padding(bin(int(binascii.hexlify(second).decode('utf-8'), 16))[2:])
    # needs_pad_one = 128 - len(binary_first)
    # needs_pad_two = 128 - len(binary_second)
    # if needs_pad_one > 0:
    #     binary_first = '0'*needs_pad_one + binary_first
    # if needs_pad_two > 0:
    #     binary_second = '0'*needs_pad_two + binary_second
    # print(binary_first)
    # print(binary_second)
    new_blocks = build_new_message(binary_first) + build_new_message(binary_second)
    # for i in range(0, len(binary_first), 8):
    #     str_bl = binary_first[i:i+8]
    #     # print(len(str_bl))
    #     int_bl = chr(int(str_bl, 2))
    #     # print(int_bl)
    #     new_blocks += int_bl
    # for i in range(0, len(binary_second), 8):
    #     str_bl = binary_second[i:i + 8]
    #     int_bl = chr(int(str_bl, 2))
    #     new_blocks += int_bl

    # print(new_blocks)
    return new_blocks

def attack_cbc_mac(message):
    # print("message is", message)
    new_message = get_bytes_array(message.encode('utf-8'))
    # print("new message is", new_message)
    iv = bytes(bytearray([0]*16))
    # print("iv is ", iv)
    for i in range(0, len(new_message), 2):
        first_block = new_message[i]
        second_block = new_message[i+1]
        new_first_block = xor_two_bytes(first_block, iv)
        new_mac_msg = concat(new_first_block, second_block)
        tag_res = Mac(new_mac_msg, len(new_mac_msg))
        iv = tag_res
    return iv


f = open(sys.argv[1])
data = f.read()
f.close()

Oracle_Connect()

tag = attack_cbc_mac(data)
# print(tag)
# ret = Vrfy(data, len(data), tag)

# if ret == 1:
#     print("Message verified successfully!")
# else:
#     print("Message verification failed.")

print(tag.hex())

Oracle_Disconnect()
