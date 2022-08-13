import sys

input = sys.stdin.readline

if __name__ == '__main__':
    # 집합 속 원소 갯수
    # (1) Built-in 함수 활용
    # bin_정수를_이진수문자열로 변환
    print(bin(11))  # 0b1011
    # ->  bin().count('1')로 1의 갯수 세기
    print(bin(11).count('1'))  # 3


    # (2) 자체 구현
    # -> 반복문 속에서 n을 >>1 right shift로 이동해가며
    #    이진수의0 번째자리를 [ & 1 ]로 연산하여
    #    이진수 0번째자리가 1일 경우 누적합
    def count_bits(n):
        ret = 0
        while n:  # 0000 or 0 이 되기전까지 돌림.
            # 0번째 자리가 1이면, 누적
            if n & 1:
                ret += 1
            # 다음자리수를 0번째로 이동
            n = n >> 1
        return ret


    print(count_bits(11))  # 3

    ## 참고 __name__
    # -> 모듈이름인데, import된 모듈이 아니라 실행모듈일 경우만 __main__이 할당된다.
    # -> import된다면, __name__에는 해당a.py의 a만 들어가서, 실행되지 않는다.
    # -> main으로 실행될때만, 실행코드를 if __name__ == '__main__':에 넣어주자.

    # (3) 부분집합 연습 : 두 수의 합이 7인 경우의 수
    # input.txt
    # 6
    # 1 2 3 4 5 6
    N = int(input().strip())
    arr = list(map(int, input().split()))


    def solve():
        ret = 0
        # 1) 원소갯수가 N개인 경우의 모든 부분집합 경우의수를 나타내기
        #    0 ~ 2**n-1의 십진수 == 0000  ~ 1111포함여부 이진수가 생성된다.
        for i in range(1 << N):
            # 2) 해당 포함여부 비트표현 이진수를 -> 문자열로 바꾼 다음
            #    불켜진 것이 2개인 것 == 원소 2개인 부분집합만 골라낸다.
            if bin(i).count('1') != 2:
                continue
            # (원소가 2개인 경우)
            # 3) sum을 구해볼 예정
            sum = 0
            # 4) 포함여부가 0or1 아니라 배열의 j번째 암묵적 매핑배열원소를
            #   실제 값을 가져온다.
            # -> 이 때, 이진수에 대해 [각 자리별 shift를 위한 반복문]을 돌려서, 이진수 원소포함여부(1인지)확인된 것만, 매핑된값을 누적해야한다
            for j in range(N):
                # 5) j번째 비트자리가 불켜졌는지 확인한다.
                # -> 확인된 것만 누적한다.
                if i & 1 << j:
                    sum += arr[j]

            # 6) 합이 7인 것만 카운팅한다.
            if sum == 7:
                ret += 1
        return ret


    print(solve()) # 3


    pass
