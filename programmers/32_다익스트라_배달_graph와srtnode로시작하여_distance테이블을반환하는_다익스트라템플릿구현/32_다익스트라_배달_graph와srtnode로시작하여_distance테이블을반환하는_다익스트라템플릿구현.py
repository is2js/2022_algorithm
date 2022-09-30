import heapq
import sys
 
input = sys.stdin.readline

def dijkstra(srt_node):
    ## 최다비용 distance 테이블을 INF로 초기화 -> 첫node는 0으로 [방문(최단비용맞나)체크생략 + 테이블업뎃 + inqueue]하고 시작
    INF = float('inf')
    distance = [INF] * (N + 1)

    ## queue관련은 inqueue전 방문 체크 -> 표시 -> 아는 것 모두 inqueue해놓고 pop해서 확인주체(기준)이 된다.
    # 첫 node는 방문체크 생략. 표시만 하고 inqueue
    distance[srt_node] = 0 # 방문표시 대신, distance테이블에 srt부터의 비용 o을 넣는다.
    pq = [] # 다익스트라는 deque의 queue가 아니라, 우선순위큐
    heapq.heappush(pq, (0, srt_node)) # (cost, node)

    ## queue는 존재한다면, 기준을 빼서 시작한다.
    while pq:
        ## queue는 inqueue전 방문체크하니, 뽑을 땐 편하게 뽑아쓴다. (뽑고나서 방문검사X)
        curr_cost, curr_node = heapq.heappop(pq)

        ## queue에서 직후peek을 검사하는 것이 아니라, graph에서 후보들을 꺼내서 검사한다
        ## (1) 방문체크 되신 경유비용(curr최단비용 + 경유 추가비용 < 기존 최단비용)일 때만 inqueue가 허용된다.
        ## (2) 방문표시 대신 distnace테이블 업뎃 -> (경유 총 비용, node)로 distance테이블 업데이트
        for next_node, additional_cost in graph[curr_node]:
            ## 방문체크 대신, 최단비용체크 (현재로부터 경유해서 더 오래걸리면 탈락)
            if distance[curr_node] + additional_cost >= distance[next_node]:
                continue
            ## 방문안한 새로운 최단비용(curr최단비용 + 경유 추가비용 < 기존 최단비용) 일 경우 -> table업뎃 + inqueue
            distance[next_node] = distance[curr_node] + additional_cost
            heapq.heappush(pq, (distance[next_node], next_node))

    return distance

if __name__ == '__main__':
    ## 배달: https://school.programmers.co.kr/learn/courses/30/lessons/12978
    ## 시작node로부터 최단거리 구하기 -> 다익스트라?!
    N, road_num = map(int, input().split()) # 2차원road -> road_num은 내가 만듦

    graph = [[] for _ in range(N + 1)]

    for _ in range(road_num):
        a, b, c = map(int, input().split())
        graph[a].append((b, c)) # (다음node, 비용)로 append
        graph[b].append((a, c))
    # print(graph)

    k = int(input().strip())

    ## (1) 최단거리문제는, bfs로 queue에 방문체크하고 넣어서, 다음번째 오는 놈들을 중복허용안하고 안받아서, 최단거리만 고집한다
    ##     최단거리 1짜리일 때, 거리를 물어보지 않는다면, 방문배열이 필요하지만,
    ##     distance 테이블(INF초기화)에 srtnode -> 각 node별 걸리는 거리를 기록해야한다면, visited(False초기화)를 대체한다.
    ## => 비용테이블을 inf로 초기화한다


    ## (2) 다익스트라는 (graph, 시작정점)으로 시작하며, 내부에서 src -> 각 node별 최단비용 distance테이블을 채워 반환한다.
    distance = dijkstra(graph, 1)


    def dijkstra(graph, srt_node):
        ## 최다비용 distance 테이블을 INF로 초기화 -> 첫node는 0으로 [방문(최단비용맞나)체크생략 + 테이블업뎃 + inqueue]하고 시작
        INF = float('inf')
        distance = [INF] * (N + 1)

        ## queue관련은 inqueue전 방문 체크 -> 표시 -> 아는 것 모두 inqueue해놓고 pop해서 확인주체(기준)이 된다.
        # 첫 node는 방문체크 생략. 표시만 하고 inqueue
        distance[srt_node] = 0  # 방문표시 대신, distance테이블에 srt부터의 비용 o을 넣는다.
        pq = []  # 다익스트라는 deque의 queue가 아니라, 우선순위큐
        heapq.heappush(pq, (0, srt_node))  # (cost, node)

        ## queue는 존재한다면, 기준을 빼서 시작한다.
        while pq:
            ## queue는 inqueue전 방문체크하니, 뽑을 땐 편하게 뽑아쓴다. (뽑고나서 방문검사X)
            curr_cost, curr_node = heapq.heappop(pq)

            ## queue에서 직후peek을 검사하는 것이 아니라, graph에서 후보들을 꺼내서 검사한다
            ## (1) 방문체크 되신 경유비용(curr최단비용 + 경유 추가비용 < 기존 최단비용)일 때만 inqueue가 허용된다.
            ## (2) 방문표시 대신 distnace테이블 업뎃 -> (경유 총 비용, node)로 distance테이블 업데이트
            for next_node, additional_cost in graph[curr_node]:
                ## 방문체크 대신, 최단비용체크 (현재로부터 경유해서 더 오래걸리면 탈락)
                if distance[curr_node] + additional_cost >= distance[next_node]:
                    continue
                ## 방문안한 새로운 최단비용(curr최단비용 + 경유 추가비용 < 기존 최단비용) 일 경우 -> table업뎃 + inqueue
                distance[next_node] = distance[curr_node] + additional_cost
                heapq.heappush(pq, (distance[next_node], next_node))

        return distance

    print(len([node for node, cost in enumerate(distance[1:], start=1) if cost <= k]))
