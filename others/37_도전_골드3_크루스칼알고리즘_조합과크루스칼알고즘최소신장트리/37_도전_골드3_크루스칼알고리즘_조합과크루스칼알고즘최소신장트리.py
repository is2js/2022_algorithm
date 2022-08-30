import math
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## 백준 1774: https://www.acmicpc.net/problem/1774
    # 풀이: https://velog.io/@smkim104/BOJ-1774-%EC%9A%B0%EC%A3%BC%EC%8B%A0%EA%B3%BC%EC%9D%98-%EA%B5%90%EA%B0%90Python-%EC%B5%9C%EC%86%8C%EC%8B%A0%EC%9E%A5%ED%8A%B8%EB%A6%AC-%ED%81%AC%EB%A3%A8%EC%8A%A4%EC%B9%BC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
    N, M = map(int, input().split())
    ## node가 좌표라면, index를 node에 매핑시킨, 좌표상태배열이 존재해야한다.
    sins = [(0, 0)]
    for _ in range(N):
        row, col = map(int, input().split())
        sins.append((row, col))
    # print(sins)
    ######## combination NC2시, cost를 계산하는데, 이미 연결중인지를 판단이 필요하다
    # -> graph(인접행렬)로 만들어놓는다. 좌표가 아니라 몇번 node끼리 연결인지만 필요하다 (연결여부만 판단)
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, input().split())
        ### 최소 비용cost인데, cost없이 이미 연결되었다면, 0을 cost로 가져야할 것이다.
        ### => 연결안된 것의 여부는 빈행렬에 아무것도 없는 len == 0을 판단으로 하면 된다.
        graph[u].append((0, v))
        graph[v].append((0, u))

    # 최소신장트리를 만드려면, N-1개이상의 간선정보가 필요하다.
    # -> 좌표node에는 서로의 cost가 내포되어있으니, NC2씩 짝지으면서, cost를 통한 edge정보를 추출해야한다.
    # -> 그리고, 그 중에 M에 포함된 것은 이미 최소신장트리 구성에 포함시켜야하므로 제외시켜야한다.
    numbers = list(range(1, N + 1))
    edge_set = list()  # .sort()써서 cost오름차순하려면 set안됨. 튜플안됨. list여야한다.


    def solve(prev_cnt, prev_position, prev_result):
        if prev_cnt == 2:
            # 이미 연결되었는지 정보가 필요하다... => 인접행렬 with 0,1
            # -> 양방향으로 넣어놨으니, 한쪽만 검사해도 된다.
            # 연결되어있따면 cost를 0으로 넣는다.
            first = prev_result[0]
            second = prev_result[1]
            for cost, v in graph[first]:
                if v == second:
                    edge_set.append((cost, first, second))
                    return
            # 연결안되어있다면. node번호 -> 좌표로 치환해서 거리를 계산해서 cost로 만들어 넣어줘야한다.
            first_xy, second_xy = sins[first], sins[second]
            cost = math.sqrt(math.pow(first_xy[0] - second_xy[0], 2) + math.pow(first_xy[1] - second_xy[1], 2))
            edge_set.append((cost, first, second))

            # edge_set.append(selected_tuple)
            return
        if prev_position == N:
            return

        solve(prev_cnt + 1, prev_position + 1, tuple(prev_result + (numbers[prev_position],)))
        solve(prev_cnt, prev_position + 1, tuple(prev_result))
        return


    # solve(prev_cnt, prev_position, selected_tuple)
    solve(0, 0, ())
    # print(combination_set)
    # except_edges = set()
    # for _ in range(M):
    #     edge = tuple(map(int, input().split()))
    #     edge.sort()
    #     except_edges.add((row, col))

    ####### => 이미 연결된 것은 cost를 0으로 주면, 먼저 선택되고 && 거리에 계산도안된다!!
    ######     직접 조합에서 빼줄 필요가 없다.
    # print(edge_set)

    ### union, find를 통해, MST(최소신장트리)를 구성하려면 parent_table
    parent_table = [0] + [i for i in range(1, N + 1)]

    edge_set.sort()


    def find_parent(parent_table, node):
        if node == parent_table[node]:
            return node

        parent_table[node] = find_parent(parent_table, parent_table[node])
        return parent_table[node]


    def union(parent_table, first, second):
        first_parent = find_parent(parent_table, first)
        second_parent = find_parent(parent_table, second)
        # 무작위로 한 곳을 반영해도 되지만, 자식node(index)가 작은 곳을 root node로 취급해준다.
        if first < second:
            parent_table[second_parent] = first_parent
            return
        parent_table[first_parent] = second_parent
        return

    # print(edge_set)
    result_edges = []
    mst_cost = 0
    for edge in edge_set:
        cost, a, b = edge
        # (5) 싸이클 발생시키는 같은 집합 node들끼리의 간선이면 건너띈다.
        if find_parent(parent_table, a) == find_parent(parent_table, b):
            # print(node, b)
            # print(parent_table)
            continue

        # print(parent_table)
        union(parent_table, a, b)
        result_edges.append((cost, a, b))
        mst_cost += cost

    # print(parent_table)
    # print(mst_cost, result_edges)
    print(f"{mst_cost:.2f}")


