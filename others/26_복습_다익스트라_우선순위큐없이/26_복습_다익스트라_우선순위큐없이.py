import sys

input = sys.stdin.readline


def poll_smallest_cost_node_in_distance():
    min_of_cost = INF
    min_of_cost_node = 1  # 최소값 노드 탐색시, 초기값은 시작정점으로 통상알려진 최소값을 반영하게 한다.
    # distance를 돌면서 최소값을 찾되, 그 위치의 visited를 매번확인해야하므로, value가 아닌 inex로 돈다.
    # -> index도 1부터 돌아서 검색한다( 0번 node안씀 )
    for curr_node in range(1, len(distance)):
        # queue(inqueue전 방문마킹)가 아니므로, 꺼내고 나서 방문마킹하는 데, [꺼낼 때 조회를 직접한다면, 조회시 돌면서 제외시키자]
        # -> 돌면서(조회) 최소값을 찾는 데, 방문이미 한 것(존재x)은 제외시키고 조회하도록 한다.
        if visited[curr_node]: continue
        # 최소값을 찾고, 최소값 반환이 아니라, 그 때의 node를 꺼내줘야한다.
        if distance[curr_node] < min_of_cost:
            min_of_cost = distance[curr_node]
            min_of_cost_node = curr_node
    return min_of_cost_node


def dijkstra(start_node):
    # 다익스트라 특징: 시작node의 비용은 0으로 미리 업뎃해놓고 뽑아야, 반복문 속 자식뽑혀서 하는 것과 동일해짐
    # -> 자식은 최소비용 업뎃후 뽑힐 수 있음
    distance[start_node] = 0

    # 다익스트라 특징: 반복 횟수 == 최소비용으로 뽑힌 횟수 == 마지막node를 제외한 수만큼만 추출
    # -> 마지막node는 뽑아도, 이미 다 방문, 뽑힌 상태라서, 업뎃안되고 최소비용 찾을 때 초기값node만 튀어나와서 오류
    # -> 1~N까지 node -> N-1번만 반복한다.
    for _ in range(V - 1):
        # distance테이블에서 최소비용 node를 뽑는 것으로부터 시작된다. start_node가 0으로서 먼저 뽑힐 것이다.
        curr_min_cost_node = poll_smallest_cost_node_in_distance()
        # 현재 최소비용 node가 뽑힘 -> 최단경로 확정 -> 방문체킹
        visited[curr_min_cost_node] = True
        #                        -> 부분 최단경로로서 -> 인접node들 중 최단경로들을 업뎃 -> 새로운 최단경로 후보들을 만든다
        for (next_node, additional_cost_to_next) in graph[curr_min_cost_node]:
            new_total_cost = distance[curr_min_cost_node] + additional_cost_to_next
            distance[next_node] = min(distance[next_node], new_total_cost)


if __name__ == '__main__':
    INF = float('inf')
    V, E = map(int, input().split())
    start_node = int(input().strip())

    visited = [False] * (V + 1)  # 순서중요 탐색용 방문배열
    distance = [INF] * (V + 1)  # 최소비용 테이블

    # 인접행렬을 빈 행(first)렬(second)에 모아서, 반복문시 graph[first]만으로 정보((second, weight)튜플) 존재하는 것만 탐색
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):  # 간선정보를 인접행렬에 입력
        u, v, weight = map(int, input().split())
        graph[u].append((v, weight))  # 가중치 존재 간선정보는 (second, weight) 튜플로 u별 빈행렬에 입력

    dijkstra(start_node)  # 다익스트라는 시작정점 -> 모든 정점 최단거리 테이블 갱신

    for cost in distance[1:]:  # 0번 node안쓸 경우, index강제포함 0을 제외하고 출력
        print(cost if cost != INF else "INF")  # 최단경로 없음 -> INF에서 업뎃안됨 -> 문자열로 출력
