import heapq
import sys

input = sys.stdin.readline


## 8.
def dijkstra(n, graph, traps, srt, end):
    ## (1) 다익이 모든정점이 target이 아닐 때는, distance가 아닌 visited + pq를 그대로 쓴다.
    ## (2) visited를 쓰되, traps_state별 재방문은 허용된다면, 2차원 index에 state_bit를 매핑하자.
    visited = [[False for _ in range(1 << len(traps))] for _ in range(n + 1)]
    pq = []
    ## (3) pq에 초기항 (cost, node)를 넣되, stack별 stack까지 관리되도록 traps_state_bit도 넣어줘야한다.
    ## => 재귀가 아닌 state관리는 파라미터 대신, pq에 들어가는 node tuple에 넣어서 보관하면 된다.
    traps_state = 0
    heapq.heappush(pq, (0, srt, traps_state))

    while pq:
        w, u, state = heapq.heappop(pq)

        ## (4) 자신처리 전 가지치기 & 종착역 -> 그때까지의 비용 반환
        if u == end:
            return w

        ## (5) dfs처럼, pq 뭐가 먼저 나와서 체킹될지 모를 땐, [자신의처리]에서 나오는 순서대로 방문체킹-> 방문표시
        ## => 원래 다익은, bfs-queue로 돌리면서 모든 node를 다 검사하고 최소비용만 inqueue하지만
        ##    state별 다익은, dfs처럼 뭐가 먼저 나올지 모르므로, 먼저 나온 것을 체킹후 방문표시 -> inqueue시 방문체킹만
        if visited[u][state]: continue
        visited[u][state] = True

        ## (6) 현재도착node u가 trap이면, v탐색시 trap_state가 바뀐체로 graph를 탐색해야한다.
        #  => curr_trapped 상태를 파악해야한다.
        ## => if조건만족시 해당한다면 -> default값으로 시작해서 flag를 바꿔준다.
        curr_trapped = False
        ## (6-1) state_bit 매핑 대상인 모든traps를 돌면서, 각각이 불켜졌나 확인해야한다.
        ## => state에 매핑된 trap는 index로 매핑되어있기 때문에 [불켜진state ->  매핑대상trap]을 찾으려면 index로 돌려야한다
        ##   index-traps   index-traps_state(bit) => i번째bit , i번째 trap
        ## (6-5) 불켜진 i번재 node가, 현재 밟은 node u가 아니라서 꺼지지 않을 때 => dict에 모은다.
        trapped = {}
        for i in range(len(traps)):
            bit = 1 << i  # i번째 1 bit -> state_bit와 &연산해서 불켜졌는지 확인한다.
            if state & bit:
                # (6-2) 현재 불켜진 i번째 bit => i번째 trap => 현재 node에 해당하는지 확인한다.
                if u == traps[i]:
                    # (6-3) 내가 불켜진 상태면, 밟아서 불을 꺼야한다.
                    # => 불끄는 방법은 (1) [해당자리 1 bit]를 반전하여 0으로 만든 뒤, 그 자리 0과 (2) & 연산시켜서 끝다.
                    # state = state & (~bit)
                    state &= ~bit
                # (6-4) 불켜진 것이 현재node u가 아니라면, [계속 켜져있을 것]이므로 -> 켜진 node를 dict에 True로 모은다.
                else:
                    trapped[traps[i]] = True
            # (6-6) 불이 꺼져있는 i번째 자리에 대해서, 내가 불꺼져 있는 것이라면 (1)켜고 -> (2)dict에 넣어주고 -> (3) curr_trapped에 False를 표시한다.
            #       => 현재node u가 켜져있는 것이었다면, 현재 밟아서 꺼주면, curr_trapped는 False로 유지됬지만,
            #          꺼져있는 것이었다면, 현재 밟아서 켜주고, curr_trapped도 True로 표시해줘야한다.
            else:
                if u == traps[i]:
                    # (6-7) 불 켜는 방법은 [해당자리 1bit]를  |연산시켜서 켜준다.
                    state |= bit
                    # (6-8) 커졌으면, 해당node를 dict에 넣어준다.
                    trapped[traps[i]] = True
                    # (6-9) 꺼졌다가 켜질때만, curr_trapped = True
                    curr_trapped = True

        ## (7) 모든 traps를 돌면서, 현재node u와 비교해서, 불켜져있으면, 끄고 불꺼져있으면 켜면서
        ##     => 현재node는 어떤 상태인지 curr_trapped에 표시했다.
        ##     => 현재 켜져있는 상태면, trapped = {} 에 다 모아놨다.
        ##    my) 나는 지금까지 켜진 갯수가 짝수면 => uv graph / 홀수면 vu graph를 쓰면 될 것 같은데
        ##    => 시작 1->[2]     vs   발동2 -> 1로 온 상태에서의 1 -> [2]
        ##    => 발동시 역방향으로 바뀌는 문제라면, 내가 1 -> 다음으로 갈 2는, 발동된 체로 왔던 것일 수 있다.
        ##       처음 시작1이 아니라, 2에서 발동되어 역방향으로 온 1이라면... 1->2로 못간다.(2에서 발동되어 역방향graph써야하는 상태)
        #### curr -> next로 갈때, (1) 발동안된 쌔 길이라서 순방향graph를 쓰는 것일 수도 있찌만
        ####                      => (curr X next X => 순방향)
        ####         (2) 그 curr는 next가 trap발동되어 next -> curr로 온 상태로서, 역방향graph를 써야하는 curr일 수 도있다.
        ####             => next의 발동여부가 중요하다. (next O, curr X => 역방향)
        ####         (3) 그 curr가 trap발동이 된다면, 다시 순방향graph를 써야하는 curr이다.
        ####             => (next O, curr O => 순방향)
        ####         (4) 그 curr가 trap발동 했는데, next는 발동안된 상태면, 역방향graph로 가야한다.
        ####             => (next X, curr O => 역방향)
        #### => curr_trapped 여부를 판단하고 -> next trapped여부도 판단해야한다.
        ####    (1) curr는 현재까지의 trap_state에서, traps에 존재하고, traps_state에 불들어왔으면 O이다.
        ####    (2) next는 curr에서 traps_state에서, 자신의 발동여부를 확인할 때, 켜진 것들을 dict에 모아놨다면,
        ####              in 으로 이미 켜진 것인지 확인할 수 있다. (확인된다면 next에서 역방향으로 온 curr이 다시 next로 가는 상황)
        #### => 중요한 것은, curr -> next로 가는 것이, next에서 발동됨으로 인해 역방향으로 왔다가, 다시 가는 것일 수 도 있다는 것(next가 오히려 prev인 셈)
        ####    역방향으로 유지된다면 다시 갈 수 없다. curr가 발동되어, 다시 순방향으로 바꿨을 때만 뻗을 수 있다.

        ## (8) 자식들 탐색시, graph의 방향을 모르기 때문에, [모든node를 자식들로서, 탐색하되, 자기자신node는 pass]해서 전체를 다 돌릴 수 있다.
        for v in range(1, n + 1):
            if u == v: continue

            ## (9)_ graph를 쓰기 위해선 next_trapped여부를 curr_trapped확인시 모아둔 것을 활용해야한다.
            next_trapped = True if v in trapped else False
            ## (10) prev가 될지도 모르는 next와, 발동여부를 서로 비교해서, 어떤 graph를 쓸지 선택한다.
            ## OO XX로 같은 상태면, 순방향 / OX XO로 다른 상태면 역방향을 쓴다.
            if curr_trapped == next_trapped:
                ## (11) 순방향 그래프를 쓰되, 인접행렬을 cost가 INF가 아닐때만 유효하다
                if graph[u][v] != INF:
                    ## (12) 다익스트라에서 비용은 누적된다. 그때까지 도달할때까지 총 비용을 넣어줘야한다.
                    ##      state는 이미 curr_trapped 확인할 때 변경해줬었다.
                    heapq.heappush(pq, (w + graph[u][v], v, state))
            else:
                if graph[v][u] != INF:
                    heapq.heappush(pq, (w + graph[v][u], v, state))

    ## 혹시나 종착역을 못찾을 경우 디버깅을 위해서 (종착역 도착못하면 pq를 다쓰고 여기로 옮)
    return INF

