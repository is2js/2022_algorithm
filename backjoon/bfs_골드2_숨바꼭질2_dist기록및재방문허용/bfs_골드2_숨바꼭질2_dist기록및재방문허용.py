import sys
from collections import deque

input = sys.stdin.readline

if __name__ == '__main__':
    ## https://www.acmicpc.net/problem/12851
    N, K = map(int, input().split())

    MAX = 100_000

    def bfs(start):
        ## start부터 걸린시간/횟수를 세는 배열 -> dist[next] = dist[curr] + 1로 업데이트
        dist = [0] * (MAX + 1)
        # => 만약, visisted와 겸용으로 사용하려면, -1로 초기화한다.
        #    dist 0을 방문한 것으로 간주하기 위해서는 if dist != -1로 방문체킹해야한다.
        # dist = [-1] * (MAX + 1)

        ## 재방문 금지를 위해 if visitied:로 검사하고
        ## 최단거리 재방문 허용하려면, if visisted and dist[next] != dist[curr] + 1로 최단거리 아닌 조건까지 추가하여 검사한다.
        ## 방문횟수를 카운팅하려면, visited += 1로 체킹한다
        visited = [False] * (MAX + 1)

        queue = deque()  # bfs-queue는 이중연결리스트인 collections.deque를 활용한다
        ## 암기) bfs는 자료구조queue를 이용할 때, inqueue전에 방문마킹하여 -> 경유node라면 무시시킨다.
        dist[start] = 0
        visited[start] += 1 # 재방문 허용의 상황일 땐, 방문 횟수를 카운팅 한다. 아니라면 visited = True
        queue.append(start)  # 자신도 루프에 등록 -> 자료구조에서 맨처음 넣고, 나와서 자신이 되는 업데이트를 root_node부터 적용시키기

        # visit_count = 0
        while queue:
            curr = queue.popleft()

            ## 자신의 처리 -> 이미 방문체킹한 후보들만 꺼내니, 따로 체킹안해줘도된다. 넣을때만 하자.
            # print(curr, end=" ")
            # if curr == K:
            #     visit_count += 1

            # 자식들 처리 -> 일단 탐색은 모든node들을 다돌리고 필터링
            for next in [curr - 1, curr + 1, curr * 2]:
                # 좌표이동은 이동해놓고 1순위로 범위검사부터 한다.
                if not (0 <= next <= MAX):
                    continue
                # if dist[next]: # 거리 기록이 있다면 방문체크로서 건너띈다.
                #     continue
                ## 최단거리는 방문 허용할 때는, 추가조건을 붙여서 재방문을 방지한다.
                if visited[next] and dist[next] != dist[curr] + 1:
                # if dist[next] != -1 and dist[next] != dist[curr] + 1:
                    continue
                dist[next] = dist[curr] + 1
                visited[next] += 1

                queue.append(next)

        return dist[K], visited[K]


    dist, count = bfs(N)
    print(f"{dist}\n{count}")
