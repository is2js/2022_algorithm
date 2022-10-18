import sys
from collections import deque
from dataclasses import dataclass
from typing import List

input = sys.stdin.readline

Board = []
N = 0
Q = deque([])
Visited = [[[False] * 4 for _ in range(100)] for _ in range(100)]
UP, RIGHT, DOWN, LEFT = range(4)

D = ((-1, 0), (1, 0), (0, -1), (0, 1),)  # 상하좌우 순서에 따른 index에 (drow, dcol) 매핑
#### 22.  ccw(0,1)순서에 따른index(1) / 회전축회전방향(dir, UP/RIGHT/DOWN/LEFT)순서에 따른index(2)에 (drow, dcol)매핑
####      에 따라 회전축아닌 2번째 좌표가 움직일 DELTA
Drot = (
    # ccw 0 -> 회전축방향: UP(0) / RIGHT(1) / DOWN(2) / LEFT(3)
    ((1, 1), (1, -1), (-1, -1), (-1, 1)),
    # ccw 1 ->
    ((1, -1), (-1, -1), (-1, 1), (1, 1))
)
#### 25.
Dcor = (
    # ccw 0 -> 회전축방향: UP(0) / RIGHT(1) / DOWN(2) / LEFT(3)
    ((-1, 1), (1, 1), (1, -1), (-1, -1)),
    # ccw 1
    ((-1, -1), (-1, 1), (1, 1), (1, -1)),
)


@dataclass
class Point:
    row: int
    col: int
    time: int
    dir: int


def is_valid_point(points: List):
    for pt in points:
        # 새 좌표 범위 검사
        if not (0 <= pt.row <= N - 1) or not (0 <= pt.col <= N - 1):
            return False
        # 새 좌표 장애물 검사
        if Board[pt.row][pt.col]:
            return False
        # 새 좌표 방문체킹 => 방향성까지 검사한다.
        if Visited[pt.row][pt.col][pt.dir]:
            return False
    return True


