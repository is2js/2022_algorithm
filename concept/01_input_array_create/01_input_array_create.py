import sys

input = sys.stdin.readline


def solution():
    # # 01 input1개는 map안쓰고 int(), 2개~3개는 map -> 튜플 언패킹
    # 10 5
    # 1 10 4 9 2 3 8 5 7 6
    # a, b = map(int, input().split())
    # print(a, b)
    # c = list(map(int, input().split()))
    # print(c)

    # # 02 1개는 int()
    # 9
    # 0 0 0 1 1 1 -1 -1 -1
    # 0 0 0 1 1 1 -1 -1 -1
    # 0 0 0 1 1 1 -1 -1 -1
    # 1 1 1 0 0 0 0 0 0
    # 1 1 1 0 0 0 0 0 0
    # 1 1 1 0 0 0 0 0 0
    # 0 1 -1 0 1 -1 0 1 -1
    # 0 -1 1 0 1 -1 0 1 -1
    # 0 1 -1 1 0 -1 0 1 -1
    # N = int(input().strip())

    # # 03 2차원 배열은 횟수만큼 list comp 상에서 list(map())
    # paper = [list(map(int, input().split())) for _ in range(N)]
    # print(paper)

    # 04 2차원 && 구분자없음 -> map(func, *iterable)의 iterable자리에 문자열을 split없이 바로 넣으면 된다.
    # 3 3
    # 011
    # 111
    # 110
    # N, M = map(int, input().split())
    # MIRO = [list(map(int, input().strip())) for _ in range(N)]
    # print(MIRO)

    # 05 차원별 변수들을 이용해서, [특정 값으로 초기화된 배열 선언]하기
    INIT = -1  # 반복되는 배열 요소의 초기화 값을 상수로 미리 선언
    W = row = N = 5  # 행의 갯수의 다양한 표현. 1차원일때는 행의 갯수대신 -> 열이자 && 요소의 갯수로서 작동한다.
    H = column = M = 4  # 열의 갯수
    C = channel = 3  # 행렬의 갯수 3차원
    B = batch = 3  # 3차원행렬의 갯수

    # 1차원 -> 내부요소가 값이라서, list * N개의 [얕은복사를 통한 extends]로 가능함( 2차원 == 요소가 mutable컬렉션 -> 요소 공유되서 하면 안된다)
    # -> index 사용안하는 (상수)list comp는 상수 append로서 [요소 복제]
    # -> 일차원일 땐, 행의 갯수가 아닌 == 열의 갯수 == 요소의 갯수다.
    d1 = [-1 for _ in range(H)]
    d1_2 = [-1] * H
    print(f"d1 >>> {d1}")
    print(f"d1-2 >>> {d1_2}")

    # 2차원 -> (1) 열(H, col)갯수만큼 요소 복제해서 1행을 만들고,
    #         (2) 그 생성된 행을 [똑같은 상수 행렬]로서 행의갯수 W만큼 append하여 복제한다.
    d2 = [[-1 for _ in range(H)] for _ in range(W)]
    print(f"d2 >>> {d2}")

    # 3차원 -> 열만큼 요소복제 = 1행 -> 행수만큼 행 복제 -> channel만큼 복제
    d3 = [[[-1 for _ in range(H)] for _ in range(W)] for _ in range(C)]
    print(f"d3 >>> {d3}")

    # 4차원
    d4 = [[[[-1 for _ in range(H)] for _ in range(W)] for _ in range(C)] for _ in range(B)]
    print(f"d4 >>> {d4}")
    pass


pass

if __name__ == "__main__":
    solution()