if __name__ == '__main__':
    ## 미로탈출: https://school.programmers.co.kr/learn/courses/30/lessons/81304
    n, start, end = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(2)]
    traps = [int(input().strip())]

    ## 1. trap역방향을 미리 기록해두면, 자식들 탐색시 같이 걸리므로, state에 따라서,
    ## (1) 인접list가 아닌 인접행렬로 저장  (2) state에 따라 [v]->[u]를 쓰게 한다.

    ## 2. [상태값은 될 수 있으면, 매핑index별 O/X의 bit]로 표시해야하므로 => 전체trap에 대한 state를 bit로 관리한다.
    ##  => 만약, node별 traps여부도 매핑한다면, 너무 복잡해진다? node별.. visited별.. traps여부별..traps상태까지?
    ##  => [traps node별 state(bit)] 따로 관리하되, [node별 traps_state별] -> visited에 같이 매핑할 예정이다.

    ## 3. 최소비용을 구해야하므로, 매번 srt->end의 dijkstra를 구현해야한다.(기존에는 srt -> 모든distance에 대해 구함)
    ##   => graph가 바뀌니, 바뀐 graph에 따라 매번 dijkstra를 str->end로 구현한다.

    ## 4. [cost가 있는 인접행렬]은 [초기값을 INF로, 자기자신은 비용0으로 초기화]해야한다.
    ## -> 인접list라면, 자기것만 append하면 되지만, 인접행렬은 값을 초기화해야하며 cost이므로 INF로
    INF = float('inf')
    ## 5. 0번부터 쓰면 좋지만, traps까지 node번호를 들고 있으니, 1번부터 쓸 수 있게 갯수+1로 초기화한다.
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    # -> 안쓰는 0은 INF로 나오게 1번부터 자기자신 초기화
    for i in range(1, n + 1):
        graph[i][i] = 0
    for u, v, w in roads:
        ## 6. 서로 다른 두 방 사이에 직접 연결된 길이 여러 개 존재할 수도 있습니다.
        ## => 인접list가 아닌 인접행렬은 value에 cost가 1개만 들어가야한다. => 최소비용 문제니, 최소비용만 들어가도록 해야한다.
        # graph[u][v] = w
        if w < graph[u][v]:
            graph[u][v] = w

    ## 7. dijkstra를 통해, 시작정점srt부터 종착역end까지 찾아나간다.
    ## => 원래 전체다익은 시작정점 + visited대신 distance로 + pq로 bfs-queue개념으로 모든 정점까지의 거리를 한번에 구하지만
    ## => 중간에 로직이 변하는 다익은 직접 구현시, 조금 다르다.
    ## => (1) 자식들 탐색이 graph에 국한되는 것이 아니라, 거꾸로 바뀔 수도 있으면 -> 모든node돌면서, skip해야하니 -> n이 필요하다
    ## => (2) 내부 로직에 traps에 대한 state_bit를 만들어 쓰기 때문에, traps도 들어가야한다.
    print(dijkstra(n=n, graph=graph, traps=traps, srt=start, end=end))
