import heapq
import sys

input = sys.stdin.readline


## 6.
def dijkstra(n, graph, start, end, traps):
    # 1) pq 도입 -> 2) visited필요(distance로 대신하면 됬었으나, 여기선 node별/[상태별] 방문정보를 저장하기 위해
    #                 1차원node지만, 2차원visited를 도입함.
    pq = []
    # 3) visited 2차원에는 [traps별 state_bit ]를 traps갯수에 따른 모든 부분집합(경우의수)를 index에 미리 매핑해놔야하므로
    #    traps_state_bit의 모든 부분집합의 갯수이자 순차탐색은 range( 1<<len(traps)) 이다
    visited = [[False for _ in range(1 << len(traps))] for _ in range(n + 1)]
    # cf) 모든 부분집합 1자리씩 처리한 배열 만들기
    # for subset in range(1 << n):
    #     temp = [0] * n
    #     ## ryon vs apeach를 1자리씩 채우면서 점수 비교
    #     ## 갯수제한이 있다면, 1에서 cnt += 1
    #     # cnt = 0
    #     for i in range(n):
    #         if subset & (1 << i):
    #             ## 불들어왔으면 ryan의 승리로서 ryon배열(temp)에 값 할당 및, 가변변수에 점수 누적
    #             temp[i] = 1
    #             # cnt += 1
    #         else:
    #             ## 불꺼져씅면 apeach의 승리로서 apeach 집계 가변변수에 누적(단, apeach도 0이면 점수 누적X)
    #             temp[i] = 0

    # 4) 시작점을 inqueue  (cost, node, traps_state))
    # -> traps을 밟은 적이 없으니 발동된 trap이 없는, 0으로 넣어준다.
    heapq.heappush(pq, (0, start, 0))

    while pq:
        curr = heapq.heappop(pq)
        ## 5) tuple의 각 요소를 꺼내놓는다.
        # -> u는 [현재 도착한 node]를 의미한다. / state는 graph상태를 의미한다?!
        w, u, state = curr[0], curr[1], curr[2]

        ## 6) bfs의 가지치기 -> 없으면 종착역을 설정한다.
        ## => 도착점에서 [도착할때까지의 비용] w를 반환한다.
        ## => my) node탐색에서 간선비용누적은, pq속에서하다가, 도착하자마자 자신의처리없이
        if u == end:
            return w
        ## 7) 종착역을 지나서는 [종착역직전까지 처리할 자신의 처리]를 해준다.
        ##   원래bfs-다익스트라는, 시작->모든정점에 대해, inqueue전에 distance체킹(->distance업뎃->inqueue)처리했지만, 여기 다익스트라는, dfs-stack처럼 처리했지만,
        ##   목표지점-다익스트라는, dfs처럼 visited활용 + 일단집어놓고 먼저나오면 그때부터 금지인(자처:방문체킹방문표시 + 자식들처리:방문체킹후inqueue)를 고수한다.
        ##   => 들어갔어도 언제 뭐가 먼저 나올지 모를 때 쓰는 전법. bfs-queue와 다익-pq는 다름.

        #### 자신의 처리로서, 자료구조속 중복으로 집어넣고 언제뭐가 먼저나올지모르는 자료구조(dfs-stack, 다익-pq)는
        #### 자신의 처리에서 visited가지치기 -> 방문체킹+방문표시 다한다(자식들처리에서는 방문체킹만)
        # => 현재 node u에 이 state로 온적이 있는지.. 있으면 가지친다.
        if visited[u][state]: continue
        visited[u][state] = True

        ## 8) 인접node로 이동할 때, (1) 현재node에 trap이 발동햇는지 여부 + (2) 다음node에 trap발동여부를 알아야한다.
        curr_trapped = False  # 일단 False로 초기화해놓고, state+traps를 통해 확인해서 결정한다.
        ## 9) 어떤node가 함정발동되어있는지 dict에 저장해둘 것이다.(인접node로 빠르게 이동하기 위함)
        ##   => 함정목록을 하나하나 확인하며, [발동 켜진(1bit & state) 매핑 node(traps)를 하나하나 dict]에 넣어줄 것이다.
        trapped = {}
        for i in range(len(traps)):
            ## 9-1) 함정목록 index에 따라, 불켜진 bit(00100)를 만들어놓을 것이다.
            bit = 1 << i
            ## 9-2) 켜진bit와 state를 and연산해서 불켜짐 여부를 확인한다.
            ## -> 현재bit의 함정node가 발동된 상태다.
            if state & bit:
                # -> i번째 자리가 불켜졌다면, i번째에 매핑된 node [traps[i]]를 dict에 넣어준다.
                #### my) 매핑value(arr) 매핑state(bit)를 두고 불켜진 value를 찾는 방법
                #### => (1) 둘다 index에 매핑되어있으므로 for i in range(len(arr))로 index를 돌린다
                #### => (2) 해당i에 1bit를만들고, state bit와 &연산하여 불켜진 유무 확인
                #### => (3) if문을 통해 불켜졌다면, arr[index]를 통해 불켜진index->불켜진 value를 가져와, 처리한다.
                #### => (4) 현 상황에서 여러자리의 불켜진 value를 찾고 싶다면, dict의 key에 불켜진value들을 = True로 불켜졌다고 넣어준다.
                #### + (5) 현재node u가, 현재자리의 불켜진 index의 nodet값 traps[i]와 같다면,(traps 중에 1개라면)
                ####       => 다음node는 반전을 쳐야하므로, 불켜지면 끄고/불꺼지면 켜줘야한다.
                ####          trapped는 다음node가 받을 불켜짐 목록이다??!
                # trapped[traps[i]] = True
                if u == traps[i]:
                    #### 다음node를 위해 불끄는 방법은 반전(~)후 & 연산이다.
                    # cf) n번째자리 불끄기 => bit & ~(1 << n)
                    #     -> 해당자리만 1 -> (~)반전으로 해당자리만 0 -> &시켜서 죽이기
                    state &= ~bit
                #### + (6) 현재node u가 trap발동node가 아닐 때만, 불켜졌다고 dict에 넣어준다.
                else:
                    trapped[traps[i]] = True
            #### 9-3)  state & bit가 아닌 경우 -> 현재자리가i가 state상 불이 안켜진node라면
            else:
                #### 9-4) 직전에 보내준 state에서는 불이 안켜졌는데, 도착하고 보니 traps에 있는 node라면
                ####      |= 연산으로 불을 켜줘야한다.
                if u == traps[i]:
                    state |= bit
                    ## 불켜줬으니, dict에도 넣어줘야한다.
                    trapped[traps[i]] = True
                    #### 9-5) 현재node가 state상 켜져있음녀 꺼지는 거지만, 꺼져있는데 켜지는 경우는
                    ####      curr_trapped는 켜져야한다.
                    curr_trapped = True

        #### 10. for문이 끝나고 나면,
        # (1) curr_trapped로 인해, 현재 켜지는 찰라라서 켜지는, 발동여부가 결정되고
        # (2) 발동된 것들은 모두 trapped dict에 다 저장되어있다.
        #### => 이 상태에서 인접node로 이동해본다.
        #### => graph를 이용하지않고, 모든node를 돌리면서 skip한다.
        for v in range(1, n + 1):
            # 모두 살펴볼 땐, 자기자신으로의 이동은 skip
            if u == v: continue
            #### 11. 자기자신이 아니라면, 이동할 수 있는지 없는지 확인해야하는데, 원래간선vs뒤집은간선 결정해야한다.
            # (1) u와 v의 발동여부를 보고, 둘다 발동안됬거나, 둘다 발동되면 원래간선을 쓴다.
            # (2) 하나만 발동되면, 뒤집힌체로 가거나, ??가서 뒤집히니?? 뒤집힌 간선을 쓴다?
            #### => v에 해당하는 node가 함정이 발동되었는지를 먼저 확인해야한다.
            #### => 다음node를 위한 현재발동을 고려한 trapped dict를 통해 확인한다.
            next_trapped = True if v in trapped else False
            ## 발동상태가 같으면XX OO 원래graph아니라면, 대칭index...거꾸로쓰기...
            if curr_trapped == next_trapped:
                # graph[u][v]
                ## 일단 인접lst가 아니라면, 간선이 존재하는지부터 봐야한다.
                # -> cost 인접행렬에서는INF초기화후, INF가 아니면 간선정보 있는 것
                if graph[u][v] != INF:
                    ## cost는... 현재에서 +@로 해줘야한다.
                    heapq.heappush(pq, (w + graph[u][v], v, state))
            else:
                # graph[v][u]
                if graph[v][u] != INF:
                    heapq.heappush(pq, (w + graph[v][u], v, state))

    ## 문제에서 항상 도착node가 있다고 했으니, 혹시나 디버깅을 위해서
    ## q가 중간에 종착역에 도착안하고 끝날 때를 대비해서, cost를 INF를 반환한다
    return INF


