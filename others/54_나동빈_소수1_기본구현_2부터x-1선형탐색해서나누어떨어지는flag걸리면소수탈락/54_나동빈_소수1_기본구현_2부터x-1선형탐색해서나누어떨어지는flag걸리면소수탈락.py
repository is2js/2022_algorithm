import sys 
 
input = sys.stdin.readline


def is_prime_number(number):
    # 1과 자기자신 사이의 수 2~N-1을 돌면서, 해당수가 1개라도 나누어 떨어지면 탈락 flag
    for k in range(2, number):
        if number % k == 0:
            # flag를 이용한 로직이 없다면, [바로 return 불린]으로 끝낼 수 도 있다.
            return False
    return True

if __name__ == '__main__':
    ## 자주출제1: 소수
    # -> 1과 자기자신을 제외한 자연수는 [나누어 떨어지지 않는 자연수]
    # -> 2부터 x-1까지의 숫자를 탐색하여 하나라도 나누어 떨어진다면 소수아님이다.
    # -> 반복문속 if + flag를 쓰거나 / flag로 로직이 이어지는게 아니라면 [flag상황에서 return boolean]을 해버리면 된다.
    # -> flag 대신 다통과else시 처리해줄 수 도 있다.

    ## 1. 기본 알고리즘
    # => 2~x-1까지 선형탐색하므로 O(N)이 걸린다.
    print(is_prime_number(4))
    print(is_prime_number(7))




    pass 
