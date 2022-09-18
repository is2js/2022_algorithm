import sys 
 
input = sys.stdin.readline 
 
 
if __name__ == '__main__':
    ## 빙고: https://velog.io/@rapsby/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%B9%99%EA%B3%A0-python
    ## 빙고 게임 보드에 적힌 숫자가 담겨있는 배열 board, 게임 보드에서 순서대로 지운 숫자가 들어있는 배열 nums가 매개변수로 주어질 때, board에서 nums에 들어있는 숫자를 모두 지우면 몇 개의 빙고가 만들어지는지 return하도록 solution함수를 완성해주세요.
    ## 입출력까지 예시: https://chaelinyeo.github.io/%EC%BD%94%ED%85%8C/Level03%EB%B9%99%EA%B3%A0/
    N = int(input().strip())
    board = [list(map(int, input().split())) for _ in range(N)]
    nums = list(map(int, input().split()))


    ## (1) 2차원배열에서 체킹value -> 해당index를 튜플로 매핑하는 방법
    # -> board를 인덱스로 순회하면서, 정답 value가 나타났을 때 -> index를 매핑한다.
    # -> if in으로 검사하면 nums의 길이만큼.. 또 순회하니 시간복잡도가 많이 늘어난다
    # => 배회중에 검사하지말고 일단, 다 넣어두자.
    value_of_indexes = dict()
    for row in range(len(board)):
        for col in range(len(board[row])):
            # value = board[row][col]
            # if value in nums:
            #     value_of_indexes[board[row][col]] = (row, col)
            value_of_indexes[board[row][col]] = (row, col)

    # print(value_of_indexes)
    # {6: (0, 0), 15: (0, 1), 17: (0, 2), 14: (0, 3), 23: (0, 4), 5: (1, 0), 12: (1, 1), 16: (1, 2), 13: (1, 3), 25: (1, 4), 21: (2, 0), 4: (2, 1), 2: (2, 2), 1: (2, 3), 22: (2, 4), 10: (3, 0), 20: (3, 1), 3: (3, 2), 18: (3, 3), 8: (3, 4), 11: (4, 0), 9: (4, 1), 19: (4, 2), 24: (4, 3), 7: (4, 4)}
    # print(dict.fromkeys(nums))
    # {15: None, 7: None, 2: None, 25: None, 9: None, 16: None, 12: None, 18: None, 5: None, 4: None, 10: None, 13: None, 20: None}

    ## (2) 정답value에 대한 index들을 가져와서, 카운팅 하되,
    ##  => 각 row별 상태배열을 만들고, 중복되는 것은 없으니, 해당row나올시 +1씩 해줘서 4까지 차는지 확인한다
    ##     각 col별 상태배열을 만들고, 해당col에 해당하는 것이 4개 이상 나타나는지 확인한다.
    ##     각 대각선별 상태배열을 2개 만들고,
    ##       x==y 일 경우 좌측대각선 +1,  y == len - 1 - x 이 좌대각선+1씩 해줘서 4개가 나타나는지 확인한다.
    row_checker = [0] * len(board)
    col_checker = [0] * len(board)
    diag_checker = [0] * 2

    for num in nums:
        row, col = value_of_indexes[num]
        ## 가로, 세로는 그냥 등자시마다 + 1
        ## 대각선은 if문으로 확인해서 + 1
        row_checker[row] += 1
        col_checker[row] += 1
        if row == col :
            diag_checker[0] += 1
        if col == len(board) - 1 - row :
            diag_checker[1] += 1

    # print(row_checker, col_checker, diag_checker)
    # [1, 5, 2, 3, 2] [1, 5, 2, 3, 2] [4, 3]
    ## 해당 line별 5번이상 등장했다면 빙고
    # => .count로 5를 찾는다.
    answer = row_checker.count(5) + col_checker.count(5) + diag_checker.count(5)
    print(answer)




