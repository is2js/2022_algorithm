import sys

input = sys.stdin.readline


def rotate(arr, board):
    ## 8. 들어온 행렬을 회전시킨 행렬을 반환해야하는데,
    ##  => 그냥 board에 그리는게 낫다? => 만약 행렬반환하면, board 또 다시 그려야한다.
    ##  => 회전된 행렬을 board에 그리기
    pass


def create_board_and_lock(n, lock):
    board = [[0] * n for _ in range(n)]
    ## 4. board가 완성되면 lock을 offset을 시작위치로 복사해놔야한다.
    ## => 행렬복사: 대상행렬을 i,j로 돌면서, 복사할위치는 offset을 시작좌표로 그린다.
    for row in range(len(lock)):
        for col in range(len(lock)):
            board[lock_offset + row][lock_offset + col] = lock[row][col]
    return board


def rotate_key_and_match(board, key, row, col, rot):
    ## 10. 가장안쪽인 rot를 먼저 처리하면서 순서대로 만들어나간다
    ## rot 0,1,2,3 상태에 따라 0 90 180 270 회전이다.
    ## => 복사대상 key를 순회해야하는데, 정사각행렬이므로 미리 n을 빼놓는다.
    key_len = len(key)
    if rot == 0:
        ## 10-1. 0도 회전이면 현재key를 row,col을 시작위치로 for i for j key를 그려나간다.
        for i in range(key_len):
            for j in range(key_len):
                # key[i][j] 를 board의 row,col을 시작위치하는 행렬i,j로 그려나간다.
                # board[row + i][col + j] = key[i][j]
                ## 이 때, lock이 그려진 도화지므로 겹칠때는 [원소를 누적합]으로 그려나가야한다.
                board[row + i][col + j] += key[i][j]
    elif rot == 1:
        ## 10-2. 행렬의 90도 회전한 것을 복사하는 것은,
        ## (1) i, j를 돌되, 시작위치를 어느지점부터 해야할지 먼저 판단한다.
        ##   => 회전 전 원본(0,0)에 대해, 어느지점이 (0,0)으로 가야할지 [반대로 회전된 상태의 시작위치]를 정한다.
        ##      ↱(0,0)
        ##
        ##      ↳(n-1,0) => 이 지점이 0,0으로 가야하니 시작좌표offset은 (n-1과, 0)이다.
        ## (2) 그다음은 col인 j가 진행함에 따라 => 반대회전지점이 어떻게 진행되는지 본다.
        ##     [복사도화지 행렬]의 col(j)우측으로 1칸씩 갈때마다 => [복사대상행렬의 역회전 가상행렬](n-1,0)에서는 row가 올라간다
        ##     col은 [원본행렬의 for순회 변수j]이고 => row는 실제인덱싱해야할 [ ][ ] 위치 + 방향성이다(-)
        ##     => for i, j진행되는 자리를 채우는데 => 복사대상행렬은 다른곳에서 뽑아내야한다.
        # for i in range(key_len):
        #     for j in range(key_len):
        # board[row + i][col + j] += key[(n-1) - j]
        ## (3) 다음은, row인 i가 진행됨에 따라 => [복사행렬의 역회전행렬]은 col이 정방향 진행된다.
        for i in range(key_len):
            for j in range(key_len):
                board[row + i][col + j] += key[(key_len - 1) - j][0 + i]

    elif rot == 2:
        for i in range(key_len):
            for j in range(key_len):
                # board[row + i][col + j] += key[(key_len - 1)][(key_len - 1)]
                board[row + i][col + j] += key[(key_len - 1) - i][(key_len - 1) - j]
    else:
        ## 270도는 역으로 270를 하기보단, 정방향 90도를 역회전행렬이라 생각한다.
        for i in range(key_len):
            for j in range(key_len):
                # board[row + i][col + j] += key[0][key_len-1]
                board[row + i][col + j] += key[0 + j][key_len-1 -i]
    # print(*board, sep="\n")


def check_lock(board, offset, n):
    for i in range(n):
        for j in range(n):
            if board[offset + i][offset + j] != 1:
                return False
    else:
        return True


