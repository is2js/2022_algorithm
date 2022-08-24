import sys

input = sys.stdin.readline

if __name__ == '__main__':
    N, M = map(int, input().split())
    INF = float('inf')

    # a->b가 아닌 최단경로 a->k->b는 플로이드워셜로 풀어야한다.
    # -> 2차원 인접행렬이면서, INF초기화 + 자기자신으로 가는 것은 0으로 초기화
    distance = [[INF] * (N + 1) for _ in range(N + 1)]
    for row in range(len(distance)):
        for col in range(len(distance)):
            if row == col: distance[row][col] = 0
    for _ in range(M):
        u, v = map(int, input().split())
        # 양방향시 입력 조심
        distance[u][v] = distance[v][u] =  1 # 가중치가 없거나 같을 경우 1

    X, K = map(int, input().split())
    # a->b를 도는데, 가장바깥에서 거쳐가는 경로 k를 돌린다.
    # 여기서 자기자신으로 가는 것은 건너띈다.
    # => Da,b = min( Da,b , Da,k + Dk,b)로 k를 거쳐갔을 때 최단경로이면 업데이트한다.
    for k in range(1, N+1):
        for a in range(1, N+1):
            for b in range(1, N+1):
                if a == b: continue
                distance[a][b] = min(distance[a][b], distance[a][k] + distance[k][b])

    # one_to_k = distance[1][K]
    # k_to_x = distance[K][X]
    # if one_to_k == INF or k_to_x == INF:
    #     print('-1')
    # else:
    #     print(one_to_k + k_to_x)
    #inf도 덧셈 됨. -> 합에서 큰 수(INF)포함 여부는, INF보다 크거나 같은지로 비교한다!
    destination_distance = distance[1][K] + distance[K][X]
    print(destination_distance if destination_distance < INF else -1)







    pass
