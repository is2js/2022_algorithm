import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## 칼럼순으로 순회 여러가지 방법
    # -> row가 아닌 col index부터 바깥쪽에서 돌리는 2중for문
    lst_2d = [[x + row * 3 for x in range(1, 3 + 1)] for row in range(4)]
    for row in lst_2d:
        print(*row)
    # 1 2 3
    # 4 5 6
    # 7 8 9
    # 10 11 12

    ## 1. 이중반복문을 col부터 돌린다.
    n, m = 4, 3
    for col in range(m):
        for row in range(n):
            print(lst_2d[row][col], end=" ")
        print()
    # 1 4 7 10
    # 2 5 8 11
    # 3 6 9 12

    ## 2. list comp에서, 안쪽을 row -> 뒤쪽을 col로 돌리면 된다.
    # [lst_2d[row] for row in range(n)]
    # [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    # [[lst_2d[row][col] for row in range(n)] for col in range(m)]
    print([[lst_2d[row][col] for row in range(n)] for col in range(m)])
    # [[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12]]

    ## 3. [고난도] 2d_lst를 map에 넣어 row별로 조작하되, 바깥에서 0부터 col index의 요소만 뽑아내게 한다
    # print(list(map(lambda row: row, lst_2d)))
    # [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    # -> row마다 0번째 요소만 모아놓고 -> 1번째 요소들만 -> 2번째 요소들만
    print([list(map(lambda row: row[col], lst_2d))
           for col in range(m)])

    ## 4. zip(*row)로 index매핑된 col들을 튜플로 모아서 처리하기
    # print(list(zip(*lst_2d)))
    # [(1, 4, 7, 10), (2, 5, 8, 11), (3, 6, 9, 12)]
    # => zip(*)의 결과는 튜플이므로, map(list,)를 적용해야 lst_2d가 된다.
    print(list(map(list, zip(*lst_2d))))
    # [[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12]]
