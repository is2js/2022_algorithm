import sys 
 
input = sys.stdin.readline


def n_queen(n, row, queens):
    # (3) 종착역에서 반환되어 집계될 값은, 갯수다 -> 종착역마다 1이 누적되도록 반환해준다
    # => 최종계산이 n-1에서 이루어져야하므로, n에서는 최종결과값을 반환해주기만 하게 한다.
    #   만약, row == n-1로 잡으면, n-1을 처리하기 전에 반환되어버린다.
    # => 집계될 값을 건네준다면, 한칸 더갔을 때 반환해주자.
    if row == n:
        return 1

    # (4) 자신의 처리는 보통 현재node를 출력해서 경로 확인용으로
    # print(row, dst= ' ')
    # (5) 상태배열이 있다면 자신의 처리를 해준다.
    # -> 현재row에 사용할 col을 매핑해야하는데, col을 탐색해서 flag에 안걸리는 것을 넣어줘야한다.
    count = 0
    for col in range(n):
        # (6) 직전row들을 모두 확인하고 할당해줘야하지만,
        #    dfs에서는, [매 자식마다 할당] 후 다음stack으로 진입시키게 되어있는 상황으로
        #   (6-1)  실패시, 다음col이 해당row에서 사용되도록 덮어쓰고
        #   (6-2) 맨 마지막col이 실패해서 queens[row] = col로 남아있는 것 같지만,
        #         다음node의 stack으로 진입 (X) -> 종착역으로 가지못하여 반환값x -> 집계에 X
        queens[row] = col

        # -> 직전row들을 순회하면서 사용col값을 비교하여, 같은col을 못쓰게 한다
        # (7) 현재 col을 사용해도 되는지 flag로 확인한 뒤, else로 통과시 넘어가게 한다.
        #    또한, 현재row, col의 대각선들을 탐색해서, 대각선col을 못쓰게 한다.
        for prev_row in range(row):
            prev_col = queens[prev_row]
            ## (8) for if break로 flag처리하고, 다 통과하느 else:에서 다음stack으로 넘어가게 한다
            ## (8-1) 직전row들과 같은 col이 있으면 break에 걸려 else:다음stack으로 못넘어간다
            if prev_col == col: break
            ## (8-2) 직전row들과 같은 대각선에 위치하면 flag에 걸려 else:다음stack으로 못넘어간다.
            # -> row+col 가 같다 = 우상향대각선/에 위치한다
            # -> row-col 가 같다 = 우하향대각선\에 위치한다.
            # -> abs(row-row2) == abs(col-col2) 현재좌표의 양쪽대각선에 위치한다
            if abs(prev_row - row) ==   abs(prev_col - col): break
        else:
            # (9) flag에 안걸리는 col을 체크한 queens상태배열이 넘어간다
            #    -> 중간에 걸렸으면, 해당 queens는 다음스택에 못넘어가고 끝난다.
            #    -> 실패한 제일 마지막col이 있을지라도, 종착역으로 진입못해서 사라진다.
            # (10) flag에 걸리면 다음재귀로 넘어가지도 못해서 집계자체가 안된다.
            count += n_queen(n, row + 1, queens)

    return count


if __name__ == '__main__':
    ## N-queen 복습: https://school.programmers.co.kr/learn/courses/30/lessons/12952
    n = int(input().strip())

    ## (1) nbyn board에 대해, [row별 1가지 col]만 써야한다면, row 상태 배열에 사용col 1개를 value로 매핑
    # => queen의 위치에 따른 value는 중요하지 않고 && 위치만 매핑할 때 1차원배열에 매핑할 수 있다.
    queens = [0] * n

    ## (2) dfs에서, case마다 상태배열을 굳이 깊은 복사할 필요 없는 경우?
    # => 상태배열의 index가 왔다갔다하지않고, 탐색할 stack변수(row index)와 상태배열의 index탐색순서가 동일할 때
    #    자식node마다 for문에서 진입전, 현재index의 value를 매번 덮어쓰기 해서 진행하면 된다.
    # => 시작node로부터 탐색하는 dfs는 인자에 srt만 주면 된다.
    #    or src node가 없다면, stack마다 증가하는 stack변수를 넣어준다.
    #    -> 그 앞에 종착역시 사용되어야할 상수가 있다면 넣어준다.
    #    -> 상태배열이 있다면, 상태배열을 같이
    #    => 집계해서 1개만 반환한다면, 변수에 넣을 필요 없다
    #    -> 매탐색마다 누적할 변수가 있다면 default값([], (), 0) 등을추가한다.
    # n_queen(n,
    #         srt_row_index, queens)
    print(n_queen(n,
                  0, queens))


