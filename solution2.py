

import sys
from collections import deque

input = sys.stdin.readline


def bfs(delivery, pick, complete_count, src, tb, distance):
    cnt = 0
    q = deque([(src, tb, distance)])

    while q:
        c_node, c_tb, c_dist = q.popleft()
        c_cap = CAP - c_tb
        if  cnt == complete_count:
            return c_dist

        for k in range(-n, n + 1):
            n_node = c_node + k
            if not ( 0<=n_node<=n): continue

            if not delivery[n_node] and not pick[n_node]: continue
            if not c_cap: continue
            for t in range(0, c_tb + 1):
                if c_cap < t: continue
                delivery[n_node] -= t
                c_cap += t
                for p in range(0, pick[n_node] + 1):
                    if c_cap < p:continue
                    pick[n_node] -= p
                    c_cap += p








def permutate(complete_count, src):
    global MinDistance


    for k in range(1, cap + 1):
        distance = bfs(delivery=list(DELIVERY), pick=list(PICK), complete_count=complete_count, src=src, tb=k, distance=0)
        MinDistance = min(MinDistance, distance)


if __name__ == '__main__':
    DELIVERY = []
    PICK = []
    TB = []
    MinDistance = float('inf')
    CAP = 0

    cap, n = map(int, input().split())
    deliveries = list(map(int, input().split()))
    pickups = list(map(int, input().split()))

    global DELIVERY, PICK, TB, CAP

    total_count = sum(deliveries)

    DELIVERY = deliveries = [0] + deliveries
    PICK = pickups = [0] + pickups
    TB = takbaes = [total_count] + [0] * n
    CAP = cap

    permutate(complete_count=total_count, src=0)
