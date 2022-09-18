import sys

input = sys.stdin.readline


def poll_smallest_node_in_distance():
    # index로 묶여있으니, index로 탐색해서, 그 index를 node로 활용해야한다.
    min_cost = INF
    min_cost_node = 1 # 업뎃 안됬으면, 최소값을 가진 node는 1이므로 1으로 초기화한다.
    for index in range(1, N+1):
        # queue가 아니므로, 방문 마킹확인해서, 방문안한 것만 조회한다.
        if visited[index]:
            continue
        # 당시의 index(start)를 알아야하므로, min()이 아닌 if로 최소값 업뎃 + index를 건져낸다.
        if distance[index] < min_cost:
            min_cost = distance[index]
            min_cost_node = index
    return min_cost_node # 해당node를 반환한다.




def dijkstra(start):
    # 시작node는 이전 최단경로가 업뎃해주지 않으므로 0으로 최단거리를 미리 업뎃해준다.
    distance[start] = 0

    # 횟수를 N회가 아닌 n-1회만 돌리는 이유: 맨 마지막node는 인접node를 탐색하지 않도록?
    # => 방문하지 않은 것들을 탐색해야하므로, queue를 안쓴다면, 횟수만큼 돌려야한다
    # => 그 횟수는, 처음부터, 마지막 직전node까지만 탐색하면 된다.
    # => 맨 마지막node는 탐색하지 않아도, [방문처리만 안됬을 뿐, 기존 fix 최단경로들이 업데이트 해놧을 것]이다.
    #    만약, INF로 유지된다면, 아예 경로가 없다는 뜻이다.
    # => 만약, 마지막node도 탐색을 한다면, distance에 자신을 제외하곤, 꺼내져서 방문마킹 되어있으니
    #    distance내에서 방문안된, 제일 짧은 것 node를 pop하더라도
    #    제일 짧은 것이 자기자신 -> INF(or 업데이트 된 값)-> 최소값 업뎃안되고, 초기화된 지역변수 값만 나와서
    #    -> 오류가 난다.
    # for row in range(n):
    for _ in range(N):
        # distnace내에 총비용이 가장짧은 것을 꺼낸다 -> 최단경로로부터 만들어진 최단경로 후보
        curr_min_node = poll_smallest_node_in_distance()
        # 꺼냈으면, 최단경로 확정으로서 방문 마킹한다.
        visited[curr_min_node] = True
        # print(curr_min_node, distance[curr_min_node]) # 최단경로 확정된 것들만, 다음것 탐색전에 로 출력
        # -> 맨 마지막 것은 탐색할 node없어서 탐색하지 않는다?

        # 이제 최단경로와 인접한node들을 업뎃해준다.(queue/테이블속 다음 최단경로 후보들)
        for next_node, next_cost in graph[curr_min_node]:
            cost = distance[curr_min_node] + next_cost
            # if cost < distance[next_node]:
            #     distance[next_node] = cost
            distance[next_node] = min(distance[next_node], cost)


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


    INF = int(1e9)
    N, M = map(int, input().split())
    start = int(input().strip())

    visited = [False for _ in range(N+1)]
    # 다익스트라에서 우선순위큐를 안쓰는 최단거리테이블은 INF로 초기화하는 list
    # -> node와 index값으로 암묵적으로 묶임.
    distance = [INF for _ in range(N+1)] # 최대node명이 N이라면, 0부터 n+1까지..(인접행렬은 0부터 시작)


    # graph = [[0 for row in range(n+1)] for row in range(n+1)]
    # graph를 행렬로 그리면, 인접node들의 목록을 받아볼 수 없기 때문애
    # -> dict나, 2차원 빈 행렬에 인접node + 가중치를 tuple로 append하자
    # -> dfs, bfs와 다르게, 모든node를 탐색하지 않고, 인접node만 탐색하도록 함.
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v, w = map(int, input().split())
        # graph[first][second] = w
        # graph는 인접행렬이 아닌, 각u마다 빈 행렬에 second, weight를 append한다.
        # -> graph[first]로 접근하면 (인접node1, w1), (인접node2, w2)로 나타나서
        # -> 반복문을 돌리면, 인접node + weight를 동시 접근할 수 있다.
        # -> 반복문에 걸었는데, []로 없으면 반복문이 자동skip되서 좋다.
        graph[u].append((v, w))

    # 다익스트라는, root start(시작 정점)이 필수다
    dijkstra(start)

    # 다익스트라를 다 돌고나면, distance가 최단경로들로 업뎃되어있다.
    # => 다익스트라는, [start부터 모든 정점별 최소비용]이므로, 최단경로를 만드는 진행경로가 아니다.
    # => 이미 정해진 정보라서 출력해주면 된다.
    for cost in distance[1:]:
        print(cost if cost != INF else "INF")



