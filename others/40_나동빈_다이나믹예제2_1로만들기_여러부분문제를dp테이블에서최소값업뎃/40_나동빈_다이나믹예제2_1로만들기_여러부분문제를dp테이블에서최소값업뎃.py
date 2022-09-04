import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## 1로 만들기
    # 연산종류 4가지 /5 /3 /2 -1 => 1로 만들기

    ###### 내풀이
    # => FourSquare처럼, 재귀식이 부분문제 중 택1이라 다 해보면서 최소값 업데이트(greedy)해야한다
    # f(n) = n%5==0 -> f(n%5)
    #        n%3==0 -> f(n%3)
    #        n%2==0 -> f(n%2)
    #        f(n-1)
    #  4가지를 다 해보고, 그 중 min()을 선택 -> 부분문제들로 해결이 되며 부분문제들이 반복된다.
    # X = int(input().strip())

    # d = [0] * (X + 1)
    # d = [0] * (30000 + 1)  # -> dp테이블은 X가 아니라, 문제에서 주어지는 범위의 끝을 다 커버가능하게 만들어야한다.
    # d[0] = 0
    # d[1] = 0
    # d[2] = 1
    # d[3] = 1
    # d[4] = 1 + 1
    # d[5] = 1
    # for i in range(6, X + 1):
    #     result = i
    #     possible_case = []
    #     if result % 5 == 0:
    #         possible_case.append(1 + d[result // 5])
    #     if result % 3 == 0:
    #         possible_case.append(1 + d[result // 3])
    #     if result % 2 == 0:
    #         possible_case.append(1 + d[result // 2])
    #     if result >= 2:
    #         possible_case.append(1 + d[result - 1])
    #     d[i] = min(possible_case)
    #
    # print(d[X])

    ####### 풀이
    # ai = i를 1로 만들기 위한 최소연산 횟수
    # 점화식 ai = min(ai-1, ai/2, ai/3, ai/5) + 1
    # 나누기는 나누어떨어질때만 적용
    ### 차이점
    # -> dp테이블은 문제요구사항 전체를 커버하도록 선언한다.
    # -> dp테이블은 최소한만 만들어줘도 알아서 적용된다. -> i-1이 있으니 d[1]까지만 처리해준다. 나머지는 해당될 경우 처리하므로
    # -> 각 case별 최소값은 d[i] = min(ai-1 + 1) -> 해당하는 경우 d[i] = min(d[i], ai/2 + 1)처럼
    #    => 최소값은 case별로 연쇄적으로 적용할 수 있다.
    x = int(input().strip())
    d = [0] * (30000 + 1)
    # d[1] = 0
    for i in range(2, x + 1):
        # 택4 중에 확실한 것부터 dp테이블에 이미 배정을 하고, 필요시마다 업데이트해주면 된다.
        d[i] = 1 + d[i - 1]

        if i % 2 == 0:
            # 이미 업데이트된 table값으로 min업데이트를 해줄 수 있다. case별로 모든 값을 모으지 않아도 된다.
            # 최소최대탐색은, 결과변수 자리를 가변변수로서 업데이트 계속 해줄 수 있다.
            d[i] = min(d[i], 1 + d[i // 2])
        if i % 3 == 0:
            d[i] = min(d[i], 1 + d[i // 3])
        if i % 5 == 0:
            d[i] = min(d[i], 1 + d[i // 5])

    print(d[x])
