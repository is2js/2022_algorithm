import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## 플로이드 워셜 알고리즘즘
    #  다익스트라 -> 1개의 시작정점에서 모든 정점까지의 최단경로
    #  플로이드 워셜 -> 모든 정점에서 다른 모든 정점까지의 최단경로

    # 공통점: 단계별 거쳐가는 노드 기준 알고리즘 수행 -> 다익스트라와 동일
    # 차이점: 매 단계마다 방문하지않느 노드 중 최소비용 노드 찾는 과정이 없음
    # -> 2차원 테이블에 비용 기록함
    # -> 점화식으로 2차원 테이블을 갱신, 3중 반복문
    # -> 다익스트라보다는 쉬운 편 O(N**3)이라서, node갯수 적을때 가능.

    ## 점화식
    # Dab = min(Dab, Dak + Dkb)
    # -> 각 단계마다 특정노드 k를 거쳐가는 경우를 확인한다.
    # -> start to b 비용 vs start to k to b 비용 비교
    # 2차원 테이블: 행은 출발node 열은 도착node를 의미함.(인접행렬로 초기화)
    # (1) 이중반복문으로 Dab를 구하되
    # (2) 현재k에 대해 반복문을 돌려, Dak+Dkb를 구해 갱신하는 3중 반복문

    ## boj 11404: https://www.acmicpc.net/problem/11404
    INF = float('inf')

    n = int(input().strip())  # start 갯수
    m = int(input().strip())  # edge 갯수
    # graph 인접행렬을 INF로 초기화 -> 자기자신으로 가는 것은 weight(cost) 0 -> 간선정보(weight, cost)를 입력함
    # graph = [[INF for row in range(n + 1)] for row in range(n + 1)]
    graph = [[INF] * (n+1) for _ in range(n + 1)] # 1차 배열은 [값] * x의 얕은복사로 생성간으
    for a in range(1, n + 1):  # 0번째 행, 0번째 열은 node없음이니까 무시하고, 1번부터 논다.
        for b in range(1, n + 1):
            if a != b: continue
            graph[a][b] = 0

    # graph 간선정보 입력
    for _ in range(m):
        u, v, weight = map(int, input().split())
        # graph[first][second] = weight
        # 요구사항) 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.
        # -> 같은 간선경로인데, weight가 다른 게 중복해서 들어오므로,더 작은 것만 입력되게 하기
        if weight < graph[u][v]:
            graph[u][v] = weight

    # 반복문으로 거쳐갈 k node를 돌면서, 모든 start, b node를 이중반복문을 통해 업데이트한다.
    # Da,b = min( Da,b  Da,b + Dk,b) -> for k    for start for b
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                if a == b: continue  # 경로 계산할 때, 자신경로는 업뎃하지 않는다(0으로 초기화된 상태)
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    # 모든정점 -> 다른 모든 정점에 대한 최소비용이 업데이트된 인접행렬 출력
    # 0을 무시하고 1번node부터 출력, INF값이라면, 경로가 없는 것인데 0으로 출력
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][b] == INF:
                print("0", end=" ")
                continue
            print(graph[a][b], end=" ")
        print()
