import sys

input = sys.stdin.readline

from collections import deque

## (6) 마지막 bfs를 작성한다. queue를 이용한다. 상하좌우를 위해서 DELTA를 정의한다.
D = ((-1, 0), (1, 0), (0, -1), (0, 1))


def bfs(place, row, col):
    visited = [[False] * 5 for _ in range(5)]

    q = deque([])
    visited[row][col] = True
    ## inqueu시 거리까지
    q.append((row, col, 0))

    while q:
        curr = q.popleft()

        #### (7) 거리는 맨하탄거리==최단거리 2까지만 검색하면 된다. 3이상은 종착역으로 짤라야한다.
        #### => 이 떄, [재귀가 아닌 bfs q탐색은, 가치지치를 continue]로 한다.
        ####    break하면 전체 bfs탐색이 종료되므로, 원하는 곳 1개만 찾는 [종료지점]이 아닌 이상
        ####    [bfs 가치치기는 continue로 skip] 하자
        if curr[2] > 2:
            continue
        #### (아직 거리2 이하)
        ## => 종료되어야할 종착역은 2이내에서, P를 만나는 경우다 (parition시 진입못하는 것은 아래에서)
        # if place[curr[0]][curr[1]] == 'P':
        #### 조심!! 종착역이 P인 좌표인데, 시작점도 P이므로,
        ####      시작과 같은 값의 확인시에는 [처음이 아니라는 추가조건]을붙여줘야한다.
        #### => 시작위치 == 거리가 0인 좌표 가 아니면서(and)
        #### my) 장애물 확인요소와 시작점이 같을 경우, 시작점아닐때를 먼저 명시
        if curr[2] != 0 and place[curr[0]][curr[1]] == 'P':
            ## 가치지기가 아닌 1개의 종착역이면 return으로 끝낸다.
            return False
            ## break가 아니라 return이라서 남은 q를 걱정할 필요 없다
            ## 만약, 종착역에 안걸리면 성공return True인데,
            ##    bfs는 점점 cost가 커지면서 2를 초과하면서 continue로 스킵되어 자식을 못뻗으므로
            ##    queue는 계속 popleft되면서 비어지게 된다. -> while문끝나면 성공이다.


        ## (거리2이내, P안만난 상태 )
        for i in range(len(D)):
            nr = curr[0] + D[i][0]
            nc = curr[1] + D[i][1]
            if nr < 0 or nr > 4 or nc < 0 or nc > 4:
                continue
            if visited[nr][nc]:
                continue
            #### (8) partition은 visiste처럼 이동할 수 없는 좌표이다.
            #### -> 거리두기는 2이내 P에 도달하면 종료이며
            #### => [parition은 visited와 같은 개념으로서, skip으로 해당 경로로 방문못하게 한다]
            if place[nr][nc] == 'X': continue

            visited[nr][nc] = True
            q.append((nr, nc, curr[2] + 1))

    else:
        return True


def check(place):
    ## (2) 응시자 위치를 찾는 것은 2차원배열을 탐색해서 p인지 아닌지 찾아보는 것이다.
    for r in range(5):
        for c in range(5):
            if place[r][c] == 'P':
                ## (3) P위치마다 bfs를 호출해주면 된다.
                ##     cursor개념의 visited되에, board위에 장애물 표시까지 알아야한다면
                ##     시작좌표 외에 배열도 같이 인자로 줘야한다.
                # bfs(place, r, c)
                ## (4) bfs는 2이내 P를 만나게 될 경우, False를 반환하게 할 것이다.
                ##    1칸이상의 flag는 이처럼 return으로 바로 끝낸다.
                if bfs(place, r, c) == False:
                    return False
    ## (5) 깊은곳의 if만 return False(flag-break)라면, 가장바깥의 for문과 동일선상에
    ## -> 다 돌면 통과이므로 return True 1개만 주면 된다.
    return True




if __name__ == '__main__':
    ## 거리두기확인하기: https://school.programmers.co.kr/learn/courses/30/lessons/81302
    places = [list(input().split()) for _ in range(5)]

    #### 유클리디언:2점의 거리, 맨하탄: 축별 거리의 합 => 한 축에만 2점이 존재하면, 유==맨
    #### 2차원에서의 최단거리 == 상하좌우로 몇번이동했나 == 맨하탄거리와 동일하다.
    #### 거리두기의 확인대상은, [각 응시자별 맨하탄거리 2까지만 확인]하면 된다!
    # -> 그 이후로는 거리두기 안지켜도 상관없다.
    #### => 우리는 bfs로 거리2만큼만 이동하면 된다.
    #### bfs는 dfs와 달리 [1칸마다 갈 수 있는  상하좌우를 동시에 움직이는 개념 -> visited는 동시의 다른길에서 재방문이 최단거리가 아니어서 짜른다]이다.
    #### X는 parition으로 막혀서, 갈수 없는 곳으로 잘라내서 -> 거리두기ok로 취급한다.
    #### -> 거리2이내에 && parition으로 안막히는 최단거리 && P가 안나와야지 통과
    ####    거리2이내면서 O로 열린 길이 p가 나오자마자 탈락이다. => partition으로 막히면 더이상 진행못해서 거리두기 통과된다.
    # 그림:https://raw.githubusercontent.com/is3js/screenshots/main/image-20220927214905383.png

    answer = []

    for place in places:
        ## (1) 각 대기실마다 check(place) -> True반환되면 거리두기 지키는 것
        if check(place):
            answer.append(1)
        else:
            answer.append(0)

    print(answer)