import sys

input = sys.stdin.readline


def floyd(distance, n):
    ## (1-3) 2차원distance를 3중for문(k경유지 + u출발점 + v도착점)으로 플로이드워셜을 구현한다.
    ## 경유지k -> 출발점u -> 도착점v 순으로 돈다
    for k in range(n + 1):
        for u in range(n + 1):
            for v in range(n + 1):
                ## u -> v까지 갈 때, k를 경유해서 가는 경우 vs u ->v보다 작으면 업뎃
                ## u->v의 최단거리를 k를 경유해서 가는 비용으로 업뎃해준다
                if distance[u][k] + distance[k][v] < distance[u][v]:
                    distance[u][v] = distance[u][k] + distance[k][v]
    ## => 3중for문이 끝나고 나면, 경유지k를 고려한 최단비용이 업뎃된 상태다
    return distance


if __name__ == '__main__':
    ## 합승택시요금: https://school.programmers.co.kr/learn/courses/30/lessons/72413
    n, s, a, b = map(int, input().split())
    fares = []
    for _ in range(9):
        fares.append(list(map(int, input().split())))

    #### 개념
    # 어느지점까지 합승할지가 관건이다.
    # 합승지점이 정해진다면 -> 그 지점에서 a, b로 가는 최단경로를 더해야하므로
    # => 각각을 다익스트라 하는게 아니라, 미리 모든 지점에서 -> 모든 지점으로의 최단경로,
    # => 플로이드워셜을 써야한다.
    # => 합승도착지점은 완전탐색해서 지정될 수 밖에 없다 1이 합승종료지점일때, 5가 합승종료지점일 때...
    # => 각 합승종료지점으로서 순회하면서, min greedy탐색하면 된다

    ## (1) 플로이드워셜을 이용해서, 2차원distance 각지점 -> 모든 지점의 최단거리 기록 table생성
    ## 충분히 큰 dist는  (node갯수*2*가장큰요금)으로 해주면 된다.
    INF = (200 * 100_000) * 2
    ## (1-1) visited + graph를 대신하는 2차원 distance를 INF로 초기화하고, 자기자신으로 갈 때 0으로 초기화한다.
    distance = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        distance[i][i] = 0

    ## (1-2) 주어진 graph정보로 distance를 채운다.
    for u, v, cost in fares:
        distance[u][v] = cost
        distance[v][u] = cost

    ## (1-3) floyd메서드를 distance, node의 갯수를 입력받아 구현한다.
    distance = floyd(distance, n)


    def floyd(distance, n):
        ## (1-3) 2차원distance를 3중for문(k경유지 + u출발점 + v도착점)으로 플로이드워셜을 구현한다.
        ## 경유지k -> 출발점u -> 도착점v 순으로 돈다
        for k in range(n + 1):
            for u in range(n + 1):
                for v in range(n + 1):
                    ## u -> v까지 갈 때, k를 경유해서 가는 경우 vs u ->v보다 작으면 업뎃
                    ## u->v의 최단거리를 k를 경유해서 가는 비용으로 업뎃해준다
                    if distance[u][k] + distance[k][v] < distance[u][v]:
                        distance[u][v] = distance[u][k] + distance[k][v]
        ## => 3중for문이 끝나고 나면, 경유지k를 고려한 최단비용이 업뎃된 상태다
        return distance

    #### (2)이제 강제로 경유지k를 합승종료지점으로 지정해서, k->a, k->b로의 최단비용을 합산하여
    ####    min greedy를 구한다.
    answer = INF
    ## 실제 경유지는 없는 0은 빼줘야한다.
    for k in range(1, n+1):
        answer = min(answer, distance[s][k] + distance[k][a] + distance[k][b])

    print(answer)