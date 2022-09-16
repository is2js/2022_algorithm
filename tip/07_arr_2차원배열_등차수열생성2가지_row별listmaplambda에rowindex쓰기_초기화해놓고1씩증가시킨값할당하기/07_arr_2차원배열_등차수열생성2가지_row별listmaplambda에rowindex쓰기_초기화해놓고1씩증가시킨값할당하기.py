import sys

input = sys.stdin.readline

if __name__ == '__main__':

    # 1. 한번에 1씩 올라가는 등차수열 만들기 by row별 list(map(lamdba: +rowindex*N))
    lst_2d = [list(map(lambda x: x + (row * 4), [x for x in range(1, 4 + 1)])) for row in range(4)]
    for row in lst_2d:
        print(*row)
    # 1 2 3 4
    # 5 6 7 8
    # 9 10 11 12
    # 13 14 15 16

    # 2. 0으로 다 초기화해놓고, 개별로 1씩 증가하는 값 할당하기
    lst_2d = [[0] * 4 for _ in range(4)]

    k = 0
    for row in range(len(lst_2d)):
        for col in range(len(lst_2d[row])):
            k += 1
            lst_2d[row][col] = k
    for row in lst_2d:
        print(*row)

    # 1 2 3 4
    # 5 6 7 8
    # 9 10 11 12
    # 13 14 15 16

    # 3. listmap안쓰고, 바로 listcomp에서 컨트롤하기
    # (1 ~ n ) 값을 가진 첫row생성 -> row별로 돌릴 때 rowindex인 i로 N만큼 시작항 다르게 등차주기
    n = 4
    lst_2d = [[col + row * n for col in range(1, n + 1)] for row in range(n)]
    for row in lst_2d:
        print(*row)
    # 1 2 3 4
    # 5 6 7 8
    # 9 10 11 12
    # 13 14 15 16
