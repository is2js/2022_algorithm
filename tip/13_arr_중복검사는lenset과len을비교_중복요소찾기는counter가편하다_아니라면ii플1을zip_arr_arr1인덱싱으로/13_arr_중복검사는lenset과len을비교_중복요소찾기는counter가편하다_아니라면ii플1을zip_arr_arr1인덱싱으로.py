import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ##
    a = 'abcde'  # 중복x
    b = 'aabbc'  # 2+2로 중복
    c = 'aaabc'  # 3+1로 중복

    # (1) 중복값의 존재 확인 len(set())과 len을 비교
    for arr in [a, b, c]:
        if len(set(arr)) == len(arr):
            print('중복값이 없습니다.')
        else:
            print('중복값이 존재합니다.')

    # (2) 중복 상태는 sorted + i와i+1로 비교한다.
    # aabbc -> {'a': 1, 'b': 1}
    from collections import defaultdict
    count_of_kinds = defaultdict(int)
    for i, j in zip(b, b[1:]):
        if i == j:
            count_of_kinds[i] += 1
    print(count_of_kinds)
    from collections import Counter
    print(Counter(b)) # Counter({'a': 2, 'b': 2, 'c': 1})


    count_of_kinds = defaultdict(int)
    # aaabc ->  {'a': 2}
    for i, j in zip(c, c[1:]):
        if i == j:
            count_of_kinds[i] += 1
    print(count_of_kinds)
    print(Counter(c))
    # Counter({'a': 3, 'b': 1, 'c': 1})
    print([(i, count) for i, count in Counter(c).items() if count >= 2])
    # [('a', 3)]



