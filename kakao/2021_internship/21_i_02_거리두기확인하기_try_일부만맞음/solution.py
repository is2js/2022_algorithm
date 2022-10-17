import itertools
import sys
from collections import deque

input = sys.stdin.readline


def check_distance(p_combinations):
    for p1, p2 in p_combinations:
        if get_m_distance(p1, p2) < 2:
            return False
    else:
        return True


def get_m_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def bfs(place, src, dst):
    visited = [[False] * 5 for _ in range(5)]

    visited[src[0]][src[1]] = True
    q = deque([src])

    while q:
        c_row, c_col, c_cost = q.popleft()

        if c_row == dst[0] and c_col == dst[1]:
            return True

        for d_row, d_col in DELTA:
            n_row, n_col = c_row + d_row, c_col + d_col
            if not (0 <= n_row <= 4 and 0 <= n_col <= 4):
                continue
            if get_m_distance((c_row, c_col), (n_row, n_col)) == 2 and\
                    place[n_row][n_col] == 'O':
                return False
            if visited[n_row][n_col]: continue
            visited[n_row][n_col] = True
            q.append((n_row, n_col))


## 좌표탐색은 board가 필요없는 보통 커서로 탐색인데, 그 자리에 뭐가 있다면 board가 필요하다.
## global로 확인해도 되지만,, for문안에 1개씩이라 불가
def check_partition(place, p_combinations):
    for (row1, col1), (row2, col2) in p_combinations:
        if not bfs(place, (row1, col1), (row2, col2)):
            return False
    else:
        return True


if __name__ == '__main__':
    ## 거리두기확인하기: https://school.programmers.co.kr/learn/courses/30/lessons/81302
    places = [list(input().split()) for _ in range(5)]

    DELTA = ((-1, 0), (1, 0), (0, -1), (0, 1),)
    places = [list(map(list, place)) for place in places]
    answer = []
    for place in places:
        ## 1. 각 p의 좌표들을 저장해서, nC2 거리를 체크한다.
        ps = []
        for row in range(len(place)):
            for col in range(len(place[row])):
                if place[row][col] == 'P':
                    ps.append((row, col))

        p_combinations = itertools.combinations(ps, 2)
        if not check_distance(p_combinations) or not check_partition(place, p_combinations):
            answer.append(0)
            continue
        else:
            answer.append(1)

    print(answer)
