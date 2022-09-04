import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## 구현 -> 시뮬과 완전탐색에 초점
    # 코드 긴 것 + 실수/소수점 + 문자열끊어처리 + 라이브러리 찾아서 사용
    # -> 2차원 공간(행렬)로 사용
    #    왼쪽위가 *0,0 첫번재 좌표
    #    특정위치 + 방향벡터로 다음위치를 확인

    ## 예시1: 상하좌우
    # NbyN 공간 가장위 (1,1) 가장아래(N,N) -> 상하좌우이동 -> L,R,U,D
    # 공간벗어나면 무시

    N = int(input().strip())
    plans = list(input().split())
    # directions = {
    #     'U': lambda x, y: (x + -1, y + 0),  # 상
    #     'D': lambda x, y: (x + 1, y + 0),  # 하
    #     'L': lambda x, y: (x + 0, y + -1),  # 좌
    #     'R': lambda x, y: (x + 0, y + 1),  # 우
    # }
    #
    # curr_direction = (1, 1)
    # for plan in plans:
    #     next_direction = directions[plan](*curr_direction)
    #     if not (1 <= next_direction[0] <= N + 1 and 1 <= next_direction[1] <= N + 1):
    #         continue
    #     curr_direction = next_direction
    #
    # print(*curr_direction)

    ## 풀이
    # (1) 시작 좌표를 x와 y를 나누어서 튜플로 만든다?
    x, y = 1, 1
    # (2) 방향벡터도 x와 y를 나누어서 처리한다.
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    # (3) 방향벡터 2개를 암묵적인덱스로 묶은 배열을 만들어 매핑한다.
    move_types = ['L', 'R', 'U', 'D']

    for plan in plans:
        # (4) 주어진plan과 매핑배열의 value가 일치하는 [index]를 찾아야,
        #  -> 매핑배열에 연결된 암묵적 배열들을 사용할 수 있다.
        #  -> 암묵적 매핑은 index를 찾아야한다.
        for i in range(len(move_types)):
            if plan == move_types[i]:
                # (5) python은 가변변수nx, ny를 반복문위에서 초기화하지 않아도
                #     greedy(반복문 속  매번 업데이트) or 증감연산이 아니라면
                #     -> 1번만 필터링되서 찾는 것이면 초기화없이 반복문안에서 선언한 뒤, 바깥에서 쓰면 된다.
                nx = x + dx[i] # index를 찾았으면, 매핑된 배열들을 다 사용할 수 있따.
                ny = y + dy[i]
        # (6) 좌표탐색은 next좌표를 처리하기 전에 범위검사부터
        if nx < 1 or ny < 1 or nx > N or ny > N:
            continue
        x, y = nx, ny

    print(x, y)




