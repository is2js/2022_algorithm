import sys

input = sys.stdin.readline


def dfs(DELTA,
        board, row, col):
    ## 좌표탐색의 종착역은, 이미 방문체크된 좌표일 때다( 방문표시 좌표인 경우 탐색 종료)
    # -> 좌표유효성은 다음 좌표로 이동시 이미 한다.
    ## 계산이 없는 종착역인 경우, default값 0을 return해준다.
    if not board[row][col]: return 0

    ## 자신의 처리 ( 방문 처리, 자신의 집계값 선언후 자시들과 누적할 변수 선언)
    # -> dfs-재귀는 자신의 처리에서 방문표시한다. 방문체크는 다음좌표 진입전에 한다
    # -> dfs는 재귀, stack에 앞에 같은 좌표를 미리 쌓아놓을 수 있어서, 가장 최근 좌표에 진입 후 방문체크한다.
    board[row][col] = 0
    ## 여러 경로의 종착역이 존재하는 경우, 누적결과값을 들고 다니지만,
    ## => 계산이 없는 종착역인 경우, default값 0 vs 계산좌표에서는 자신의 집계값을 변수로 가지고 있다가
    ##   자신의 집계값(count는 1) += 자식node의 반환값과 함꼐 누적 집계해서 부모node에 반환해준다.
    count = 1

    ## 자식들 처리
    for d_row, d_col in DELTA:
        n_row, n_col = row + d_row, col + d_col
        if not (0 <= n_row <= N - 1) or not (0 <= n_col <= N - 1): continue
        ## 진입 전, 방문체크 (dfs의 방문표시는 꺼내서 한다)
        if not board[n_row][n_col]: continue
        ## 자식들은 자신의 갯수를 1씩 반환한 것들을 집계해서 넣어준다.
        count += dfs(DELTA, board, n_row, n_col)

    return count


if __name__ == '__main__':
    ## 단지번호붙이기: https://www.acmicpc.net/problem/2667
    # -> 끊기는 좌표탐색은, global visited + 시작좌표들 배회하며 dfs, bfs를 탐색한다.
    N = int(input().strip())
    board = [list(map(int, input().strip())) for _ in range(N)]
    DELTA = ((-1, 0), (1, 0), (0, -1), (0, 1),)

    total_count = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            # 시작좌표는 1인 것만 출발한다.
            # -> 방문표시 역시 0으로 해야할 것 같다.
            if not board[row][col]: continue

            ## 시작좌표마다 탐새한 좌표의 갯수를 반환해준다.
            total_count.append(dfs(DELTA, board, row, col))

    print(len(total_count))
    # print('\n'.join(sorted(map(str, total_count))))
    print(*sorted(total_count), sep='\n')
