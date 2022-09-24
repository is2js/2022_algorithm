import sys

sys.setrecursionlimit(100_000)  # 많이 풀면 메모리초과 뜬다.
input = sys.stdin.readline

if __name__ == '__main__':
    ##  개선된 LCA
    # => 기존 LCA는 2 node가 같아질떄까지 1칸 씩 부모로 등산하는데,
    #    최악의 경우 O(N)의 등산 시간복잡도가 발생한다.
    #    M개의 쌍을 lca한다면 O(M N)이 발생한다.

    ## 심화문제: https://www.acmicpc.net/problem/11438
    # N이 10^6, M이 10^6개 주어진다면, -> 1.5초라도 시간 제한에 걸린다.
    # -> 부모를 거슬러 올라가는 N을 lgN으로 만들어야한다.
    #   ex> 총 15칸 거슬러 올라가야한다고 계산이 된다면
    #       8칸 -> 4칸 -> 2칸 -> 1칸으로.. 15에 가까운 2^k승으로 간 뒤 나머지를 1칸씩 거슬러 올라가면 된다.
    # => 메모리를 더 사용(배열 추가?)하여 각 node에 대해 2^i번째 부모에 대한 정보를 각각 기록해놓는다.

    ## (1) 각 node에 대하여, 2^i번째 부모에 대한 정보를 배열로 기록하게 한다.
    # -> dfs로 자신의 부모를 입력하고, 그 정보를 이용해 dp로 2^i번째 부모도 모두 구할 수 있다.
    # ex> 1-2-5-11-15로 내려온다면, 1번째부모는 2^0 -> i=0번째 부모는 11
    #     2^1 -> i=1 번째 부모는 5
    #     2^2 -> i=2 번째 부모는 1 ( 3번째는 건너띄고 기록한다)
    # i = 0  1  2
    #    [11 5 1 ] => 모든 node에 대해 2^i번째 부모를 각각 배열로 기록하게 해야한다.
    #                 그렇다면 N개의 node에 대해 각각  N * lgN만큼의 메모리가 필요해진다.

    ## (2) 2 node의 depth를 맞추는 작업은 동일하나
    #     등산시, 2의제곱꼴로 빠르게 등산하게 한다.
    # => dp를 이용해 시간복잡도를 계산할 수 있다.
    # => O(M lgN)

    LOG = 20 + 1  # 2^i == 2^20 -> 1,000,000 데이터가 최대 100만개 M간선정보 들어올거라고 가정

    N = int(input().strip())  # node의 갯수
    # 간선 정보 N-1개 받기
    graph = [[] for _ in range(N + 1)]

    for _ in range(N - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # dfs재귀(모든node 1회 탐색)를 위한 visited 배열 / node별 depth기록 배열
    visited = [False] * (N + 1)
    depth_table = [False] * (N + 1)
    # (1) dfs자식탐색시, node별 부모(value) 기록 -> node별 2^i번째 부모들(배열)을 기록하기 위한 2차원 배열
    # -> 각 node별 2^i번째 부모를 0으로 초기화한다. max 2^LOG(20 + 1)개 == 10^6개(최대간선정보갯수)의 부모가 존재한다고 가정한다.
    # 각 node별 2^i번째 부모를 기록하는 배열이다.
    # -> 기본1차배열은 2^0번째 = 1번째 위 부모만 저장해서 1칸씩 타고 올라갔었음
    parent_table = [[0] * LOG for _ in range(N + 1)]


    # node별 depth기록(depth_table) 및 부모 기록(parent_table)을 위한 dfs탐색
    def dfs(x, depth):
        # visisted배열을 쓰는 순간, 알아서 뻗을 자식이 없어서 종착역으로서 종료 됨.
        # 자신의 처리 -> visited체크 후 depth 기록
        visited[x] = True
        depth_table[x] = depth

        # 자식들 탐색
        for y in graph[x]:
            # 자식은 꺼내고나서 방문체킹 후에야 -> 자식stack으로 들어간다.
            if visited[y]: continue
            # (2) 자식y에 대해서, 부모x는 2^0번째 부모이므로, 현재 parent_table[x][0]만 기록할 수 있다.
            parent_table[y][0] = x

            dfs(y, depth + 1)


    # (3) dfs(root start, depth = 0)의 탐색을 그냥 하지 않고 dp로 하여, 2^i번째 부모들을 배열에 채운다.
    # -> 전체 부모들을 저장하는 dp함수
    # => dfs를 main에 돌리지 않고, 메서드안에서 호출한다.
    def set_parent():
        # (3-1) dfs(root_node, depth=0)을 일단 돌려, parent_table[node마다][0]을 채워놓는다.
        dfs(1, 0)
        # (3-2) dfs -> 1번째 부모가 채워짐 -> 2^0번재 부모로서 각 node별 i=0번째가 채워져있다.
        # -> 모든 node별로 1개씩 i -1 => i부터 모든 node들이 다 채우게 해놓기 위해
        #    for i 별로 -> for 모든 node들을 다 i번째 부모를 채운다.
        for i in range(1, LOG):
            for node in range(1, N + 1):
                # (3-3) i번째부모는 i-1번째부모의 i-1번째부모
                # => 매핑 자체가 2^i승이기 때문에 부모(i-1)node의 부모(i)를 다음 부모(*2만큼 떨어진 부모)로 채워주면 된다.
                # i -> p[start][1] =>  p[ i-1  ][0] == p[  node의부모  ][0](1차부모)
                # i-1 -> p[  start  ][0]
                # start
                parent_table[node][i] = parent_table[parent_table[node][i - 1]][i - 1]


    # (4) 현재 2차원 배열인 parent_table이 채워진 상태로, lca를 정의한다.
    set_parent()
    # print(parent_table)


    # print(parent_table)

    # (5) LCA 알고리즘
    def lca(a, b):
        # (5-1) 원래는 depth가 같아질 때까지 while을 돌리며 깊은쪽을 부모로 등산했었지만
        # -> 이제는 1칸씩 등산을 안하기 때문에,
        # -> depth 깊은 쪽을 한쪽 변수[b]에 몰아놓는다.
        if depth_table[a] > depth_table[b]:
            a, b = b, a
        # (5-2) depth의 길이를 맞출 때, 그 depth차이보다 작거나 같은 2^k승의 k를 찾아서
        #     2^i부모배열을으로 한번에 건너띈다.
        #  -> 이 때, 2의 i승을 미리 정해둔 20부터 [큰 수]부터 내려와서, 작거나 같은 가장 큰수를 찾는다.
        # => i에 대해 2^i을 만드는 방법은 1 << left shift i 를 이용하면 된다.
        # => 배열인덱스를 2^i로 가정했다면, 인덱싱하기 전에 확인은 1<<i로 해서 맞으면 꺼내온다.
        # diff_of_depth = depth_table[b] - depth_table[a]
        for i in range(LOG - 1, 0 - 1, -1):
            ##### 조심 if 속 반복되는 코드 같길래, 지역변수로 뺐는데
            # => 반복문 속에서 b가 없데이트되는 동적인 값이다.
            # => 뺄라면 반복문 안에서 빼야하며, 아니라면 건들이면 안된다.
            if depth_table[b] - depth_table[a] >= (1 << i):
                # depth차이보다 같거나 작은 2^i승을 찾아내서
                # parent배열 속의 값을 이용하여 빠르게 건너띈다.
                # => 배열인덱스를 2^i로 가정했다면, 인덱싱하기 전에 확인은 1<<i로 해서 맞으면 꺼내온다.
                b = parent_table[b][i]
        # (5-3) 큰 수부터 처리해서 빠르게 등산했다.
        # ex> 13 => 8 -> 4 -> 1  3번만에 등산

        ## (6)depth가 맞쳐줬으면, 같은 값이 될때까지 동시에 등산한다.
        # -> 이 때도, parent배열을 이용한다.
        # (6-1) while로 돌린다면, a==b같아질때까지 돌려서, [같으면 애초에 안돌아가지만]
        # -> for문으로 큰 수(2^i)부터 parent배열 하나씩 다 뒤지기 때문에
        # -> 애초에 같으면 먼저 끝내야한다. (탐색할 땐, 탐색할 것이 없는 것은 빨리 미리 처리)
        if a == b:
            # print("depth만 맞췄는데 값이 같아져서 반환")
            return a
        # (6-2) 큰 수부터 2^i번째 부모를 확인하여, [부모가 다르다면, 동시에 2^i번째로 등산한다]
        # => 2의 k승으로 줄여나가면, 1까지 도달할때는 무조건 걸리게 되어있다.
        for i in range(LOG - 1, 0 - 1, -1):
            # if a != b:
            # (6-4) 이 때, a != b를 비교하는게 아니라,
            # -> 큰 수 i번째 부모로 건너띌까말까를 판단해야한다.
            # -> 아직 부모가 다르다면, 일단 가야한다.
            # -> a!=b가 다른 것으로는, i번째 부모로 건너띌 조건이 안된다.
            if parent_table[a][i] != parent_table[b][i]:
                a = parent_table[a][i]
                b = parent_table[b][i]

        # (6-4) i번째 부모가 다를 때마다 등산했기 때문에
        # -> 현재는 [부모가 같은 상황]이다. -> 같은 부모를 꺼내서 LCA로 반환한다.
        return parent_table[a][0]


    M = int(input().strip())

    for _ in range(M):
        a, b = map(int, input().split())
        print(lca(a, b))
