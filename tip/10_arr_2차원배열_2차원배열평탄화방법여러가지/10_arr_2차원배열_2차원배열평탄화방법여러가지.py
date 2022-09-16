import itertools
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    lst_2d = [list(map(int, input().split())) for _ in range(5)]
    # for row in lst_2d:
    #     print(*row)

    # 1. [이중반복문]으로 [개별요소까지 접근한 뒤, 빈list에 append]
    lst_1d = []
    for row in lst_2d:
        for e in row:
            lst_1d.append(e)
    print(lst_1d)
    # [5, 10, 7, 16, 2, 4, 22, 8, 17, 13, 3, 18, 1, 6, 25, 12, 19, 23, 14, 21, 11, 24, 9, 20, 15]

    # 2. 1개 반복문으로 [row별 빈 list에 extend]
    lst_1d = []
    for row in lst_2d:
        lst_1d.extend(row)
    print(lst_1d)

    # 3. 1개 반복문으로 [row별 빈 list에 배열 누적합 += ]
    lst_1d = []
    for row in lst_2d:
        lst_1d += row
    print(lst_1d)

    # 4. chain(*lst_2d)로 [*언패킹row + chain]
    # => chain은 2차원배열을 언패킹하여 쓴다.
    #    그렇지 않으면 1차원배열 여러개를 인자로 준다.
    print(list(itertools.chain(*lst_2d)))
    # [5, 10, 7, 16, 2, 4, 22, 8, 17, 13, 3, 18, 1, 6, 25, 12, 19, 23, 14, 21, 11, 24, 9, 20, 15]

    # 5. chain.from_iterable(lst_2d)
    print(list(itertools.chain.from_iterable(lst_2d)))
    # [5, 10, 7, 16, 2, 4, 22, 8, 17, 13, 3, 18, 1, 6, 25, 12, 19, 23, 14, 21, 11, 24, 9, 20, 15]


    # 6. reduce + add로 개별 row들 extend
    from functools import reduce
    from operator import add

    print(list(reduce(add, lst_2d)))
    # [5, 10, 7, 16, 2, 4, 22, 8, 17, 13, 3, 18, 1, 6, 25, 12, 19, 23, 14, 21, 11, 24, 9, 20, 15]









