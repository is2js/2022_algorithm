import sys
from collections import defaultdict

input = sys.stdin.readline 
 
 
if __name__ == '__main__':
    tickets = []
    for _ in range(5):
        tickets.append(input().split())

    graph = defaultdict(list)
    for u, v in tickets:
        graph[u].append(v)

    ## 알파벳순서대로 방문하기 위해서, 정렬하는데
    #  stack의 pop() 특성을 고려해서 역순으로 정렬해둔다.
    for u, v in graph.items():
        graph[u] = sorted(v, reverse=True)

    ## dfs탐색용 stack -> 꼬리재귀처럼 1개 경로 -> 1개의 결과값만 반환하는 경우에만 dfs를 stack으로 사용할 수 있다.
    stack = []
    ## stack을 통한 [배열탐색]
    # bfs라면 queue에 넣기전에 방문처리(중복안되도록 모은다)
    # dfs는, stack에 중복에서 쌓여갈 수 있으므로 자신의 처리에서 방문처리(중복되도록 모으되 최근것부터 중복처리해서, 나중에 또 pop되어도 continue로 씹히게 한다)
    ## (1) stack은 해당node를 push한 상태를 진입상태로 본다.
    stack.append('ICN')

    ## 재귀 파라미터 속 누적결과값 변수
    routes = []

    while stack:
        ## 진입처리
        ## (2) 현재 진입된 node는 peek으로 처리한다. -> 종착역보다 먼저 진입된 node를 변수로 받아와야 처리할 수 있다.
        ##     만약, 종착역 검사 및 다음node탐색이 따로 필요없다면(방문배열), 생략하고 바로 pop해서 종착역으로 써도 된다?!
        curr = stack[-1]

        ## (3) 종착역(다음node없음) 처리
        # -> 탐색의 마지막 node 조건 (1) graph(dict)에 출발점u로 등록이 안되어있거나 (2) 등록되었더라도 방문edge들이 pop되어 빈 배열만 가지고 있다.
        # -> 다음node로 가는 길이 없기 때문에,
        # => [pop()으로 현재진입node를 버리고 직전node로 돌아가기 위해 pop() -> continue -> while stack -> [-1]peek으로 진전node로 진입한다]
        #    이 때, pop()한 종착역(다음node없음)을 결과에 저장하고 싶으면 [continue전에 배열에 저장]한다.
        if curr not in graph.keys() or len(graph[curr]) == 0:
            routes.append(stack.pop())
            # 다음node가 없는 종착역으로서 pop된 node는 누적결과값변수에 저장 -> continue로 stack상 직전node로 진입하게 한다
            continue

        ## (4) 다음node가 있는 상황(종착역에 안걸림)이라면, 다음node에 진입하기 위해
        #     (1) graph에서 다음node를 가져온다(pop으로 가져와서 edge방문처리)
        #     (2) stack에 push(그 node진입상태)하고 -> 바로 peek을 보러 다음while문으로 간다.
        stack.append(graph[curr].pop())
    else:
        ## (5) stack을 다비웠다는 말은 pop후 진입할 다음node가 stack에 안쌓였다. -> 끝
        # => 누적결과값변수는 최초종착역부터 쌓여있으니, 역순으로 출력한다
        print(routes[::-1])