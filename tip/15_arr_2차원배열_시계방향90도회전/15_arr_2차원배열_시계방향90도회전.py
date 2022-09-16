import sys 
 
input = sys.stdin.readline 
 
 
if __name__ == '__main__':
    ## 행렬회전
    # 4 by 6
    lst_2d = [[col + row * 6 for col in range(1, 6 + 1)] for row in range(4)]
    for row in lst_2d:
        print(*row)
    # 1 2 3 4 5 6
    # 7 8 9 10 11 12
    # 13 14 15 16 17 18
    # 19 20 21 22 23 24

    # 1. 90도 회전 -> for col부터접근 & for row는 역순으로 접근 -> 90도 돌리기 전의 원소들 세로1줄 접근
    # cf) col별 순회 -> (1) col부터 돌리는 이중반복문 (2) map(lambda row[col]) for col

    for col in range(6):
        for row in range(4):
            print(lst_2d[-(row + 1)][col], end=" ")
        print()
    # 19 13 7 1
    # 20 14 8 2
    # 21 15 9 3
    # 22 16 10 4
    # 23 17 11 5
    # 24 18 12 6

    #  4by6 -> 6by4로 90도 회전하려면, 6by4배열을 미리 만들어놓고 할당해야한다.
    lst_2d_90 = [[0] * 4 for _ in range(6)]
    for col in range(6):
        for row in range(4):
            lst_2d_90[col][row] = lst_2d[-(row + 1)][col]

    for row in lst_2d_90:
        print(*row)

    # 19 13 7 1
    # 20 14 8 2
    # 21 15 9 3
    # 22 16 10 4
    # 23 17 11 5
    # 24 18 12 6

    ## 2. zip(*2d)로 col별 row의 위쪽index부터 모았으면 개별 역순처리한다.
    # (1) col별로 모아 row를 만들고 -> row를 역순
    lst_2d_90_2 = [col[::-1] for col in zip(*lst_2d)]
    for row in lst_2d_90_2:
        print(*row)
    # 19 13 7 1
    # 20 14 8 2
    # 21 15 9 3
    # 22 16 10 4
    # 23 17 11 5
    # 24 18 12 6

    # (2) row를 역순 먼저 시키고 -> col별로 위쪽부터 모으기
    for row in lst_2d[::-1]:
        print(*row)
    # 19 20 21 22 23 24
    # 13 14 15 16 17 18
    # 7 8 9 10 11 12
    # 1 2 3 4 5 6
    lst_2d_90_3 = [x for x in zip(*lst_2d[::-1])]
    for row in lst_2d_90_3:
        print(*row)
    # 19 13 7 1
    # 20 14 8 2
    # 21 15 9 3
    # 22 16 10 4
    # 23 17 11 5
    # 24 18 12 6

    # 동일한데 map으로 하기(zip의 결과는 tuple list)
    print(list(map(list, zip(*lst_2d[::-1]))))
    # [[19, 13, 7, 1], [20, 14, 8, 2], [21, 15, 9, 3], [22, 16, 10, 4], [23, 17, 11, 5], [24, 18, 12, 6]]





    pass
