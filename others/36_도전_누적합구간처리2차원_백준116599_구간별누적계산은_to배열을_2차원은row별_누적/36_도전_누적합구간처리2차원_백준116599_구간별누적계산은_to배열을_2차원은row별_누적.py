import sys

input = sys.stdin.readline


def process():
    srt_row, srt_col, end_row, end_col = map(int, input().split())

    total_sum = 0
    for row in range(srt_row, end_row + 1):
        # row별 누적합을 미리 구해놓으면, col은 반복문이 아니라, 인덱싱 차이로 바로 구할 수 있다.
        row_sum = sum_matrix[row][end_col] - sum_matrix[row][srt_col - 1]
        total_sum += row_sum

    # 이제 전체 갯수를 알면 나누기 하면 된다.
    avg = total_sum // ((end_col - srt_col + 1) * (end_row - srt_row + 1))

    print(avg)



if __name__ == '__main__':
    # 구간합 2차원
    # 백준 16507: https://www.acmicpc.net/problem/16507

    R, C, Q = map(int, input().split())
    picture = [[0] * (C + 1)] + [[0] + list(map(int, input().split())) for _ in range(R)]

    # 누적 구간합 배열 -> 누적 구간 합 2차원을 구해놓고, 셀의 갯수에 따라 나누기??
    # => 누적반복을 하기 전에 미리 구해놔야한다
    sum_matrix = [[0] * (C + 1)]
    for row in range(1, R + 1):
        row_sum = [0]
        temp = 0
        for col in range(1, C + 1):
            temp += picture[row][col]
            row_sum.append(temp)
        sum_matrix.append(row_sum)
    # print(sum_matrix)

    for _ in range(Q):
        process()



    ## 추가)
    # 요소별진행하며, 누적합이 아닌 최소값 배열을 만들면서 자료구조를 만들면
    # stack(스택)에서 O(1)으로 현재의 최소값을 뱉어낼 수 있다.
    # https://wayhome25.github.io/algorithm/2017/05/15/find-min/

