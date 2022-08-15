import sys

input = sys.stdin.readline

# [6] queue는 from queue import Queue도 가능하지만
#     python에서는 deque(스택pop + 큐popleft 둘다가능)를 통해 사용한다.
# 스택, 큐를 구현할 때 사용하는 라이브러리
# 가장 앞 원소추가, 가장 앞 원소제거에서 O(1)의 시간복잡도를 가진다
# 인덱싱, 슬라이싱 등은 사용할 수 없다.
# collections.deque : 빠르고 강력한 스택
# 스택(pop)과 큐(popleft)로 모두 사용가능한 자료구조다.
# -> 데크는 내부적으로는 [이중 연결리스트로 구현]되어 있다.
# -> 따라서 특정 요소 접근에 [시간 복잡도 O(n)] 만큼 소요된다. in linked list

# from queue import Queue
from collections import deque


def bfs(node):
    # [7] 순서가 잇는 탐색(순열, 그래프node탐색)은 다 visited가 있어야한다.
    visited = [False for _ in range(N)]

    # [8] bfs로 너비(level)우선탐색을 한다면, 자료구조를 queue를 만든다.
    queue = deque()  # myqueue = Queue()

    # [9] dfs와 다르게, inqueue하기 전에 visisted를 마킹한다.
    # -> dfs의 재귀/stack에서는 실제 방문할 때 방문여부를 체킹했다.
    # => queue에서도 그렇게 해도 되지만, 차이점이 존재한다.
    # -> stack은 먼저 들어간 node가 나중에 pop되어,
    #    첫 node를 제외하고, inqueue node가 방문을 바로 하지 않는다.
    # => 반면, queue는 먼저 넣은 node가 100% 먼저 방문하게되어있다.
    # => 그래서, 이후 전체node탐색시, 동일한node를 inqueue하는 것은 의미가 없다
    # -> stack은 첫node제외, 먼저들어간다고해서 먼저 방문을 하는 것이 아니므로
    # -> 탐색시 걸리는 동일node라도 중복해서 stack에 넣어주고,
    # -> 먼저 나오는 node를 실제방문할 때 체크해줘서, 그다음에 pop되는 먼저들어간node는 방문안하게 한다
    # => queue에서는, 먼저 들어갔으면 100% 먼저 방문이기 때문에
    # => 중복node를 inqueue하는 것을 막는다. => 메모리를 아낄 수 있다.
    # ###### Queue에서는 inqueue하기 전에, visisted마킹이 일반적인 방법이다 ##########
    # ###### stack은 inqueue하더라도 먼저 방문한 보장이 없고, 그 뒤에 똑같은 놈이 탐색되어 들어올 수 있어서
    # ###### append는 중복을 허용하고, 실제방문할 때 체킹해주면, pop되더라도 건너뛴다.

    visited[node] = True  # queue를 통한 bfs는 inqueue전에 방문체크해서 다음node전체탐색시 중복이 없게 한다.
    queue.append(node)  # myqueue.put(node)

    # [10] stack이든 queue든 탐색시, 첫번재 것은 넣고 while통과후, 빼서 curr를 만든다.
    while queue:  # while not myqueue.empty():
        curr = queue.popleft()  # myqueue.get()
        # [11] 실제 방문(curr) 의미(자신 처리)로 출력을 한다.
        print(curr, end=" ")
        # [12] 실제 방문 자신 처리후, 다음node를 전체탐색하되 visited로 필터링한다.
        #     -> 방문한적 없고 && 인접한node면
        for next_node in range(N):
            if not visited[next_node] and graph[curr][next_node]:
                # 선택된 다음node는 inqueue할 것인데, queue는 inqueue전에 방문체크해서 중복inqueue르 방지한다.
                visited[next_node] = True
                queue.append(next_node) # -> 바로 다음부터는 dequeue해서  curr가 될 예정이다.
    # [13] 과정
    #      0✔ [ ==== 1✔ 2✔]
    #      0✔ 1✔ [ ==== 2✔ 3✔ 4✔] 0x
    #      0✔ 1✔ 2✔ [ ==== 3✔ 4✔] 0x 0x 4x
    #      0✔ 1✔ 2✔ 3✔ [ ====  4✔]
    #      0✔ 1✔ 2✔ 3✔ 4✔ [ ====  ]
    # -> queue는 넣은 순서대로 나오니, 미리 방문체크해놓으면, 다음node 전체 탐색시 중복inqueue를 막는다.

    # [14] 결과
    # 0 1 2 3 4 None
    # root node로부터 인접한 node들을 모두 순서대로 나오도록 deqeue(queue)에 먼저 집어넣으므로
    # deqeue시 집어넣은 순서대로 나오게 된다.

    ##    0
    ##   / \
    ##   1  2

    ##    0
    ##   / \
    ##   1  2
    ##  / \/
    ## 3 - 4

    ## [15] 간선의 가중치가 없거나 동일하다고 하면
    ## 최단경로는 공짜로 나온다.
    ## -> 가장 먼저 방문되는 것이 최단경로의 길이가 된다.



