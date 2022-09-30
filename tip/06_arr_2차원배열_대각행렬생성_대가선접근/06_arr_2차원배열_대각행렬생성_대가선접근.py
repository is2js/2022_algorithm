import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## 대각선으로 동일한 2차원배열 만들기
    # (1) listcomp안에서 첫번째 row를  col_index로 등차수열(1,n+1)로 만들고
    # (2) map(lambda, row)를 row _index(0, n)에 따라 변하도록 각 row를 생성한다
    #    이 때 각 요소별로 col + row를 해주면, row = 0, 1,2,3,씩 추가된다.
    # => 첫 row를 유지하기 위해선 row_index는 0부터 시작하게 해야한다.
    # => col은 그와 상관없이 시작숫자를 편하게 준다.

    # (3) 2차원행렬의 생성은 list comp로 한다.
    # lst_2d = [col for col in range(1, 4 + 1)]
    # lst_2d = [[col for col in range(1, 4 + 1)] for row in range(4)]
    # => 아직 row마다 map(lambda로 터치를 안줬다)
    # for row in lst_2d:
    #     print(*row)
    # 1 2 3 4
    # 1 2 3 4
    # 1 2 3 4
    # 1 2 3 4
    lst_2d = [list(map(lambda x: x + row, [col for col in range(1, 4 + 1)]))
              for row in range(4)]
    for row in lst_2d:
        print(*row)
    # 1 2 3 4
    # 2 3 4 5
    # 3 4 5 6
    # 4 5 6 7

    # (4) 첫row의 col이 증가하는만큼, row index의 터치도 똑같이 들어가도록 변경할 수 있다.
    # -> 첫 row를 등차를 1를 준다 ( 끝index는 == 끝항 + 1 == (2n(4)-1) + 1)
    # -> 각 row별로는 + (rowindex*2)씩 더해지도록 한다.
    lst_2d = [list(map(lambda x: x + (2 * row), [col for col in range(1, (2 * 4 - 1) + 1, 2)]))
              for row in range(4)]
    for row in lst_2d:
        print(*row)
    # 1 3 5 7
    # 3 5 7 9
    # 5 7 9 11
    # 7 9 11 13

    # (5) 가운데 대각선 1줄 접근하기
    # -> ↗ 방향이라 가정하고, row 는 뒤에서부터, col은 처음부터 동시에 접근하는 것이다.
    # -> for문 1개로 1개의 대각선을 추출할 수 있다.
    for i in range(len(lst_2d)):
        print(lst_2d[-(i + 1)][i], end='')  # 7777
    print()

    # 가운데 대각선이 아니라면, row는 끝-1~0 , col은 0~끝-1의 index로 접근하면 된다.
    for i in range(len(lst_2d) - 1):
        print(lst_2d[-(i + 1 + 1)][i], end='')  # 555
    print()

    # 가운데에서 위쪽으로만
    for k in range(4):
        for i in range(len(lst_2d) - k):
            print(lst_2d[-(i + 1 + k)][i], end='')
            # 7777
            # 555
            # 33
            # 1
        print()

    # 처음부터 출발하되, N(가운대대각선)을 넘어가면, row는 n-1고정.. col은 출발점을 +1씩..
    N = 4
    # (3) 이제 가운데 대각선이 아니라 처음부터 진행하도록 for문을 역순으로 돌린다.
    # for k in range(2 * N - 1 -1, 0 - 1, -1):
    for k in range(2 * N - 1):
        # (1) row_index는 시작점이 0, 1, 2, 점점 커지며, 거기서부터 1씩 내려간다.
        # -> 1줄씩 touch이므로, row,col이중for문이 아니라, -> i에 대해서 인덱스만 역순으로처리하게 한다.
        # -> i는 0부터 시작하므로, 뒤에서 역순탈라면 -(i+1) or len - 1 - i에서 시작점을 k를 터치해야한다.
        if k <= N - 1:
            # (2)
            # for i in range(N):
            # k에 따라 갯수도 회전 총 갯수도 줄어든다 -> range를 터치한다.
            # for i in range(N - k):
            #     print(lst_2d[-(i + 1 + k)][i], dst='')
            # k = 0 -> (0,0) 1개
            # k = 1 -> (1,0) (0,1) 2개
            #     i -> (i+1)부터 0까지 줄어들고, 총 i+1개

            for i in range(k + 1):
                print(lst_2d[-i + k][i], end='')
            print('|')

        # (4)
        # 반대쪽은 else에서 N-1개(k==2N-1 ~ N +1)를 처리하면 되는데,
        else:
            # (5) 일단 시작row는 마지막N-1자리로 고정이다.
            #   횟수는 2N -1 - (반대k)
            # print(2*N-1-k)
            k = 2 * N - 1 - k  # 3, 2, 1
            for i in range(k):
                # row 마지막행 고정에서 역순
                # col은.. 뒤에서 k만큼 나온데서 [정순] -> 앞에서 (N-k)부터 출발?
                print(lst_2d[-i + N - 1][i + (N - k)], end='')
                pass
            print('|')

    ## test
    # 1. 대각선으로 동일한 등차수열 2차원배열만들기
    # (1) listcomp에서 col을 등차수열로 선언한다
    # (2) row별로 map(lambda(x:x+rowindex*등차, ))로 요소변화를 row_index를 통해 등차만큼 touch해서 각 row를 생성한다
    lst_2d = [list(map(lambda x: x + (2 * row), [col for col in range(1, (2 * 5 - 1) + 1, 2)]))
              for row in range(5)]
    for row in lst_2d:
        print(*row)
    # 1 3 5 7 9
    # 3 5 7 9 11
    # 5 7 9 11 13
    # 7 9 11 13 15
    # 9 11 13 15 17

    # 2. 가운데 대각선 1줄터치는 1개 반복문 i에 대해 -> row는 역index col은 정index를 사용하면 된다
    for i in range(len(lst_2d)):
        # print(lst_2d[-(i+1)][i], dst="") # python전용
        print(lst_2d[len(lst_2d) - 1 - i][i], end="")
    print()

    # 3. 개별 대각선k마다 수를 처리하고 싶다면

    N = len(lst_2d)
    # (1) 가운데를 포함한 N개 + 가운데빼고 N - 1개 = 2N - 1를 k로 돌린다.
    for k in range(2 * N - 1):
        # (2) 0 ~ N - 1개의 대각선을 처리한다.
        if k <= N - 1:
            # (2-1) 대각선 한 줄을 처리할 for i를 돌리는 데,
            # -> 대각선k=0부터 시작하지만, 갯수도 k개 돌리기 위해 range(k + 1)를 돌린다.
            for i in range(k + 1):
                # (2-2) row는 역순으로 가기 때문에 -1등차의 -i 에다가
                #       시작row_index는 k(초항)이 되도록 돌린다
                #       col은 k=0부터 그대로 가니까 i로 돌린다.
                print(lst_2d[-i + k][i], end='')
            print('|')

        # (3) 나머지 절반은 k  index가  N ~ 2N -2까지.. N -1개를 따로 처리한다
        else:
            # (3-1) 대각선을 기준으로 대칭되는 k와 갯수를 맞춰주기 위해서
            # -> 전체갯수len - 1 - 현재k = 역index처럼 대칭k를 가지게 한다.
            #  012 3 456 => 7 - 1 - 4 = 2
            #            => 7 - 1 - 5 = 1
            k = 2 * N - 1 - 1 - k
            # (3-2) k=0부터니까 갯수는 1부터 시작하려면 k + 1로 돌린다.
            for i in range(k + 1):
                # (3-3) row는 역순이지만 맨마지막row고정이라 -i 에다가 + (N-1)이 초항으로 들어가게 한다.
                #       col인덱스는 정순i에다가  + 시작을 N-k부터
                #     -> 0 + 4 - 3 (1)부터
                #        0 + 4 - 2 (2)부터
                #     => k에 대한 역순index인 N - 1 - k 에다가 +1 한데서 출발해야하므로
                #        +1 i에다가 N - k에서 시작하게 한다.
                print(lst_2d[-i + N - 1][i + (N - k)], end='')
            print('|')
    # 1|
    # 33|
    # 555|
    # 7777|
    # 99999|
    # 11111111|
    # 131313|
    # 1515|
    # 17|
