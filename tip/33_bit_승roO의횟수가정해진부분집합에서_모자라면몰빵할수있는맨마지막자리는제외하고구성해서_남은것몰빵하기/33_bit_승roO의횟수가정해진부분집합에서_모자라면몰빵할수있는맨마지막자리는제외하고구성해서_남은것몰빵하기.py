import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## k개를 다써야하는데, 다못쓰는 경우
    # => 쉽게한다면, case마다 계산해놓고, count != n 이면 스킵하면 된다.

    n = 3
    k = 2
    result = []
    for subset in range(1 << n):
        cnt = 0
        temp = [0] * n
        for i in range(n):
            ## [1] for문 시작할 때, break면, 직전에 이미 탈출조건이 달성된 상태 반복문을 빠져나가 끝났을 수도 있다.
            ##   => [가변변수를 탈출조건에 도달(그까지 탐색)시킨체 stop]시키려면, while 조건처럼 for시작부에 탈출조건을 둔다.
            ##   => 반면에, [도달한다면 실패 flag라면, 가변변수 업뎃 직후 검사한다.]
            # if cnt > k: break
            if subset & (1 << i):
                temp[i] = 1
                cnt += 1
                ## [2] 탈출조건에 진입하기 전에 break를 하고 싶다면, 반복문 로직 마지막에 업뎃에서 확인하라.
                ##   => 반면에, [도달시 실패 flag라면, 가변변수 업뎃 직후 검사한다.]
                ## => 탈출조건 만족한상태에서, for문만 안들어갈뿐이지
                ## 갯수제한을 넘어선 경우, 아예 break해서 해당subset은 만들필요가 없다
                if cnt > k: break
            else:
                temp[i] = 0
        else:
            # flag에 안걸리고 다 만들어지면 저장
            result.append(temp)
    print(*result, sep='\n')
    # [1, 0, 0]
    # [0, 1, 0]
    # [1, 1, 0]
    # [0, 0, 1]
    # [1, 0, 1]
    # [0, 1, 1]

    # => 어렵게 가자면, case마다 계산해놓고, count > n 초과시에만 skip
    #    (1) 계산에 영향을 안주는 원소 1개를 경우의수를 비워둔다.
    #    (2) count > n 초과시만 skip한다
    #    (3) count == n와, count < n을 묶어서, n - count는 초과안하므로 n ~ 0까지 차지하는데
    #       남은 것을 경우의수 고려안한 해당 원소에 배정해서, 알아서 경우의수를 만들게 한다.

    ## ex> 원소는 6개(5,4,3,2,1,0)이 있고, 각 과녁에 화살을 쏠 수 있는데
    ##     총 3개를 쏴야한다.

    ##     각 독립된 원소에 쏠지 안쏠지 [선택하는 조합의 경우의 수](부분집합)을 bit subset을 구성한다.
    ##     이 때, subset을 0을 제외하고 5개만 구성하게 한다( 00000 ~ 11111) + ?
    ##     subset을 순회하며 직접 temp배열을 만들 때,
    ##     계산에 영향주지 않는, 맨 마지막 원소는[부분집합 중 남은게 있으면 거기다]가 배정해서 n개를 맞출 것이다.
    n = 3
    k = 2
    result = []
    # for subset in range(1 << n):
    ## (1) 계산에 영향안주고 && 경우가 미리 정해져있지 않은 독립원소 [0]점 자리를 제외하고
    ##     부분집합을 구성한다. ->  k=2개 중 남은 count가 있으면 그곳에 배정할 것이므로..
    for subset in range(1 << (n - 1)):
        temp = [0] * n
        count = 0
        for i in range(n - 1):
            if subset & (1 << i):
                temp[i] = 1
                count += 1
            else:
                temp[i] = 0
        ## (2) subset으로 1자리를 빼고, 다 부분집합의 상태로 구성했다.
        ##     나머지 자리 temp[-1] or temp[n-1]은 count를 보고 직접 결정해준다.
        ## (2-1) 일단 초과사용된 subset은 skip한다.
        ## => 원래 남은 자리 없다면 count != k이면 다 skip한다.
        if count > k: continue
        ## (2-2) 남은 자리에 남은count를 배정해준다.
        temp[-1] = k -count

        result.append(temp)

    # print(*result, sep='\n')
    # => 마지막자리를 제외하곤 O,X  0or1로서 정해진다(부분집합 구성원소)
    #    사용갯수가 모자라면, 경우의수를 지정해주 않은 곳에 몰빵해준다.
    # [0, 0, 2] 0, 0 => 2
    # [1, 0, 1] 1, 0 => 1
    # [0, 1, 1] 0, 1 => 1
    # [1, 1, 0]