def rotate_bfs(ccw, rot_axis_index, curr_points):
    #### 17. 경우의 수에 따른, 회전 new_points를 만들고, 전역Queue에 집어넣을 것이다.
    ## 일반 bfs의 while Q내부에서, curr가 나온상태며, next -> 종착역시 값return 아니면 0return -> inqueue까지 수행한다.
    new_points = []
    #### 18. 경우의 수에 따라, rot_axis_index가 정해지면, 나머지 좌표는 자동으로 뽑을 수 있어야한다.
    ## => 회전축좌표의 index를 a, 나머지좌표를 b로 만들자.
    a = rot_axis_index
    # b =  rot_axis_index가 0이면, 1  반대로 1이면 0이 되어야한다
    # b = rot_axis_index + 1 # 0 -> 1
    # b = rot_axis_index + 1 #  1 ->  2가 되니, % 2로 나머지 연산해주면 된다.
    ## => [정해진 갯수에서 환형으로 만드려면, 1씩 증가 하면서 총갯수로 나머지연산]
    b = (rot_axis_index + 1) % 2
    #### 21. 회전축좌표의 방향에 의해 나머지좌표들의 회전이 정해지니 -> 회전축좌표의 방향은 a,b,와 함께 미리 저장해둔다.
    a_dir = curr_points[a].dir

    #### 19. 회전축좌표 curr_points[a]부터 회전시키자.
    # (1) 좌표는 이동이 없다
    # (2) 방향이 바뀐다. 시계0방향이면 UP -> RIGHT / RIGHT -> DOWN   => 직전방향 + 1
    #                  반시계1방향이면, UP -> LEFT / LEFT -> DOWN   => 직전방향 - 1
    # (3) 시간 + 1
    #### 0~3 4개로 회전방향을 잡았으면, 반시계는 직전방향 - 1 대신 (4-1) + 3으로 이동하는 것으로 보고 나머지연산을 해주면 똑같은 위치에 속한다
    #### => 반시계는 -1씩 줄어가는 가되 나머지 연산일 것인데,  -1 대신 총갯수-1로 돌려서 나머지 연산시킨다
    new_points.append(
        Point(
            curr_points[a].row, curr_points[a].col,
            curr_points[a].time + 1,
            (curr_points[a].dir + (3 if ccw else 1)) % 4,
        )
    )

    #### 20. 회전축아닌좌표 curr_points[b] 회전시키기.
    #### (1) 좌표가 이동되는데, [ccw]에 따라 달라지며, ccw결정이후 이동DELTA를 결정짓는 것은 [회전축좌표의 방향dir]가 결정한다
    #     예를 들어  D  이라면 D의 curr좌표는 U라는 방향성에 의해 ↓ → R 쪽으로 이동해야만한다.
    #              U
    #### 21. 회전축좌표의 방향에 의해 나머지좌표들의 회전이 정해지니 -> 회전축좌표의 방향은 a,b,와 함께 미리 저장해둔다.
    ## -> a, b, dir
    #### 22. ccw에 따라 dir에 따라 -> row, col의 DELTA까 정해지니,
    ####     [ccw]의 순서마다 / [dir] 순서마다 => (drow, dcol)을 DELTA를 매핑한다
    ####    원래는   [상하좌우] 순서마다 => DELTA를 매핑햇었으니,
    #### => ccw를 앞차원으로서 -> 정의시에는 더 바깥에서, 순서에 따른 경우의수마다 [dir순서에 따른 drow, dcol]을 매핑해준다.
    ## 23.
    new_points.append(
        Point(curr_points[b].row + Drot[ccw][a_dir][0], curr_points[b].col + Drot[ccw][a_dir][1],
              #### 24. ccw에 따라 회전 방향도 달라지는데,
              # 시계 D -> L / L -> U / U -> R / R -> D 으로 시작만다르지, 값으로 1씩 증가하는 것은 똑같다.
              # 반시계 D -> R / R -> U / U -> L / L -> D 으로 시작만 다르지, 값으로 -1씩 감소, +3씩 증가+나머지연산은 똑같다
              curr_points[b].time + 1,
              (curr_points[b].dir + (3 if ccw else 1)) % 4,
              )
    )

    ## 24. 회전된 새 좌표에 대해 범위+장애물+종착역검사를 한다
    if not is_valid_point(new_points):
        ## 앞에서는 main내부라서 유효하지않으면 continue로 skip했지만
        ## => 여기는 함수내부라서 continue가 아니라, 종착역이 아닐때의 기본반환값 0으로 끝낸다.
        ##    각 경우마다 아닌 것에 대해서는, 0 -> 밖에서는 0을 스킵하거나 필터링한다.
        return 0
    #### 25. 회전된 새 좌표에 대해 범위+장애물+종착역 이외에 [회전상태에 따른 모서리 장애물]검사가 추가되었다.
    # -> 이 역시 ccw별 a_dir별에 따라 검사해야하는 좌표가 고정값으로 달라지니, 각 회전축좌표curr_points[a]에 대해 모서리DELTA를 매핑해놓고 매번 검사하게 한다
    ##   ccw별 회전방향별 회전축좌표에 더해져야할 DELTA를 통해 Board에서 회전가능한지 장애물 검사를 한다.
    if Board[curr_points[a].row + Dcor[ccw][a_dir][0]][curr_points[a].col + Dcor[ccw][a_dir][1]]:
        # continue
        return 0
    #### 26. 새좌표가 모든 검사들을 통과(범위+장애물+방문체킹+회전장애물까지)했으면
    ## (1) 종착역 검사
    ## (2) 종착역 아니라면, 방문표시 -> inqueue
    for pt in new_points:
        if pt.row == N - 1 and pt.col == N - 1:
            return pt.time
        Visited[pt.row][pt.col][pt.dir] = True
    Q.append(new_points)


