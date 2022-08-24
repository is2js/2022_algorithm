import sys

input = sys.stdin.readline

if __name__ == '__main__':
    # 쉬운 회전초밥 중등부: https://www.acmicpc.net/problem/2531
    # -> N 3만  K 3천/ 어려운 300백만
    # -> N개를 현재위치로 탐색 for 10^4
    # #  내부에서 k개 먹을 수 있는지 0,1,2,.. 10^3
    # => 만만억 -> 만곱하기 만은 1억이고, 1초..10*8은 1초안에 풀린다. -> 별 다른 알고리즘 없이 N과 K를 각 탐색
    # 3만 * 3천 -> 9천만 -> 1억보다 작아서 1초안에 풀린다. -> 특별한 알고리즘이 필요치 않는다.

    # (1) 리스트가 끝없이 회전 ( 마지막 초밥 -> 다음초밥 -> 첫 초밥)
    # -> 방법1: index가 N-1보다 크면, N을 빼주는 방식
    # -> 방법2: 나머지 연산 이용하기 -> 회전하는 배열, 회전하는 요일 문제를 풀 수 있음.
    # day = ['월', '화', '수', '목', '금', '토', '일', ]
    # print(day[0])
    # print(day[6])
    # print(day[7 - 7])  # 방법1: index가 N-1(6)을 넘는 순간, -len 을 해주기?
    # print(day[7 % len(day)])  # 방법2: index % len ->  첫번째부터 구간반복되는 효과
    # print(day[13 % len(day)])  # 방법2: index % len ->  첫번째부터 구간반복되는 효과
    # #  len의 배수가 첫번재 요소이다.
    # print(day[14 % len(day)])
    # print(day[200 % len(day)])  # 200일이 지난 후 요일은?? 어차피 0일 때 첫요소부터 반복되니, 구해진다.
    # print(day[3000 % len(day)])

    # (2) 쿠폰 -> k개밥을 먹었는데, 이미 쿠폰을 먹을 경우, vs 쿠폰 먹지 않았을 경우 -> +1만
    # -> 최대값을 구할 때마다, 쿠폰초밥이 있는지 vs 없는지 -> + 1
    # -> 가장 먼저 쿠폰을 먹었다고 가정하고, 최대값찾으면 더 쉽게 해결된다.
    # -> 처음과 끝의 순서를 바꿀 때, 주의점 확인해야함.
    # 이문제에서는 먹는 순서를 바꿔서 먹어도 상관없다고 한다.

    N, d, k, c = map(int, input().split())
    belt = []
    for _ in range(N):
        belt.append(int(input().strip()))

    # 최대값을 탐색해서 구할 때는, 반복문 전 지역변수로 선언해야한다.
    max_sushi = 0

    # N개의 초밥 위치를 다 뒤져봐야한다.
    for i in range(N):
        # 각 시작위치 마다, 쿠폰 초밥은 이미 먹었으니 카운팅에 1을 넣고 시작한다.
        eat_sushi = 1
        # 각 자리마다 먹었는지 안먹었는지 방문배열을 사용한다. -> 중복 문제는 [종류별 상태배열]로 체크한다 (자리별은 안됨)
        # -> 암묵적매핑에서 0은 취급안하기 때문에, 항상 종류+1개로
        check = [0] * (d + 1)
        # 쿠폰초밥은 이미 먹은 것으로 체크한다.
        check[c] = 1
        # 현재 위치(i)로부터 k개의 초밥을 먹는다. range(i, i+k)
        for j in range(i, i + k):
            # 현재 먹는 초밥j를 바로 쓰지말고, 회전배열이라면 [인덱스 %len]를 써서 돌아가도록 한다.
            sushi = belt[j % len(belt)]
            # 아직 먹지 않은 종류(check배열 0)라면, 종류별 첨 먹은갯수 카운팅을 늘린다.
            if not check[sushi]:
                eat_sushi += 1
            # 이미 먹은것이라도(check배열 >=1), 종류별 먹은 갯수는 무조건 +1 늘려준다
            # -> 그냥 먹은 것은 왜 1로 체크가 아니라, 갯수를 늘려줄까??
            # -> 어려운 초밥 문제에 필요하다.
            check[sushi] += 1

        # 현재i위치에서 연속으로 먹은 갯수가 최대값인지 업데이트해준다.
        max_sushi = max(max_sushi, eat_sushi)
    print(max_sushi)