if __name__ == '__main__':
    ## 미로탈출:https://school.programmers.co.kr/learn/courses/30/lessons/81304
    n, start, end = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(2)]
    traps = [int(input().strip())]

    ## 1. \자신기준 대칭index의 [단방향 저장인데 역방향 꾀하기]를 위해서는
    ## => 인접빈행렬이 아니라, 2차원 정사각 인접행렬을 선언후, value에 cost를 담아야한다.
    ## => 다익스트라의 graph(cost 있는 graph)는 distance를 INF로 초기화하듯이, graph를 INF로 초기화한다.
    ## => 간선연결X -> cost INF, 자기자신거리 -> cost 0 까지 추가 초기화한다.
    INF = float('inf')
    ## 2. 보통같으면 node번호 -1 씩 써서 [갯수n에 맞게 선언후 =>  0부터 쓰지만]
    ##    traps에도 node가 걸려서 나오고, 다 1씩 빼주기가 번거로우니.. [갯수n+1 선언후  => 0번을 빈것으로 1번부터 쓴다.]
    graph = [[INF] * (n + 1) for _ in range(n + 1)]  # 10001by10001인데 0번빼고 쓴다.

    ## 3. cost있는 인접행렬graph는 자기자신 0으로 초기화까지 해주자.
    # -> 1부터
    for i in range(1, n + 1):
        graph[i][i] = 0
    ## 4. 간선정보받기
    ## => 1node당 여러node를 갈 수 있다면, [인접lst]의 경우에만 가능하다.
    ## => [인접행렬]은 u->v에 대해, 1가지 root만 w를 입력할 수 있다.
    ## => but 우리는 u->v 중에.. 같은node로 간다면, 굳이 먼 길/돌아가는길의 경로를 알 필요가 없으며 && cost(가중치, w)가 작은 것 1개만 입력하게 한다.
    ##   -> 인접행렬value로 들어갈 cost(w) 중에 greedy로 min값만 1개 입력하게 한다.
    ##   => 최단거리 문제의 graph만 가능한 일이다?
    for data in roads:
        u = data[0]
        v = data[1]
        w = data[2]
        ## 들어오는 w가 작다면 그것으로 업데이트한다.(min업뎃을.. 행렬value를 가변변수라 생각)
        if w < graph[u][v]:
            graph[u][v] = w

    ## 5. 다익스트라 수행을 위해 함수만들기
    ##  원래 전역변수아니라면, node갯수 필요(visited or distance), graph필요(대칭index로 바뀌기도)
    ##  src만 필요하지만, 문제에 의해 각node별 -> dst node까지의 거리를 구해야함.
    ##  traps 함정정보 -> 검사해야함.
    print(dijkstra(n=n, graph=graph, start=start, end=end, traps=traps))
