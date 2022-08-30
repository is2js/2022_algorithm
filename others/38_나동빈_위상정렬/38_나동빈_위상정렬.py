import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## 위상정렬: [싸이클없는 방향그래프DAG]에서 방향성 유지한체 순서대로 나열하는 방법
    # ex> 선수과목을 고려한 학습순서 설정
    # 자료구조 -> 알고리즘
    # 자료구조 -> 고급 알고리즘
    # 알고리즘 -> 고급 알고리즘
    # => 자료구조 -> 알고리즘을 들어야 -> 고급 알고리즘을 들을 수 있을 때

    # 진입차수 indgree : 들어오는 방향 간선의 갯수
    # 진출차수 outdgree : 나가는 방향 간선의 갯수

    # 위상정렬 : dfs도 가능하지만 queue를 이용해, [(방향)싸이클없는 방향그래프DAG]에서 방향성 유지한체 순서대로 나열하는 방법
    # (0) 각 node의 [진입차수 매핑배열]에 계산한다
    # (1) 진입차수가 0인 node를 queue에 넣는다.
    # (2) queue가 빌 떄까지
    # (2-1) 꺼낸 node의 나가는 간선(진출차수, outdgree)들을 graph(진입차수 매핑배열)에서 제거(-1)
    # (2-2) 새롭게 진입차수가 0이 된 node를 queue에 넣기
    # => 각 노드가 queue에 들어온 순서 == 위상정렬 순서
    # => 싸이클이 존재하는 node는 진입차수가 항상 1이상이 되어 queue에 안들어온다
    # => 한 단계에서 진입차수가 0이되는 node가 여러개 존재할 수 있으므로, 넣는 순서를 정해줌에 따라 답이 여러개 일 수 있다.
    # => 모든 node를 방문하기 전에 queue가 비어버린다면, 방향싸이클이 존재한다고 판단할 수 있다.
    # 성능분석: 전체node순회하면서 진입차수배열 생성 O(V) ->이후 각 간선들 제거 O(E)
    #          queue에 들어간 node와 나가는 간선들 확인 -> O(V + E)
    from collections import deque

    v, e = map(int, input().split())
    # (1) 진입차수 매핑배열을 만든다 (0으로 초기화) -> graph(인접빈행렬) 만들 때, 같이 채운다
    indegree = [0] * (v + 1)
    # (2) 간선정보를 저장할 graph
    graph = [[] for _ in range(v + 1)]
    # (3) 간선 정보 입력
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)  # 간선 등록
        indegree[b] += 1  # 각 node별 진입차수 등록


    def topology_sort():
        result = []  # queue에서 꺼내자마자 append한 순서 = 위상정렬 순서
        q = deque()
        # 진입차수가 0인 것을 찾아서 자료구조queue에 삽입
        for i in range(1, v + 1):
            if indegree[i] == 0:
                q.append(i)

        while q:
            curr = q.popleft()
            result.append(curr) # 꺼낸 순서가 위상정렬

            # 꺼낸 원소의 진출차수(outdgree)에 해당하는 node들의 진입차수배열에서 -=1씩 해준다.
            for next in graph[curr]:
                indegree[next] -= 1
                # 깍았을 때, 진입차수배열의 값이 0인 것은 자료구조에 넣어줘서 다음타자가 되게 한다. (작은 순서대로 돌고 있음)
                if indegree[next] == 0:
                    q.append(next)

        # 결과 출력
        print(*result)

    topology_sort()





    pass
