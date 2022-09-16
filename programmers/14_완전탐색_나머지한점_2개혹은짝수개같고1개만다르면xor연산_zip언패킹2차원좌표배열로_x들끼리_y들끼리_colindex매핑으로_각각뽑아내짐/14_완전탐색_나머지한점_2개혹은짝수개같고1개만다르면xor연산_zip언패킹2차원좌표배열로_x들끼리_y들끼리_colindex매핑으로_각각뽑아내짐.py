import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## https://school.programmers.co.kr/learn/courses/18/lessons/1878
    v = []
    for _ in range(3):
        v.append(list(map(int, input().split())))

    # (1)3개 중 x중복 안된 1개가 나머지 x좌표
    # (2)3개 중 y중복 안된 1개가 y좌표
    # xs = list(map(lambda x: x[0], v))
    # x = [x for x in xs if xs.count(x) == 1][0]
    #
    # ys = list(map(lambda x: x[1], v))
    # y = [y for y in ys if ys.count(y) == 1][0]
    # print([x, y])

    ## 좌표 배열 = 2차원 배열의 zip(*lst_2d)를 통해 index매핑된 0번째 자리 x들만, 1번재 자리 y들만 모을 수 있다.
    # => col index끼리 매핑하는 것 뿐만 아니라, 좌표배열에서도 같은 index끼리 == x좌표끼리, y좌표끼리 모을 수 있다.
    xs_and_ys = [coords for coords in zip(*v)]
    print(xs_and_ys)
    # [(1, 3, 3), (4, 4, 10)]

    x_and_y = [coord for coords in zip(*v) for coord in coords if coords.count(coord) == 1]
    print(x_and_y)

    ## 같은 것이 짝수로 있고, 다른 것이 1개만 있는 상황이면, 순서상관없이 ^ 연산을 해주면, 다른 것 1개만 남는다(같은것들은 짝수개를 ^하면 사라진다)
    # print(4 ^ 10)  # 14
    # print(4 ^ 10 ^ 4)  # 10
    # print(4 ^ 10 ^ 4 ^ 4)  # 14
    # print(4 ^ 10 ^ 4 ^ 4 ^ 4)  # 10
    xs, ys = [coords for coords in zip(*v)]
    print(xs, ys) # (1, 3, 3) (4, 4, 10)

    from functools import reduce
    from operator import xor
    # 같은 것이 짝수개 존재하는 상황일 때, 누적해서 xor해줘서, 다른 것 1개만 남기기
    print(reduce(xor, xs), reduce(xor, ys)) # 1 10
    print([reduce(xor, coords) for coords in zip(*v)]) # [1, 10]

