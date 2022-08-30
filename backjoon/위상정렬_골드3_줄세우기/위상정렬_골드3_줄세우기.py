import sys 
 
input = sys.stdin.readline 
 
 
if __name__ == '__main__':
    # 백준 : 줄세우기: https://www.acmicpc.net/problem/2252
    # -> 위상정렬은 싸이클이 없는 방향그래프의 줄세우기인데,
    # -> 키 순서 -> 방향성으로 생각해야하고, 출발부터 줄세우려면, 1 3은 1 ->3으로 해석되어야한다.
    N, M = map(int, input().split())

    graph = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)

    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        indegree[v] += 1

    from collections import deque

    q = deque()

    for node in range(1, N + 1):
        if indegree[node] == 0:
            q.append(node)

    result = []
    while q:
        curr = q.popleft()
        result.append(curr)

        for next in graph[curr]:
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)

    print(*result)
