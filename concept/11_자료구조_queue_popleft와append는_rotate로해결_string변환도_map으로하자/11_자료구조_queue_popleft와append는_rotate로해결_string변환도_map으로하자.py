import sys
from collections import deque

input = sys.stdin.readline


def solution():
    ## deque : queue의 python버전 (cf) list은 stack의 python버전)
    ## -> FIFO의 popleft() 뿐만 아니라 pop()도 가능하여 queue + stack이다.
    ## -> 앞에서 뺀 것을 append할 수 있으니, 돌아가는 수열을 만들 수 있다.
    # https://www.acmicpc.net/problem/11866

    N, K = map(int, input().strip().split())

    ## 교훈) N까지 등차수열은 range를 이터러블 생성자에 바로 대입한다.
    dq = deque(range(1, N + 1))
    result = []

    ## 교훈) 요소를 pop하는 반복문은 길이가 아니라, 빈배열전까지 돌도록 돌린다
    counter = 0
    while dq:
        counter += 1
        # 수열을 왼쪽으로 돌리면서 k번째마다 맨 앞에 것을 뺀다
        if counter % K == 0:
            result.append(dq.popleft())
            continue
        dq.rotate(-1)

    print("<" + ", ".join(map(str, result)) + ">")

if __name__ == '__main__':
    solution()
