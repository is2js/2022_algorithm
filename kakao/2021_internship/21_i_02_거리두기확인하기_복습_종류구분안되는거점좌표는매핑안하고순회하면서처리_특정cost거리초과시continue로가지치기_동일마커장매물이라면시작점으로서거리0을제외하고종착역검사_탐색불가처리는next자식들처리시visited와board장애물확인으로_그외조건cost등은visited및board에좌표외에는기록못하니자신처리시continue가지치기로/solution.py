import sys
from collections import deque

input = sys.stdin.readline


def bfs(place, row, col):
    visited = [[False] * 5 for _ in range(5)]

    ## 7. inqueue전에 방문표시
    visited[row][col] = True
    q = deque([])
    q.append((row, col, 0))

    while q:
        cr, cc, cost = q.popleft()

        ## 8. bfs탐색시, 가지치기는 continue로 한다.
        # => 거리2초과하는 좌표들은 아예 탐색안하고 못간다 -> visited?
        ##   => 좌표를 통한 가지치기(진입불가)는 자식들next좌표를 가지치기 ex> visited, board
        ##   => cost 등 좌표외에 탐색불가 조건은 자신의 처리에서 continue로 가지치기
        if cost > 2: continue

        ## 9. 동일한 마커장애물이라면, 시작좌표(거리0)는 제외하고 종착역을 설정한다.
        if cost != 0 and place[cr][cc] == 'P':
            return False

        for dr, dc in DELTA:
            nr = cr + dr
            nc = cc + dc
            if not (0 <= nr <= 4 and 0 <= nc <= 4): continue
            if place[nr][nc] == 'X': continue  # 좌표관련 장애물 가지치기. like visited
            if visited[nr][nc]: continue
            visited[nr][nc] = True
            q.append((nr, nc, cost + 1))

    else:
        return True


def check(place):
    ## 3. 각 p의 위치마다 시행한다. (미리 p의 좌표를 모아둘 필요 없다??)
    ##  my) collection에 모아둬야. for문돌리면서 경우의 수로서 순서대로 돌아갈텐데..
    # => P들이 서로 구분이 되지 않으면, 나열(순열, 조합)문제가 아니므로 [모아놓고 자식들로서 탐색]안해도 된다.
    # => 각 [P들 좌표]에서 bfs를 돌릴테므로, index로 순환한다.
    for row in range(len(place)):
        for col in range(len(place)):
            ## 4. 종류구분이 없어서 순서대로 탐색만 할 때, P가 발견되면, 그 지점에서 bfs를 돌린다.
            ## => bfs가 T/F를 반환할 수 있다.
            # P만 찾는다면 나머지를 skip해서 indent를 줄인다.
            if place[row][col] != 'P': continue
            ##  5. bfs를 돌릴 때, visited이외에 [장애물이 있는 board]면, 인자로 같이 주던지 global선언한다.
            ##  -> 시작좌표만 주어진다면, r, c는 개별인자로 / 시작끝좌표를 동시에 준다면, (,,0)(,,0) tuple로 인자를 주자.
            ## => bfs로 거리2이하에서 & P에 도달하면  발견False,  거리2이하를 다돌았는데 P발견 못하고 끝나면 True다. 
            if bfs(place, row, col) == False:
                return False
    ## 6. 다돌면서 & P마다 bfs돌면서& bfs로 거리2이하에서 P를 발견못한 경우 모두 True만 반환해서 다돌았을 때
    ## break는 1개의for만 취소시키는 flag지만, return은 2중이라도 괜찮다. 맨 바깥for문에 else를 달아 처리하자
    else:
        return True


if __name__ == '__main__':
    ## 거리두기확인하기: https://school.programmers.co.kr/learn/courses/30/lessons/81302
    places = [list(input().split()) for _ in range(5)]

    DELTA = ((-1, 0), (1, 0), (0, -1), (0, 1),)

    ## 1. 맨하탄거리 -> bfs 최단거리  / parition -> 막혀서 못가는 visited개념
    ##    각 p에 대해 맨하탄 2이하(초과시 가지치기)에 대해서, bfs p -> p에 도달하면 탈락
    answer = []
    for place in places:
        ## 2. check로 성공(bfs도달X)하면 1, 실패(맨하탄2이하 p->p 도달)하면 0
        if check(place):
            answer.append(1)
            continue
        answer.append(0)

    print(answer)