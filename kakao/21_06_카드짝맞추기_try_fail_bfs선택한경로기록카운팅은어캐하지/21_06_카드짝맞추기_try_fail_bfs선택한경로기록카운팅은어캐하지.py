import sys
from collections import deque

input = sys.stdin.readline


def find_same_card(r, c):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if r!=row and c!=col and board[r][c] == board[row][col]:
                return row, col


def bfs(board, visit, r, c, er, ec):
    q = deque([(r, c)])
    count = 0

    ## bfs에서는 선택한 길만 카운팅을 어캐하지?
    routes = []

    while q:
        cr, cc = q.popleft()

        if cr == er and cc == ec: break

        for dr, dc in DELTA:
            nr, nc = cr + dr, cc + dc
            if not( 0<=nr<=3 and 0<=nc<=3): continue

            if visit & (1 << (nr * 4 + nc)): continue
            visit = visit | (1 << (nr * 4 + nc))
            q.append((nr, nc))

    return count


if __name__ == '__main__':
    ## 카드짝맞추기: https://school.programmers.co.kr/learn/courses/30/lessons/72415
    board = [list(map(int, input().split())) for _ in range(4)]
    total_count = 0
    DELTA = ((-1, 0), (1, 0), (0, -1), (0, 1),)

    # visited = [[False]*4 for _ in range(4)]
    # board를 visited로 복사해서 쓰고 싶지만, 2차원배열은 깊은복사가 안된다.
    # => bit를 통해 4*4를 통해 나타낸다?
    visit = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] != 0:
                ## 0이 아닌 자리는 다 장애물이 있는 것으로 간주
                visit = visit | (1 << (row * 4 + col))

    r, c = map(int, input().split())
    if visit & (1 << (r * 4 + c)):
        total_count += 1

    ## 일단, 현재위치에서, 가야하는 위치를 찾고 -> bfs로 최단거리를 움직이되, 직전과 같은 방향이면 count세지 않는다.
    er, ec = find_same_card(r, c)
    print(er, ec)
    count = bfs(board, visit,
                r, c, er, ec)

    print(bin(visit), count)
