import itertools
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## N번째 요소들만 추출

    lst_2d = [[i + row * 4 for i in range(3)] for row in range(4)]
    for row in lst_2d:
        print(*row)

    lst = list(itertools.chain.from_iterable(lst_2d))

    # 3의배수 자리들만 요소들만 선택해보기
    ## 1. index에 나머지 연산자 활용하기
    for i in range(len(lst)):
        # 0번째 요소 제외하고 3번째 자리들 뽑기
        if i and i % 3 == 0:
            print(lst[i], end=" ")
    print()
    # 4 8 12

    ## 2. range의 등차 이용하기
    for i in range(3, len(lst), 3):
        print(lst[i], end=" ")
    # 4 8 12
    print()

    ## N번째 방만 불끄기 -> 스위치(방문)배열 or bit 이용
    # (1) 상태배열 + index나머지연산으로 방문배열 toggle하기
    # -> 0번째는 제외시킨다면, 불켜놔도 상관없다.
    N, target = 10, 3  # 3번째 방만 확인한다.
    gate = [0] * (N + 1)  # -> 출력시 1번째방부터 출력 state[1:]
    # for i in range(len(gate)):
    #     # 1, 4, 7...
    #     if i % 3 == 1:
    #         ## T/F의 toggle은 not을 붙여서 not value로 toogle 한다.
    #         # 0/1의 값 toogle은 ( +1 )%2로 하는 방법도 있다. 0 -> 1 , 1-> 0 나온다.
    #         # gate[i] = not gate[i] # 0 -> 1 , 1 -> 0
    #         gate[i] = (gate[i] + 1) % 2
    # print(gate) # [0, True, 0, 0, True, 0, 0, True, 0, 0, True]
    # [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1]

    # #  1부터 N까지 돌면서, 각 수의 배수들 토글하기
    # for number in range(1, N +1):
    #     ## 그 수부터 나머지가 0인 것들 다 토글하면 된다.
    #     # => 시작이 0부터가 아니라면.. number보다 작은 나머지들 중 1개를 선택해서 나머지로 넣어준다.
    #     for i in range(len(gate)):
    #         # i를 조건으로 줘서 0은 제외하고 토글하기
    #         if i and i % number == 0:
    #             gate[i] = (gate[i] + 1) % 2
    #     print(gate)
    #

    ## (2) 배수 토글은 range(1배수, 배수)의 range등차를 이용하자 -> 시작명확 + if문이 없어진다.
    # 상태배열 + range배수등차( range(t, 끝index+1, t)
    for target in range(1, N + 1):
        for i in range(target, N + 1, target):
            gate[i] = (gate[i] + 1) % 2
        print(''.join(map(str, gate[1:])))

    ## (3) 이진수bit를 상태배열로 + range배수등차
    # N번재1로 만들어서 XOR로 토글
    # -> 1번째부터 bit를 사용할거라면, 쉬프트시 N + 1로 만들어줘야한다.
    gate = 0
    for target in range(1, N + 1):
        for i in range(target, N + 1 + 1, target):
            gate = gate ^ (1 << i)
        # 이진수는 0번째 자리도 가지고 있어서 빼고 출력 + 보려면 역순으로 출력
        # ::-1 역순인덱스의 시작끝은 원래인덱스로 지정한다.
        # (1) [2: -1] 마지막인덱스가 0자리이므로 빠지게 end자리에 둔다.
        # (2) 역순으로 출력한다 [2:-1:-1]
        print(bin(gate)[2:-1:-1])