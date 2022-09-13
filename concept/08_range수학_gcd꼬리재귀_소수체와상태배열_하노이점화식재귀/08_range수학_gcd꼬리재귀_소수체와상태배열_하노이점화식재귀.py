import sys

input = sys.stdin.readline


def solution():
    ## 수학
    ## range에 수학식을 쓰자.
    for i in range(min(4, 6)):
        pass

    ## 유클리드호제법은 꼬리재귀로 외우자
    def gcd(a, b):
        # start >b
        # if start % b == 0:
        #     return b
        # return gcd(b, start % b)
        return b if a % b == 0 else gcd(b, a % b)

    # print(gcd(10, 10))

    ## 소수판별과 에라토스 테네스의 체
    # (1) 2~n-1까지 모두 체크 -> 나누어떨어지면, 소수아님 -> return False
    def is_prime(number):
        for 약수 in range(2, number):
            if number % 약수 == 0:
                return False
        return True

    # (2) 약수는 항상 곱하기의 짝으로 존재하므로, 1 2 44 8 16
    #    -> 약수를 다 돌지말고, 루트N까지만 돌면 이미 다 체크된다.
    #    -> 루트N을 표현할 방법이 없으니, for i in range(루트N)
    #      대신 while i*i <= n 까지만 돈다.
    def is_prime_sqrt(number):
        i = 2
        while i * i <= number:
            if number % i == 0:
                return False
            i = i + 1
        return True

    # (3) 에라토스 테네스의 체
    ## 이미 정해진 배열을, 하나씩 제외시킬 때는, check 상태배열을 사용한다.
    ## count정렬 / 체 / DFS BFS
    ## - 소수인 2부터 돌면서 -> 소수는 챙기고, 소수의 제곱부터 시작해서, 소수만큼 등차-> 소수x2, 소수x3 등의 소수의 배수들은 다 True로 탈락시킨다.
    ## -> 다음 수에서는 상태값이 True면 소수로 탈락 -> 그 다음수
    ##                상태값이 False면 소수 합격 -> 담고 -> 소수의 제곱 ~ 소수의 배수들
    def era(number):
        ## 상태배열을 False로 초기화
        # 상태배열은 index(값)에 안걸리면 안쓰면 되므로 처음부터(1부터) 초기화한다.
        # -> 암묵적 index로 묶임 (객체지향에선 linked list, 데코 객체(상태필드)로 묶음)

        ## 초기화배열과, 결과 누적용변수는 같이 초기화하자.
        check, result = [False for _ in range(number + 1)], []

        ## 값 배열이 for문의 index와 동일한, 1씩 증가하는 배열이면
        #  -> 굳이 배열로 선언할 필요없이
        #     어차피 돌릴 반복문의 index를 해당 값으로 보면된다.
        for i in range(2, number + 1):
            ## 상태값이 True로 체크되었다면, 그냥 넘긴다.
            ## -> 아직 아래로직은 작성안했지만, [조건에 따른 append]용 반복문이라면
            ##    [상태배열을 활용해서 빠르게 early continue]를 작성해보자.
            if check[i]:
                continue

            ## (check[i] == False상태) 첫번째 2부터 생각하면, 소수라고 판단해서 result에 저장한다.
            ## False로 초기화해서 다 append될 것 같지만 -> 아래에서 [미래의 값들을 True로 체크하는 로직]이 있을 것이라 생각한다
            result.append(i)

            ## 첫째항이자 소수2에 대해서,
            ## 2의 2배수부터 시작해서 등차를 2로 주어, 2의 배수들을 모두 소수탈락이다. True로 체크해둔다.
            ## -> 2부터 소수는 통과, 소수의 배수들은 탈락 -> 살아남으면 소수 -> result에 담기
            #    -> result에 담고나서 다시 소수의 2배수부터 배수들은 다 탈락시킨다.
            for j in range(i + i, number + 1, i):
                check[j] = True

        ## 메서드에서 반환할 때는, 결과배열 뿐만 아니라 상태배열도 튜플로 같이 반환해서
        ## main에서 써먹을 수 있게 해보자.
        return check, result

    # print(era(40))

    ## 하노이 by 점화식의 재귀
    ## 꼬리 재귀가 아니므로 return할 필요없다
    ## 연산이 아닌 print이므로 아랫단계 점화식을 꼭 연결할 필요가 없다
    ## n개를 옮긴다면, 1-> 3으로 n-1개만 +  1->3으로 1개 + 다시 2->3으로 n-1개
    ## f(n) = f(n-1) + 1 + f(n-1)


    ## 하노이는 stack(depth,자신->자식들)를 부분문제(n->n-1,n-2부분문제)로 풀 때, n->n-1만 변하는게 아니라
    ## -> 시작기둥 / 끝기둥도 바뀌니, 변수에 올려야한다.
    ## f(n) = f(n-1) + 1 + f(n-1) 역시 연산식으로 +가 아니라
    ## -> f(n-1, s,남은기둥)해결 -> (1, s,e기둥) -> f(n-1, 남은기둥, e기둥) 형식으로
    ##    순서대로 해결해서 출력만 하면 되니까, 연산식으로 + 되진 않는다.
    # 1->3
    def hanoi(n, start, end):
        if n == 1:
            print(start, end)
            return
        # 1,2,3기둥이름 고정 -> 1에서 3이동이라면, 나머지기둥은? 6-(1+3)기둥
        rest = 6 - (start + end)

        hanoi(n - 1, start, rest)

        print(start, end)

        hanoi(n - 1, rest, end)

    hanoi(3, 1, 3)

    pass


if __name__ == '__main__':
    solution()
