import sys 
 
input = sys.stdin.readline 
 
 
if __name__ == '__main__':
    ## 2차원배열 출력 2가지 방법
    # for row -> print(*row) : 언패킹row를 통해, 개별요소들 따로 출력
    lst_2d = [[col + row * 4 for col in range(1, 4 + 1)] for row in range(4)]

    # 1. 반복문 + 언패킹row -> 개별요소들 출력
    for row in lst_2d:
        print(*row)
    # 1 2 3 4
    # 5 6 7 8
    # 9 10 11 12
    # 13 14 15 16

    # 2. 언패킹2차원 -> sep으로 row별 줄바꿈해서 row별 출력
    print(*lst_2d, sep='\n')
    # [1, 2, 3, 4]
    # [5, 6, 7, 8]
    # [9, 10, 11, 12]
    # [13, 14, 15, 16]

    # row별 출력, 연습
    # (1) 90도 회전배열 -> 회전하기 전 line(col) 순서대로 접근
    # 0번째col값들을 뒤에서부터 만져야하니 -> row역순 -> zip(*2d_arr)로 col별 매핑하여 위에서부터 접근
    print(*list(zip(*lst_2d[::-1])), sep='\n')
    # (13, 9, 5, 1)
    # (14, 10, 6, 2)
    # (15, 11, 7, 3)
    # (16, 12, 8, 4)

    # (2) 반시계90도 회전 -> col을 마지막부터 -> row눈 정순 접근 -> col역순은 복잡하니 -> zip으로 모아서 맨마지막에 row역순으로
    print(*list(zip(*lst_2d))[::-1], sep='\n')
    # (4, 8, 12, 16)
    # (3, 7, 11, 15)
    # (2, 6, 10, 14)
    # (1, 5, 9, 13)
