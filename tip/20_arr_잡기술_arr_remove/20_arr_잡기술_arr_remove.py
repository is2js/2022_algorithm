import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## 잡기술
    # (1) 1en은 10의 n승이다.
    print(1e6)  # 1000000.0

    # (2) 소수점 계산은 [2진수 순환소수]로서 메모리에서 cut당한다. 만약해야한다면, 소수4자리로 반올림해주면된다.
    print(0.3 + 0.6)  # 0.899999999999999
    print(round(0.3 + 0.6, 4))  # 0.9

    # (3) listcomp는 필터링append뿐만 아니라 요소 데이터 변형(list,map)에도 사용하자
    print([pow(x, 2) for x in range(1, 10)])
    print(list(map(lambda x: pow(x, 2), range(1, 10))))
    # [1, 4, 9, 16, 25, 36, 49, 64, 81]

    # (4) list의 index, reverse뿐만 아니라 .insert, .count, .remove가 있는데
    # -> insert와 remove는 배열을 변화시킨다.
    print([1, 2, 3, 4, 5, 5].count(5))  # 2


    # (5) remove는 insert와 같이 inplace다
    # -> 1개 삭제는 .remove()를 이용한다
    l = [1, 2, 3, 4, 5, 5]
    print(l.remove(3))  # None
    print(l)  # [1, 2, 4, 5, 5]

    # -> 여러개 삭제는 삭제set를 돌리면서 [원소가 삭제set에 포함되지 않는 것들만 필터링]한다
    remove_set = {1, 2}
    lst = [1, 2, 3, 4, 5, 5, 6, 7, 7]
    result = []
    for x in lst:
        if x not in remove_set:
            result.append(x)
    print(result)
    # [3, 4, 5, 5, 6, 7, 7]

    # list comp
    # (7) set에 여러개 add는 .update(iter)를 쓴다.
    remove_set.update({3, 4})
    print([x for x in lst if x not in remove_set])
    # [5, 5, 6, 7, 7]


    pass
