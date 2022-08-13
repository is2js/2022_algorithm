import sys

input = sys.stdin.readline


def solution():
    # https://www.youtube.com/watch?v=zE4GMGjzSf0
    ## 재귀를 통한 Food fill 알고리즘
    # input에서 0은 빈공간, 1은 경계선
    # 1 1은 임의의 좌표
    # -> 1, 1부터 빈 공간을 1로 채우는 예제
    # -> 그림판에서 경계면을 만날때까지 색이 다 칠해지는 예시
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    start_row, start_col = map(int, input().split())

    def fill(r, c):
        # 2) 재귀메서드를 정의한다면, stack결정 파라미터들로 종착역을 먼저 작성한다
        # -> board를 벗어난 좌표를 걸어준다.
        # -> N by N의 좌표는 0~N-1을 벗어나면 종료다.
        if r < 0 or r > N - 1 or c < 0 or c > N - 1:
            # 결과값을 반환할 게 아니라면 그냥 return이다.
            # 만약, board를 파라미터에 넣는다면, 완성된 board를 return
            # => print처럼, 전역변수에 마킹만 한다면, 그냥 종료만 시키면된다.
            # => return되는값이 필요없다 + 동적트리순회는 return후 back해도 다음자식을 부르고 마지막자식끝나면 바로 종료다.
            return

        # 3) 좌표를 업데이트하면서 [경계선1]을 만난 경우도 stop이다.
        # -> 업데이트된 좌표r, c를 받았다고 생각하고, 그 좌표가 != 0이면 중단
        if board[r][c] != 0:
            return

        # 4) 종착역이 아니면, 자신의 처리로서 1로 채운다
        board[r][c] = 1
        # 5) 자신의 처리가 끝났으면, 다음 좌표를 입력해준다.
        # -> 상하좌우순서대로 호출할 것이다.
        # -> 한칸위는 r좌표 + 1이 아니라 r -1 이다.
        # => 좌표의 이동은 동적트리순회와 비슷하다.
        # => return되는값이 필요없다 + 동적트리순회는 return후 back해도 다음자식을 부르고 마지막자식끝나면 바로 종료다.
        fill(r - 1, c)
        fill(r + 1, c)
        fill(r, c - 1)
        fill(r, c + 1)

        ## 동적트리순회(좌표이동, 자식돌기)는 누적변수를 올리지 않는다.  1개값 return(꼬리재귀)이 불가능하다.
        ## 동적트리순회는 끝처리 없이 바로 종료되는 경우가 많다.
        ## 트리들이 1개당 4개좌표씩 벗어나거나, 경계선 물리면 알아서 종료된다.
        ## 빽 후 끝처리 하지 않는 좌표이동은 4개의 트리가 순식간에 뻗어나갔다가, 자신처리만 하고 종료된다.

    # 1) 재귀를 통해 board를 업데이트한다고 가정하고, 재귀메서드를 호출한다.
    # -> start 행렬의 좌표를 최초인자로 준다.
    # -> 행렬의 좌표는 재귀stack을 구분시켜주는 업데이트 변수이므로 맨 앞에 준다.
    ## 동적트리순회(좌표이동, 자식돌기)는 누적변수를 올리지 않는다.  1개값 return(꼬리재귀)이 불가능하다.
    ## -> board를 누적결과값으로 올리지 않는 것도, 좌표이동은 동적트리순회돌기 때문에,
    ## -> 자신이 전역변수처리만 하고 업데이트된 값 반환없이 종료되기 때문이다.
    fill(start_row, start_col)

    # 6) 1->4좌표 동적트리순회가 끝났다면, 마킹된 전역변수를 찍어본다.
    for num in range(N * N):
        row, col = num // N, num % N
        if col != N - 1:
            print(board[row][col], end=" ")
            continue
        print(board[row][col])
    # 1 1 1 1 1
    # 1 1 1 1 1
    # 1 1 1 1 0
    # 1 1 1 1 0
    # 0 0 0 0 0
    pass


if __name__ == '__main__':
    solution()
