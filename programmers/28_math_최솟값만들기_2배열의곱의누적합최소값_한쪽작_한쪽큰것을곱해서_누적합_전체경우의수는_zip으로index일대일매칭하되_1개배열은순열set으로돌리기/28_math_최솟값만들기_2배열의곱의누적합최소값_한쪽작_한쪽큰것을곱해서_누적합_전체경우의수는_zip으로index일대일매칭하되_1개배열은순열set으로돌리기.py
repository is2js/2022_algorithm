import itertools
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## 최솟값 만들기: https://school.programmers.co.kr/learn/courses/30/lessons/12941#:~:text=%EB%B0%B0%EC%97%B4%20A%2C%20B%EC%97%90%EC%84%9C%20%EA%B0%81%EA%B0%81,%EB%90%98%EB%8F%84%EB%A1%9D%20%EB%A7%8C%EB%93%9C%EB%8A%94%20%EA%B2%83%EC%9D%B4%20%EB%AA%A9%ED%91%9C%EC%9E%85%EB%8B%88%EB%8B%A4.
    # 풀이: https://daekyojeong.github.io/posts/Algorithm7/
    ## ->2배열에서 1개씩 뽑아 곱한다 -> 곱집합(조합)이 가능한가?
    ## => 곱하도 교환법칙이 성립하므로 뽑기만 하면 된다.
    ##   product는 배열당 1개씩 뽑아준다.
    ##   => 문제는 모든 곱집합이 아니라..  배열당 1개씩만 사용되어야하고 그 뒤로 나오면 안된다.
    # => 배열당 1포인터? merge정렬처럼?
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ## 1:1매칭되는 경우의 수
    # => 배열 1개는고정해놓고, 나머지 배열이 순열로 순서에 따른 경우의 수를 나눠 매칭시킨다.
    # => 1:1매칭시키는 방법은 index로 매칭시켜야하므로 순서만 바꿔놓으면 된다.
    #    zip활용하면 바로 매칭된 값끼리 연산 된다.
    # => 중복된 원소를 가진 순열은 set()으로 중복을 제거해준다.
    # => 순열로 섞어준 배열을 먼저 for문으로 돌리고 고정된 배열을 index로 매칭시킨다.
    min_value = float('inf')
    for b in set(itertools.permutations(B)):
        sum_ = sum(x * y for x, y in zip(A, b))
        if sum_ < min_value:
            min_value = sum_
    print(min_value)

    ## 2. 암기
    ## => 길이가 같은 2배열의 [매칭 택1 곱의 누적합]의 최소값은
    ## => 최소값 x 최대값 순으로 곱해서 더하는 것이다
    A.sort()
    B.sort(reverse=True)
    print(sum([a*b for a, b in zip(A, B)]))
