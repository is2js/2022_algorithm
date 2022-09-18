import sys

# print(help(input))
input = sys.stdin.readline
# print(help(input))

if __name__ == '__main__':
    ## prefix sum_: 구간(누적) 합 -> 중간합계를 자주 구해야하는 경우

    # 슬라이딩 윈도우: 여러번의 누적연산시 그 갯수가 고정으로 여러번 할 때,
    # -> [고정된 범위의 부분합]을 여러번 수행
    # ex> 주식 이동 평균선 / 날씨 변화량

    # 누적 합: 여러번의 누적연산시 그 갯수가 고정적이지 않을 때
    # ex> 카드사용내역 중간합계 구간별 / 유튜브 조회수 기간별 합계 / 물건판매량 분기별 확인 (다른)
    # -> 일일히 계산하면, 한달에 1초, 6개월 6초, 10년 2분...
    # -> 9일까지의 누적합 - 3일까지의 누적합 = 4~9일까지의 누적합
    # -> 단, 2수의 차이로 바로 중간합계를 구할 수 있다.

    # 백준: 11659 번 https://www.acmicpc.net/problem/11659

    ### 누적합 알고리즘을 모를 때######################
    # N, M = map(int, input().split())
    # lst = [0] + list(map(int, input().split()))
    # for row in range(M):
    #     from_, to_ = map(int, input().split())
    #     print(sum_(lst[from_:to_ + 1]))

    ### 누적합 알고리즘을 알 때######################
    N, M = map(int, input().split())
    ## 주어진 시작/끝index가 1부터 시작한다면,
    ## 맨 앞에 [0]을 집어넣어서, 주어진 값으로 인덱싱되게한다!!
    arr = [0] + list(map(int, input().split()))

    # (1) 점진적 누적연산에 참여하는 모든 원소들에 대해
    #  -> 원소들 1개씩을 누적하면서, 매번 누적합을 빈 배열에 매번 모아둔다.
    #  5 4 3 2 1
    #  5 5+4 5+4+3 5+4+3+2 5+4+3+2+1
    #  -> 이렇게 해놓으면, 2번째(5 4)까지의 누적합을 인덱싱으로 바로 알 수 있고
    #  ->  4번째(5 4 3 2)까지의 누적합을 인덱싱으로 바로 알 수 있고
    # 슬라이싱에서 생길 O(N)없이 각 구간까지의 누적합을 바로 알 수 있다.
    # cf) (Slice	l[start:b]	O(b-start)	l[:] : O(len(l)-0) = O(N))

    sum_arr = []
    temp = 0
    #for i in range(N): # 원래 구간에 [0] 을 넣어줬으므로, 횟수는 N+1까지 구간합배열을 구해야한다
    for i in range(N + 1): # 조심!!
        temp += arr[i]
        sum_arr.append(temp)

    # (2) 완성된 구간합배열을 이용하면 start~b까지의 구간합을 인덱싱(O(1))로 구할 수있다.
    #  -> sum_arr[4] 5+4+3+2  - sum_arr[2] (5+4)
    #  -> sum_arr[4] 5+4+3+2  - sum_arr[1] (5)
    #  ->  =  2~4까지의 구간합
    #  => a에서b까지의 구간합은, b까지의 구간합 in 구간합배열 - (start-1)**까지의 구간합 in 구간합배열
    #  로 구해야한다.
    for _ in range(M):
        i, j = map(int, input().split())
        print(sum_arr[j] - sum_arr[i-1])

        ### 매번 누적합을 구하는 경우
        # sum_a = 0
        # for start in arr[i:j + 1]:
        #     sum_a += start
        # print(sum_a)

        ### for문 대신 sum을 사용하더라도, 인덱싱때문에 똑같다..?!
        # print(sum_(arr[i:j + 1]))

    ## 누적합 배열은 list로도 사용하지만, 2차원 행렬로도 사용한다.
    # 백준: 16570


