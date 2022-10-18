import sys
from collections import deque

input = sys.stdin.readline


## 2-5.
##  (좌표, 시간) 정도면 tuple로 쓰는데, 여기서는 (좌표, 방향, 시간)으로 여러가지 요소가 등장하므로
##   튜플보다는 클래스를 활용한다.
## => robot은 2개의 Point로 이루어져있게 된다.
class Point:
    def __init__(self, row, col, dir, time):
        self.row = row
        self.col = col
        self.dir = dir
        self.time = time


## 9
def is_valid(block):
    for pt in block:
        ## 1) 2개를 행렬 좌표 확인
        if pt.row < 0 or pt.row > N - 1 or pt.col < 0 or pt.col > N - 1:
            return False
        ## 2) Board상 장애물 확인
        if Board[pt.row][pt.col] == 1:
            return False
        ## 3) 원래는 inqueue전에 방문여부 확인후 방문체킹인데, 여기서 해버린다.(inqueue직전이니 상관없다)
        ##   => 방문여부는 방향성까지 포함한다고 했다.
        if Visited[pt.row][pt.col][pt.dir]:
            return False
    return True


## 14.
def rotate(curr, ccw, idx):
    ## (1) 마찬가지로 회전된 newPt(새로운 Point객체 List)를 만들어 낼 것이다.
    newPt = []
    ## (2) 회전된 좌표 만들어내기 -> 그림의 가운데가 회전축: ![image-20221016162742759](https://raw.githubusercontent.com/is3js/screenshots/main/image-20221016162742759.png)
    ## => a는 회전축인덱스idx를 둔다고 한다. b는 a가 아닌 나머지 인덱스를 주어서
    ##    curr[a]: 회전축Pt, curr[b]: 나머지Pt로 쓸 수 있게 한다.
    #    (1) a가 0이면, b는 1   =>  b = idx + 1
    #    (2) a가 1이면, b는 2가 되는데, 이것을 % 2를 통해 0으로 만든다. => b = (idx + 1) % 2
    #  => 회전축 기준으로 방향도 기억해둔다.
    a = idx
    b = (idx + 1) % 2  # index가 1개만 들어올 때, 나머지 index를 뽑아낸다.
    dir = curr[a].dir # 회전축좌표의 방향은 -> 회전축이 아닌 좌표curr[b]에서 회전으로 인한 좌표이동시 어디로 회전할지를 나타내느정보로서 뽑아놔야한다.

    ## (3) 회전축의 새Pt를 만들자. => 회전축은 위치좌표는 바뀌지 않으니, 그대로 쓴다 :그림의 가운데가 회전축: ![image-20221016162742759](https://raw.githubusercontent.com/is3js/screenshots/main/image-20221016162742759.png)
    ## (4) 문제는 방향이다. 시계방향부터 생각하자.
    # 회전축이 U(0) + 시계방향 회전 -> R가 된다 => 1개 증가한 값이 되서 편하다 (1)
    # 회전축이 R + 시계방향 회전 -> D -> curr[a].dir + 1 (2)
    # 회전축이 D + 시계방향 회전 -> L -> curr[a].dir + 1 (3)
    # 회전축이 L + 시계방향 회전 -> U -> curr[a].dir + 1(4) => (X) => 4가 아닌 0으로 바꿔야한다.
    # => 1씩 증가하다가 k일 때 0되어아하면 % k 로 나머지연산해준다!!!
    ## => (curr[a].dir + 1) % 4
    # newPt.append(
    #     Point(curr[a].row, curr[a].col,
    #           (curr[a].dir + 1) % 4,
    #           curr[a].time + 1)
    # )
    ## (5) 반시계방향 회전일때는 ? 회전축이라면, 위치는 그대로고, 방향만 달라진다.
    # 회전축이 U(0) + 반시계방향 회전 -> L(3)가 된다 => 0을 4라보면 1개 감소다.
    # 회전축이 L(3) + 반시계방향 회전 -> D(2) -> curr[a].dir -1
    # 회전축이 D(2) + 반시계방향 회전 -> R(1) -> curr[a].dir -1
    # 회전축이 R(1) + 반시계방향 회전 -> U(0) -> curr[a].dir -1
    ## => 나머지연산은 0 - 1 => -1음수가 나오는 경우는 연산이 안되므로
    ## => 시계/반시계회전되는 상황에서 나머지 연산을 해야할 때, 반시계로 -1을 하는 대신
    ## => 전체갯수(4) - 1(반시계방향) =  +3 => -1을 빼는 대신, +3을 더해줘서 나머지가 음수가 안나오게 만든어 나머지 연산을 하낟.
    ## => ccw가 1로 반시계인 경우에만 +3으로 나머지 연산해서 방향을/ 시계방향의 경우 +1로 나머지연산을 해준다.
    newPt.append(
        Point(curr[a].row, curr[a].col,
              (curr[a].dir + (3 if ccw else 1)) % 4,
              curr[a].time + 1)
    )

    ## (6) 회전축이 아닌 좌표 curr[b]는 회전할때마다 위치도 바뀐다.
    ## => 상하좌우 움직일때처럼, 바뀌는 drow, dcol의 DELTA값 Drot를 정의해주고 온다.

    ## 17. Drot 정의를 끝내고, 회전축아닌 좌표 curr[b]의 회전을 시행한다.
    # -> 현재좌표 + Drot[ccw][회전축좌표의방향UPorRight..][row=0 or col=1]
    ## 18. 바뀌는 방향은 회전축의 방향변화 (+1 or +3) % 4 와 동일하다.
    ##    반시계시 D -> R 로 바뀐다.  U R D L 순서로 봤을 때, -1인데 -> 4개반복이므로 -> +3으로 대체하고 %4 연산하는 것과 동일하다
    newPt.append(
        Point(curr[b].row + Drot[ccw][dir][0], curr[b].col + Drot[ccw][dir][1],
              (curr[b].dir + (3 if ccw else 1)) % 4,
              curr[b].time + 1)
    )
    ## 19. 회전으로도 새로운좌표가 만든 것이므로 유효한지 확인해야한다.
    if is_valid(newPt) == False:
        ## 가짜면 0을 반환하자.
        return 0

    ## 20. 일단 회전은 시켰지만, 또 확인해야한다. 회전하는 중간이 0으로 비어있어야한다.
    ## => 일단 회전시켜놓고, 모서리를 확인한다.
    ## => 모서리도 delta를 이용해서 확인한다. 인덱스는 Drot와 동일하게 쓸 것이다.
    ##   즉, 회전축의 방향을 기준으로 확인하는 점을 delta로 구성한다.

    ## 21. 회전축 curr[a]를 기준으로, 모서리(corner)가 0인지 board장애물 확인한다.
    if Board[curr[a].row + Dcor[ccw][dir][0]] [curr[a].col + Dcor[ccw][dir][1]] == 1:
        return 0

    ## 22. 여기까지 왔으면 유효한 회전이므로, 방문마킹 후 inqueue해야한다.
    ## 마킹은 pt별 방향마다 마킹하고, queue에는 ptList를 inqueue한다.
    for pt in newPt:
        ## 23. 회전 유효좌표들에 대해서도 종착역을 방문체킹/inqueue전에 종착역을 확인한다.
        ## => 목적지 도착한 경우만 시간반환, 그외 0 반환
        if pt.row == N -1 and pt.col == N-1:
            return pt.time
        Visited[pt.row][pt.col][pt.dir] = True
    Q.append(newPt)


