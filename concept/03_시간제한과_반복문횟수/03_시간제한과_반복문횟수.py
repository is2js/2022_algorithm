import sys 
 
input = sys.stdin.readline 
 
 
def solution():
    ## 반복횟수당 연산속도
    # 10^6 회 -> 백만 -> 1초 이내
    # 10^7 회 -> 천만 -> 1초 이내
    # -> python은 1초안에 10^7~ 5*10^7 회 연산 가능
    # 10^8 회 -> 1억 -> 1초안에 불가능 -> 알고리즘 바꿔야함

    ## 문제에서
    # (1) 시간제한 확인: 시간제한 1초 -> 일반 반복문이면 5 * 10^7번 이하로 돌아야한다.
    # (2) 입력에서 반복문횟수 확인: 첫째 줄에  N이 주어진다 (1 <= n <= 100,000,000)
    #     -> 10^9(10억)회 반복 -> 일반 반복문으론 풀이 불가능 -> 다른 알고리즘
    #     -> O(n)으로는 못푼다는말 -> O(logN) or O(루트N) or O(1)로 풀어야한다.







    pass 
 
 
if __name__ == '__main__': 
    solution() 
