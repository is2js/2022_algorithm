import sys

input = sys.stdin.readline

if __name__ == '__main__':
    # 플로이드 워셜 최단경로 알고리즘 : 모든 정점 -> 다른 모든 정점 최단경로 구하기(2차원행렬 3중반복문 업데이트)
    # Dab = min(Dab, Dak + Dkb)
    # -> 거쳐가는 경로 k를 반복문으로 돌면서,
    # -> [인접행렬 겸 distance 2차원 테이블]을 node->b의 모든 경로를 돌면서 최소비용으로 업뎃하는 3중 반복문

    INF = float('inf')
    V, E = int(input().strip()), int(input().strip())

    # 다익스트라의 빈행렬의 인접행렬과 달리, 가중치를 업뎃해서 기록하는 2차원행렬로 graph인접행렬 초기화
    # (1) INF로 초기화한다 (2) 자신에서 자신으로는 0으로 초기화한다.
    graph = [[INF] * (V + 1) for _ in range(V + 1)]
    for u in range(1, V + 1):
        for v in range(1, V + 1):
            if u != v: continue
            graph[u][v] = 0

    for _ in range(E):  # 간선정보를 인접행렬에 입력
        u, v, cost = map(int, input().split())
        # 바로 대입하면 좋겠지만, 간선정보에 중복되는 간선인데 cost만 다른 경우가 있어서, 기존 비용보다 작을 때 할당
        # -> 기존 집용은 앵간하면 INF로 초기화되어있지만, 간선정보에서 똑같은 경로지만 cost가 다른 경우가 존재
        if cost < graph[u][v]:
            graph[u][v] = cost

    # 1번node부터 거쳐가는 경로 k로 생각하며, node -> b  vs   node-> k ->b를 구한다.
    for k in range(1, V + 1):
        for u in range(1, V + 1):
            for v in range(1, V + 1):
                # 자가지신에게 가는 경로는 업뎃안한다(0)
                if u == v: continue
                # Dab = min(Dab, Dak + Dkb)
                graph[u][v] = min(graph[u][v], graph[u][k] + graph[k][v])

    # 모든 first -> v를 출력한다. 경로가 없어 업뎃안되는 INF는 문자열 0으로 출력한다.
    for u in range(1, V + 1):
        for v in range(1, V + 1):
            cost = graph[u][v]
            print(cost if cost != INF else "0", end=" ")
        print()