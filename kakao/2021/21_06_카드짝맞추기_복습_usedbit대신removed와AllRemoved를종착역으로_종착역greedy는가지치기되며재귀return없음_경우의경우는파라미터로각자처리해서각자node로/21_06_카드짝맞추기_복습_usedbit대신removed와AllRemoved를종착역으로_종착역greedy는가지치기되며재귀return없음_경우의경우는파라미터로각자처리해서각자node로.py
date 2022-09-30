import sys
from collections import deque

sys.setrecursionlimit(10_000)
input = sys.stdin.readline


def bfs(removed, src, dst):
    global BOARD
    ## (13) 재방문을 안할 경우, dst가 있어도 bfs자체의 visited는 사용된다.
    visited = [[False] * 4 for _ in range(4)]

    visited[src[0]][src[1]] = True
    q = deque([src])  # src는 3번째에 cost까지 들고 있는 좌표다.

    while q:
        row, col, cost = q.popleft()
        ## (14) 종착좌표가 있는 bfs는 꺼내자마자 확인해서, 종착역에서 3번째 원소에 최단거리를 반환한다
        if row == dst[0] and col == dst[1]:
            return cost

        ## (15) 자식좌표들 탐색진행 및 최단거리 업뎃하여 inqueue
        for d_row, d_col in DELTA:
            n_row, n_col = row + d_row, col + d_col
            if not (0 <= n_row <= 3 and 0 <= n_col <= 3): continue

            ## bfs필수 inqueu전..
            if visited[n_row][n_col]: continue
            visited[n_row][n_col] = True
            q.append((n_row, n_col, cost + 1))

            ## (16) 거리추가없이 ctrl+움직임 구현하기
            # => (1) n_row, n_col만 [갈 수 있는만큼 업데이트] 한다.
            #        while break -> 진행횟수가 정해져있으면 for 횟수 break로 돌린다.
            #       [조건] no cursor로서 (1) 현재위치기 장애물card가 아니여야함
            #                           (2) 다음위치가 유효한 좌표
            for _ in range(2):
                ## (17) 현재자리의 카드있나 확인 -> board[][]카드번호 -> removed 제거된 상태(1)인지 0이면 탈락-> break
                ## => 이미 n_row, n_col은 q에 들어간 상태이므로, 가변변수로서 활용해도 된다.
                if removed & (1 << BOARD[n_row][n_col]) == 0: break
                ## (18) 현재위치에서 더 나아갈 수 있다면, 현재의 DELTA로 이동한 뒤, 좌표유효검사
                # n_row, n_col = n_row + d_row, n_col + d_col
                # if not (0 <= n_row <= 3 and 0 <= n_col <= 3): break
                ## (19) break에 걸리기 전에 업뎃하면 가변변수가 유효하지 않은 상태에서 멈추므로
                ## => 그 직전까지 while break 탐색은, [업데이트 전에 가상값으로 검사하여 if break]
                ## my) 그때상태에서 if break => 업데이트 후 넘어와서 break걸리게
                ##     그 직전까지가 유효하다 => 업데이트 하지말고 [가상의 다음값]으로 if break
                ## => 가변변수를 그 탈락탐색의 직전(유효한 마지막)으로 유지하려면, next로 업뎃전에 검사해서 break한다.
                if not (0 <= n_row + d_row <= 3 and 0 <= n_col + d_col <= 3): break
                n_row, n_col = n_row + d_row, n_col + d_col
                ## => 그까지 탐색용 횟수반복문은, break될때까지 업데이트 하고, 이후로직은 반복문 나가서 처리한다.

            ## (19) break에 걸리기 직전상태(유효한 최대상태)의 n_row, n_col을 queue에 넣어준다.
            ## => inqueue전에 방문검사는 필수다.
            if visited[n_row][n_col]: continue
            visited[n_row][n_col] = True
            q.append((n_row, n_col, cost + 1))

    ## (20) 종착역이 잇는 bfs는 종착역 못찾을때 처리를 해준다.
    return float('inf')


