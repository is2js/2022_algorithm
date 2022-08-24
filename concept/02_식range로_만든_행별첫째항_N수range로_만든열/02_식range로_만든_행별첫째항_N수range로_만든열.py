import sys

input = sys.stdin.readline


def solution():
    # range의 끝범위에 식을 넣어, 등차수열 행렬 만들기
    # - 등차수열 An = a1 + d(n-1)
    # - 1씩 오르는 등차수열  An = a1 + 1(n-1)
    # - n씩 증가하는 등차수열 An = a1 + n(n-1)
    n = 5

    ## range에 식을 이용하지 않고, 1씩 증가하는 N으로 사용 -> 식은 요소에 주기
    # (0) range에 식 없이 N번째항을 만드는 점화식의 N으로 사용하여 N번재 수열을 append한다.
    # -> 3부터 2씩 증가하는 등차수열 10개
    print([3 + 2 * (i - 1) for i in range(1, 10 + 1)])
    # [3, 5, 7, 9, 11, 13, 15, 17, 19, 21]

    # (0) 1부터 3씩 증가하는 등차수열 5개
    print([1 + 3 * (i - 1) for i in range(1, 5 + 1)])

    ## 이렇게 할 경우, 만들어진 요소들을 기반으로 더이상 i를 컨트롤할 수 없게 된다.
    ## -> 각 행의 첫째항을 만들고, 이후 그 것을 바탕으로 열을 붙이고 싶다면
    ## -> range자체에 식을 대입하여, 원하는 요소들이 i(ndex)로 나오도록 먼저 완성해야한다.

    ## range의 생략된 3번째 인자는 등차를 의미한다.
    # (1) 1부터 5번째항까지 1씩증가 등차수열 -> range(첫항, 끝항+1 by n) or range(첫항, 끝항+1 by n, 1)
    result = []
    for i in range(1, (1 + (n - 1)) + 1, 1):  # range 끝에선 값 + 1
        result.append(i)
    print(result)
    # [1, 2, 3, 4, 5]

    ## range의 끝항을 등차 + 변수N을 이용한 식으로 만들면, N개가 뽑힌다
    # (2) 1부터 [식]5번째항까지 2씩 등차수열 -> range(첫항, 끝항+1 by n, 2)
    result = []
    for i in range(1, (1 + 2 * (n - 1)) + 1, 2):
        result.append(i)
    print(result)
    # [1, 3, 5, 7, 9]

    # (3) 1부터 n(5)개를, n(5)씩 증가하는 등차수열
    result = []
    for i in range(1, (1 + n * (n - 1)) + 1, n):
        result.append(i)
    print(result)
    # [1, 6, 11, 16, 21]

    # 2차원 행렬을 만드려면, 각 행의 첫번째 값을 만들어야 한다.
    # [1],2,3,4,5
    # [6],7,8,9,10
    # -> 첫번째항을 만드려면, 열의갯수만큼 등차를 띄어야한다.

    # (4) 1부터 칼럼의갯수만큼 증가하는, 총 10개의 등차수열
    column_count = 5
    result = []
    for i in range(1, column_count * (10 - 1) + 1, column_count):
        result.append(i)
    print(result)
    # [1, 6, 11, 16, 21, 26, 31, 36, 41]

    ## 2차원행렬을 만드려면, 1차원행렬의 요소 갯수(식의 n)가 2차원의 행의 갯수가 될 예정이다.
    # -> 요소의 갯수를 통해 첫째항으로서 행의 갯수를 만든다고 가정한다.
    # -> 열의 갯수는 등차값이다.
    ## 1차원 요소갯수N (2차원 행수) X 1차원 등차(2차원 열의 갯수)를 이용해
    # -> = 2차원 요소의 갯수를 정한다.
    row_count = 5  # 1차원 요소갯수이자, 2차원 (첫째항으로) 행수
    col_count = 3  # 1차원 등차이자, 2차원 열수
    result = []
    for i in range(1, 1 + col_count * (row_count - 1) + 1, col_count):
        result.append(i)
    print(result)
    # [1, 4, 7, 10, 13]

    # 이제 첫째항인 i를 바탕으로 행을 구성해주기
    result = []
    for i in range(1, 1 + col_count * (row_count - 1) + 1, col_count):
        # 열의 갯수 col_count를 N자리에
        result.append([i for i in range(i, i + (col_count - 1) + 1, 1)])
    print(result)
    # [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]

    ## range+식으로 i를 추출한 상황이라면, 각 i마다 i + 식없는 갯수range를 이용한 배열을
    #  쉽게 만들 수 있다.
    result = []
    for i in range(1, 1 + col_count * (row_count - 1) + 1, col_count):
        result.append([i + 1 * (j - 1) for j in range(1, col_count + 1)])
    print(result)
    pass


if __name__ == '__main__':
    solution()
