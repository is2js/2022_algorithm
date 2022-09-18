import heapq
import sys

input = sys.stdin.readline

import heapq as pq

def dijkstra(start_node):
    # 다익스트라 특징: 시작node의 비용은 0으로 미리 업뎃해놓고 뽑아야, 반복문 속 자식뽑혀서 하는 것과 동일해짐
    distance[start_node] = 0
    # 최소비용을 가진 node를 뽑아, 최단경로를 만드는데, 우선순위큐를 사용하기 위해, 자료구조 및 초기갑 ㅅ선언
    heap = [] # 우선순위큐의 기반 lst
    pq.heappush(heap, (0, start_node)) # 우선순위큐에는 (시작정점으로부터 총비용, 해당node)의 tuple을 입력


    # 다익스트라 특징: 반복 횟수 == 최소비용으로 뽑힌 횟수 == 마지막node를 제외한 수만큼만 추출
    # for row in range(V - 1): -> 자료구조 도입으로 인한, 반복횟수 직접 지정 안해도 됨.
    while heap:
        curr_cost, curr_node = pq.heappop(heap)

        # visited[curr_node] = True # 방문배열 대신, distance의 업뎃여부를 통해, 방문을 확인한다.
        # -> 넣순대로 나오는 queue가 아니라면, 방문체킹은 꺼낸 뒤 한다.
        # -> INF로 초기화 되어있어서 최소 1번은 업뎃되고, 그 업뎃이 최단경로 확정이자 방문체킹이다.
        if distance[curr_node] < curr_cost: continue

        for next_node, additional_cost in graph[curr_node]:
            # 최단경로(curr_node)를 부분 최단경로해서 해서 만들어질, 최단경로 후보들은
            # 기존값보다 더 작아진다면, 우선순위큐에 집어넣어, 먼저 나오게 한다.
            if distance[curr_node] + additional_cost < distance[next_node]:
                distance[next_node] = distance[curr_node] + additional_cost
                heapq.heappush(heap, (distance[next_node], next_node))




if __name__ == '__main__':
    # 1. 출발 노드 지정
    # 2. 최단 거리 테이블 초기화
    # 3. 방문한 적 없는 노드 중에서 최단 거리가 제일 짧은 노드를 선택
    # 4. 해당 노드를 거쳐 다른 노드로 가는 거리를 구하여 최단 거리 테이블을 업데이트
    # 5. 위 3, 4번 과정을 모든 노드를 방문할 때까지 반복

    # greedy 최소비용 선형탐색 O(N) -> 우선순위큐(heapq)를 이용한 O(lgN)으로 줄임.

    INF = float('inf')
    V, E = map(int, input().split())
    start_node = int(input().strip())
    #visited = [False] * (V + 1)  # 순서중요 탐색용 방문배열 -> 우선순위큐 사용시 visited불필요
    distance = [INF] * (V + 1)  # 최소비용 테이블

    # 인접행렬을 빈 행(first)렬(second)에 모아서, 반복문시 graph[first]만으로 정보((second, weight)튜플) 존재하는 것만 탐색
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):  # 간선정보를 인접행렬에 입력
        u, v, weight = map(int, input().split())
        graph[u].append((v, weight))  # 가중치 존재 간선정보는 (second, weight) 튜플로 u별 빈행렬에 입력

    dijkstra(start_node)  # 다익스트라는 시작정점 -> 모든 정점 최단거리 테이블 갱신

    for cost in distance[1:]:  # 0번 node안쓸 경우, index강제포함 0을 제외하고 출력
        print(cost if cost != INF else "INF")  # 최단경로 없음 -> INF에서 업뎃안됨 -> 문자열로 출력