def permutate(removed, control_count, src):
    ## 함수를 정의하면 global로 공통변수들을 땡겨쓰자
    # global BOARD, COORDS_OF_CARD, AllRemoved
    ## (6) 재귀로 greedy를 한다면 -> 가변변수를 전역변수를 선언해놓고, 종착역에서 누적값 그리디를 한다.
    global BOARD, COORDS_OF_CARD, AllRemoved, MinControlCount
    ## (7) [재귀로 누적결과값을 전역변수 greedy]를 한다면, 종착역위에서 [return 가지치기]가 가능하다.
    if control_count >= MinControlCount:
        return

    if removed == AllRemoved:
        MinControlCount = min(MinControlCount, control_count)
        ## (6-1) 재귀로 경우의 수별 집계를 전역변수로 한다면, return만 명시해주면 된다.
        return

    ## (8) 순열은 자신의처리 없이, 바로 자식들처리에서 경우의수iter를 for문 반복해서 경우의수를 넘어간다.
    ##    이 때, [파라미터에 경우의수 선택시 처리된 값으로 업데이트]하여 넘기는데,
    ##    여기서는, 각 경우의수마다 2가지 경우의수가 나오므로, 다 처리 => 각각 경우의수node를 뻗어야하므로
    ##    카드선택마다 3(123) * 2(순차/역순)을 [for 3 -> 각 2개의 node]를 만들어서, [6개의 node]로 뻗어나간다
    ##    => permuatete카드선택 후 카드처리순서까지 선택을 해야, 다음 카드선택permutate까지 넘어오기 때문에
    ##    => permutate의 기준인 [다음 카드 선택]이 나올 때가지 미리 모든 경우의 수를 한 permutate함수에서 끝내야하기 때문이다.
    for number, coords in COORDS_OF_CARD.items():
        ## (9) 순열은, userd_bit검사를 자식들 넘어갈때만 한다. 방문체킹은 파라미터에서 한다.
        ##  cf) dfs-stack => 자신의처리에서 방문표시 => 자식들방문체킹만
        ##      bfs-qeueue => inqueue전 방문체킹, 방문표시
        ##      dfs-순열 => 자식들 방문체킹 => 파라미터에서 방문표시
        if removed & 1 << number: continue
        ## (10) 각 카드선택마다, 2가지 순차/역순 2가지 node를 뻗어야한다.
        ##   => 이 때, 경우의 수는 [각 경우의수마다 처리된 값을 파라미터]에 넣어서 처리하므로
        ##   => node를 뻗기전에 2가지 경우의 처리를 해서 업데이터 파라미터를 구해야한다.
        ## (11) 순차: 선택된 카드를 0번 좌표까지 이동 -> 1번까지좌표로 이동한 조작횟수
        ##           최단거리니 bfs를 활용한다
        ##           bfs는 시작점 + visited => 종착역 없이 다차셔 더이상 queue에 node X로 종착역이거나
        ##           bfs   시작점, 도착점 => while q에서 꺼내자마자 바로 종착역 확인
        # -> enter를 입력해야하므로 중간에 +1 씩 해준다.
        # -> bfs로 구해지는 값은 조작횟수다.
        # ordered = bfs(src=src, dst=coords[0]) + 1 + bfs(src=coords[0], dst=coords[1]) + 1

        ## (12) 좌표탐색에서, bfs가 최단거리르 반환한다면, 딱히 다른 파라미터가 필요없지만
        ## => ctrl + 방향키로 인해, 갈 수 잇는 만큼 가야한다?
        ## => 1칸은 기본적으로 [커서]로서 움직인 상태에서,
        ##    ctrl움직임은 [no 커서]로서 (1) 움직인 현재자리가 board속 장애물인card가 아니면서 (2) 유효한 좌표일때,
        ##    최단거리를 증가시키 않고 움직임으로서, ctrl움직임을 구현할 수 있다.
        ##    [직전 => 다음자리에 장애물 검색을 하지 않는 이유]는 직전에는 커서였기 때문이다.
        ##    [1] 커서로서 1칸 움직임믄 카드장애물을 인식하지 않고 유효하면 inqueue된다
        ##    [2] ctrl움직임은, [노 커서]로서 [시작부터, 현재자리에 카드가 있는지]통과되면 움직인다.
        ##                    시작부터 확인하니, 다음좌표에는 돌아와서 현재 카드있는지를 재활용확인한다
        ## => 이 때, ctrl움직임을 위해, 현재자리BOARD[i][j] => removed로 카드제거된 상태(1)인지 확인해야한다.
        ##    연속적인 움직임을 할 때는, 장애물상태변수인 removed가 필요하므로 파라미터로 넣어준다.
        ordered_control_count = bfs(removed=removed, src=src, dst=coords[0]) + 1 + bfs(removed=removed, src=coords[0],
                                                                                       dst=coords[1]) + 1
        reverse_control_count = bfs(removed=removed, src=src, dst=coords[1]) + 1 + bfs(removed=removed, src=coords[1],
                                                                                       dst=coords[0]) + 1
        ## (21) 경우의수 안에 경우의 수는, 각각을 직접 계산처리해서 그 값의 파라미터로 넣어준다
        ##   => global전역변수로 종착역을 처리한다면, 재귀함수에 return값이 없다
        permutate(removed | 1 << number, control_count + ordered_control_count, coords[1])
        permutate(removed | 1 << number, control_count + reverse_control_count, coords[0])

