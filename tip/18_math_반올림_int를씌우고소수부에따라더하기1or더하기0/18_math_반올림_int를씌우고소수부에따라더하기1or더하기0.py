import math
import sys
 
input = sys.stdin.readline 
 
 
if __name__ == '__main__':
    ## 0.5의 반올림은 python에서 짤린다.
    n = 2.5
    print(round(n))
    # (1) 소수점(수-내림수)이 0.5이상 달고 있으면 ceil로 올리고, 아니면 floor로 내린다.
    if n - math.floor(n) >= 0.5:
        print(math.ceil(n))
    else:
        print(math.floor(n))

    # (2) int로도 구현가능 -> int(n)이 중복이다.
    if n - int(n) >= 0.5:
        print(int(n) + 1)
    else:
        # print(int(n))
        print(int(n) + 0)

    # (3) 일단 int를 씌우고, 소수부가 0.5보다 크면 + 1 아니면 + 0을 더한다.
    print((int(n) + 1 if n - int(n) >= 0.5 else 0))

