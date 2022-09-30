import sys

input = sys.stdin.readline

import heapq


def dijkstra(graph, srt_node):
    distance = [float('inf')] * (n + 1)

    distance[srt_node] = 0
    pq = []
    heapq.heappush(pq, (0, srt_node))

    while pq:
        curr_cost, curr_node = heapq.heappop(pq)

        for next_node, next_cost in graph[curr_node]:
            if distance[curr_node] + next_cost > distance[next_node]: continue
            distance[next_node] = distance[curr_node] + next_cost
            heapq.heappush(pq, (distance[next_node], next_node))

    return distance


# def dfs(graph, visisted, node, result):
#
#     temp_result = dijkstra(graph, s)
#
#     if a in graph[node] or b in graph[node] or not graph[node]:
#         return result + temp_result
#
#     next_node, next_cost = graph[node]
#
#     pass


if __name__ == '__main__':
    ## 합승택시요금: https://school.programmers.co.kr/learn/courses/30/lessons/72413
    ## -> 문제는 합승을 내리는 지점을 어디로 잡을찌다.
    n, s, a, b = map(int, input().split())
    fares = []
    for _ in range(9):
        fares.append(list(map(int, input().split())))

    graph = [[] for _ in range(n + 1)]
    for fare in fares:
        u, v, cost = fare
        graph[u].append((v, cost))
        graph[v].append((u, cost))

    not_transfer_fare = dijkstra(graph, s)[a] + dijkstra(graph, s)[b]

    ## 합승은, a or b로 가는 다음역이 직접적인 길이 있는 경우, 거기까지 가서 깨진다
    ## => 합승끝나는 곳까지의 탐색이 힘듦.
    # dfs(graph, 0 | (1<<0), s, 0)

