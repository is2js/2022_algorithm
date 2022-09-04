import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## 구현3 : 왕실의 나이트
    # 8x8좌표평면의 특정좌표에 나이트가 서있다.
    # -> 말을타고L자형태로 이동, 정원밖으로는 나갈 수 없다.
    # -> 특정위치에서 다음과 같은 2가지로 이동
    # 1. 수평 2칸 이동후 수직1칸
    # 2. 수직 2칸 이동후 수평1칸
    # -> 나이트가 이동할 수 있는 경우의수 출력
    # 행 1~8, 열a~h로 표현
    # ex c2 -> 6가지 경우의 수

    ## 내풀이
    # col번호와 매핑할 배열을 만든다.
    # columns = [0] + list('abcdefgh')
    # columns = {
    #     'a': 1,
    #     'b': 2,
    #     'c': 3,
    #     'd': 4,
    #     'e': 5,
    #     'f': 6,
    #     'g': 7,
    # }
    # board = [[0] * (8 + 1) for _ in range(8 + 1)]
    #
    # location = list(input().strip())
    # x, y = int(location[1]), columns[location[0]]
    #
    # # 좌표탐색을 1칸씩 해서 1번이라도 걸리면 아웃이다.
    # U, D, L, R = (-1, 0), (1, 0), (0, -1), (0, 1)
    # possible_directions = {
    #     'RRU': [R, R, U],
    #     'RRD': [R, R, D],
    #     'LLU': [L, L, U],
    #     'LLD': [L, L, D],
    #     'DDL': [D, D, L],
    #     'DDR': [D, D, R],
    #     'UUL': [U, U, L],
    #     'UUR': [U, U, R],
    # }
    # count = 0
    # nexts = []
    # for coord_name, coord in possible_directions.items():
    #     nx, ny = x, y
    #     for direction in coord:
    #         nx += direction[0]
    #         ny += direction[1]
    #         if not (1 <= nx <= 8 and 1 <= ny <= 8):
    #             break
    #     else:
    #         count += 1
    #         nexts.append(coord_name)
    # # print(count, nexts)
    # print(count)


    ## 풀이
    # 8가지 방향벡터를 list에 정의 -> 경로를 확인해나감..?!
    # -> 매번 각 위치로 이동가능한지 확인해야한다?
    # => 중간의 걸리는 것 확인안하고, 바로 그 목적지의 방향벡터만 확인한다.
    data = input().strip()
    # (1) 문자열은 굳이 list로 안만들어도 인덱싱이 되므로 2~3개의 문자열은 list로 바꾸지 말자!
    row = int(data[1])
    # (2) a와 1을 매칭하는 방법은 아스키 코드를 이용하는 방법이다.
    # ord('a')는 97부터 시작하는 등차수열인데, a를 1로 기준으로 삼고 싶다면, - ord('a') + 1을 해주면 될 것이다.
    # ex> ord('b') - ordr('a') = 98 - 97
    col = ord(data[0]) - ord('a') + 1 #  a부터 1로 매핑하는 방법

    # (3) 여러 좌표는 방향벡터를 포함하여 튜플list나 2차원 튜플로 모으면 된다.
    # -> 이동할때마다 1칸씩 확인할 필요가 없으므로 끝 좌표만 확인한다.
    delta_steps = (
        (-2, -1), # UUL
        (-2, -1), # UUR
        (-1, -2), # LLU
        (1, -2), # LLD
        (2, -1), # DDL
        (2, 1), # DDR
        (1, 2), # RRD
        (-1, 2), # RRU
    )

    # (4) 각 방향벡터마다 이동한 좌표가 격자안에 들어오는지 확인한다.
    count = 0
    for delta_step in delta_steps:
        nrow = row + delta_step[0]
        ncol = col + delta_step[1]
        if not (1<= nrow <=8 and 1<=ncol<=8):
            continue
        count += 1

    print(count)