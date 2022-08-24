import sys

input = sys.stdin.readline


def process():
    ## 교훈) 상수가 아니면 언패킹하지말고 묶어라
    ## -> 2개이상이면 일단 묶고 일괄 처리해라
    # a, b, c, d = map(int, input().split())

    ## 교훈) 요소들을 대소비교 하는 배열은, 일단 정렬하고 시작하라
    ## -> 객체가 아닌 값의 배열일 때, 주어진 순서와 상관없는 문제면, 일단 정렬하고 시작하라
    # lst = list(map(int, input().split()))
    lst = sorted(list(map(int, input().split())))

    ## 교훈) 중복관련이면 if len(set(lst))을 활용해라
    ## set(list)를 뒤없은 값을 활용하되, list로 풀어나간다.
    if len(set(lst)) == 1:
        return 50_000 + (lst[0] * 5_000)

    ## 교훈) 순서가 정해진 배열의 중복요소라면, 많은 것들이 가운데를 정복한다. 같다면 가운데가 다르다.
    if len(set(lst)) == 2:
        # 2개+2개 도 len(set()) == 2
        # 1133
        if lst[1] != lst[2]:
            return 2_000 + lst[1] * 500 + lst[2] * 500
        # 3개+1개
        # 1113 1333 -> 큰수가 3개라면, 1,2가 같다.
        # 1113 1333 -> 작은 수가 3개라면, 1,2가 같다.
        return 10_000 + (lst[1] * 1000)
    if len(set(lst)) == 3:
        #1123
        #1223
        #1233
        ## 교훈) 인접 2개만 중복일 경우, for문으로 돌면서 i, i+1로 확인하자.
        ##      i, i+1을 쓰는 경우, 마지막껀 아예 반복문을 돌지않도록 range에서 마지막항 제거 설정하자.(->if문 제거)
        # for i in range(len(lst)):
        #     if i == len(lst) - 1:
        #         continue
        for i in range(len(lst) - 1):
            if lst[i] == lst[i+1]:
                return 1000 + lst[i] * 100
    return lst[-1] * 100




def solution():
    ## early return과 early continue
    # -> white condition을 미리 만들어 indent를 줄인다.

    # ## early continue
    # # 잘못 사용한 예
    # for i in range(n):
    #     if state:
    #         process()
    #
    # # early continue
    # for i in range(n):
    #     if not state: continue
    #     process()

    ## early return과 삼항연산자
    # 잘못사용한 예
    def function(x):
        if x:
            return True
        else:
            return False

    # early return
    def function(x):
        if x:
            return True
        return False

    ## early return이후 [나머지 return도 조건문]인 경우
    ## -> 삼항 연산자로 대체할 수 있다.
    ##  ex> 꼬리재귀 -> if종착역 return 결과값변수 / return stack 다음재귀
    def function(x):
        # if x:
        #     return True
        # return True if x
        # return False
        return True if x else False

    ## 적용 예시: https://www.acmicpc.net/problem/2484
    TC = int(input())

    # answer = float('-inf')
    # for _ in range(TC):
    #     answer = max(answer, process())
    #
    # print(answer)

    ## 교훈 -> 최대값 찾아 업데이트도 list comp로 해결할 수 있다.
    ## - list comp로 append == stream으로 쓴다 -> .max() 대신 외부에서 max()때린다.
    ## -> java의 stream처럼 쓰면 된다.
    print(max(process() for _ in range(TC)))

    pass


if __name__ == '__main__':
    solution()
