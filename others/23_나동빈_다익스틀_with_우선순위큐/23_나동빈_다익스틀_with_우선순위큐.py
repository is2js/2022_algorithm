import heapq
import sys

input = sys.stdin.readline


def dijkstra(start):
    heap = [] # 우선순위 큐 기반이 되는 list

    # 자료구조를 이용하여, pop된 자식들도 반복수행 하기 위해서, 시작정점도 먼저 넣어준다.
    # -> [자식들은 넣기 전, distance테이블을 업뎃하고 들어가기 때문에, 시작정점은 0으로 cost를 업뎃해준다.]
    # -> 우선순위큐에 넣을 땐, 순위비교할 cost가 맨 앞으로 가도록 튜플을 만들어서 넣어준다.
    distance[start] = 0 # 큐에 넣기 전엔, [직전최단거리 start]로부터 거리를 업뎃하고 들어가는 규칙.
    # -> 우선순위큐는 업뎃여부로, visited를 대신한다. bfs-queue처럼 넣은 순서대로 나온다면, 고정된 가중치의 똑같은 node는 안들어가게 inqueue전에 넣어주는데
    # -> 우선순위큐는, [직전최단경로node의 인접node로서 업뎃된 후보node]만 넣어주기 때문에 inqueue전 업뎃한다.
    pq.heappush(heap, (0, start)) # list기반 이진힙은 삽입/삭제가 lgN

    # 자료구조에서 빼면서 시작하는 것은 while 자료구조:로 다 빠질때까지 진행하게 한다.
    while heap:
        curr_cost, curr_node = pq.heappop(heap) # tuple  (value, start)를 최소비용인 것을 가져오니, 언패킹해서 받아준다.

        # 방문체킹 대신, 업뎃 여부를 통해, 업뎃 안된거면, 이미 방문된 거라 판단하고, 건너띈다.
        # -> 기존까지 비용(INF초기화) vs 현재 후보로서 비용 -> 한번 pop되서 나오면, 최단경로 확정된 상태인데
        #   (왜냐면, 최단경로로의 인접node && 모든node보다 비용적으면 100% 최단경로 fix)
        # -> [확정된 node도 cost가 더 큰 상태]로 (간선정보에 의해) 또 나올 수 있다.
        #    경유경로로서 pass해야한다. 최단경로 구할 때, 경유경로로서 cost큰 상태로 한번 더 나올 수 있음을 생각하자.
        # --> 왜냐면, 현재level ~ 이전level들 모두 모인 데서, 이미 나와서 업뎃 되었으면 ->[기존 최단경로의 인접node이며, 100% 최단 경로 fix]이다.

        # 경유경로로서, cost 더 크지만 한번더 같은node가 나올 수 있다(inqueue전에 방문체크 안하면!)
        # -> bfs-queue만, 넣은 순서대로 나오는게 보장될 때만, 같은게 안나온다.
        if distance[curr_node] < curr_cost: continue # 경유경로, 섞임pq에서, 재등장시 -> pass
        # -> visited를 대신할 수 있다.
        # -> 이것을 통과했다면, [fix된 최단경로의 최초 등장]이다. -> 인접node를 탐색한다.
        #   (방문체킹이전에 inqueue하는 자료구조(queue를 제외한 stack/heapq)는, 꺼낸 뒤, 중복확인, 방문확인 해야한다)
        #   (최단경로는 visited대신, INF -> 더 작은 값으로 업뎃됬는지 여부로, 방문 체킹을 할 수 있다)
        # => inqueue에는 cost는 다른 node가 올라가더라도, [꺼낸 후 처리]는 1개 node의 처리는 중복되면 안된다.

        # -> while로 돌릴 때, 최대 inqueue되는 갯수만큼 이루어지지만, 중복처리제거로 횟수를 낮춰야한다.
        # => 인접node탐색은 간선의 갯수만큼이루어진다 x 그 인접node탐색자체는 pop되는 갯수 == inqueue되는 갯수 == 간선의 갯수이다.
        # => E(pop되서 도는 while) * lg E (인접node들 이진힙에 삽입/삭제(pop))
        # => E개의 원소를 우선순위큐에 넣었다가 빼는 것과 직관적으로 유사 => ElgE
        # => E는 V^2보다 작다
        # => E lg V^2 -> 2 ElgV -> ElgV만큼의 시간복잡도보다 작다
        # => 다익스트라의 기본복잡도: O(ElgV)
        # => 간선의 갯수 10만개(10^6) + 노드의 갯수 1만개(10^4) -> lgV -> 10^2
        # => 간선갯수 10만개 * lg(노드갯수 1만개) -> 10^8 이하까지는 다 계산할 수 있게 된다.


        ## fix된 최초 최단경로node는 -> 인접node들 중에서, 최단경로 후보들 탐색하며, distance비교후, inqueue해야한다.
        for next_node, weight in graph[curr_node]:
            # 1) 인접node의 기존 총비용 in distance vs fix최단경로비용 + 연결된 비용을 비교한다.
            next_cost = distance[curr_node] + weight
            # 기존 총 비용보다 현재 경유경로의 비용이 더 작으면, 업뎃후 inqueue한다.
            if next_cost < distance[next_node]:
                distance[next_node] = next_cost
                heapq.heappush(heap, (next_cost, next_node))


