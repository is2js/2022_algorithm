import sys
INF = sys.maxsize
input = sys.stdin.readline

n, m = int(input()), int(input())
dis = [[INF]*n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    if c < dis[a-1][b-1]:
        dis[a-1][b-1] = c
for k in range(n):
    for a in range(n):
        for b in range(n):
            if a != b:
                dis[a][b] = min(dis[a][b], dis[a][k]+dis[k][b])
for i in range(n):
    for j in range(n):
        if dis[i][j] == INF:
            dis[i][j] = 0
for t in dis:
    print(*t)