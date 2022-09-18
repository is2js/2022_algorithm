import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## 빙고: https://velog.io/@rapsby/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%B9%99%EA%B3%A0-python
    ## 빙고 게임 보드에 적힌 숫자가 담겨있는 배열 board, 게임 보드에서 순서대로 지운 숫자가 들어있는 배열 nums가 매개변수로 주어질 때, board에서 nums에 들어있는 숫자를 모두 지우면 몇 개의 빙고가 만들어지는지 return하도록 solution함수를 완성해주세요.
    ## 입출력까지 예시: https://chaelinyeo.github.io/%EC%BD%94%ED%85%8C/Level03%EB%B9%99%EA%B3%A0/
    N = int(input().strip())
    board = [list(map(int, input().split())) for _ in range(N)]
    nums = list(map(int, input().split()))

    ## (1) board에서 각 숫자를 지우기
    # => 여러 개 지우기는 not in  [ 지울set]
    result = []
    for row, row_value in enumerate(board):
        for col, col_value in enumerate(row_value):
            if col_value in nums:
                # board[row][col] = -1
                result.append((row, col))
    # print(board)
    # print(result)

    answer = {
        'horizontal': [[(row, col) for col in range(0, 3 + 1)] for row in range(0, 3 + 1)],
        'vertical': [[(row, col) for row in range(0, 3 + 1)] for col in range(0, 3 + 1)],
        # 'diagonal1': [(-(i + 1), i) for i in range(0, 3 + 1)], # 다 2차원이면 대각선도 2개 묶어서 2차원으로 만들자
        # 'diagonal2': [(i, i) for i in range(0, 3 + 1)],
        # 'diagonal': [[(-(i + 1), i) for i in range(0, 3 + 1)],[(i, i) for i in range(0, 3 + 1)]]
        ## => lst[]인덱싱이 아니라, 인덱스만 뽑을 땐, 역index는 -(i+1)쓰면 안된다!!!!!!!!
        'diagonal': [[(4 - 1 - i, i) for i in range(0, 3 + 1)], [(i, i) for i in range(0, 3 + 1)]]
    }
    # print((1, 1) in [(1, 1), (1, 2)]) # True => 튜플도 값이다.
    # print([(1, 1)] in [(1, 1), (1, 2)]) # False => 튜플list와 튜플list는 in으로 바로 비교 안된다..
    count = 0
    for key, coords in answer.items():
        # 2차원배열 -> 1차원배열(튜플lst)
        for coord in coords:
            # 튜플lst  vs 튜플lst
            if all([xy in result for xy in coord]):
                count += 1
                # print(key)
    print(count)
