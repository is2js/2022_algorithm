import sys

input = sys.stdin.readline

if __name__ == '__main__':
    N, d, k, c = map(int, input().split())
    belts = [int(input().strip()) for _ in range(N)]

    ## O(N) O(k)를 2번 반복하면 1초의 10**7 을 뛰어넘어버린다.
    # -> 슬라이딩 윈도우는 [각 구간진행하며 누적 to]이 아니라, 앞에 1개 제거 + 뒤에 1개 추가의 [k개만 누적]이다.
    # -> 객체가 아니므로 to필드를 만드는 것이 아니라 [to배열]을 만들 되, [매요소 진행하며 누적]이 아니라
    #    [첫 요소의 k개는 누적]해놓고, 다음부터는 O(1)로 첫요소제거 마지막요소 추가를 통해 k개씩 누적집계하는 to배열을 만든다.

    # (1) 각 구간 조회전, 첫번째 구간의 to(슬라이딩윈도우k개)를 미리 계산한다
    # -> 다음 구간부터는 O(1)로 연산가능하게 만들어준다.
    # (2) 카운팅배열 + 종류갯수 카운팅변수를 적용한다
    #    -> 나머지 구간들을 돌며 윈도우구성만 바꾸면서, 집계할 것이다.
    count_sushi = [0] * (d + 1)
    kinds_of_sushi = 0
    # (3) 쿠폰초밥은 없는데 제공받았다고 가정해서 0->1로 카운팅 + 종류카운팅
    if not count_sushi[c]:
        kinds_of_sushi += 1
    count_sushi[c] += 1

    # (4) 첫번째 윈도우 미리 처리해놓고, 2번째 윈도우는 앞/뒤 요소만 제거/추가한다4
    # -> 구간문제의 to필드로서, 각각을 to필드값을 배열에 저장할 수도있지만
    #    최대값만 원하고 있으므로 그렇게 하진 않는다.
    for i in range(k):
        sushi = belts[i % len(belts)]
        if not count_sushi[sushi]: # 0 -> 1일 때만 종류 카운팅
            kinds_of_sushi += 1
        count_sushi[sushi] += 1

    # (5) 이제 첫번째구간을 제외한 2번째구간~마지막구간부터, N-1개를 슬라이딩 하되
    #     윈도우의 앞뒤만 바꿔주면 된다.
    #     -> 이미 처리한 N번째를 간다고해도, 회전배열이라서 첫번째 처리가 되니 상관없다.
    max_kinds_of_sushi = float('-inf')
    # for i in range(N-1):
    for i in range(N):
        except_sushi = belts[i % len(belts)]
        include_sushi = belts[(i + k) % len(belts)]

        # (5-1) 직전구간의 처리에서 앞짤/뒷더하기의 O(1)로 O(k)를 다 탐색하지 않기
        # 앞요소의 카운팅을 뺄때는, 뺴놓고, 1->0일 때, 종류카운팅을 -1한다.
        count_sushi[except_sushi] -= 1
        if not count_sushi[except_sushi]:
            kinds_of_sushi -= 1

        # 0 -> 1일때는, + 더하기 전에, 0일 때, 종류카운팅을  +1한다.
        if not count_sushi[include_sushi]:
            kinds_of_sushi += 1
        count_sushi[include_sushi] += 1

        max_kinds_of_sushi = max(max_kinds_of_sushi, kinds_of_sushi)

    print(max_kinds_of_sushi)

