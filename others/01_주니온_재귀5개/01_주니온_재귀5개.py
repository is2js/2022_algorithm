import sys

input = sys.stdin.readline


def factorial(n):
    # n! = n * (n-1)!
    if n == 0 or n == 1:
        # 부분문제가 return을 시작하는 곳
        # 점점 return해서 자식재귀()까지 온다.
        # 종료return이 아니라 값return이면, 그 값이 누적적용되서 온다
        return 1

    # 자신의 처리 ->
    # return n *
    # 부분문제 호출 처리
    return n * (((factorial(n - 1))))

    pass


def fibonacci(n):
    # an = a(n-1) + a(n-2)
    if n == 1 or n == 2:
        return 1
    # 자신의 처리
    # return
    # 부분문제(자식)호출처리
    return fibonacci(n - 1) + fibonacci(n - 2)
    #
    pass


def binomial(n, k):
    # n,k = n-1,k + n-1,k-1
    if k == 0 or n == k:
        return 1
    # 자신의 처리
    # return
    # 부분문제나 자식호출
    return binomial(n - 1, k) + binomial(n - 1, k - 1)


def gcd(n, m):
    # n,m == m, r
    # -> 파라미터로 반환될 값이 업데이트되고, 점화식이 등치여서 같은 재귀함수만 호출하는 경우, [꼬리재귀]이다.
    # -> 객체지향에서는 (동일메서드를부르는)같은형의 객체 && 파라미터가 업데이트될 때 [꼬리재귀]를 쓴다.
    if m == 0:
        return n

    # 자신의 처리
    # return

    # 부분문제나 자식으로 처리
    # 꼬리재귀일 경우, 같은 메서드 1개만 파라미터 바꿔서 호출
    return gcd(m, n % m)


def hanoi(n, src, dst, via):
    if n == 1:
        print(f"{src} -> {dst}")
        return

    # 자신의 처리

    # 부분문제(자식들) 호출 처리
    hanoi(n - 1, src, via, dst)  # src -> via
    # 자신의처리(중간)
    print(f"{src} -> {dst}")
    hanoi(n - 1, via, dst, src)  # via -> dst

def solution():
    ## 재귀 ->
    # 0) 부분문제를 이용한 점화식을 생각한다.
    #    # n! = n * (n-1)! -> function(n): return[자신의처리] n[자신의처리] * function(n-1)[부분문제이자 자식호출]
    # 1) base case
    # 2) n일 때의 자신의 처리
    # 3) n-1, 자식depth+1 등은 [부분문제]/[자식문제]로서
    #    업데이트된 인자로 자신의 처리를 하도록 한다.
    #    부분문제에서 달라지는 것이 있으면, 파라미터로 올려준다.
    #    변한인자로 자식재귀호출한다면, 해당문제는 해결되었다고 가정한다 ex> 메서드()호출은 값 반환
    # 4) 부분문제에서 받은 값으로 끝처리를 한다.

    # 1) 팩토리얼
    print(factorial(5))

    # 2) 피보나치 n번재항은?
    # 1, 1, 2, 3, 5, 8, 13
    print(fibonacci(4))

    # 3) 이항계수(조합)
    # 두 자연수 n, k(n>=k)에 대해 이항계수(조합) (n k) = nCk를 구하라
    # 배경지식이 필요함
    # nCk = n! / k!(n-k)!
    # nCk = n-1Ck + n-1Ck-1
    # 종료조건 k=0, k=n이면 1
    # 점화식 Bnk = Bn-1k + Bn-1k-1
    # -> n뿐만 아니라 부분문제나 자식에서 k도 줄어들 수 있다.
    print(binomial(5, 2))

    # 4) 최대공약수
    # 배경지식: 유클리드의 정리
    # r = n%m(n>=m)일 때, gcd(n, m) == gcd(m, r)과 같다
    # n을 m으로 업데이트, m은 n%m으로 업데이트
    # 종료조건 m == 0-> 0과의 최대공약수는 나머지 큰수 자기자신이다.
    # 재귀호출: gcm(n, m) == gcd(m, n%m)

    # -> 파라미터로 반환될 값이 업데이트되고, 점화식이 등치여서 [같은 재귀함수만 호출]하는 경우, [꼬리재귀]이다.
    # -> 객체지향에서는 (동일메서드를부르는)같은형의 객체 && 파라미터가 업데이트될 때 [꼬리재귀]를 쓴다.
    print(gcd(10, 5))

    ## 공식상으로 인자만 다르지만,같은 식으로 풀리고, 결과값이 인자에서 움직이 ㄹ때,
    ## 꼬리재귀를 쓴다.

    # 5) 하노이의 탑
    # return함수없이 재귀의 과정을 이용하는 것
    # 입력조건: 원반갯수n
    # 현재기둥source(src)->목적지기둥(destination)dst, 경유할기둥via
    # 종료조건: 원반 1개를 src -> dst로 옮긴다
    # 부분문제: n-1개 src -> via
    #          1개   src -> dst
    #         n-1개  via -> dst
    hanoi(2, 1, 3, 2)  # 2개의 원판을 1번기둥에서 3번기둥으로 옮기는 법

    pass


if __name__ == '__main__':
    solution()
