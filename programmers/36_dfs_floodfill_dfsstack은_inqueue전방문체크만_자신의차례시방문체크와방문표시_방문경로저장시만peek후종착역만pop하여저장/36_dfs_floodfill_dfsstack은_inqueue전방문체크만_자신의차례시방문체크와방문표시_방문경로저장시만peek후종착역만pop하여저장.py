import sys

input = sys.stdin.readline


def dfs(images, visited, row, col):
    # 좌표탐색은 visisted + stack자료구조

    ## bfs와 다르게, inqueue전에는 방문체크만 하고, 꺼냈을 때 방문표시한다.
    # => 원래는 생략이며, 여러 시작좌표는 방문체킹은 이미 진입전에 했다?!
    stack = []
    stack.append((row, col))

    routes = []
    counter = 0
    ## dfs에서의 stack은, [배열순회하며 append시점에서 직전과 비교]가 없이,
    ## => 쌓아두고 종착역이면 pop해서 경로를 저장하기 위해 쓴다.?!
    ##    방문경로가 필요없다면, peek 확인도 안하고 pop해서 다음node를 탐색하면 된다.
    while stack:
        c_row, c_col = stack[-1]
        ## stack의 dfs 종착역 검사는 반복문 진입하자마자 한다.
        ## -> 종착역일 때, pop을 해서, routes에 방문경로를 저장후 continue로 다음으로 넘어간다
        ##    stack에아직 존재함에도 다음node가 없으면, continue를 통해, stack에 존재하는 node로 넘어간다
        if visited[c_row][c_col]:
            ## 방문경로 저장은, 오로지 1개의 경로만 생길 때 한다. 여기선..?
            routes.append(stack.pop())
            continue

        ## 자신의 처리
        ## -> stack은 자신의처리에서 [방문체크 -> 방문표시]를 한다. [방문체크만 append전에 해서, node중복 append는 허용해도 방문node는 배제한다.]
        ##  방문체크를 append로 넣기전에도 하지만, 중복으로 들어간node들이 있기 때문에, 이미 1번 나와서 방문표시된 것은 피한다.
        ## => 종착역으로서 이미 했다.
        visited[c_row][c_col] = True
        ## 자신의 처리에서 카운팅을 1개씩 한다?
        counter += 1

        ## 자식node들 탐색하여 stack에 쌓아주기
        for d_row, d_col in DELTA:
            n_row, n_col = c_row + d_row, c_col + d_col
            # 좌표 검사 / 색 검사
            if not (0 <= n_row <= n - 1) or not (0 <= n_col <= m - 1): continue
            if images[n_row][n_col] != images[c_row][c_col]: continue
            stack.append((n_row, n_col))

    ## break가 없으므로 남은 처리는 안해줘도 된다.
    ## 최종경로가 1개이면 방문node 저장의 의미가 있지만, 아니라면 없다?!
    # print(routes)
    # [(0, 0)]

    # [(0, 1), (1, 1), (0, 1)]

    # [(0, 2)]

    # [(1, 0)]

    # [(1, 2)]
    return counter

if __name__ == '__main__':
    ## floddfill: https://chaelinyeo.github.io/%EC%BD%94%ED%85%8C/Level03FloodFill/
    ## dfs-stack으로 풀이
    n, m = map(int, input().split())
    images = []
    for _ in range(int(input().strip())):
        row = list(map(int, input().split()))
        images.append(row)

    ## (1) 끊기는 좌표탐색은 global visited와 시작좌표 순회를 한다.
    visited = [[False] * m for _ in range(n)]
    DELTA = ((-1, 0), (1, 0), (0, -1), (0, 1),)

    total_count = []
    for row in range(len(images)):
        for col in range(len(images[row])):
            if visited[row][col]: continue
            total_count.append(dfs(images, visited, row, col))

    print(total_count)
    print(len(total_count))
    # [1, 2, 1, 1, 1]
    # 5

