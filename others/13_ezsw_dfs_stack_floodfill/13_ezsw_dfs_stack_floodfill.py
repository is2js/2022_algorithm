import sys

input = sys.stdin.readline


def dfs(r, c, color):
    # [5] 재귀가 아닌 stack의 dfs는 visited배열을 지역변수로 쓴다.
    #    dfs로 행렬탐색은, 각 좌표를 하나하나의 node로보고 상태배열을 선언하기 때문에
    #    2차원 마킹배열 -> 2차원 node -> 2차원 visited로 선언해야한다.
    visited = [[False for _ in range(N)] for _ in range(N)]

    # [6] stack을 이용한 node탐색은, 첫 node는 일단 stack에 넣었다가
    #    while문 통과후 pop해서 curr로 받아서, 방문여부 검사후 쓴다고 했다.
    stack = []
    stack.append((r, c)) # [7] 각 좌표는 뎃후 튜플로 묶어서 stack에 넣는다.
    while stack:
        curr = stack.pop() # 처음에는 방문안한 시작점이 pop된다.
        if visited[curr[0]][curr[1]]:
            continue
        # [8] 방문여부확인은 방문여부체킹(add)할려고 하는 것이다.
        # -> 바로 해주고, 로직을 전개한다.
        visited[curr[0]][curr[1]] = True
        # [9] 요구사항상 현재node(좌표)에서 해줘야할 일은,
        #     전역변수 board에 color로 색칠하는 것이다.
        board[curr[0]][curr[1]] = color

        # [10] 다음좌표탐색은 Delta를 이용해서 순서대로 탐색한다.
        for i in range(len(D)):
            # [11] 각각의 좌표를 업뎃한다.
            next_row = curr[0] + D[i][0]
            next_col = curr[1] + D[i][1]
            # [12] 좌표는 업뎃후 바로 범위를 확인한다.
            if not(0 <= next_row <= N-1) or not(0 <= next_col <= N-1):
                continue
            # [13] stack을 통한 탐색에서는, next node의 방문여부 + @요구사항를 확인하고 append(push)해준다.
            if visited[next_row][next_col]:
                continue
            # [14] 탐색할 node append전, 요구사항 확인
            if board[next_row][next_col] == 1:
                continue
            stack.append((next_row, next_col))
    # [15] dfs를 이용한 탐색은, 순서대로 최대한 stack/node를 깊이가려고 한다
    #  -> 도착점까지 길을 찾을 때도 쓸 수 있다
    #  -> board값을 비교해보고 있으면 early return True
    #  -> 다돌아도 없으면 맨끝에서 return False


if __name__ == '__main__':
    # DFS스택 활용 flood fill
    # [1] 탐색할 좌표방향의 델타 값을 dx, dy가 아닌 튜플로 x,y 쌍으로 정의할 수도 있다.
    # 상하좌우
    D = ((-1, 0), (1, 0), (0, -1), (0, 1),)
    N = int(input().strip())
    board = [list(map(int, input().split())) for _ in range(N)]
    # [2] 좌표를 r, c로 받는다.
    sr, sc, color = map(int, input().split())

    # [3] dfs-stack에서, 시작좌표를 각각 인자로 넣는다. 추가로 필요변수도 넣는다.
    dfs(sr, sc, color)

    # [4] 마킹될 전역변수는 미리 출력을 찍어준다.
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()
