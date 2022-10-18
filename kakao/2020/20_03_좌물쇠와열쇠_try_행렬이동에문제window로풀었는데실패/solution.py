import sys

input = sys.stdin.readline


def rotate_90(key):
    # return [list(row) for row in zip(*key)]
    return [list(row[::-1]) for row in zip(*key)]


if __name__ == '__main__':
    ## 자물쇠와 열쇠:https://school.programmers.co.kr/learn/courses/30/lessons/60059
    key = []
    for _ in range(3):
        key.append(list(map(int, input().split())))
    lock = []
    for _ in range(3):
        lock.append(list(map(int, input().split())))

    # print(*rotate_90(key), sep="\n")

    ## key를 lock안에서 움직이는 부분집합들로 나눈다면..
    ## 원소1개짜리..
    ## 원소2개짜리..
    ## 원소M개 짜리..
    e_1 = []
    for row in range(len(key)):
        for col in range(len(key)):
            e_1.append(key[row][col])
    ## => 최소 lock에 구성된 0으로 구성된 사각형을 만족해야한다. 그거 이상으로 구하면 된다.

    ## 1) lock의 구멍위치 찾기
    lock_coords = []
    for row in range(len(lock)):
        for col in range(len(lock)):
            if lock[row][col] == 0:
                lock_coords.append((row, col))
    ## 2) 구멍들로 구성된 사각형 만들기
    ## 2-1) 가장왼쪽 찾기
    min_col = min(col for (row, col) in lock_coords)
    max_col = max(col for (row, col) in lock_coords)
    min_row = min(row for (row, col) in lock_coords)
    max_row = max(row for (row, col) in lock_coords)
    # print(min_row, min_col, max_row, max_col)
    min_rec_x = max_col - min_col + 1  # 차이랑 갯수랑은 다르다.. window 구성갯수는 차이+1
    min_rec_y = max_row - min_row + 1
    # print(min_rec_x, min_rec_y)

    ## 3) key를 4가지 회전시켜보고, 거기서 min_rec_x ~ lock_x  / min_rec_y ~ lock_y 사각형들의 경우의수를
    ##    만든 뒤, lock과 일치하는지 봐야하낟.
    ##   => 다 만들지말고..window를 만들어서 서로 확인하면 될듯?
    windows = []
    # window 크기 1씩 증가
    for window in range(min_rec_x, len(key) + 1):
        y_pos = 0
        # 0부터, 윈도갯수만큼 인덱싱한 행렬이 필요함(부분행렬)
        while y_pos + window <= len(key):
            ## 가변변수도 자신의 반복문바로 위에있어야한다. 한꺼번에 올려놓으면,
            ## 상위반복문 넘어갈대 초기화 안하 그대로 이어서 간다
            x_pos = 0
            while x_pos + window <= len(key):
                temp_window = [row[x_pos:x_pos + window] for row in key[y_pos:y_pos + window]]
                windows.append(temp_window)
                # print(temp_window)
                x_pos += 1
            # print(temp_window)
            y_pos += 1

    ## 이제 4방향 다돌려서..
    key2 = rotate_90(key)
    key3 = rotate_90(key2)
    key4 = rotate_90(key3)
    windows = []
    for key in [key, key2, key3, key4]:
        # window 크기 1씩 증가
        for window in range(min_rec_x, len(key) + 1):
            y_pos = 0
            # 0부터, 윈도갯수만큼 인덱싱한 행렬이 필요함(부분행렬)
            while y_pos + window <= len(key):
                ## 가변변수도 자신의 반복문바로 위에있어야한다. 한꺼번에 올려놓으면,
                ## 상위반복문 넘어갈대 초기화 안하 그대로 이어서 간다
                x_pos = 0
                while x_pos + window <= len(key):
                    temp_window = [row[x_pos:x_pos + window] for row in key[y_pos:y_pos + window]]
                    windows.append(temp_window)
                    # print(temp_window)
                    x_pos += 1
                # print(temp_window)
                y_pos += 1

    # print(windows)
    ## 이제 lock내부에 해당 windows가 포함되는지 확인해야한다
    ## 이 때, 0<-> 1이바뀐체로 있어야한다.
    is_opened = False

    for window in range(min_rec_x, len(lock) + 1):
        y_pos = 0
        while y_pos + window <= len(lock):
            x_pos = 0
            while x_pos + window <= len(lock):
                temp_window = [row[x_pos:x_pos + window] for row in lock[y_pos:y_pos + window]]
                for row in range(len(temp_window)):
                    for col in range(len(temp_window)):
                        if temp_window[row][col] == 0:
                            temp_window[row][col] = 1
                        else:
                            temp_window[row][col] = 0

                # print(temp_window)
                if temp_window in windows:
                    print(temp_window)
                    is_opened = True
                    break
                x_pos += 1
            y_pos += 1

    print(is_opened)
