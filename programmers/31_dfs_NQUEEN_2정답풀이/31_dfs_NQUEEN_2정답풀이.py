import sys

input = sys.stdin.readline


def dfs(n, row, row_visited):
    # 이미 0 ~ n-1까지 다 겪고 지나간 종착역 -> 결과값 반환만
    ## 종착역을 마지막수 + 1로 해서 최종결과값만 반환한다.
    if row == n:
        return 1 # 성공count집계를 위한 1

    ## (1) 해당row에 대해 방문처리 => row별 여러개라서 반복문내에서 한다.
    ## => 해당row에 대한 여러col이 존재하며, 반복문을 돌면서
    ##    각 col번호를 넣어 위치처리를 할 것이다.
    # row_visited[row] = 1

    ## (2)이제 각 col별 col인덱스를 0부터 n-1까지 준다.
    ## 각 row별 들어가있는 col_index가 queen의 위치가 될것이다.
    ## => 2차원을 [index:row -> value:col] 의 1차원으로 관리한다.
    ##    여기서 상세 좌표가 필요없기 때문?
    count = 0
    for col in range(n):
        ## (3) 현재row(index)에 현재col번호를 집어넣고, queen이 거기있다고 가정한다.
        ## => queen이라는 value가 중요하지 않으므로 이렇게 2차원을 1차원으로 관리할 수 있다.
        row_visited[row] = col
        ## (4) 이제 현재 col에 대해, row를 0부터 돌면서, 다른queen이 없는지 확인한다.
        ##    [row] = col로 인해, col은 보장받은 상태다. 1개밖에 못들어가므로
        # for i in range(n):
        ## (4-0) 0부터 현재row전까지만 체크한다. 현재row와 비교하기 위해서이다.
        ##      ex> row를 0번부터 확인하고 있으니, 현재row에 대해 그 직전까지만 확인하면서 나아간다?
        for i in range(row):
            ## (4-1) 만약, i번째 row의 값(col)과  현재row의 값(col)이 같으면?
            ## 같은 col에 2개의 queen이 다른row에 존재하게 되는 것이다.
            ## => 같은 열(value)에 2개의 row가 queen이 있찌 못하게 검사한다.
            ## 열 체크
            if row_visited[i] == row_visited[row]:
                ## (4-2) 이렇게 되면, 현재col은 망한 것이므로, continue가 아니라 break
                # continue
                break
            ## (4-3) 우상향 대각선 체크 (4, 0) (3, 1) (2,2) (1,3) (0,4)
            ## => 5by5에서, 우상향대각선들은 좌표의 합이 같게 된다.
            ##    만약 중간에 있는 것도 (2, 0) (1,1) (0,3)
            ## => 우상향 대각선은, 각 line마다 row+col index가 같다.
            ##    현재 0~row-1까지만 i 돌아가고 있으니, row입장에서는 위쪽 + /방향대각선이다.
            # if i + row_visited[i] == row + row_visited[row]:
            #     break
            ## (4-3) 우하향 대각선 체크
            ## \ 대각선은, 00 11 22 로 row col index의 차가 0으로 같다
            ## => 0~직전orw까지만 검사하므로 \/ 2개의 대각선만 검사하면 되는데
            ##    지금까지 visisted에 등록된 것 중에 row - col 이 같은 곳에 queen이 등록되었었따면
            ##  (lst[i]가 가능한 것 자체가 queen 존재)
            ##   \대각선에 queen이 존재하게 된 것
            ## => 아래쪽 /\ 대각선들은, row를 진행함에 따라 자동 검사될 것이ㄷ
            # if i - row_visited[i] == row - row_visited[row]:
            #     break
            ## (4-4) 시간초과로 인해, 대각선을 한번에 체크
            ## (/)row+col 같다 or (\)row-col이 같다
            ##   (1,1)     (1,3)
            #      -1   (2,2) - 1
            ##        -1    +1
            ## => 대각선에 있다면, row2-row == col2 - col
            ## => row차이와 col차이가 같다
            ## => 우상향이면, row차와 col차이가 부호반대다
            ## => 좌상향이면, row차와 col차이가 부호같다
            ## => 상향이면, col차이는 음수고정 / row차이는 좌(-)우(+)
            ##    row차이를 +-차이 다 허용해주려면 반대로 [ == col차이에 abs()]달아주고 &  row차이는 양수가 되게 해준다.
            #     => [좌우상관없는 양쪽] 상향대각선이다.
            ##   반대로 col차이를 +- 다 허용해주려면 반대 [==abs (row차이)]를 걸어주고  & col차이는 양수가 되게 잡아준다.
            ## => 만약 둘다 달아준다면? abs(row차) -> col차이+-허용-> 좌or우한쪽의 상하대각선 /
            #     abs(col차) => row차이 +-허용 -> 좌우양쪽의 상or하한쪽 대각선
            ##    어차피 row는 0~row-1까지만 탐색하므로 abs(row) == col차이 상하허용 은 안해줘도 된다.
            ## => col에 abs걸
            if row - i == abs(row_visited[row] - row_visited[i]):
                break

        ## (5) 체크를 위한 0~row-1까지의 flag에 안걸려서 다 통과했다면
        ##     다음 row로 넘어가도 된다. 한번이라도 if break 플래그에 걸리면, else:는 실행안된다. => 다음재귀가 없다
        ##     visisted[row] = col 선언한것도 의미가 없어진다??
        ## => 다음재귀로 넘어가기 전에 직전row들과의 검사를 끝내고 flag안걸리면 else에서 넘어간다
        ##    이 때, 맨 바깥에서 도는 col도 계속 바뀌므로, 해당 현재 row, col에 놓아둔queen은 걸리면 다음재귀로 못넘어간다??
        else:
            count += dfs(n, row + 1, row_visited)

    return count


if __name__ == '__main__':
    ## N-queen: https://school.programmers.co.kr/learn/courses/30/lessons/12952
    n = int(input().strip())

    ## 빙고처럼 각 row index별 checker 상태배열/col별 상태배열/ 대각선별 상태배열을
    ## 만들어서 dfs의 가지치기(continue)를 쉽게할 수 있다.

    ## 좌표로 1칸씩 탐색할 필요가 없다??
    ## => 2차원배열로 1방향 꼬리재귀(with 방문배열)가 아닌,
    #     여러경로를 탐색한다면, visited의 깊은복사 처리가 안된다.
    ##    2차원인데, 여러경로? => row별 visited로 탐색만 하고 -> 내부에서 col을 돌려 처리한다.
    ## (1) row상태 1차원배열과 탐색
    row_visited = [0] * n
    # 종착역확인을 위한 n상수,
    # 시작node(row), 상태배열
    print(dfs(n,
              0, row_visited))
