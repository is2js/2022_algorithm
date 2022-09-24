import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## 1. [1개의 배열에서 재방문금지로 인한 1case 경로]라면, global visited 2차원배열을 써서 공유하면 되지만,
    ## 여러 정답case && 들고다닐 수 없는 2차원 visited -> 다른방식이 필요하다
    board = [[col + row * 4 for col in range(1, 4 + 1)] for row in range(4)]
    # print(*board, sep="\n")
    # [1, 2, 3, 4]
    # [5, 6, 7, 8]
    # [9, 10, 11, 12]
    # [13, 14, 15, 16]

    ## 2. / 우상향 대각선은 가운데가 아니더라도 [row - col index] index차가 일정하다
    # for k in range(-3, 4):
    #     print([board[row][col] for col in range(4) for row in range(4)
    #            if row - col == k])
    # [1, 6, 11, 16] k = 0 일때는, 정 가운데 대각선
    # [5, 10, 15] k = 1 -> 가운데부터 1칸아래 대각선
    # [9, 14]
    # [13]

    # [4] => k = -3 부터.. \ 우하향대각선이 나타난다. 좌측부터 내려간다.
    # [3, 8]
    # [2, 7, 12]
    # [1, 6, 11, 16] => k = 0 일때 \ 우하향 가운데 대각선
    # [5, 10, 15]
    # [9, 14]
    # [13] => k = 3 일 때, \ 맨 아래 우하향 대각선

    ## 3. / 우상향 대각선은 가운데가 아니더라도 [row + col index] index합이 일정하다
    # for k in range(0, 3 + 3 + 1):
    #     print([board[row][col] for col in range(4) for row in range(4)
    #            if row + col == k])
    # [1, 2, 3, 4]
    # [5, 6, 7, 8]
    # [9, 10, 11, 12]
    # [13, 14, 15, 16]

    # [1] => k = 0

    # [1] => k =0, 좌측부터 올라간다.
    # [5, 2]
    # [9, 6, 3]
    # [13, 10, 7, 4] => k = 3
    # [14, 11, 8]
    # [15, 12]
    # [16] => k = 7

    ## 4. 특정 row, col에 대해서 -> 그 \ 우하향 대각선은 ?
    # => (1) index차가 일정한데, 얼마나 일정한지 k로 확인하고,
    #    (2) k를 만족하는 row, col을 돌면서 index차가 동일한 것을 고르면 된다.
    # row, col = 2, 1
    # k = row - col
    # for k in range(0, 3 + 3 + 1):
    # print([board[row][col] for col in range(4) for row in range(4)
    #        if row - col == k])
    # [1, 2, 3, 4]
    # [5, 6, 7, 8]
    # [9, <10>, 11, 12]
    # [13, 14, 15, 16]

    # [5, 10, 15]

    ## 4-2. 자신을 뺀 것을 찾으려면, 필터링 조건에서 제외시키자.
    # print([board[row][col] for col in range(4) for row in range(4)
    #        if row - col == k
    #        and row != 2 and col != 1])
    # [5, 15]

    ## 5. 특정 row, col에 대해서 -> 그 / 우상향 대각선은 ?
    # => (1) index합이 일정한데, 얼마나 일정한지 k로 확인하고,
    #    (2) k를 만족하는 row, col을 돌면서 index합가 동일한 것을 고르면 된다.
    # row, col = 2, 1
    # k = row + col
    # for k in range(0, 3 + 3 + 1):
    #     print([board[row][col] for col in range(4) for row in range(4)
    #            if row + col == k])

    # [1, 2, 3, 4]
    # [5, 6, 7, 8]
    # [9, <10>, 11, 12]
    # [13, 14, 15, 16]

    # [13, 10, 7, 4]

    # print([board[row][col] for col in range(4) for row in range(4)
    #        if row + col == k
    #        and row != 2 and col != 1])
    # [13, 7, 4]

    ## 6. 특정 row, col에 대해서, 우상향과 우하향을 동시에
    # (1) 특정 좌표에 대칭되는 대각선들은, row차이와 col차이의 절대값이 같다
    ##
    s_row, s_col = 2, 1

    print([board[row][col] for col in range(4) for row in range(4)
           # if row - s_row == col - s_col ])  # 차 일정 -> [5, 10, 15]
           # if row - s_row == - (col - s_col)]) # 합 일정 -> [13, 10, 7, 4]
           # if abs(row - s_row) == col - s_col]) # row차이에 abs(상하)를 걸고, col차는 양수(우측대각선만) 만들어놓기 -> [10, 7, 15, 4] 상/ 와 하\
           # if abs(row - s_row) == s_col - col]) # row차이에 abs(상하)를 걸고, col차는 음수(좌측대각선) 만들어놓기 -> [5, 13, 10] 상\ 와 하/
           if abs(row - s_row) == abs(col - s_col)]) # row차, col차 둘다abs()걸면 -> 양쪽대칭대각선 -> [5, 13, 10, 7, 15, 4]

    # [1, 2, 3, 4]
    # [5, 6, 7, 8]
    # [9, <10>, 11, 12]
    # [13, 14, 15, 16]
