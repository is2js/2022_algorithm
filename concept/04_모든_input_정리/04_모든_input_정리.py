import sys 
 
input = sys.stdin.readline 
 
 
def solution():
    ## 입력의 종류 3가지
    # (1) 숫자 1개 -> map없이 int
    num = int(input())
    # (2) 숫자 2~3개 -> map만 -> 변수에서 언패킹
    a, b, = map(int, input().split())
    # (3) 문자열 -> 일반문장이면 input() / 1글자씩 쪼갠다면 split없이 -> list(input())
    string = input()
    char_lst = list(input()) # 다시 붙이려면 "".join

    # (4) 구분자 없는 숫자배열 -> 문자열로 취급 -> split없이 list(map(int,
    lst = list(map(int, input()))
    # (5) 구분자 있는 배열-> list(map(int, input().split()))
    lst = list(map(int, input().split()))

    # (6) 2차원 입력은 [1차원배열 node input] + list comp N회 돌리기 감싸기
    lst_2d = [list(map(int, input().split())) for _ in range(10)]


    # (6) 초기화 배열은 list comp(같은 숫자append)로 + 네이밍에 _1d, _2d 차원
    lst_1d = [0 for _ in range(10)] # 횟수가 요소의 갯수==열
    lst_2d = [[0 for _ in range(10)] for j in range(10)] # 안쪽부터 열의 갯수 -> 바깥이 행의 갯수

    pass 
 
 
if __name__ == '__main__': 
    solution() 
