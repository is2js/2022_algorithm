import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## 계차수열, 삼각수
    # An+1 - An = 6*n
    # An = An-1 + 6*(n-1)

    ## 1. 탑다운(재귀+memo)
    memo = [False] * 1_000


    def solve(n):
        if n == 1:
            return 1

        if memo[n]:
            return memo[n]

        memo[n] = solve(n - 1) + 6 * (n - 1)
        return memo[n]


    n = 1
    while solve(n) < 100:
        n = n + 1
    print(n, solve(n))

    ## 2. 보텀업(for+dp테이블) 점화식
    dp = [0] * 1_000
    dp[1] = 1
    final_i = None
    for i in range(2, 1000 + 1):
        dp[i] = dp[i - 1] + 6 * (i - 1)
        if dp[i] >= 100:
            final_i = i
            break
    print(final_i, dp[final_i])

    ## 3. 누적합에 초항(i는 1에서 시작) + 가변변수로 누적(+1씩count)
    # -> i는 2서부터 탐색하며, 초항+bn을 누적합으로 계산해버린다.
    i = 1
    sum = 1
    while sum < 100:
        i += 1
        sum += (i - 1) * 6
    print(i, sum)
