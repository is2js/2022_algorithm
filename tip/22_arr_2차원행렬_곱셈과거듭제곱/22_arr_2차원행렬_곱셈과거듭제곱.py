import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## 행렬곱셈 -> 같은행렬의 거듭제곱 재귀까지
    # (1) 3by2(1부터등차)  2by3 10부터
    lst_A = [[col + row * 2 for col in range(1, 2 + 1)] for row in range(3)]
    # -> b - a + 1 = 갯수
    # -> a + 갯수 - 1 = b
    lst_B = [[col + row * 3 for col in range(10, 10 + 3 - 1 + 1)] for row in range(2)]
    print(*lst_A, sep='\n')
    # [1, 2]
    # [3, 4]
    # [5, 6]
    print(*lst_B, sep='\n')
    # [10, 11, 12]
    # [13, 14, 15]

    # (2) 앞 뒤 행렬의 접근순서
    # 앞 ->
    #    ->
    #    ->
    # 뒤 ↓ ↓ ↓

    # => 앞행렬은 행i부터 j개의 열을, 뒤행렬은 열k부터 j개의 행에 동시접근한다
    for i in range(len(lst_A)):
        for k in range(len(lst_B[0])):

            for j in range(len(lst_A[0])):
                # print(lst_A[i][j], lst_B[j][k])
                pass
            # print()
    # [1, 2]
    # [3, 4]  [10, 11, 12]
    # [5, 6]  [13, 14, 15]
    #
    # 1 10
    # 2 13 => 2개의 연산이 누적되어야한다. j만큼 돌리면서 0에 += 누적합
    #
    # 1 11
    # 2 14

    # (3) 앞행i에 대해, 뒤열k가 다 돌아가는 식으로 진행된다.
    #  -> 3 by 3에서  1row씩 만든다.
    #  -> 빈행렬 3by3을 초기화하고, [i][k]를 연산결과를 j가 동시에 돌아가는 동안 초기화 0에 누적합 연산해야한다.
    lst_C = [[0] * 3 for _ in range(3)]
    for i in range(len(lst_A)):
        for k in range(len(lst_B[0])):
            for j in range(len(lst_A[0])):
                lst_C[i][k] += lst_A[i][j] * lst_B[j][k]


    # print(*lst_C, sep='\n')
    # [26, 28, 30]
    # [52, 56, 60]
    # [78, 84, 90]

    # (4) 3중for문이 들어가지만 함수로 만들어놓고 사용할 수 있다.
    def multi_matrix(A, B):
        I, K, J = len(A), len(B[0]), len(A[0])
        temp = [[False] * K for _ in range(I)]
        for i in range(I):
            for k in range(K):
                for j in range(J):
                    temp[i][k] += A[i][j] * B[j][k]
        return temp


    # print(*multi_matrix(lst_A, lst_B), sep='\n')
    # [26, 28, 30]
    # [52, 56, 60]
    # [78, 84, 90]

    # (5) X 곱하기 2개 피연산자를 가진 연쇄연산(앞에 결과가 뒤의 피연산자)은
    #     => [피연산자들을 동일한 것 -> 거듭제곱 횟수n을 stack변수로 도입]하면
    #         [A의 거듭제곱]을 부분문제를 가지는 재귀로 풀 수 도 있다.
    #    AxAxA = f(3) = f(f(A,A), A) = f(2) * f(1)
    memo = [False] * 1_000
    def pow_matrix(A, n):
        if n == 1:
            return A

        # memoization섞어주기(부분문제들 보니까 반복될 것 같음)
        if memo[n]:
            return memo[n]

        # => 거듭제곱의 경우, n이 짝수일 때 vs n이 홀수일 때 부분문제가 다르다.
        #    짝수인 경우, 부분문제가 쉽게 풀린다. 부분문제 f(n//2) 한 것들의 곱 f(n//2) * f(n//2)
        #    홀수인 경우, 부분문제가 f(n-1) * f(1)
        if not n % 2:
            memo[n] = multi_matrix(pow_matrix(A, n//2), pow_matrix(A, n//2))
            return memo[n]

        memo[n] = multi_matrix(pow_matrix(A, n - 1), A)
        return memo[n]

    lst_2d = [[col + row * 3 for col in range(1, 3 + 1)] for row in range(3)]
    print(*pow_matrix(lst_2d, 1), sep='\n')
    # [1, 2, 3]
    # [4, 5, 6]
    # [7, 8, 9]
    print(*pow_matrix(lst_2d, 2), sep='\n')
    # [30, 36, 42]
    # [66, 81, 96]
    # [102, 126, 150]
    print(*multi_matrix(lst_2d, lst_2d), sep='\n')
    # [30, 36, 42]
    # [66, 81, 96]
    # [102, 126, 150]

    print(*pow_matrix(lst_2d, 3), sep='\n')
    # [468, 576, 684]
    # [1062, 1305, 1548]
    # [1656, 2034, 2412]

