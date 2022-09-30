import heapq
import sys

input = sys.stdin.readline


def dijkstra(graph, node, next):
    distance = [float('inf') for _ in range(n)]
    distance[node] = 0
    pq = []
    heapq.heappush(pq, (0, node))

    while pq:
        cost, curr = heapq.heappop(pq)

        for next, cost in graph[curr]:
            if distance[node] + cost >= distance[next]: continue
            distance[next] = distance[node] + cost
            heapq.heappush(pq, (distance[next], next))

    return distance[next]




def dfs(node, end, is_trapped, distance):
    global result
    if node == end:
        # print(node, distance)
        result = distance
        return

    visited[node] = True
    # print(node)

    temp_graph = graph if not is_trapped else r_graph
    for next, cost in temp_graph[node]:
        if visited[next]: continue
        dijkstra_to_next = dijkstra(temp_graph, node, next)
        if next + 1 in traps:
            is_trapped = not is_trapped
        dfs(next, end, is_trapped, distance + dijkstra_to_next)


if __name__ == '__main__':
    ## 미로탈출:https://school.programmers.co.kr/learn/courses/30/lessons/81304
    n, start, end = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(2)]
    traps = [int(input().strip())]

    ## trap 만나는 순간, 상태가 바뀐체로 진행되어야하므로 dfs -stack을 이용한다?!
    ## trap 만나는 순간, 역방향 graph가 있어야하므로, 방향유무는 is_traped / graph는 2개로 저장하자.
    # => 최소시간이면서 cost가 1이 아니므로 => 다익스트라..?
    # => 플로이드워셜은 정해진 길에 대해서만..=> 다익스트라는 매번.. 시작정점에 대해 모든..

    # 0번부터 쓰기
    graph = [[] for _ in range(n)]
    r_graph = [[] for _ in range(n)]
    for P, Q, cost in roads:
        graph[P - 1].append((Q - 1, cost))
        r_graph[Q - 1].append((P - 1, cost))
    # print(graph)
    # print(r_graph)
    visited = [False for _ in range(n)]
    result = 0
    dfs(start - 1, end - 1, False, 0)
    print(result)