if __name__ == '__main__':
    ## 블록이동하기: https://school.programmers.co.kr/learn/courses/30/lessons/60063
    board = []
    for _ in range(5):
        board.append(list(map(int, input().split())))

    ## 1. 다른함수 속에서 재할당되는 것들 or 매번 인자로 가서 확인해야하는 변수들은 전역변수로 만들어놓기
    ## (1) 매번 board르 전역변수로 넘기는 것은 번거로우니 전역변수Board에 담아 사용한다. => 장애물 확인해야할 땐 board 전역변수화
    ## (2) 정사각행렬 board의 크기도 전역변수N으로 담아 사용한다.
    ## (3) bfs에 사용할 queue도 전역변수에 담아서 사용한다.
    ## (4) visited도 전역변수로 사용한다 => 가장 바깥쪽 차원부터 안쪽에서 선언해야한다.
    ## => board의 크기에 따라 선언해도 되지만, 전역변수로 먼저 만들어놓으려면 최대크기100으로 만들어놓으면 된다.
    Board = []
    N = 0
    Q = deque([])
    Visited = [[[False] * 4 for _ in range(100)] for _ in range(100)]
    # in solution
    # global Board, N, Q, Visited
    Board = board
    N = len(board)

    ## 2. bfs탐색을 하기 전에, 좌표탐색을 하기 위해서 Point라는 class를 정의한다

    ## 3. inqueue -> 2개의 좌표를 2개의 point객체로 넣으면서, 1묶음으로 [point1, point2]로 넣는다.
    ## => nbyn말고 3차원의 방향 문자열 -> index매핑은, 종류가 많고 기억하기 어려우면, dict["문자열"] = index로
    ##    단순0부터 매핑이며, 쉽다면, 그냥 문자열을 변수명 = 0 에 매핑하면 된다.
    ## => 위에서부터 시계방향으로 1씩 증가하도록 index를 매핑한다. => 회전을 for문으로 1씩 증가하게 하려면 이렇게 한다.
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    D = ((-1, 0), (1, 0), (0, -1), (0, 1),)
    ## 15. 회전축 아닌 좌표의 회전시 움직이는 DELTA깞 Drot: https://raw.githubusercontent.com/is3js/screenshots/main/image-20221016172456221.png
    ## => 상하좌우처럼, delta가 (1,1) ~ (-1, -1)안에서 끊기니 정의해놓고 사용한다.
    ##    회전축의 방향이 UP인 경우, 나머지좌표는 회전축위에있다. 회전축 방향이 R인 경우, 나머지좌표는 회전축오른쪽에 있다
    ## => 회전축의방향을 활용해서 UP->RIGHT->DOWN->LEFT을  순서대로 [시계방향이동시 필요한 delta]를 정의한다.  ex> Drot[UP] -> 회전축 위에 2번재 좌표 -> 시계방향 이동시 -> 행아래로+1,열오른쪽+1
    ## => 행   감소or증가 판단 => 열  감소or증가 판단하면서 delta를 작성하자.
    # Drot = (
    #     (1, 1), # UP (회전축이 UP을 보는 방향으로서, UP위치에 2번재 좌표가 있으며, 시계방향회전시 [행부터] + 1 [열은] + 1
    #     (1, -1), # RIGHT
    #     (-1, -1), # DOWN
    #     (-1, 1), # LEFT
    # )
    ## 16. 반시계방향으로도 회전하느 delta가 필요하며, ccw 0과 1로 나타내니,
    ##  => tuple이 되도록 ([0] 시계방향detla, [1] 반시계방향delta)형태로 만들어준다.
    Drot = (
        ((1, 1), (1, -1), (-1, -1), (-1, 1)), # 시계방향
        ((1, -1), (-1, -1), (-1, 1), (1, 1)) # 반시계방향
    )

    ## 21. 회전축좌표의 방향을 기준으로 확인해야할 모서리 detla를 Dcor로 정의한다
    # -> Drot를 복사해서 수정해서 사용하자. 회전방향 생각하는것과 비슷?
    Dcor = (
        ((-1, 1), (1, 1), (1, -1), (-1, -1)),  # 시계방향
        ((-1, -1), (-1, 1), (1, 1), (1, -1))  # 반시계방향
    )

    Visited[0][0][RIGHT] = True
    Visited[0][1][LEFT] = True
    Q.append([Point(0, 0, RIGHT, 0), Point(0, 1, LEFT, 0)])

    ## 4. deque
    while Q:
        curr = Q.popleft()
        ## 5. 상하좌우부터 이동한다. -> 인덱스는 j부터 쓰는데, i는 Point 2개를 구분할 때 쓴다.
        for j in range(4):
            ## 6. 새로운 좌표들(PtList)은 newPt = [] 빈 리스트에 저장할 것이다.
            newPt = []
            ## 7. 좌표가 2개니까 또 반복문을 돌려 만들어낸다. -> 상하좌우 이동시 방향은 바뀌지 않는다.
            for i in range(2):
                newPt.append(
                    Point(curr[i].row + D[j][0], curr[i].col + D[j][1],
                          curr[i].dir,
                          curr[i].time + 1)
                )
            ## 8. 새로운 좌표가 유효한지 검사 by is_valid(newPT)가 == False를 반환하면 continue로 skip
            if is_valid(newPt) == False: continue

            ## 10. 유효한 좌표들을 방문표시(for문으로 개별로)후 inqueue
            for pt in newPt:
                #### 11. bfs는 방문체킹<-> 방문표시 사이에 inqueue전에 좌표를 확인해서
                ####     종착역을 inqueue전에 처리해서, 필요한 것을 반환? 혹은 break하게 한다
                if pt.row == N - 1 and pt.col == N - 1:
                    # return pt.time
                    print(pt.time)
                    exit() # 반복문 2개 이상깊이부터는 break로종료X exit

                Visited[pt.row][pt.col][pt.dir] = True
            Q.append(newPt)

        ## 11. for j in range(4) 상하좌우와같은 레벨로, 회전을 처리한다.
        ## 회전은 시계/반시계 다 해야한다. counter clock wise -> 0이면 시계 / 1이면 반시계
        for ccw in range(2):
            ## 12. 회전축도 2개 중 아무거나 다될 수 있다. -> 0이면 첫번째 좌표 / 1이면 2번재 좌표가 회전축
            for i in range(2):
                ## 13. curr(현재위치, 좌표2개) +   ccw(방향) + i(회전축)으로 rotate를 구현한다
                # rotate(curr, ccw, i)  # i 0 -> 첫번째좌표, i 1 ->2번째좌표를 회전축으로 각각 쓸 경우
                ## 24. rotate결과로 종착역도착시 pt.time이 반환, 아니면 0이 반환된다.
                ret = rotate(curr, ccw, i)
                if ret:
                    # return ret
                    print(ret)
                    exit()

    ## 25. 문제에서 종착역에 도착한다고 했으나, 디버깅용으로 return 0
    print(0)
    exit()
