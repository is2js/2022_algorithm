import sys
import heapq as pq

input = sys.stdin.readline


def dijkstra(srt_node):
    distance[srt_node] = 0

    heap = []
    pq.heappush(heap, (0, srt_node))

    while heap:
        cost, curr_node = pq.heappop(heap)

        # 방문체킹 with 업뎃여부
        if distance[curr_node] < cost: continue

        for add_cost, next_node in graph[curr_node]:
            if distance[next_node] <= distance[curr_node] + add_cost: continue
            distance[next_node] = distance[curr_node] + add_cost
            pq.heappush(heap, (distance[next_node], next_node))



if __name__ == '__main__':
    # 문제: https://kom-story.tistory.com/173
    N, M, C = map(int, input().split())
    INF = float('inf')
    graph = [[] for _ in range(N + 1)]
    distance = [INF] * (N+1)
    for _ in range(M):
        X, Y, Z = map(int, input().split())
        graph[X].append((Z, Y))

    dijkstra(C)

    count = 0
    max_cost = float('-inf')
    for node, cost in enumerate(distance):
        if node <= 1: continue
        if cost == INF: continue
        count += 1
        max_cost = max(max_cost, cost)
    print(count, max_cost)


