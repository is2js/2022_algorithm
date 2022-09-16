import sys

sys.setrecursionlimit(100_000) # 너무 많이 풀면 메모리초과가 자동으로 뜸.
input = sys.stdin.readline

if __name__ == '__main__':
    ## LCA(Lowest Common Ancestor): 최소 공통 조상
    # 백준: LCA https://www.acmicpc.net/problem/11437
    # -> 2 node의 가장 가까운 공통 조상이 몇번인지 출력한다
    # -> N 5만, M 1만 -> O(NM)으로 설계해도 통과한다고 한다.
    # 최소 공통 조상 알고리즘
    # (1) 모든 node마다 depth를 계산한다 by dfs
    # (2) LCA(최소 공통 조상)을 찾을 2 node를 매번 확인한다.
    #    (2-1) 두 node의 깊이가 동일하도록 거슬러 올라간다
    #    (2-2) 이후에 부모가 같아질때까지, 반복적으로 부모방향으로 거슬러 올라간다
    # (3) 모든 LCA(a,b) 연산에 대해 2번을 반복한다.

    ## 예시 8과 15
    #                 1
    #                / \
    #              [2]   3      => (3) 부모가 같아질때까지 동시에 거슬러 올라간다.
    #             / |     | \
    #          [4]  [5]   6  7  => (2) depth가 같아진 순간부터, 동시에 거슬러 올라간다.
    #         / |  / |     | \
    #      [8]  9 10 [11]  12 13 => (1)2node 중 짧은 depth로 깊이를 맞춰준다.
    #              / |
    #            14 [15]

    ## 매 쿼리(M)마다 부모로 거슬러 올라가므로, 최악의 경우 O(N) -> O(NM)이 요구되는 코드다.
    # -> 첫째 줄에 노드의 개수 N이 주어지고, 다음 N-1개 줄에는 트리 상에서 연결된 두 정점이 주어진다.
    # -> 그 다음 줄에는 가장 가까운 공통 조상을 알고싶은 쌍의 개수 M이 주어지고, 다음 M개 줄에는 정점 쌍이 주어진다.
    N = int(input().strip())

    # (1) N -1개의 간선정보를 인접빈행렬에 기록한다.
    graph = [[] for _ in range(N + 1)]

    for _ in range(N - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # (2) LCA을 찾기위해서는 각 node별 depth를 기록해놓아야하며,
    #  -> depth는 재귀dfs(visited for 자식node들 중에 중복으로 탐색할 수도 있으니, node별 한번만 처리)로
    #     stack이 쌓일 때마다 +1씩 해줘야하니 재귀함수의 파라미터로 업뎃하며,
    #     depth기록용 배열 추가 후 기록해야한다.
    visited = [False] * (N + 1)
    depth_table = [False] * (N + 1)
    # (7) LCA 처리를 위해, x의 자식y탐색시, 부모를 기록할 parent_table도 준비한다.
    # -> 부모 테이블은, depth 맞추기 등, 기록해놓으면 [부모로 거슬러 올라갈 수 있다]
    parent_table = [False] * (N + 1)


    def dfs(x, depth):
        # (3) visited를 사용한 재귀는, 종착역 대신, 자식node탐색시 이미 필터링되어 더이상 탐색하지 않고 종료하게 된다.

        # (4) 자신의 처리에서 방문체크 + 현재 depth를 depth기록용 배열에 기록한다.
        visited[x] = True
        depth_table[x] = depth

        # (5) 항상 모든 경우의 자식node들을 꺼내고, 방문체킹을 한다.
        for y in graph[x]:
            if visited[y]: continue
            # (6) x와 그 자식들y의 depth를 기록하면서, 동시에 x->y로 자식들 꺼내 탐색할 때
            # ->  인접행렬에 접근할 때, 자식node로 진입하기 전에, 부모-자식관계도 parent_table에 기록해둔다.
            parent_table[y] = x
            # (7) 이미 방문체크 + 부모기록 했으면, 해당 자식y의 stack으로 넘어가면서 depth + 1로 업데이트하며 넘어간다.
            dfs(y, depth + 1)


    dfs(1, 0)  # root start, root depth


    # (10) LCA를 구하는 로직 정의
    def lca(a, b):
        # (10-1) 2 node의 depth를 맞출때까지 [깊은쪽을 부모로 거슬러 올라가기] while을 돌린다.
        # -> while = 탈출하는 순간 맞춰져있음.
        while depth_table[a] != depth_table[b]:
            # 더 깊은쪽을 부모로 거슬러 올라가게 한다.
            if depth_table[a] > depth_table[b]:
                a = parent_table[a]
            else:
                b = parent_table[b]
        # (10-2) depth가 같아진 2 node는, [동시에 부모가 같아질때까지(X) -> 동시에 같은 node가 될때까지 부모로 등산] while을 돌린다.
        # while parent_table[a] != parent_table[b]:
        while a != b:
            # 동시에 부모로 등산한다.
            a = parent_table[a]
            b = parent_table[b]

        # (10-3) 같아진 순간 최소 공통 조상으로 반환
        return a


    # (8) LCA를 알고 싶은 start 쌍의 갯수 입력받기
    M = int(input().strip())

    for _ in range(M):
        a, b = map(int, input().split())
        # (9) 쌍마다 바로 lca구하기 위해, lca정의하러 가기
        print(lca(a, b))

# https://www.youtube.com/watch?v=O895NbxirM8&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=16
