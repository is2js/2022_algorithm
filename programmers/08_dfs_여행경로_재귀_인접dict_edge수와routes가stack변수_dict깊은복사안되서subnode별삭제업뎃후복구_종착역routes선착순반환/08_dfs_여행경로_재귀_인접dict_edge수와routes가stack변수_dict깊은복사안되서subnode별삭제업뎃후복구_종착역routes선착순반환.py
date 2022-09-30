import itertools
import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(100_1000)


def dfs(graph, N, node, routes):
    # (4) 종착역은 주어진 edge를 다 쓴 경우다.
    # -> a->b, b->c   a, b, c
    # => 단방향 edge수 == 탐색한 node수 - 1
    if len(routes) == N + 1:
        return routes

    # (5) 자신의 처리에서 보통은 방문체크 + 현재node를 출력해준다.
    # print(node, dst=' ')

    # (6) 인접node를 탐색하되, 한번 방문한edge는 pop시켜서 [방문체크 대신 edge체크]를 해준다.
    # for next_node in graph[node]:
    for next_index, next_node in enumerate(graph[node]):
        # (7) graph에서 이미 방문한 edge는 pop시킨 것을 건네주어, 더이상 못가게 한다.
        # => graph는 생성자 깊은복사가 안된다. 내부에 list들 똑같은 id를 가지고 있었다.

        # => 자식node별 각자의 graph를 가지게 하기 위해서는 backtrack으로 복구해줄 수 밖에 없다.
        # => 현재 lst의 index가 필요하니, 자식탐색을 enumerate로 한다.
        # => lst의 index삭제는 pop(index)로 한다.
        graph[node].pop(next_index)
        result = dfs(graph, N, next_node, list(routes) + [next_node])

        ## 현재탐색이 종착역으로 이어지기 전에 인접경로가 없어서 종착역없이 종료될 수 있다.
        # => 다음 경로case를 위해 복구해줘야한다. 새마음으로 진행.
        graph[node].insert(next_index, next_node)

        # (8) 여러 경로 중에서, 조건을 만족하여 종착역에 도달한 것만 result가 들어있으니
        #     그것만 받으면 된다? 여러개일 수 있을 건데.. 일단 발견즉시 바로 return하여
        #   => [탐색순서를 미리 정해져있고, 종착역 조건을 만족하는 것 선착순반환]하게 하여 [가장 먼저 발견한 경로만] 반환한다
        #      자식들의 결과값 1개를 모으는 집계 대신 [탐색순서가 정해진 선착순 1개 종착역 집계]는 [return값 존재시 즉시 반환하여 재귀종료]를 하게 한다
        #      [일단 자식재귀를 ret]으로 받아놓으면, 종착역 못거치는 경우는 None을 반환하며 자동종료 될 것이다.
        if result:
            return result



if __name__ == '__main__':
    tickets = []
    for _ in range(5):
        tickets.append(input().split())
    # print(tickets)
    # print(list(itertools.chain(*tickets)))


    ## (1) 숫자node가 아닌 경우, 인접빈행렬 -> 인접dict를 써야한다.
    graph = defaultdict(list)

    ## (2) dfs는 [여러 경로case별로 1번만 방문]하려면 visited배열 + route경로배열을 들고다녀야한다.
    # -> 숫자node가 아닌 경우, visited dict를 들고다녀야한다.
    # -> 여기서는 [case별 여러번 방문 가능]하므로 필요가 없다.
    # => 대신, [이미 방문한 인접경로]는 방문안하도록 내부에서 pop시켜줘야한다.
    for u, v in tickets:
        graph[u].append(v)

    # 각 자식 인접node탐색을 알파벳순서대로 되도록 미리 정렬해놓는다.
    for key in graph.keys():
        graph[key].sort()

    # (3) dfs를 시작node로 출발하는 경우, 누적결과값인 route방문경로 배열에 미리 넣어놔야한다.
    #    => case별 여러경로가 있는 것이 아니라서 [주어진 edge경로 수]를 다 쓰면 끝내도록 해야한다.
    #    => stack변수는, 주어진 edge의 수이다.
    # dfs(graph, edge수, 시작node, route)
    print(dfs(graph, len(tickets), "ICN", ['ICN']))
