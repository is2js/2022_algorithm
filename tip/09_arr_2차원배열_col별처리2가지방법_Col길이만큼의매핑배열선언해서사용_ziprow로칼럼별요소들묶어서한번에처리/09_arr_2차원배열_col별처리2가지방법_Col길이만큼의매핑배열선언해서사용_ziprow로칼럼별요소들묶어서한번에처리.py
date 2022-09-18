import sys

input = sys.stdin.readline

if __name__ == '__main__':
    # n = 10
    # lst_2d = [[0] * n for row in range(n)]
    #
    # for num in range(n ** 2):
    #     i, j = divmod(num, n)
    #     # 표준출력은 문자열만 가능하니 f-string으로 행렬의 요소를 문자열로 바꿔서 출력한다.
    #     sys.stdout.write(f"{lst_2d[i][j]}")
    #     # 구간 끝 요소일때마다 줄바꿈 추가
    #     if j == n - 1:
    #         sys.stdout.write('\n')

    ## 유성문제
    # -> 유성의 각 col마다 최소 col의 위치 - 땅의 최대col위치 -> 그 차이 중 최대값을 구해서
    # -> 유성을 이동시키기
    R, S = map(int, input().split())
    board = [list(input().strip()) for _ in range(R)]

    #### 1. 칼럼별 처리는, 칼럼매핑배열에 저장후 -> zip으로 처리
    ## 칼럼별 값을 저장하려면, 칼럼의 갯수만큼 매핑배열을 선언 -> 원하는 값을 매핑배열[col_index]에 저장해주면 된다.
    # -> 굳이 이중반복문을 col부터 돌지 않아도 된다.
    # (1) 칼럼의 갯수만큼 매핑배열을 만든다.
    # max_stars = [float('-inf')] * S
    # min_sands = [float('inf')] * S
    #
    # for row in range(R):
    #     for col in range(S):
    #         # 값을 저장할 때, 칼럼매핑배열에, 해당 칼럼index로 저장하면 된다
    #         if board[row][col] == 'X':
    #             # 저장할 최대row index를 비교해서 col별 매핑배열을 업데이트한다.
    #             # -> index가 저장할value라면, max/min 내장함수로 바로 업뎃할 수 있다.
    #             # if row > max_stars[col]:
    #             #     max_stars[col] = row
    #             max_stars[col] = max(max_stars[col], row)
    #         if board[row][col] == '#':
    #             min_sands[col] = min(min_sands[col], row)
    #
    #
    # # (2) zip을 이용하면, col별 여러개의 매핑배열들의 값을 동시 접근할 수 있다.
    # diffs = []
    # for star, sand in zip(max_stars, min_sands):
    #     diff = sand - star - 1
    #     diffs.append(diff)
    # move = min(diffs)
    #
    #
    # # (3) col별 매핑배열의 이용도, row col순서로 돌리되,
    # #  -> row를 역순으로 돌리려면, 내부에서 인덱싱을 i->역인덱스 -(i+1) or len-1-i를 쓰자.
    # for row in range(R):
    #     for col in range(S):
    #         if board[-(row + 1)][col] == 'X':
    #             board[-(row + 1)][col] = '.'
    #             board[-(row + 1) + move][col] = 'X'
    #
    # for num in range(R*S):
    #     i, j = divmod(num, S)
    #     sys.stdout.write(board[i][j])
    #     if j == S - 1:
    #         sys.stdout.write('\n')




    #### 2. 칼럼별처리를, zip(*row)를 통해, row배열별 칼럼index로매핑된 것들을 뽑아(대각선뒤집기)
    # -> 가로로 처리해서 저장
    min_distance = float('inf')
    for elements_per_col in zip(*board):
        # -> 해당칼럼에 유성이 존재하지 않으면, 어차피 최소차이를 구하는데 배제된다.?
        # if 'X' not in elements_per_col:
        #     continue
        # (1) 아래에서 오른쪽으로 누은 sand의 좌표를구한다.
        # -> 선형탐색은 .find나 .index로 한다.
        # -> 찾더라도.. 가장 왼쪽 sand를 구해야하므로 index로 바로 구해진다.
        sand_index = elements_per_col.index('#')
        # (2) 왼쪽에 있는 star중에 가장 오른쪽 인덱스를 구해야한다.
        # -> [뒤집어놓고 선형탐색한 뒤, index처리]해주면, 가장 왼쪽 -> 가장오른쪽이 될 것이다.
        # -> 그렇지 않으면, 문자열이라면 rfind가 가능하다.
        # -> 튜플은 index범위지정이 안되넹..
        # -> 문자열이라면 뒤에서부터 인덱스를 알려주는  rindex가 가능하다...
        # find() 메서드 : 지정 문자열 처음 위치. (없을 시, -1반환)
        # index() 메서드 : 지정 문자열 처음 위치. (없을 시, Exception 반환.)
        # rfind() 메서드 : 지정 문자열 끝 위치. (없을 시, -1반환)
        # rindex() 메서드 : 지정 문자열 끝 위치. (없을 시, Exception 반환.)
        # star_index = - (elements_per_col.index('x') + 1) # - (i + 1) or len-1-i의 역인덱스
        try:
            star_index = - (elements_per_col.index('X') + 1) # - (i + 1) or len-1-i의 역인덱스
        # star는 없을 수 있다. -> .index()는 에러난다.
        except ValueError:
            star_index = -1  # star가 없으면 -1에 위치한다고 왼쪽side에서 -1에 위치에 존재한다고 가정하고 차이를 구하게 한다

        # 순수차이는 [index차이(b-a)- 1]다.
        move_distance = sand_index - star_index - 1
        # 칼럼별 값처리 하여, 모든 칼럼중에 최소값을 찾는다.
        # -> 값 업데이트라면, 바로 내장함수 업데이트
        min_distance = min(min_distance, move_distance)

    # print(min_distance)

    for row in range(R):
        for col in range(S):
            if board[-(row + 1)][col] == 'X':
                board[-(row + 1)][col] = '.'
                board[-(row + 1) + min_distance][col] = 'X'

    for num in range(R*S):
        i, j = divmod(num, S)
        sys.stdout.write(f'{board[i][j]}')
        if j == S - 1:
            sys.stdout.write('\n')