if __name__ == '__main__':
    ## 블록이동하기: https://school.programmers.co.kr/learn/courses/30/lessons/60063
    board = []
    for _ in range(5):
        board.append(list(map(int, input().split())))

    ## 1. 장애물확인용 board와 그 길이는 [다른함수에서도 쓸 수 있게 전역변수]로 만들어 쓴다.(함수인자로 주어진다면)
    ## -> 함수내에서 주어진 것을, global선언후 -> 전역변수 기본값 선언 -> 같은값을 전역변수에 재할당
    # global Board, N
    Board = board
    N = len(board)
    ## 2. queue를 함수들 사이에서도 조절할이 있다면, 전역변수로 만들어 쓴다.
    ## 3. 방문배열도 전역변수로 만들어서, 다른함수에서도 체킹가능하게 한다.
    #### 4. 2개 이상의 점을 1set로 방문체킹하려면?
    ## => a-b 와 a 는 서로 다른 방문이므로, => 좌표당  0/1이 아니라 좌표당/방향당 0/1로 표시해야한다.
    ##           b
    #### 방향성은, 좌표set의 중심을 향하도록 정한다
    ## => R-L 와 D  으로 표시하면,   시작좌표에는 [0][0][R] = 1 과 [0][0][D] = 1 다르게 마킹된다.
    ##           U
    #### 방문배열은, n by n 2차원 + 방향의 종류4개(UP/RIGHT/DOWN/LEFT)를 업을수 있는 차원 1개를 더 추가한다.
    ## => 개념적으로 생각해본다면, 3차원 각 방향당 n by n이 1개씩 저장공간이 주어지는 것으로 생각할 수 있다.
    ## => 원래는 n by n의 각 좌표마다 4개의 저장공간이 추가된 것이지만,
    ##    전체적으로 생각하면, n by n 이 총 4개(방향별 nn방문배열)가 각각 생성된 것이라고 볼 수도 있다.
    ## 5. 방향을 index로 쓰기 위해 매핑한다. dict에 'UP': 0으로 매핑해도 되지만, 여기선 0부터 순서대로 주어질 땐, 그냥 상수변수에 index를 매핑한다

    #### 6. 2개의 좌표를 묶어서, queue에 넣고 bfs탐색해ㅐ야한다.
    ## => row,col,cost외에 dir방향성까지 붙었으니, 튜플로 관리하지말고
    ##   class Point로 좌표를 관리하며, 객체list를 좌표set으로 처리한다.

    ## 7. bfs 시작. 2개의 좌표set을 방문체킹후 inqueue
    # -> queue에는 Point객체 list를 입력한다.
    Visited[0][0][RIGHT] = True
    Visited[0][1][LEFT] = True
    Q.append([Point(0, 0, 0, RIGHT), Point(0, 1, 0, LEFT)])

    while Q:
        curr_points = Q.popleft()

        for drow, dcol in D:
            ## 8. [좌표2개 set]부터는 list로 움직이며, [next좌표도 빈[] -> for i in curr_list_갯수 -> 1개씩 list에 append]로 만들어낸다.
            new_points = []
            for i in range(len(curr_points)):
                new_points.append(
                    Point(
                        curr_points[i].row + drow, curr_points[i].col + dcol,
                        curr_points[i].time + 1,
                        curr_points[i].dir, # 2set 상하좌우 이동시에는, 방향성은 변하지 않는다.
                    )
                )
            ## 9. 새 좌표 검사 -> list는 범위검사를 바로 못하니 is_valid함수를 활용한다.
            #### 10. 새좌표에 대해, 범위검사 + 장애물검사까지 한다.
            #### => 2set 돌리는 김에 [방문체킹]도 같이한다.
            if not is_valid_point(new_points): continue

            #### 12. 새좌표 범위+장애물+방문체킹까지 완료했다면
            ## => 방문표시 전 [종착역]검사부터 하고  -> 종착역 아니면 [방문체킹]을 각각해준다.
            ## => 2좌표중 1개라도 종착역이면 게임 종료이며, 그 때까지의 소요시간(최단거리)를 반환한다
            for pt in new_points:
                if pt.row == N - 1 and pt.col == N - 1:
                    print(pt.time)
                    exit()
                #### 13. 종착역이 아니면, 방문표시하고, => inqueue는 list로 한다.
                Visited[pt.row][pt.col][pt.dir] = True
            Q.append(new_points)

        #### 14. 상하좌우D 이동외에, 회전DELTA를 써서 new_points를 만들어야한다, counter clock wise여부를 먼저 결정한다
        # -> 0이면 시계 / 1이면 반시계방향을 의미한다.
        for ccw in range(2):
            #### 15. 여러개의 좌표를 회전한다면, [좌표갯수만큼 경우의 수를 돌며, 회전축을 지정]해야한다.
            for i in range(len(curr_points)):
                #### 16. 회전방향(ccw) + 회전축좌표(i)의 경우의 수에 따른 new_points -> bfs까지를 수행하는 함수를 수행한다.
                #### => rotate된 new_points를 받지말고, [bfs의 종착역에 걸리는 경우]에 값을 반환 아니면 0반환하는 함수로 정의한다.
                ####    현재 while Q: -> curr deque까지 한 상태에서 -> ( next by rotate -> 검사 -> 종착역 확인 -> inqueue) 까지의 상황을 수행한다.
                ####    모든 변수들이 전역변수라서, 메서드로 만들고, 거기서 수행해도 된다.
                #### => 경우의 수에 따라 수행할 땐, 함수로 만들어서, 각각의 경우를 지정해서 수행하게 하자
                #### => bfs()함수는 종착역이라면, 그때의 값을 / 아니라면 0을 반환하게 할 것이다.
                result = rotate_bfs(ccw, i, curr_points)  # 경우의 수에 따른, bfs 수행
                if result:
                    print(result)
                    exit()

    ## Q를 다 돌았는데도 종착역을 못찾았으면 아웃
    print(0)
    exit()
