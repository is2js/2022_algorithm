import sys
from collections import deque

input = sys.stdin.readline


def bfs(visited, DELTA, images,
        row, col):
    # visited 선언 생략, queue를 만들어 inqueue한다
    visited[row][col] = True  # 인큐 전 방문표시
    q = deque([])
    q.append((row, col))

    counter = 0
    while q:
        c_row, c_col = q.popleft()

        # 방문관련된 로직은 자신의 처리에서 한다
        counter += 1

        # 다음node탐색
        for d_row, d_col in DELTA:
            n_row, n_col = c_row + d_row, c_col + d_col
            # 좌표 검사
            if not (0<= n_row <= n-1) or not (0<= n_col<=m-1): continue
            # 색 검사
            if images[n_row][n_col] != images[c_row][c_col]: continue
            # inqueue 전 방문체크 방문표시
            if visited[n_row][n_col]: continue
            visited[n_row][n_col] = True
            q.append((n_row, n_col))

    # break가 없다면 q나 stack에 나머지 처리를 할 필요는 없다.

    return counter




if __name__ == '__main__':
    ## floddfill 문제 및 풀이: https://velog.io/@hongin/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4-lv3.-FloodFill
    ## 시작좌표부분만 bfs로 빼고, visited를 공유하기
    n, m = map(int, input().split())
    images = []
    for _ in range(int(input().strip())):
        row = list(map(int, input().split()))
        images.append(row)

    ## (1) 시작좌표가 여러 개여야하는 상황 -> 배열을 순회하면서
    ##    bfs가 끊기면, 새로운 시작좌표가 시작하되, 시작좌표도 외부에서 방문체크하도록 하기 위해
    ##    bfs내부가 아닌 외부 visited배열을 선언한다.
    visited = [[False] * m for _ in range(n)]
    DELTA = ((-1, 0), (1, 0), (0, -1), (0, 1),)

    result = []

    ## (2) 시작좌표들을 배회 단, bfs내부에서 visited 방문한 것을 피한다.
    # for row in range(len(images)):
    #     for col in range(len(images[row])):
    for num in range(n * m):
        row, col = num // m, num % m

        ## 방문체크하고 bfs를 출발좌표로 출발한다.
        if visited[row][col]: continue
        result.append(
        bfs(visited, DELTA, images,
            row, col))

    # print(result)
    print(len(result))