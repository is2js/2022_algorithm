import sys

input = sys.stdin.readline


def dfs(x, y):
    ## 꼬리재귀의 종착역
    # -> (1) 누적/집계값을 들고다닌다면, 종착역에서 해당 [집계 파라미터(최종 결과값)]를 반환
    # -> (2) 각 node마다 개별값을 반환하여 부모 -> root에서 최종 집계한다면, [누적/집계의 기본값]을 반환하여 결과에 포함안되게 한다.
    if not board[x][y]:
        return 0

    ## 자신의 처리
    # -> (1) 재방문을 막는다면 방문체킹한다
    # -> (2) 꼬래재귀라면, 자신의 누적/집계처리를 하기위해 변수를 선언 -> 자식들의 여러 반환값들을 해당지역변수에 집계까지 해야한다.
    board[x][y] = 0
    ret = 1 # 자신의 집계값

    ## 자식들 처리
    for dx, dy in Delta:
        nx = x + dx
        ny = y + dy
        if not (0 <= nx <= N - 1 and 0 <= ny <= N - 1):
            continue
        if not board[nx][ny]:
            continue
        ## 꼬리재귀에서 자식들의 값들은 누적/집계해야한다
        # -> 반복문에서 1개씩 반환된다면, 누적해놔야한다.
        ret += dfs(nx, ny)

    ## 자신의 끝처리
    # -> 꼬리재귀는 자신의 값 + 자식들의 집계값들을 최종 1개로 반환해줘야한다.
    return ret


if __name__ == '__main__':
    # dfs 단지번호 붙이기: https://www.acmicpc.net/problem/2667
    N = int(input().strip())
    board = [list(map(int, list(input().strip()))) for _ in range(N)]

    Delta = ((-1, 0), (1, 0), (0, -1), (0, 1))

    ## 순서대로 방문해주되, dfs로 지나간 자리는 0으로서 이미 체킹한 것으로 간주한다.
    ## board자체가 방문배열이 된다.

    result = []
    for row in range(len(board)):
        for col in range(len(board[0])):
            # 0찍힌 좌표는 건너띄고 1인 것만 dfs 탐색 시작하면서, 방문시 0으로 체킹한다.
            if board[row][col] == 0:
                continue
            # print(dfs(row, col))
            result.append(dfs(row, col))

    print(len(result))
    ## 숫자 lst를 map으로 문자열로 바꾸고 sorted()치면, 문자열 lst로 바뀐다.
    ## => 숫자lst를 한줄씩 출력하고 싶다면, map으로 문자열로 바꾼 뒤. \n로 join하여 출력한다.
    print('\n'.join(sorted(map(str, result))))
