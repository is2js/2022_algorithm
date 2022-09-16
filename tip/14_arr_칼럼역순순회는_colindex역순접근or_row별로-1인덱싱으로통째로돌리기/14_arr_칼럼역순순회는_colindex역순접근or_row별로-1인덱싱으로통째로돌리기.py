import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## 역순순회는 i -> len-1-i  or python -(i+1)  통째로돌기는 [::-1]
    ## row는 2d[::-1]로 바로 돌릴 수있다.
    ## col도 2d[row][::-1]로 바로 돌릴 수 있다.

    ## 칼럼도 index로 역순으로 돌릴 수있다
    lst_2d = [[i + row * 6 for i in range(1, 6 + 1)] for row in range(4)]
    for row in lst_2d:
        print(*row)
    # 1 2 3 4 5 6
    # 7 8 9 10 11 12
    # 13 14 15 16 17 18
    # 19 20 21 22 23 24

    ## 칼럼 역순으로 돌기
    # 1. row별로 col index를 역순으로 돌기
    for row in range(4):
        for col in range(6):
            # row마다 col은 거꾸로 돌다.
            print(lst_2d[row][-(col + 1)], end=" ")
        print()
    # 6 5 4 3 2 1
    # 12 11 10 9 8 7
    # 18 17 16 15 14 13
    # 24 23 22 21 20 19

    # 2. col접근없이  row별로 요소들을 역순으로 출력하기
    for row in range(4):
        print(lst_2d[row][::-1])
    # [6, 5, 4, 3, 2, 1]
    # [12, 11, 10, 9, 8, 7]
    # [18, 17, 16, 15, 14, 13]
    # [24, 23, 22, 21, 20, 19]
