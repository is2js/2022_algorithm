import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## 2Xn타일링: https://school.programmers.co.kr/learn/courses/30/lessons/12900
    # -> 세로가 2로 고정이면, 가로만 뽑으면 자동으로 세로는 채워진다.
    #   1111111  2221
    n = int(input().strip())

    ## n을 1or2의 합으로 채워야한다.
    # -> [택1 경우의 수]는 재귀로 node를 경우의수를 뻗어나가는 순열?(user_bit없는, 무제한 순열)
    #                    n번째를 만들기 우한, 점화식을 만들어서, dp로 채워나간다.
    #  f(n) = f(n-1) or f(n-2)
    # => 보텀업 + 초기값을 가진 dp테이블

    # dp = [0] * (60_000 + 1)
    # (2) 점화식서 나타나는 부분문제 갯수만큼 기본값을 채워줘야야한다
    # n-1, n-2 -> f(1), f(2)가 있어야,f(3)부터 보텀업으로 채워냐갈 수 있따.
    # dp[1:3] = [1, 2]
    ## 참고-> dp테이블을 할당이 아니라 append로 하면, 동적으로 계산하는 수만큼 채울 수 있다.
    ##    => 현재 i번째는 할당없이 i-1, i-2로 만들어서 append해줘야한다.
    # dp = [False, 1, 2]
    ##    => 반복문 마지막번째를 [-1]인덱싱으로 뽑을 것이기 때문에, False는 넣을 필요 없다
    #     => index를 사용하지 않는 동적lst
    #     => 대신 반복문은 2번째부터 ~ n-1번째까지 돌려줘야한다
    dp = [1, 2]
    # for i in range(3, n + 1):
    for i in range(2, n):
        dp.append((dp[i-1] + dp[i-2]) % 1000000007)

    ## => n번째는 dp[i]가 아닌 dp[-1]로 구할 수 있다.
    print(dp[-1])