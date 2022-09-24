import re
import sys
from collections import deque

input = sys.stdin.readline


def is_prime_number(number, k):
    # number = int(number, base=k)
    print(number, k,  number)
    number = int(number)
    if number < 2:
        return False

    ########
    if number == 2:
        return True

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    else:
        return True


if __name__ == '__main__':
    n, k = map(int, input().split())


    converted_n = ''
    while n != 0:
        div, mod = divmod(n, k)
        n = div
        converted_n += str(mod)

    converted_n = converted_n[::-1]
    print(converted_n)
    # 211020101011
    pattern_1 = r'0([1-9]+)0'
    # print(re.findall(pattern_1, converted_n, ))

    patter_2 = r'(^[1-9]+)0'
    # print(re.findall(patter_2, converted_n, ))

    pattern_3 = r'0([1-9]+$)'
    # print(re.findall(pattern_3, converted_n, ))

    patter_4 = r'(^[1-9]+$)'
    # print(re.findall(patter_4, converted_n, ))

    result = []
    for pattern in [pattern_1, patter_2, pattern_3, patter_4]:
        candidates = re.findall(pattern, converted_n)
        # print(candidates)
        for candi in candidates:
            # print(candi)
            if is_prime_number(candi, k):
                result.append(candi)

    # print(result)
    print(len(result))
