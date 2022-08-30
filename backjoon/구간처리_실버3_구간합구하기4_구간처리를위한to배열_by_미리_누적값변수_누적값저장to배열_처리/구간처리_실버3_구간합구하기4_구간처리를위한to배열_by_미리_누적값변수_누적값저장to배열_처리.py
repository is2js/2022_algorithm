import sys

input = sys.stdin.readline


def process():
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i - 1]) # A ~ B 구간처리는 B - (A-1)


if __name__ == '__main__':
    # 구간합: https://www.acmicpc.net/problem/11659
    N, M = map(int, input().split())
    # 구간처리해야할 배열은, 사실은 숫자가 객체, 구간별 누적처리는 to필드로 만들어야한다.
    # -> 구간처리를 위해서는, [누적처리용 to배열]이 필요하며, 배열은 0부터 시작하므로 1개 만들어줘야한다
    # -> 시작 특이점 객체 개념이라 생각하자.
    numbers = [0] + list(map(int, input().split()))

    # 구간처리하기 전에, 구간별 to필드값 대신, [구간처리용to배열]을 미리 매핑해놓는다.
    # -> 누적합을 위한, (1)값 누적 가변 변수
    # -> 누적합을 저정할, (2) 각 구간마다 to배열
    prefix_sum = []
    cum_sum = 0
    for i in range(N + 1):
        cum_sum += numbers[i]  # 값 누적
        prefix_sum.append(cum_sum) # 누적한 값 배열에 저장

    # print(prefix_sum)
    for _ in range(M):
        process()
