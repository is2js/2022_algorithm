import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## 반시계90도 회전
    lst_2d = [[col + row * 6 for col in range(1, 6 + 1)] for row in range(4)]
    for row in lst_2d:
        print(*row)
    # 1 2 3 4 5 6
    # 7 8 9 10 11 12
    # 13 14 15 16 17 18
    # 19 20 21 22 23 24

    ## 1. 90도 회전류는 col부터 접근하고, row는 회전이전 부분을 생각하기
    # -> 회전이전부분을 순서대로 접근하여, row로 모은다
    # -> 칼럼은 역순으로 접근 / row는 정수능로 접근
    for col in range(6):
        for row in range(4):
            print(lst_2d[row][-(col + 1)], end=" ")
        print()
    # 6 12 18 24
    # 5 11 17 23
    # 4 10 16 22
    # 3 9 15 21
    # 2 8 14 20
    # 1 7 13 19

    ## 2. zip(*)으로 row별 index(칼럼)매핑하려면,
    # (1) 미리 row별 열 역순으로 나열되어있어야한다.
    # (2) index별 매핑해놓고,만들어진 행렬의 row별(X) 행렬전체 역순으로 row들을 뒤집어도 된다.
    lst_2d_r90 = [row for row in zip(*lst_2d)][::-1]
    for row in lst_2d_r90:
        print(*row)
    # 6 12 18 24
    # 5 11 17 23
    # 4 10 16 22
    # 3 9 15 21
    # 2 8 14 20
    # 1 7 13 19

    ## 3. 동일한데 map으로 풀어해치기
    print(list(map(list, zip(*lst_2d)))[::-1])
    # [[6, 12, 18, 24], [5, 11, 17, 23], [4, 10, 16, 22], [3, 9, 15, 21], [2, 8, 14, 20], [1, 7, 13, 19]]