if __name__ == '__main__':
    ## BFS( breath first search)
    # -> 그래프(node)순회방법 중 하나
    # -> 너비우선탐색 -> dfs는 다음재귀(다음node)호출 순서대로 방문하되, 갈 수 있는 만큼 stack을 이어가서 종료되면 다음 node
    #              -> bfs는 같은level의 다음node들을 모두 방문 한 다음
    #              ->       그 다음level의 다음node들을 모두 방문 하는 식

    # DFS의 깊이우선 탐색은, (1) 재귀 or (2) stack자료구조 활용
    # -> stack(인접node, 다음node들을 모두 stack에 집어넣은 뒤, 맨마지막 push한 것을 꺼낸 뒤, 다음 인접node들 다 push..)
    # -> 재귀(먼저 만난 다음 인접node1개씩 -> 갈 수 있는 데까지 감.)
    # --> 둘이 순서는 다르지만, 해당depth(같은level)이 아닌 깊어질 수 있는 만큼 깊어짐

    # BFS는
    # tree구조에서는 root node(자신처리있는 재귀정의)에서 시작한다면
    # -> depth별(같은level)별 먼저 다 방문하게 된다.

    # BFS의 경우, 간선의 가중치가 없다고 한다면,
    # -> level별 [먼저 방문한 경로가 최단경로]가 된다.
    # -> 가중치가 없는 경우에는, [bfs로 최단경로 문제를 푼다]

    ## 예시
    ##    0
    ##   / \
    ##   1  2
    ##  / \/
    ## 3 - 4
    # 0 -> 1과 2부터 다 방문 -> 1과 인접node 3과 4 모두 방문 -> 2와 인접한node 방문

    ## BFS는 dfs(재귀, stack)과 달리 queue 자료구조를 이용한다.
    # [1] node탐색 문제는, 배열 -> 2개이상 원소 나열 case인 순열/조합과 달리
    #     node갯수N, 간선갯수E, 간선 연결정보를 받아야한다.
    #     -> (1) visited(from node갯수만큼 상태배열) 재귀시 전역변수로서 마킹가능하게
    #        (1-1) dfs-재귀-used_bit(원소나열 중 순서가 중요해서 back금지 -> 사용 후 재사용금지)
    #              순열은, root node가 1개가 아니라, 여러 출발점으로 시작하기 때문에
    #              전역변수로 관리될 수 없다 -> 파라미터로 상태배열(상태비트)가 관리된다.
    #              상태배열을 쓸 경우, 컬렉션이라 깊은복사를 매번해줘야하지만, 상태비트는 값이라서 바로 업데이트 가능하다.
    #         ===> my) root node가 1개인 순열문제(그래프-node탐색)는, 전역변수로 상태관리 가능함(모든 재귀내 무조건 1번만 등장)
    #                  root node가 n개인 순열문제는, 각각 출발후 각 case마다 업데이트될 상태배열이 필요함 -> 업데이트를 값인 상태비트로 관리한다.
    #                                             n개의 출발점마다 사용되는 것이 다르므로, 각각 관리되어야한다.
    #        (1-2) dfs-재귀(그래프 속 인접node들 탐색 -> 순열이나 마찬가지. 사용후 재사용금지)
    #        (1-3) dfs-stack(그래프 속 인접node들 탐색 -> 순열이나 마찬가지. 사용후 재사용금지)
    #     ===> my) 순서가 중요한 순열, 그래프(node)탐색은 visited배열이 있어야한다.
    #              객체라면, boolean필드를 toggle로 가능할 듯.
    #     -> (2) graph(from node갯수 by node갯수)-> 간선정보로 1마킹
    #     ===> my) 간선정보가 있다면, 무조건 만들어야한다.
    #     ===> 0행렬로 먼저 초기화하고 -> 간선정보로 1을 채워넣는다.
    #          가중치가 있을 경우, 0->1이 아니라 다른 것도 들어가기 때문에 False가 아닌 0으로 초기화한다.
    N, E = map(int, input().split())
    # [2] node -> node탐색은 root node가 정해진 순열 -> visited생각(재귀라면 전역변수로서 먼저 선언)
    #             root node가 1개로 정해져있다면, 전역변수로 상태관리한다.
    #             root node가 여러개이고 각각이 다른 case(순열탐색)이라면, 첫 재귀 내부에서 각 root마다 값으로 상태관리를 업데이트해서 진행하게 해야한다.
    #
    # [3] edge -> 간선정보는 graph 가중치예상 0으로 초기화후 넣어줘야한다. -> graph(인접행렬 생각)
    #     -> 먼저 0행렬로 초기화된 인접행렬만들고 -> 정보 받고 -> 채우기
    graph = [[0 for _ in range(N)] for _ in range(N)]
    edge_infos = list(map(int, input().split()))
    #  values를 2개씩 묶어서 pair로 처리한다면, N//2의 몫으로 돌린 뒤, 배열[2*index], 배열[2*index+1]로 각 pair에 접근한다.
    for i in range(E):
        u, v = edge_infos[2 * i], edge_infos[2 * i + 1]
        graph[u][v] = graph[v][u] = 1

    # [4] bfs는 재귀가 아닌, 일반메서드 안에서 queue자료구조로 돌린다
    #    -> 재귀아니라면, visited를 전역변수로 안해도된다. 메서드 내에서 선언하자.
    # [5] dfs재귀든, dfs스택이든, bfs든 node탐색이면 시작node를 파라미터로 받는다.
    #     좌표탐색이면, 시작좌표를 파라미터로 받는다.
    print(bfs(0))

    pass
