import math

from oracle import *
from helper import *


def build_M(byte_m):
    res = []
    for i in range(2):
        res.append(0x00)
        res.append(byte_m)
    return res


def find_divisor(m):
    for i in range(m):
        if i == 0 or i == 1:
            continue
        if m % i == 0:
            return i
    return 1


def get_signature(m, n):
    k = find_divisor(m)
    # M = 0x00 m 0x00 m = 0x00 1 0x00 1 * m = 0x00 1 0x00 1 * (a * b)
    b = int(m // k)
    # print(m / k)
    # print(b)
    sign_m = (Sign(k) * Sign(b)) % n
    inv_one = pow(Sign(1), -1, n)

    res = (inv_one * sign_m) % n
    return res


def main():
    with open('project_3_2/input.txt', 'r') as f:
        n = int(f.readline().strip())
        msg = f.readline().strip()
    # n = int(input().strip())
    # msg = input().strip()
    Oracle_Connect()

    m = ascii_to_int(msg)
    sigma = get_signature(m, n)

    print(sigma)

    Oracle_Disconnect()


if __name__ == '__main__':
    main()
