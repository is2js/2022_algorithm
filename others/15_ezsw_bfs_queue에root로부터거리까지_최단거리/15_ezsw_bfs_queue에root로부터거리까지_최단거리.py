import sys

input = sys.stdin.readline

from collections import deque

def bfs(srow, scol, drow, dcol):
    ## [3] 재귀가 아닌 dfs-stack이나 bfs-queue는 메서드안에서 끝나므로 visisted를 지역변수로 선언한다.
    ##     순서가 중요한 node탐색은 visisted를 써서 중복으로 사용되는 것을 막는다.
    ##     -> 2차원 좌표에 대한 visisted는 2차원으로 False배열을 만든다.
    visited = [[False for _ in range(N)] for _ in range(N)]

    ## 좌표탐색은, 각 좌표가 node이며, [상하좌우를 고정된 인접행렬없는 인접node들]라고 생각한다.
    ##           edge간선들은, 상하좌우 1개씩 같은 가중치 or 가중치가 없는 간선으로 본다.
    queue = deque()

    # [4] queue를 통한 bfs는 inqueue전에 visisted를 마킹해서, 중복inqueue를 막는다고 했다.
    #     node를 [queue에 넣은 순서대로 명백하게 먼저 방문]하므로, [인접node탐색시 중복탐색을 막는다]
    #     cf) dfs-stack을 이용할 땐, 모든node를 다 탐색하며 stack에 집어넣지만,
    #         (1) 넣은순서대로 실행되지 않고, (2) 인접행렬 정보에 따라 무엇이 먼저 실행될지 모르니
    #         -> visited마킹없이 일단 집어넣고,
    #         -> 먼저 pop되어 방문되는 것을 visisted마킹하여, 다음 pop되어 나오는 것은 continue로 pass하게 한다
    #         -> 메모리 비효율적인 dfs-stack이다.
    visited[srow][scol] = True
    # [5] node가 아닌 좌표를 inqueue할때는 튜플로 묶어서 넣는다.
    #     이 때, [최단거리를 판별하기 위해]
    #     -> 좌표뿐만 아니라 [root로부터의 거리 == depth이자 level]를 queue에 같이 튜플로 묵어저 집어넣는다.
    #    (현재x좌표, 현재y좌표, 간선거리)
    queue.append((srow, scol, 0)) # bfs로 최단거리를 구할 경우, node(좌표)뿐만 아니라 [root로부터 거리]를
    # myqueue.put()

    while queue: # while not myqueue.empty():
        curr = queue.popleft() # myqueue.get()

        ## [6] 다음 node탐색하기 전에, stack/queue의 종착역을 만들어준다.
        ##     현재위치가 도착지점이면, 거리를 return해준다. (좌표는 x행좌표,y열좌표를 직접 꺼내 비교한다. 객체아니면)
        if curr[0] == drow and curr[1] == dcol:
            return curr[2] # root로부터 거리

        ## [7] 아직 도착지점이 아니라면, 다음node를 탐색한다.
        for i in range(len(D)):
            # [8]행좌표 업뎃 / 열좌표 업뎃 / 거리도 업뎃해줘야하는데, 인라인되는 거라서...
            nr = curr[0] + D[i][0]
            nc = curr[1] + D[i][1]
            nd = curr[2] + 1 # 거리가 별 지정 안되어있으면 1이다.

            # [9] 좌표의 업뎃후 범위를 확인해야한다.
            if not( 0<= nr <= N-1 ) or not( 0<= nc <= N-1 ):
                continue
            # [10] 다음node(좌표) 업뎃후, 방문체크 확인여부를 확인한다.
            if visited[nr][nc]: continue
            # [11] 요구사항대로 1을 만나면, 해당 다음node의 탐색을 멈춘다.
            if board[nr][nc] == 1:
                continue

            # [12] 이제 다음node를 inqueue하기 전에, 방문체크후 넣는다.
            visited[nr][nc] = True
            queue.append((nr, nc, nd))
    # [13] 더이상 dequeue할게 없으면, 마지막에 넣은 다음node까지 다 탐색했으므로
    #      if 도착지점에 발견안되었다면 -1을 반환한다.
    return -1

    # [14] 시작위치에서부터 가까운 4방향으로 탐색해나간다
    # -> 다음좌표에서도 가까운 순서대로 방문해 나간다
    # -> 그 다음좌표에서도 자신에 가까우면서 가능한 순서대로 방문해 나간다
    # -> [queue]에는 [인접node]를 순서대로 넣고, 넣은 순서대로 탐색하니,
    # -> root로 부터 거리를 입력해놓는다면,
    # -> 원하는 가장빨리 발견한 도착node까지 거리가 [이미 최단거리]가 된다.
    # -> 왜냐면... 이미 제일 가까운것만 순서대로 탐색하고 있으니까 말이다.
    # -> 뒤에서도 도착node로 위치할 발견될 수 있지만, if 나오면 바로 함수를 종료시키니 최단거리다
    # 단, 간선정보가 다 동일하게 1일 경우만 해당한다.

    # [15] dfs, bfs모두 갈 수 있는지 없는지는 [while 다돌았는데 못찾았으면 -> return -1]로 찾는다.
    # [16] 최단경로를 확인하려면 level별 먼저 다 탐색하는, [bfs]로 해야한다
    # [17] floodfill 같은 경우는, dfs, bfs다 된다...
    # [18] 빨리 도착점 찾아보려면dfs, 최단거리찾거나 메모리 효율적이라면 bfs



if __name__ == '__main__':
    ## bfs활용 -shortest path
    # -> 간선정보에 가중치가 없을 거나 같은 경우, bfs로 최단경로를 구할 수 있다.
    # board 너비와 높이 n / 1은 벽 / 0 1은 시작위치좌표 / 4 2 는 도착위치 좌표

    ## [1] 좌표 탐색은  다음좌표를 위한 Delta값부터 2차원 튜플로 정의해놓는다.
    D = ((-1, 0), (1, 0), (0, -1), (0, 1),)

    N = int(input().strip())
    board = [list(map(int, input().split())) for _ in range(N)]
    sr, sc, dr, dc = map(int, input().split())

    ## [2] 좌표탐색의 bfs-queue메서드의 파라미터는 시작node, 시작좌표를 준다. 필요한 마지막좌표도 다 준다.
    ## -> dfs는 호출후  마킹할 전역변수를 출력미리 해놓지만
    ## -> bfs는 메서드라서 최단경로의 경우 return해주니 메서드를 print
    print(bfs(sr, sc, dr, dc))

    pass
