import sys

input = sys.stdin.readline


def dfs(node):
    # [3] stack으로 구현하는 dfs는 visited를 지역변수로 선언한다.
    # -> 이 메서드안에서 끝날 것이기 때문에
    visited = [False for _ in range(N)]

    # [4]python의 stack인 list를 이용하여 현재node를 쌓아둔다.
    stack = []
    # [5] stack 문제는 일단 첫번재 원소를 넣어놓고 ->  while stack을 통과 -> pop해서 꺼내서 처리한다.
    #     do while 대신 이렇게 하는 것 같다.
    stack.append(node)

    # [5] 현재node를 넣어놓고, while stack으로 다 pop될때까지 돈다
    # while stack:
    #     stack.pop()
    while stack:
        # [6] stack의 pop은 빼는게 아니라 빼서 활용이다. 지역변수로 받아야한다.
        curr = stack.pop()
        # [7] 현재node를 방문여부 체크한 뒤, 방문한 적 없으면 방문여부를 체킹 + 출력한다
        if visited[curr]:
            continue
        visited[curr] = True
        print(curr, end=" ")

        # [8] 이제 0~N-1까지 전체node를 확인해서
        #  (1) 방문한적이 없고, 인접행렬상 인접해있으면, stack에 push한다
        # -> 다음 stack을 돌기 전에, 할 수 있는만큼 순서대로로 다 apped한다
        for next_node in range(N):
            if not visited[next_node] and graph[curr][next_node]:
                stack.append(next_node)
        # 0은 이미 방문처리 되었으며, 현재 직전node == curr == 0과 비교해서
        # 확인한 순서대로 1,2,3,4가 방문안하고 인접한 것만 stack에 올라간다
        # 1, 2가 먼저 push된다.
    # [9] 다음 while문 턴에서
    #     0 / stack[1, 2 ===] 쌓인 상태로 2부터 먼저 pop된 순서대로
    #     curr로 만들고 방문마킹 + 출력 + 모든node를 방문여부/인접여부 확인한다.
    #     0 2 / stack[1, 4 ===]
    #     0 2 4/ stack[1, 1 ===]
    # [10] 1은 아직 pop한 curr가 안됬으므로 방문한적이 없어서
    #     중복 push된다. 그래도 상관없다.
    #     0 2 4 / stack[1, 1, 3 ===]
    #     0 2 4 3 / stack[1, 1 ===]
    #     0 2 4 3 / stack[1, 1, 1 ===]
    #     0 2 4 3 1 / stack[1, 1 ===]
    #     0 2 4 3 1 / stack[1 ===] -> 1이 또 pop했지만 이미 방문한 node라 방문체크에서 스킵
    #     0 2 4 3 1 / stack[ ===]
    #     0 2 4 3 1 / stack[ ===] -> while문 종료
    # my) stack활용시 각 level당 인접node중 가장 나중에 넣은 node가 먼저 pop되서
    #     -> 다음depth에서는 먼저 탐색된다.
    #     level별 구분이 없기 때문에, 전level을 다 돌지도 않았는데 담level의 node가 쌓인다.
    #    -> cycle로 되어있다면, 전level에서 동일위치여도, 담level에서 발견 될 수 있으니,
    #    -> 중복허용해서 일단 집어넣고, 꺼낸 뒤 방문체크해야한다.
    #    -> dfs를 통한 node탐색은 level이 중요치 않다. 방문여부만 중요하다
    #    재귀dfs시에는, 먼저 호출되는 재귀를 끝까지 종착역까지 가기 때문에
    #    -> 직감적으로 depth우선탐색인 것을 확인할 수 있따.
    #    재귀stack도 맨마지막node pop이후, 해당level 다 pop하기 전에, 마지막에 node의 다음node를 탐색하기 때문에
    #    -> dfs는 level탐색안하고, 바로 담level가는 깊이우선탐색인 것을 직감할 수 있다.
    # 반면 bfs는 queue에 inqueue만 해놓고, queue에 들어가있는 해당level을 먼저 다 탐색한다.
    #    -> 인접node들이 queue속에 후보에 오르면, 그것들부터 다 탐색하다보니
    #    -> 도착node를 발견한 순간, 첫 발견시 그것이 최단거리가 된다.

    # [11] dfs재귀와는 출력순서가 다르지만 상관없다.
    # 왜냐면, 인접node중에서, 어떤 것을 먼저 방문하느냐에 따라서 결과만 다르게 출력할 뿐이지
    # -> 깊이가 깊어지도록 방문했다면 상관없다
    # 추가 조건으로, 인접한node중에서, 번호가 가장 큰 것부터 방문해야 한다 등이 있으면
    # dfs재귀나 dfs스택이나 동일할 것이다.
    # => 문제들에서는, 경로순서를 출력하는 게 아니라, 전역변수에 마킹해서 답을 구하게 한다






    pass


if __name__ == '__main__':
    ## DFS 스택
    N, E = map(int, input().split())
    # [1] node와 간선의 갯수만 알면, visited배열과 인접행렬을 만들어야하는데
    # -> dfs가 아닌 stack을 이용할 경우, visited배열을 지역변수로 선언해서 처리한다?!
    graph = [[0 for _ in range(N)] for _ in range(N)]

    values = list(map(int, input().split()))
    for i in range(E):
        u, v = values[2 * i], values[2 * i + 1]
        graph[u][v] = graph[v][u] = 1

    # [2] stakc을 이용한 dfs도 재귀처럼 첫번째node를 인자로 시작한다.
    dfs(0)
