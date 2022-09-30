import sys

input = sys.stdin.readline


def floyd(distance, n):
    # (4) 경유지 k부터 node들을 순회하면서 k->u->v의 3중 for문을 이용해서 distance를 업데이트해준다.
    # => 경유한 거리u->k->v  vs u->v직전까지의 최단거리 비교해서 더 작은 것으로 업뎃해준다.
    for k in range(n + 1):
        for u in range(n + 1):
            for v in range(n + 1):
                if distance[u][k] + distance[k][v] < distance[u][v]:
                    distance[u][v] = distance[u][k] + distance[k][v]


    return distance


if __name__ == '__main__':
    ## 합승택시요금: https://school.programmers.co.kr/learn/courses/30/lessons/72413
    n, s, a, b = map(int, input().split())
    fares = []
    for _ in range(9):
        fares.append(list(map(int, input().split())))

    ## 정점들을 완전탐색하며, 해당정점 ->a ,->b까지의 최소비용을 구해야한다
    ## => a->b 모든 정점들에 대한 최단거리는 플로이드워셜을 사용한다.
    ## => 1가지 경우의 수는 for문 순회로 해결한다.

    # (1) 다익스트라와 다르게 2차원 distance배열에 node별(1차원) -> node(2차원)의  기록이다.
    # => 최단거리문제는 다익스트라도 INF초기화 -> 자기자신은 0으로 기록한다.
    INF = float('inf')
    distance = [[INF] * (n + 1) for _ in range(n + 1)]
    # 정사각행렬의 row == col 원소들에 접근한다면, 1줄이므로 반복문 1개로 접근할 수 있다.
    for i in range(n + 1):
        distance[i][i] = 0

    # (2) graph대신 distance를 채워서 활용한다.
    for u, v, cost in fares:
        distance[u][v] = cost
        distance[v][u] = cost

    # (3) floyd(distance, node갯수)를 받아서 distance를 채운 것을 반환해준다.
    distance = floyd(distance, n)
    # print(distance)

    ## 합승종료 지점을 완전탐색하며, 최소비용을 구해주면 된다.
    min_fare = INF
    for k in range(1, n + 1):
        min_fare = min(min_fare, distance[s][k] + distance[k][a]  + distance[k][b])

    print(min_fare)