if __name__ == '__main__':
    ###############
    # => my queue속 비용 업뎃은 [최단거리로서 fix된 node의 인접node로서, 가능성때문에 계속 업뎃],
    #    queue에서 나오는 순간, [최단거리fix된 node로부터 만들어지는 다음 최단거리 start]로,
    #    -> 방문체킹 + queue속 인접node들에게 [너네 최단경로에서 나가는 최단경로 후보node들이야. 나로부터 비용으로 예비자가 되도록 업뎃해주께]
    ###############
    # 1. 출발 노드 지정
    # 2. 최단 거리 테이블 초기화
    # 3. 방문한 적 없는 노드 중에서 최단 거리가 제일 짧은 노드를 선택
    # 4. 해당 노드를 거쳐 다른 노드로 가는 거리를 구하여 최단 거리 테이블을 업데이트
    # 5. 위 3, 4번 과정을 모든 노드를 방문할 때까지 반복

    ###############
    # 총 O(n)번 반복문(n-1번) 을 x distance짧은 것 (업데이트)탐색(V) -> O(V^2) 시간복잡도
    # python -> 1초에 2* 10^7 가능하므로, node가 5000개 이하 -> O(25x10^6) 라고 1초안에 가능하다
    #           만약 node의 갯수가 5000개이상의 10^4 -> 다익스트라 10^8 -> 1초안에 해결 불가능하다
    # => 매번 [비용이 가장 짧은 노드 선형 탐색 by for]하는 경우, 시간초과 나타날 수 있다.

    #############
    # n-1번(마지막node제외) 비용짧은node꺼낼 때, distance테이블 greedy선형탐색(n) 하지 않고,
    # -> lst기반 이진 힙(우선순위큐)을 이용하여 삽입/삭제하면 (lgN)으로 시간복잡도를 줄일 수 있다.
    import heapq as pq

    N, M = map(int, input().split())
    start = int(input().strip())

    # graph: 간선정보로 만드는 start 연결 정보
    # node의 갯수 N만큼  빈 list를 미리 만들어놓고, 간선정보가 입력되게 한다.
    # -> 이렇게 할 경우, 인접행렬이 아니므로 모든 node탐색을 할 필요가 없어진다.
    # -> row = start 번호랑 매핑되는 것. -> 0~ N까지 돌리기 위해 range(n+1)
    graph = [[] for _ in range(N+1)]

    # 다익스트라 필수 distance(최소비용) 테이블 (index = node매핑)
    # -> INF로 초기화하여, 업뎃여부로 visited 상태배열을 대신할 수 있다.
    INF = int(1e9) # 10의 9승 = 10억
    distance = [INF for _ in range(N+1)]

    # 정보를 받아 graph에 간선정보 입력하기
    for _ in range(M):
        u, v, weight = map(int, input().split())
        graph[u].append((v, weight))

    dijkstra(start)

    # 다익스트라를 돌고나면 distance에는 [시작 정점으로부터 해당node까지의 최소비용(최단거리)]가 기록되어있다.
    # -> 0번 node는 없으니 1번부터 출력해준다.
    for cost in distance[1:]:
        print(cost if cost != INF else "INIFINITY")
