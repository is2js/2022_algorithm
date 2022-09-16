import itertools
import sys
from functools import reduce
from operator import add

input = sys.stdin.readline

if __name__ == '__main__':
    #
    # 16 숫자퍼즐 게임 그림: https://raw.githubusercontent.com/is3js/screenshots/main/image-20211103151005497.png
    # 분석 블로그 그림
    # 1: https://raw.githubusercontent.com/is3js/screenshots/main/KakaoTalk_Photo_2021-07-15-09-53-27.jpeg
    # 2: https://raw.githubusercontent.com/is3js/screenshots/main/image-20211103151333583.png

    lst_2d = [[x + row * 5 for x in range(1, 5 + 1)] for row in range(5)]
    # for row in lst_2d:
    #     print(*row)
    # 1 2 3 4 5
    # 6 7 8 9 10
    # 11 12 13 14 15
    # 16 17 18 19 20
    # 21 22 23 24 25

    # (1) 당길 window좌표를 시작과 끝tuple list로받는다.
    queries = ((2, 2), (4, 4))
    # (2) 문제에서는 좌표가 1로 시작한다면, 0행렬을 추가하거나, 좌표-1을 해준다.
    #     퍼즐문제를 풀기 위해서는, srt, end좌표 다 동시에 필요하다 -> 따로주어지면 평탄화
    #    평탄화의 기본개념은 빈행렬에 개별 1차원배열 extend다.
    #    -> 빈행렬안쓰려면 stream에 reduce함수를 써야한다.
    queries = reduce(add, queries)
    # (3) 0행렬추가 안할거면 약어 -1 -> 이쁜변수명으로 업뎃해서 사용한다.
    s_row, s_col, e_row, e_col = [coord - 1 for coord in queries]
    # (4) 한칸씩 땡긴다면, 편하게 [시작좌표]를 temp에 저장해놓는다.
    temp = lst_2d[s_row][s_col]
    # (5) 4방향화살표 중에, temp를 덮어쓰는 원소가 있는 방향인 ↑올리는 부분에서,
    #                  -> 올리기 이전 : col별 row역순 접근하여 나열되는 방향으로 접근되게 하여 모은다
    # => 땡기는 것은, 반대방향으로 모으기 위한 순서대로 접근이 아니다.
    #    땡기는 앞부분부터 순서대로 1개씩 접근하면서 덮어쓰기 해야한다.
    # ->             col은 고정이라 row만 역순으로 접근해서 모으면 된다.
    for row in range(s_row + 1, e_row + 1):
        # (6) 접근해서 나열순서대로 모았으면, 나열할 index에 할당해준다.
        # -> 역시 col고정이고, row만 현재row의 1칸 위이다(row-1)
        lst_2d[row - 1][s_col] = lst_2d[row][s_col]

    # (6) 이제 땡기는 방향의 역순(↑ ←↓→)으로 하나씩 땡겨준다.
    # ←
    for col in range(s_col + 1, e_col + 1):
        lst_2d[row][col - 1] = lst_2d[row][col]
    # ↓
    for row in range(e_row - 1, s_row - 1, -1):
        print(row)
        lst_2d[row + 1][e_col] = lst_2d[row][e_col]

    # →
    for col in range(e_col - 1, s_col - 1, -1):
        lst_2d[s_row][col + 1] = lst_2d[s_row][col]

    # (7) 마지막 temp(시작좌표)는 1칸 오른쪽에 꼽아준다.
    lst_2d[s_row][col + 1] = temp

    for row in lst_2d:
        print(*row)
