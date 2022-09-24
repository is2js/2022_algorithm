import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## 배열1개에 대해 독립된 원소 승x패 포함x미포함의 경우의수를 나열할 때
    arr_1 = list(range(10))

    ## (1) 배열에 있는 독립된 원소 10개에 대해 포함/비포함 부분집합의 모든 case는
    ##     000 ~ (1 << 10) - 1으로 순회하면서 만들어진다. (개별로 확인X)
    result = []
    for subset in range(1 << 10):
        ## (2) 직접 bit를 확인할 순 없고, 불들어왔는지 안왔는지 원소 1개씩으로 확인해서
        ##  => 초기화배열에 원소 1개씩 확인후, for bit개수만큼 돌면서 확인해야한다.
        temp = [0] * (10)
        for i in range(10):
            ## (3) 불이 들어온 경우 / 안들어온 경우
            if subset & (1 << i):
                temp[i] = 1
            else:
                temp[i] = 0
        result.append(temp)
    print(len(result), result)
    #  1024
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    # [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    # ...

    ## n개 원소 배열을 각 독립원소의 (O,X  / 포함,비포함 / 승,패) 여부로 만드는 [모든case 부분집합]
    ## (1) for subset in range(1 << n):으로 0000 ~ 1111까지 [2**n개의 모든 부분집합을 순회]하면서 구성한다.(개별조회X)
    ## (2)     temp=[0]*n의 개별subset에 대한 (2-1) 원소n개의 초기화 배열을 만들고,
    ##              for i                   (2-2) bit우측부터 1자리씩(1<<i)
    #                   if subset & (1<<i):   -> 원소 i번째를 O/X,포함/비포함,승/패를 확인
    #                        temp[i] = 1(0)  ->  초기화배열을 한자리씩 할당하면서 만든다.
    ## (3) 독립된 원소들을 1자리씩 채워나가면서, 집계할 것이 있으면 temp를 선언한 곳에서 가변변수를 만들어 누적집계한다
    n = 5
    for subset in range(1 << n):
        temp = [0] * n
        ## ryon vs apeach를 1자리씩 채우면서 점수 비교
        for i in range(n):
            if subset & (1 << i):
                ## 불들어왔으면 ryan의 승리로서 ryon배열(temp)에 값 할당 및, 가변변수에 점수 누적
                temp[i] = 1
            else:
                ## 불꺼져씅면 apeach의 승리로서 apeach 집계 가변변수에 누적(단, apeach도 0이면 점수 누적X)
                temp[i] = 0

