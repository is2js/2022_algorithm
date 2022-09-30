import sys
from collections import deque

input = sys.stdin.readline


def bfs(N):
    ## 재방문 허용시,
    # (1) 방문표시 : visited에는 0(F)으로 초기화 -> +=1 로 방문표시
    # (2) 방문체크 : (방문했었다면==dist에기록된상태)재방문방지하되 [최단거리만 허용]
    #               -> 재방문 방지하되 [and 최단거리 아닌경우]만 continue로 skip
    # (3) 최단거리저장: tuple의 curr거리 vs next에 기록된 최단거리를 비교해아므로
    #                 최단거리는 시작좌표 0부터 시작하므로, [-1 or INF]로 초기화 -> 시작좌표or자기자신은 0으로 초기화

    dist = [float('inf')] * (100_000 + 1)
    dist[N] = 0
    visited = [0] * (100_000 + 1)
    visited[N] += 1
    q = deque([])
    q.append((N, 0))

    while q:
        # 좌표1개라면 curr
        curr, cost = q.popleft()

        # print(curr, cost)

        ## DELTA가 dx로의 이동만 존재하는 경우가 아니라면, 직접 delta를 만들어서 자식들을 돌려준다.
        for next in (curr - 1, curr + 1, curr * 2):
            if not (0 <= next <= 100_000): continue
            # if visited[next]: continue
            ## 3. 재방문은 기본적으로 허용하지 않지만,
            #     최단거리(next의 cost == curr cost +1)의 재방문만 허용하기 위해서는,
            #   => 최단거리가 아닌 재방문만 skip한다.
            #   => 재방문인데 && 최단거리가 아닌 경우
            #   => 그러려면, next는 이미 방문했으며, 그 cost(최단거리)가 기록되어있어야한다.
            #   => 방문했으면 continue인데, 최단거리인 경우만 허용
            #   => [1개만 조건 추가로 허용해준다면, 반대조건을 and]로 걸어준다.
            if visited[next] and dist[next] != (cost + 1): continue
            # (next는 방문안했거나 or 최단거리이거나 or 방문했으면서 최단거리 상황)
            visited[next] += 1
            dist[next] = cost + 1
            q.append((next, cost + 1))
    else:
        return visited[K], dist[K]


if __name__ == '__main__':
    ## https://www.acmicpc.net/problem/12851
    N, K = map(int, input().split())

    ## 1. 좌표탐색에는 장애물이 없는 한, board가 필요없다. visited면 충분하다.
    visit, dist = bfs(N)
    print(dist, visit, sep='\n')
    pass
