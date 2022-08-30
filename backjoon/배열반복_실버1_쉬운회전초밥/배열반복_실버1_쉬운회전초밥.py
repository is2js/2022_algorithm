import sys

input = sys.stdin.readline

if __name__ == '__main__':
    # 배열반복_실버1_쉬운회전초밥
    # 백준: https://www.acmicpc.net/problem/2531

    # 같은 종류가 배열에 있다 -> 카운팅배열에서 +2이상 가능하다.
    # 같은종류 2개이상 있는 곳에서 종류별 카운팅한다면 ->
    # -> [종류별 카운팅배열을 추가로 생성]하고
    # -> 카운팅배열 중[ 0 -> 1, 1 -> 0 ]만 카운팅하거나 제외시킨다.
    # -> 카운팅배열이 필요없다면 [F/T 방문배열]만 쓰면 된다.

    # 한 위치에서 고정된 k개 연속 집계 -> 슬라이딩 윈도우
    # 한 위치에서 고정된 k개의 카운팅?
    # -> 종류별 1개만 존재한다면, 카운팅변수(갯수) or 방문배열(종류 수)
    # -> 2종류이상 나눠서 셀땐, 카운팅 배열 or Counter
    # -> 2종류이상인데 카운트 + 종류 수(종류별 1개만 카운팅)하고 싶다면 방문배열 추가
    N, d, k, c = map(int, input().split())

    belts = [int(input().strip()) for _ in range(N)]

    max_kinds_of_eat_sushi = float('-inf')  # 돌기 전에 최대값 구하는 것이 도는 목적
    for i in range(N):
        # 매번 i부터 k개 탐색 -> 하되, 배열반복으로서 나눗셈연산자로 인덱싱
        # 돌기 전에 목적 생각하기 -> k개의 중복제외 종류만 카운팅
        kinds_of_eat_sushi = 0  # 쿠폰초밥 없는 것을 요리사 제공으로 먹어야 최대갯수 보장됨.
        count = [0] * (d + 1)  # 매번 k개에 대해 카운팅배열 초기화
        # 쿠폰초밥을 카운팅할 예정인데, 그전에 0에서 +1되는지 확인하고, 종류 갯수 변수를 +1해준다.
        if not count[c]: kinds_of_eat_sushi += 1
        count[c] += 1  # 쿠폰 1개은 종류 1개 채워놓음 -> 0 to 1로 갈때만 distinct 올라가도록

        for j in range(i, i + k):
            # (1) k개를 각각 꺼내면서 with 배열반복
            sushi = belts[j % len(belts)]
            # (2) 꺼낸 것의 갯수를 카운팅 할 건데,
            # (3) 현재 갯수가 0이라면, +1 하기전에, 확인하여 (0->1)로 인한 종류갯수+1
            if not count[sushi]:
                kinds_of_eat_sushi += 1
            count[sushi] += 1

        max_kinds_of_eat_sushi = max(max_kinds_of_eat_sushi, kinds_of_eat_sushi)

    print(max_kinds_of_eat_sushi)

