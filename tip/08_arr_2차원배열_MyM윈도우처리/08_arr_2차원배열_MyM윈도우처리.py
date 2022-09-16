import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## 행렬 window로 짜르기
    # (1) N by N 이면서 등차수열 행렬 준비
    N = 4
    lst_2d = [[col + row * N for col in range(1, N + 1)] for row in range(N)]
    for row in lst_2d:
        print(*row)
    # 1 2 3 4
    # 5 6 7 8
    # 9 10 11 12
    # 13 14 15 16

    # (2)  M by M  window =>  [1] 시작점  [2] M의 길이가 필요하다.
    # -> 행렬의 인덱싱은 0 + i, 0 + j 에서 시작점0 이 생략되어 [i][j]로 접근하는 것
    M = 2
    srt, end = 1, 1
    result = []
    for i in range(M):
        temp_row = []
        for j in range(M):
            # 행렬인덱싱은 [시작row좌표 + row등차수열i] [시작col좌표 + col등차수열i]이다.
            temp_row.append(lst_2d[srt + i][end + j])
        result.append(temp_row)
    for row in result:
        print(*row)


    # 6 7
    # 10 11

    # (3) M by M 윈도우는 시작좌표 + 길이만 받으면 언제든지 처리할 수 있는 함수가 된다.
    def window(lst, srt, end, m):
        if m > len(lst):
            raise IndexError()

        result = []
        for i in range(m):
            temp_row = []
            for j in range(m):
                temp_row.append(lst[srt + i][end + j])
            result.append(temp_row)
        return result


    for row in window(lst_2d, 0, 0, 2):
        print(*row)
    # 1 2
    # 5 6

    # (3) window가 이동가능한 크기는   윈도우 제일처음것의 끝index ~ 원본끝index 까지의 갯수이므로
    # -> n-1 - (m-1) +1  == n - m + 1과
    # -> row든, col이든 둘다 그만큼 움직일 수 있으니,
    #   [가능한window 갯수만큼 row와col를 이동시키면서 0,0부터 시작좌표를 이동]시키면 모든 window들을 이동시킬 수 있다.
    n, m = 4, 2
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            result = window(lst_2d, 0 + i, 0 + j, m)
            for row in result:
                print(*row)
            print('===')
    # 1 2
    # 5 6
    # ===
    # 2 3
    # 6 7
    # ===
    # 3 4
    # 7 8
    # ===
    # 5 6
    # 9 10
    # ===
    # 6 7
    # 10 11
    # ===
    # 7 8
    # 11 12
    # ===
    # 9 10
    # 13 14
    # ===
    # 10 11
    # 14 15
    # ===
    # 11 12
    # 15 16
    # ===