if __name__ == '__main__':
    ## 카드짝맞추기: https://school.programmers.co.kr/learn/courses/30/lessons/72415
    board = [list(map(int, input().split())) for _ in range(4)]
    r, c = map(int, input().split())

    ## 매번 독립 경우의 수(사라지지 않고 순서중요 선택 -> for)가 아니라
    ## 순열(사라지면서 1개씩 선택, 순서중요)을 위한 재귀 / 조합(사라지면서 1개씩 선택. 순서안중요) / bfs 등
    ## function 안에서 1개의 board만 가지고 놀아야한다면 전역변수로 선언해놓고, 함수에서는 global로 쓴다.
    BOARD = board
    COORDS_OF_CARD = dict()
    ## (2) 사라지면서 나열하는 순열을 위해 visited(used_bit)가 필수지만,
    ##     stack의 결정변수가 순열 원소 사용갯수cnt가 종착역이 아닐 수 있으며, used_bit로 종착역을 만든다면
    ##     매핑된 자리수가 모두 1로 만든 것이있어서 visited == 111111로 비교해야한다.
    ##     bit로 모두 불을 들어오게 만들 때, 이미 갯수를 알고 있다면, (1<<n - 1)으로 만들 수 있지만,
    ##     갯수가 동적으로 바뀐다면, 매번 [bit자리에 매핑할 숫자]마다 등장시 (| 1<<k)로 불을 켜줘야한다.
    ##  => visited대신, removed를 사용할 수 있으며,
    ##  => [bit를 종착역]으로 쓰고 싶다면 [모두 제거확인은 AllRemved라는 것을 매핑할 수등장시마다 쉬프트해서 1기록해주기]를 해야한다.
    ## => 0번카드는 이미 제거되었다고 bit에 매핑해놓는다. => removed의 출발은 0이 아닌 1로 시작한다.
    AllRemoved = 1
    MinControlCount = float('inf')
    DELTA = ((-1, 0), (1, 0), (0, -1), (0, 1),)

    ## (1) [행렬위에 경우의 수를 결정짓는 value의 좌표]가 들어가 있으면
    #   -> hash(dict)에 매핑 -> 자식들처리로서 경우의 수 node선택시 ->  hash.items()로 돌면서 처리되게 한다.
    for i in range(len(board)):
        for j in range(len(board[i])):
            card_number = board[i][j]
            if not card_number: continue
            ## (3) 사용여부visited==removed bit에 매핑할 수가 등장할때마다, 1로 불을 켜주면
            ##     종착역에서 다 사용시 bit 값 비교로 비교할 수 있다.
            # AllRemoved = AllRemoved | 1 << card_number
            AllRemoved |= 1 << card_number
            ## 누적value, 컬렉션value는 key검사를 하고, 없으면 최초의 값과함꼐 초기화한다.
            if card_number in COORDS_OF_CARD:
                ## 좌표가 bfs를 탈 것이라면, 미리 시작좌표로서 2번째 원소에 자기자신의 최단거리 cost 0을 포함시킨다.
                # COORDS_OF_CARD[card_number].append((i, j))
                COORDS_OF_CARD[card_number].append((i, j, 0))
            else:
                COORDS_OF_CARD[card_number] = [(i, j, 0)]

    # print(bin(AllRemoved)) # 0b1111  0번은 원래제거된 상태로주기. 123번카드까지 존재한다.
    # print(COORDS_OF_CARD) # {1: [(0, 0, 0), (3, 2, 0)], 3: [(0, 3, 0), (3, 0, 0)], 2: [(1, 0, 0), (2, 3, 0)]}
    # 경우의 수를 돌릴 값들은 자료구조에 매핑해놓고, for 로 돌려서 경우의 수node를 뻗어나간다.

    ## (4) 1,2,3번 중에 카드를 1개 선택한다(순열) -> 각 경우의 수마다, 2개의 카드를 또 선택해야하는 순열이온다.
    ## = 1번카드 -> 0번->1번 or 1->0번, [for문의 각 경우의수node]마다  [각 경우의 수에 맞게 처리 -> 반영된 node 2개]로 뻗어나가야한다.
    # permutate(removed=1, control_count=0) # 순열을 지탱해줄 removed 및 누적결과값인 조작횟수
    ## (5) 경우의 수안에서 bfs를 써야한다면, 시작좌표도 같이 줘야한다.
    ##     bfs가 최단거리를 구한다면 좌표에 cost를 0으로 시작하도록 준다
    permutate(removed=1, control_count=0, src=(r, c, 0))

    print(MinControlCount)
