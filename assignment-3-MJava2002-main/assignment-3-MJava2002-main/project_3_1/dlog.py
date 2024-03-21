import math


# Find x such that g^x = h (mod p)
# 0 <= x <= max_x
def get_hash_table(g, p, h, B):
    res = [h]
    power_table = {}
    g_inv = pow(g, -1, p)
    for i in range(B):
        power_table[res[-1]] = i
        res.append((res[-1] * g_inv) % p)
    return power_table


def calculate_x(a, b, B):
    return a * B + b


def wrapper(max_x, g, h, p):
    B = int(math.sqrt(max_x))
    power_table = get_hash_table(g, p, h, B)
    base = pow(g, B, p)
    prev = 1
    for i in range(B):
        if prev in power_table:
            # print(prev)
            return calculate_x(i, power_table[prev], B)
        prev = (base * prev) % p
    return 0


def discrete_log(p, g, h, max_x):
    return wrapper(max_x, g, h, p)


def main():
    p = int(input().strip())
    g = int(input().strip())
    h = int(input().strip())
    max_x = 1 << 40  # 2^40

    dlog = discrete_log(p, g, h, max_x)
    print(dlog)


if __name__ == '__main__':
    main()
