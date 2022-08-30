import sys

input = sys.stdin.readline


def union(a, b):
    pa = parent_table[a]
    pb = parent_table[b]
    if a < b:
        parent_table[pb] = pa
    else:
        parent_table[pa] = pb


def find_parent(a):
    if a == parent_table[a]:
        return a

    root = find_parent(parent_table[a])
    parent_table[a] = root
    return root


def process():
    method, a, b = map(int, input().split())
    if method == 0:
        union(a, b)
        return

    is_same_parent = find_parent(a) == find_parent(b)
    print(f"{'YES' if is_same_parent else 'NO'}")


if __name__ == '__main__':
    ## 집합의 표현: https://www.acmicpc.net/problem/1717
    N, M = map(int, input().split())
    parent_table = [i for i in range(N + 1)]

    for _ in range(M):
        process()

