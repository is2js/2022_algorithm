import sys 
 
input = sys.stdin.readline
sys.setrecursionlimit(10_000)


def dfs(n,
        sum, result):
    if sum == n:
        return [list(result)]
    ## 1, 2씩 증가한다면, 종착역을 넘어갈 수 있으니 false로 답해주고, 집계시 필터링한다.
    if sum > n:
        return False

    temp_result = []
    for x in [1,2]:
        k = dfs(n, sum + x, list(result) + [x])
        if k:
            temp_result += k

    return temp_result


if __name__ == '__main__':
    ## 2Xn타일링: https://school.programmers.co.kr/learn/courses/30/lessons/12900
    n = int(input().strip())

    ## (1) n을 1or2로 구성하는 방법을 나눠야한다.
    ## -> 택1의 경우의 수는, 재귀 or보텀업으로 풀어야한다.
    ## f(4) = f(3) + f(2)
    print(dfs(n,
              0, []))
    pass 