if __name__ == '__main__':
    key = []
    for _ in range(3):
        key.append(list(map(int, input().split())))
    lock = []
    for _ in range(3):
        lock.append(list(map(int, input().split())))

    ## 1. key가 lock에 걸친 체로 window로 진행하면서, 겹치는 것 비교는 누적합으로 한다면,
    ## -> 미리 움직이는 2차원배열을 만들어야한다.
    ## -> 정사각행렬은 len()을 변수로 빼놓는 것이 편하다.
    ## (1) board는 미리 크기를 잡을 수도 있고, 최대크기로 미리 만들어놔도 된다.
    ## => board의 좌표를 먼저 구하기 전에, 중간에 고정된 lock의 정보부터 offset으로 구해놓자.

    ## 2. 2차원 배열속에 고정된 위치의 lock은 0,0에서 시작좌표 offset을 미리 빼놔야한다.
    ## => 시작index로부터, 길이n의 끝에 걸린index이므로, 시작index + (n - 1)로 잡아놓을 수 있다.
    ## offset은 거기까지 가는 이동횟수이며, 시작index에서 + 해야할 값이다.
    lock_offset = len(key) - 1

    ## 3. 다시 board를 만들면,
    ##    lock_offset index에서 lock.len -1 로 lock의 끝index에 도착후, 다시 key길이의 끝index에 도달하면
    ## board의 마지막 index가 된다. => board의 길이는, 0시작 기준 마지막index + 1일 것이다.
    board_length = (lock_offset + len(lock) - 1 + lock_offset) + 1
    # print(board_length) # 7
    # board = [[0] * board_length for _ in range(board_length)]
    # create_board_and_lock(board_length, lock)

    # print(*board, sep="\n")
    # [0, 0, 0, 0, 0, 0, 0]
    # [0, 0, 0, 0, 0, 0, 0]
    # [0, 0, 1, 1, 1, 0, 0]
    # [0, 0, 1, 1, 0, 0, 0]
    # [0, 0, 1, 0, 1, 0, 0]
    # [0, 0, 0, 0, 0, 0, 0]
    # [0, 0, 0, 0, 0, 0, 0]

    ## 5. key라는 window의 이동횟수는, 시작index 0부터, window이동끝index인 offset + len(lock) -1까지 연산해야한다.
    ##   인덱스차는 시작을 제외한 순수차 = 이동횟수이므로 + 1 해서 [시작위치부터 포함]해서 이동해야한다.
    for row in range(lock_offset + len(lock) - 1 + 1):
        for col in range(lock_offset + len(lock) - 1 + 1):
            ## 6. 시작위치부터 col을 1칸씩 이동하기 전에, rotation도 처리해야한다.
            ## => rotation도 4번 돌려야하는데, 그 횟수만 range로 나타내고, 그 index를 이용해서 회전시킨다.
            for rot in range(4):
                ## 7. [rot index에 회전경우의수 상태의 key] => board에 누적복사 =>lock영역 비교
                ## => 회전된 행렬을 만들고, 또다시 board에 복사하는 것보다는
                ## => 회전된 행렬을, board의 들어갈 위치(시작좌표row,col)에 바로 복사해서 그리는게 낫다
                ## => 회전시키고, 그것을 그대로 쓸 것이냐 vs 회전시킨 것을 어디에 복사할 것이냐
                # rorated_key = rotate(key, board)

                ## 8. 이 때, 매번 board에 복사해야하므로, 매번 board가 새로 생성되어야하니, board 선언 및 lock복사를 method로 추출해서 여기로 옮긴다.
                board = create_board_and_lock(board_length, lock)
                ## 9. rot에 따라 회전된 상태로 key를 board에 복사한다
                ##  이 때, row, col은 key window의 시작좌표이므로, offset으로서 필요하다
                ## 반복문의 모든 요소를 가지고 method로 들어가서 비교한다.
                rotate_key_and_match(board, key, row, col, rot)

                ## 10. 회전된key가 board에 복사된 상태에서 lock영역만 검사한다
                ## => lock의 0이 1로 차있으면서, 2가 없어야한다
                ## => for if 하나라도 1이 아닌 것이 나오면 탈락 => 다 순회하면 통과
                ##    board를 offset부터 lock의 길이만큼 돌아야하니, 변수로 넣어준다.
                ##    => 순회를 위한 메서드는, len도 인자로 넣어준다. 0,0이 아니면 시작좌표 offset도 넣어준다.
                if check_lock(board, lock_offset, len(lock)):
                    ## 11. 성공했다면, True를 반환하고 멈춘다.
                    print(True)
                    exit()
    ## 12. key가 회전하며 윈도우를 다돌았는데도 안걸리면 탈락
    print(False)