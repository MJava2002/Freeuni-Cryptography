# add your imports here

# reading input (don't forget strip in other challenges!)
str_hex = input().strip()

def convert_hex_to_binary():
    hex_to_binary_map = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }
    binary = ""
    for digit in str_hex:
        binary += hex_to_binary_map[digit.upper()]

    if (6 - len(binary) % 6) % 6 > 0:
        pad_size = (6 - len(binary) % 6) % 6
        binary += '0' * pad_size
    return binary

def converter():
    hex_characters = "0123456789abcdef"
    base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    # print(len(str_hex))
    binary = convert_hex_to_binary()
    str_base64 = ""
    for i in range(0, len(binary), 6):
        str_base64 += base64[int(binary[i:i + 6], 2)]
    if len(str_hex) % 3 == 2:
        str_base64 += '=='
    elif len(str_hex) % 3 == 1:
        str_base64 += '='
    return str_base64


print(converter())
