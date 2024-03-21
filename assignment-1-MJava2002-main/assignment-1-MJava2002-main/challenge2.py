str_hex_one = input().strip()
str_hex_two = input().strip()


def convert_hex_to_binary(str_hex):
    hex_to_binary_map = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }
    binary = ""
    for digit in str_hex:
        binary += hex_to_binary_map[digit.upper()]
    return binary


def xor_two_binary(first, second):
    result = ""
    for bit1, bit2 in zip(first, second):
        if bit1 != bit2:
            result += '1'
        else:
            result += '0'
    return result


def convert_binary_to_hex(binary):
    res = []
    for i in range(0, len(binary), 4):
        res.append(hex(int(binary[i:i + 4], 2))[2:])
    return ''.join(res)


def xor_function():
    binary_first = convert_hex_to_binary(str_hex_one)
    binary_second = convert_hex_to_binary(str_hex_two)
    binary_xor = xor_two_binary(binary_first, binary_second)
    return convert_binary_to_hex(binary_xor)


print(xor_function())
