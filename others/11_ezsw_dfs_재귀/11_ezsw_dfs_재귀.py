import sys

input = sys.stdin.readline


def dfs(node):
    # [6] 다음node로만 업데이트되면서, 전역변수만 터치한다
    #   -> dfs node탐색은, 마지막node에서 종료되는 종착역이 없다.

    # [7] 자신의처리에서 전역변수를 터치한다 -> 다음재귀들 호출부터 안하면,
    #     최초인자 0(node)의 처리부터 간다는 뜻이다.
    #     0 node부터 다음재귀로 갈라진다.
    # -> 현재node를 전역변수인 상태배열에 체크해준다.
    #    진행node마다 독립적이라면, 상태배열or상태비트를 인자로 들고다니지만,
    #    여기서는 전역변수에 체크하여, 독립node가 아니라는 말이 된다?
    visited[node] = True
    # [8] 탐색한 node순서를 들고다니고 종착역에 반환할게 아니라면
    #     다음재귀가기전에, 먼저 출력해준다.
    # -> 방문한 node는 순서대로 출력하는 버릇을 가지자?
    print(node, end=" ")

    # [9] 인접행렬로 통행가능한 정보를 미리 만들어놓은 상태에서는
    #     다음 node뻗기는, [일단 모든 node를 반복문으로 다 탐색]하고
    #     [인접행렬을 이용해 필터링]해서, 다음node로 이동 가능한 것만
    #     재귀호출하게 한다 -> 다음재귀 업데이트 변수인 node를
    #     -> 0부터 4번 node를 일단 다 돌린다.
    for next_node in range(N):
        # [10] 인접행렬을 통해, 인접한node로서 이동가능한지 확인한다.
        # if graph[node][next_node]:
        # [11] 상태배열에서 아직 방문안한 node만 이동가능하다.
        # -> 2가지 조건이 다 필요하다. (방문상태배열 + 인접행렬)
        if not visited[next_node] and graph[node][next_node]:
            dfs(next_node)
    # 0 1 3 4 2
    # [10] 종착역 없이 다음재귀가 없는 마지막 stack에서는 자동 종료되면서, 직전으로 돌아간다
    #      다음재귀 끝나는 부분에 끝처리가 없다면, 계속 종료만 되니까 끝난다.
    #     -> 반복문에서 호출한 다음재귀순으로 깊숙히 먼저 진행해서 방문을 다 채워버려
    #        뒤쪽 재귀는 다음재귀를 못탈 확률이 높다.

if __name__ == '__main__':
    ## DFS depth first search
    ## 그래프 순회 방법 중 1개 / 깊이 우선 탐색
    ## root node로부터 깊이가 커지는 방향으로 탐색
    ## 더이상 방문할 인접노드가 없는 경우, [이전 노드로 돌아가서] 다시 깊이 우선탐색을 반복
    ## -> [방문 체크]를 하면서, [인접노드= 붙어있는 모든 노드, back포함 but 방문체크됨]
    ##    [아직 방문하지 않는 인접노드]를 탐색한다.

    ## 순열, 조합탐색과 다르게, 1방향이 아니다. 붙어있는 그래프상의 모든 노드를 의미한다.
    ## -> 경우의 수를 만들어내며 탐색하는 것이 아니라,
    ## -> 이미 graph는 주어져있고, 그에 따라 방문체킹하면서 탐색한다
    ## --> cycle이 있는 그래프도 탐색이 다 가능하다.

    ## graph상 인접노드를 모두 방문하되, 깊이가 깊어지는 방향이 우선이다.

    ## (1) DFS-재귀호출
    ##    0
    ##   / \
    ##   1  2
    ##  / \/
    ## 3 - 4

    ## 입력으로 graph를 주는 방법
    ## -> node갯수 5 / 간선의 갯수 6이 주어지며
    ## -> node 쌍으로 간선의 정보 직접줘야한다
    ##   0 1 / 0 2 / 1 3 / 1 4/ 2 4 / 3 4
    ## -> 방향성을 안준다면, 0->1  1->0 모두 가능한 것이다.
    # 5 6
    # 0 1 0 2 1 3 1 4 2 4 3 4
    N, E = map(int, input().split())
    # [1] node, edge수와 그래프는 별개다.
    #     node, edge가 주어진다면 -> f visited배열과 0행렬 graph를 만든다.
    #     -> node갯수 N만큼, visited 마킹배열(상태배열)을 만들고
    #     -> node갯수만큼의 n by N행렬의 graph를 만든다.
    #     -> graph는 인접리스트로 표현할 수 있지만, 여기선 0 초기화 행렬로 표현한다.
    #     -> 인접행렬 node by node란, i->j로 갈 수 있는 정보를 1로 표기한다.
    #                      반대방향이 허용되면, j -> i도 1로 표기하면 된다.
    visited = [False for _ in range(N)]
    graph = [[0 for _ in range(N)] for _ in range(N)]

    # [2] 간선 정보를 읽은 뒤, 각 node번호는 인접행렬의 index로서, 변수로 받아놓고 방향성을 생각한다.
    # -> 일단, 1줄 배열정보니까 int list로 받는다.
    values = list(map(int, input().split()))
    # -> list 배열을 2개씩 받는 방법은
    # -> 12개 전체를 돌면서, index를 짝수일때마다 끊는 방법을 썻었지만
    # -> 미리 6개의 index만 돌면서, 내부에서 index를 0부터짝수, 홀수 2개씩 배열에서 뽑아내도 된다.
    # for index in range(len(values)):
    # [2-1] 2개씩 묶일 갯수만큼만 index를 돌리고
    for index in range(E):
        # [2-2] 내부에서는, 배열에서 순서대로 2개씩 뽑아내도록
        # 0, 1 / 2, 3 -> 2*index, 2*index+1로 배열에서 원소를 2개를 뽑아내면 된다.
        # => 이렇게 하면 반복문 속에서, 묶음의 2개 원소를 동시에 배열에서 뽑아내서
        #    2개 원소를 동시에 컨트롤 할 수 있다.
        u, v = values[2 * index], values[2 * index + 1]
        # print(first, second)
        # 0 1
        # 0 2
        # 1 3
        # 1 4
        # 2 4
        # 3 4
        # [3] 2개씩 순서대로 뽑혔다면, 인접행렬에 간선정보를 표기해준다.
        # -> 방향성이 없다면, 양 node 둘다 1을 넣어줘야한다.
        graph[u][v] = graph[v][u] = 1
    # print(graph)
    # [4] 인접행렬이란? -> 현재node가 방문할 수 있는지 ==인접해있는지 정보를 준다.
    # [[0, 1, 1, 0, 0],
    # [1, 0, 0, 1, 1],
    # [1, 0, 0, 0, 1],
    # [0, 1, 0, 0, 1],
    # [0, 1, 1, 1, 0]]

    # [5] dfs를 재귀로 호출하는 데, stack결정변수는 node이며,
    #     depth마다 업데이트되거나 누적되는연산은 없이,
    #     전역변수 visited를 터치하고, 전역변수 graph만 참고한다.
    # 최초인자로 root node, 시작node를 넣어준다.
    dfs(0)


    pass
