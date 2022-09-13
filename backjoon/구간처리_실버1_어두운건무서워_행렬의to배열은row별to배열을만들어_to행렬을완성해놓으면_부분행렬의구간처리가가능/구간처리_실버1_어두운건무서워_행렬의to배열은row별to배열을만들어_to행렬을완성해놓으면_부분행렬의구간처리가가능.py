import sys

input = sys.stdin.readline


def process():
    # 각 TC별 구간처리한다. 부분행렬이 주어져도, [row별 구간처리]후 각 row별 집계값을 합산한다
    srt_row, srt_col, end_row, end_col = map(int, input().split())

    # row의 시작과 끝을 돌리면서, row별 구간처리한다.
    total_sum = 0
    for row in range(srt_row, end_row + 1):
        # for y in range(srt_col, end_col + 1):
        # 구간처리는 to배열을, B - (A-1)  O(1)으로 처리하므로, 반복문을 안돌려도 된다.
        row_section_sum = prefix_matrix[row][end_col] - prefix_matrix[row][srt_col - 1]
        total_sum += row_section_sum

    # 평균은 합 + 갯수를 알면되는데, 행렬은 갯수를 알기 쉽다.
    avg = total_sum // ((end_row - srt_row + 1) * (end_col - srt_col + 1))

    # 소수점은 거의다 출력이므로 f""string으로 쉽게 할 수 있다.
    print(f"{avg:.0f}")




if __name__ == '__main__':
    # 백준 16507 :  https://www.acmicpc.net/problem/16507
    R, C, Q = map(int, input().split())

    # 문제가 0부터 시작하지 않는다면, [0] + list()처럼, 빈행과 빈열을 추가해서 행렬을 만들어준다.
    # -> 직접 입력받은 Row, col번호 -1 해서 추출해도 되긴 한다.
    # picture = [list(map(int, input().split())) for _ in range(R)]
    picture = [[0] * (C + 1)] + \
              [[0] + list(map(int, input().split())) for _ in range(R)]

    # [구간처리 문제]는, 구간으로 잘라지기 전에, 모든 구간별 누적계산을 미리 해놔야한다.
    # -> 그 문제가 행렬이라도, row별로 독립적으로 생각하고, [row별 to배열]을 만들어 [to배열 행렬]을 완성시킨 뒤, row별 구간처리하면 된다.
    # -> [row별] 돌리면서, 각 구간별 누적값을 to 배열에 넣어둔다.
    # -> 요구사항은 평균이지만, 갯수로만 나누면 되니, 누적합으로 유지한다.
    prefix_matrix = [[0] * (C + 1)]  # 매칭시켜 만들기 위해, 빈 행렬을 만들어준다.

    for row in range(1, R + 1):  # 빈행렬을 빼고 돌린다.
        # row별 to행렬을 만들기 위해, row별 (1) 누적 가변변수 (2) 변수저장 to배열을 만든다.
        # -> 이 때, 빈 열을 채워주기 위해 [0]을 짚어넣고 시작한다.
        temp_cum_sum = 0
        row_prefix_sum = [0]
        for col in range(1, C + 1):
            temp_cum_sum += picture[row][col]
            row_prefix_sum.append(temp_cum_sum)

        prefix_matrix.append(row_prefix_sum)

    
    for _ in range(Q):
        process()
