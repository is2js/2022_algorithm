import sys 
 
input = sys.stdin.readline 
 
 
if __name__ == '__main__':
    ## 2차원배열을 -> 1차원 배열  lst [ row ] = col 로 기억하는 경우, row별 1개의 col만 매핑해놓고 쓰겠다는 의미다.
    # => 2차원배열의 값이 특정값이 아니면서, row별 1개의 col만 쓸 때, 2개의 index를 1차원배열의 index:value로 매핑한다.
    board = [[col + row * 4 for col in range(1, 4)] for row in range(4)]

    # (1) row index별 상태배열을 만든다. value에는 col index 중 1개를 넣는다.
    # => row별 1개의 col만 위치시키겠다는 의미이다.

    board_1d = [0] * len(board)

    # (2) 배열탐색을 row 0 n-1까지 한다.
    for row in range(len(board_1d)):
        # (3) col을 순회하면서, row 에 col을 value로 할당하는 순간. 그위치를 기억하는 것이다.
        # => col을 순회하면서 할당하므로, 가능한 것 1개만 할당되게해서, row별 col은 1개만 쓰게 한다.
        for col in range(len(board_1d)):
            # (4) 일단 순회하는 col을 해당row에 1개로 박아둔다.
            # => [조건에 따라 continue되면, row별 사용col가 바뀌는 것]이다.
            # => 순서대로 들어가되, 조건에 걸리면 다음으로 넘어가야한다.
            # board_1d[row] = col
            # (5) 필터링 조건은, 직전까지의 row들을 돌면서, 해당 col은 사용안했을 때, 그 col을 준다.
            # -> flag(if break)로서 하나라도 걸리면 탈락시키고, else 하나도 안걸리면 통과다
            for m_row in range(row):
                # (5-1) 이전row들에서 해당 col을 매핑해서 사용했다면 탈락
                # if board_1d[m_row] == board_1d[row]: break
                # => dfs와 달리 일반으로 돌아갈 땐, 먼저 박아두지 못한다. 마지막에 다 걸려버리기 때문
                if board_1d[m_row] == col: break
                # (5-2) 이전row들에서 사용한col이, 우상/우하향 대각선에 존재하면 탈락
                # => abs(row차) == abs(col)차에 걸리면, 탈락이다.
                # => 자신도 포함되는데, 이전row들만 순회하므로 자신은 비교대상에 안걸린다.
                # => 좌우대각선을 허용할 땐, 양수row차이에  == abs(컬럼차)로 비교한다.
                if row - m_row == abs(board_1d[m_row] == col): break
            else:
                # (6) flag에 안걸렸다면, 다음col을 살펴보지말고 그 그것을 쓰게 한다.
                # => 복구를 안해줘도 되는 것이.. 탈락되면, 다음 것이 쓰게 된다.
                # => 만약 마지막것도 탈락되면? 각 row당 맨마지막 col이 박혀있다.
                # => dfs 탈락시, 다음stack진입(X) -> row에 박았어도, 종착역에 도착못함 -> 카운팅 안됨
                #    dfs는 미리 박아두고, 다음node로 진입못하면, 최종결과에 반영안된다.
                #    dfs의 경우에만 visisted를 덮어쓰되, 다음node진입못하게 막아버리면 소용없다.
                # => dfs가 아니라면, flag다 피한곳에서 visisted에 할당하게 한다.
                board_1d[row] = col
    print(board_1d)





