import sys

input = sys.stdin.readline


# def dfs(x):
#     global visited, parent_table
#     visited[x] = True
#
#     for y in graph[x]:
#         if visited[y]: continue
#         parent_table[y] = x
#         dfs(y)


if __name__ == '__main__':
    ## LCA dfs없는 기본 문제: 촌수계산 : https://www.acmicpc.net/problem/2644
    # graph문제에서는 인접행렬에 담아두고 root depth 0으로 시작해, dfs로 돌면서 자식 등장시마다 parent_table에 기록하여 촌수를 확인하였다.

    ## 내풀이 => x, y 중 x를 root node라 치고, dfs탐색하여, y의 등반횟수를 세서 촌수를 구했다.
    # -> 그러나 문제에서 주어진 것은 부모x, 자식y로서 방향성의 tree이므로,
    # =>  이 방법으로는 x위쪽에서 더 연결될 경우를 처리 못한다.
    # => x가 root node라는 보장이 없으므로 graph방식으로는 풀 수 없다.
    # => root node를 모를 때는 dfs로 parent_table을 채울 수 없다!!!!!!!!!!!!!!

    # N = int(input().strip())
    # x, y = map(int, input().split())
    #
    # M = int(input().strip())
    #
    # graph = [[] for _ in range(N + 1)]
    # for _ in range(M):
    #     parent, child = map(int, input().split())
    #     graph[parent].append(child)
    #     # graph[child].append(parent)
    #
    # visited = [False] * (N + 1)
    # parent_table = [i for i in range(N + 1)]
    #
    # dfs(x)
    # count = 0
    # while x != y and count < N - 1:
    #     y = parent_table[y]
    #     count += 1
    #
    # if count == N - 1:
    #     print(-1)
    # else:
    #     print(count)

    ## 내풀이 => x, y 중 x를 root node라 치고, dfs탐색하여, y의 등반횟수를 세서 촌수를 구했다.
    # -> 그러나 문제에서 주어진 것은 부모x, 자식y로서 방향성의 tree이므로,
    # =>  이 방법으로는 x위쪽에서 더 연결될 경우를 처리 못한다.
    # => x가 root node라는 보장이 없으므로 graph방식으로는 풀 수 없다.
    # => root node를 모를 때는 dfs로 parent_table을 채울 수 없다!!!!!!!!!!!!!!

    ## 풀이: https://www.acmicpc.net/problem/2644
    # => root node를 모르지만, parent_table정보 자체가 주어진다 [부모, 자식]
    N = int(input().strip())
    x, y = map(int, input().split())

    M = int(input().strip())

    parent_table = [i for i in range(N + 1)]
    for _ in range(M):
        parent, child = map(int, input().split())
        parent_table[child] = parent

    # => 2 node에서 동시에 타고 올라가면 안된다(depth보장이 없다)
    # => 각 node가 타고 올라가면서, 조상들을 모아놓고, 같은 조상이 있다면, 만나는 것이다.
    x_ancestors, y_ancestors = [], []

    # => 추가적으로 찾은 공통 조상까지의 거리를 거기서 index, index로 찾아 더하는 것보다는
    # => 부모들을 모을 때, 거리까지 튜플로 같이 lst에 기억해놓는다.
    # 자기자신이 부모라면, 거기가 마지막 조상이다.
    # => 올라가는 것만 넣을 게 아니라, (자기자신, 0)도 포함시켜야, 등반안하는 경우도 처리가 된다.
    # distance = 1
    distance = 0
    while x != parent_table[x]:
        x_ancestors.append((x, distance))

        distance += 1
        x = parent_table[x]
    # => 다음 것을 append하는 것이 아니라, 현재의 것을 append한다면, 탈출조건시 포함되는 것은, 따로 넣어줘야한다.
    x_ancestors.append((x, distance))


    distance = 0
    while y != parent_table[y]:
        y_ancestors.append((y, distance))

        distance += 1
        y = parent_table[y]

    y_ancestors.append((y, distance))


    # => 2개의 배열을 탐색하기 위해, 2중for문으로 걸어놓고, 같은 것이 있는지 확인한다
    # for x, dx in x_ancestors:
    #     for y, dy in y_ancestors:
    #         if x == y:
    #             print(dx + dy)
    #             break
    # else:
    #     print(-1)

    # => python에서 flag처리를 else로 하려면, 이중 포문은 되고, 1개의 for문 + if break에서 처리된다.
    # => 2중 포문이라도, 1개 for문에 먼저 플래그를 걸 수 있으면 걸어놓고 진입하자.
    for x, dx in x_ancestors:
        if x in [y for y, dy in y_ancestors]:
            for y, dy in y_ancestors:
                if x == y:
                    print(dx + dy)
            break
    else:
        print(-1)






