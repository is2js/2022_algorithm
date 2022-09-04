import sys 
 
input = sys.stdin.readline


def process():
    numbers = [int(x) for x in list(input().strip())]

    # (1) 연산을 하기 위해, 첫번째 피연산자는 일단 빼놔야한다.
    first = numbers[0]

    for i in range(1, len(numbers)):
        second = numbers[i]
        # (2) 1개라도  1이하라면 더하기를 그렇지 않으면 곱하기를 수행한다.
        if first <= 1 or second <= 1:
            first += second
            continue
        first *= second
    print(first)



if __name__ == '__main__':
    ## greedy 곱하기 혹은 더하기 -> 문자열 숫자가 주어진다.
    # => 특정조건에서만 greedy
    # -> 0 or 1인 경우만, 더하기를 수행하는 것이 더 효율적이다.
    # -> 즉, (둘다 교환법칙은 성립하니) 피연산자 2개 중 1개라도 0or1이 포함된 경우엔, 더하기 연산이 더 효율적이다.
    # => greedy이나, 특정 조건에서만 작동, 다른 조건이면 다른 연산 수행

    for _ in range(2):
        process()
