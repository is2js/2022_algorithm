import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## 카펫: https://school.programmers.co.kr/learn/courses/30/lessons/42842
    ## => 풀이 구루미: https://gurumee92.tistory.com/181?category=782306

    brown, yellow = map(int, input().split())

    ## (1) 전체 격자 수 정보를 저장
    # total_carpet = brown + yellow

    ## (2) 테두리 정보로 b와 y를 연결할 수 있다.
    ## 테두리 갯수 - 4 == 안쪽 도형의 둘레
    ## => 이 정보로 b와 y관계를 고정시켜 탐색할 수 있다.
    ## (2-1) brown갯수는 나와있으니, yellow가 만드는 직사각형의 둘레를 탐색해야한다.

    ## (3) yellow의 갯수 고정 -> 사각형 넓이 고정 ->  yellow의 둘레(2*(x+y))를 구해야한다
    ## -> 갯수 == 넓이가 되므로, y_row * y_col == 갯수가 되어야한다
    ## -> 넓이가 고정된 직사각형은 다향한 모양을 만드는데,
    ## -> 그 만드는 조합은 1 * 24  2 * 12 등의 약수의 곱 == 사각형의 모양을 만들어낸다.

    ## (4) 넓이를 바탕으로 [넓이의 약수들]을 먼저 구하고 -> [대칭 곱]을 만들어낸다.
    ##    -> 소수는 2~k-1를 약수로 치고 나누어떨어지면 탈락
    ##    -> [약수는 1~k까지 나누어떨어지면 ok다]
    # y_factors = [k for k in range(1, yellow + 1) if yellow % k == 0]
    # print(y_factors)
    # [1, 2, 3, 4, 6, 8, 12, 24]

    ## (5) 테두리 - 4 = 안쪽사각형의 둘레가 맞는지 1개의 예로 확인한다.
    # print(brown - 4 == 2 * (1 + 24)) # False
    # print(brown - 4 == 2 * (2 + 12)) # False
    # print(brown - 4 == 2 * (3 + 8)) # False
    # print(brown - 4 == 2 * (4 + 6)) # True
    ## => 테두리와 둘레와의 관계 && 넓이 고정 -> 1개(짝 2개)의 직사각형이 고정된다.
    # ex> 3by3 테두리(8) - 4 = 2 * (1 + 1)

    ## (6) x에 대해 대칭되는 약수는 곱만 알고 있다면, 24 // x 로 구할 수 있다.
    # ex> 24 // 6 = 4
    # => 약수배열 for x로 돌면서, 대칭 짝 약수는 yellow // x으로 쓴다.

    ############ 풀이 시작

    ## (1) b + y를 합하여 전체 카펫의 넓이를 구한다
    carpet = brown + yellow
    ## (2) 넓이고정 -> [사각형의 넓이를 만드는 가로, 세로] -> 넓이의 약수의 쌍들이다
    ## => carpet의 약수들(1~N까지 N에 나누어떨어지는수)을 구하되, 약수의 탐색은 1부터 제곱근까지만 하고, N // k를 짝약수로 쓴다.
    # -> N//k로 짝약수를 바로 불러올 수있다면, 제곱근까지만 탐색하면, 제곱수일경우 제곱수까지, 아닐경우 가운데에서 왼쪽정도까지 구해질 것이다.
    # carpet_factors = [k for k in range(1, carpet + 1) if carpet % k == 0]
    carpet_factors_pair = [(k, carpet // k) for k in range(1, int(carpet ** 0.5) + 1) if carpet % k == 0]
    # print(carpet_factors_pair)
    # [(1, 48), (2, 24), (3, 16), (4, 12), (6, 8)]

    ## (3) 가로 세로 여러 case => brown 테두리로 가로, 세로 중 1개를 fix한다.
    ##  =>  가로 세로 여러 case => 둘레인 brown이 만들어본다
    #   => (가로 + 세로) *  2 - 4 == 둘레
    ## 사각형의 테두리 - 4 == 안쪽 사각형의 둘레
    ## 사각형의 둘레 == 가로 + 세로
    for row, col in carpet_factors_pair:
        if (row + col) * 2 - 4 == brown:
            ## (4) 여기서 가로가 더 길어야하므로, 약수의 반대쪽을 탐색안했으면 결과만 뒤집어 주면 된다
            print(col, row)
            break

