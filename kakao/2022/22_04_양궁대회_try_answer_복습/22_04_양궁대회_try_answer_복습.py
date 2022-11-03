import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## 양궁대회: https://school.programmers.co.kr/learn/courses/30/lessons/92342
    n = int(input().strip())
    info = list(map(int, input().split()))

    ## 가장 큰 점수차이 -> 점수차이diff를 max greedy해야한다.
    #  => max_diff = 0(차이의 default값은 0으로 시작해서 발견안되면 비긴 경우다)
    #  => 매번 2배열의 점수차이를 기록해놓아야한다. => greedy for문위에서 가변변수 1개로 재활용하자.
    #  => ryan이 이기는 경우를 발견해야하므로, max_diff의 계산은 ryan - apeach 로 순서가 정해져있따
    #     r - a > 0인 경우가 이기는 경우로서 greedy되고,같거나 지는 경우는 무시되고, max_diff는 0으로 남는다.
    ## max_diff가 업뎃 안되는 경우는 -1을 반환해야한다.
    # max_diff = 0 # ryan- apeach
    # if max_diff == 0: print(-1); exit()

    ## 10 ~ 0을  info index에 매핑해놨다
    ## => 숫자는 매핑가능하지만, 이렇게 완전역순도 매핑가능하다.
    #      그러나 매핑을 풀어 계산할 떈 idx 대신 (len - 1 - idx)로 계산해야한다.
    ## => val에 count가 담기지만, 매핑주체는 idx * val이 아니라 (len-1-i) * val 로 쓰어야한다

    ## 비교할 2배열 중 1개는 이미 정해져있다
    # => 나머지 1개의 배열을, 정해진 배열을 가지고 기준에 맞춰서 생성한 여러 case가 있을 것이다

    ## 일단 n개를 10~0사이에 배분하는 경우의수를 모두 탐색하면서 & 안되는 경우 잘라내야한다.
    ## 갯수는 일단 2번째로 생각하고, 그 전에, 해당k과녁에 어피치가 이길 것인지 vs 라이언이 이길 것인지 정할 수 있다.
    ## => 분배하기 이전에, idx(10-idx) * val의 누적으로 계싼할 것인데
    ##  (1) 미리 각 index과녁마다, 사용할 것인지(1 == ryon승) vs 안할것인지(0 == ryon패, 갯수가 같거나 지거나 둘다 0이거나)
    ##   => 각 과녁을 승으로 쳤다면, apeach보다 +1개를 배정해야한다. count가 증가한다(n과 바로 비교ㄴㄴ 나중에)
    ##   => 각 과녁을 못쓴다면, 굳이 여기에 화살을 던질필요가 없다, 이기면서 차이가 커야하므로 다른데 던져야한다.
    ##      이 때, 화살은 안쏘더라도, apeach가 점수가 오를 수도 있고(어피치 1이상, ryon 0, 안오를 수 도 있다(둘다 0)
    ## (2) 각 경우의 수에 맞춰 count를 계산해놓고, n을 넘어서면 버려야한다.
    ## (3) n을 맞춰서 ryon배열을 완성했다면, 각각의 점수를 비교해서 -> max_diff를 greedy탐색 중 업뎃한다.
    ## (4) 추가로 같은 max_diff를 만족하는 여러 ryon배열이 완성될 수 있으니 == 조건을 주고, 추가조건에 맞으면 또 업뎃한다

    ## 1. answer가 info와 동일한 길이의 ryon 배열인데, 미리 0으로 초기화해놓는다.
    # answer = [0] * 11
    ##  => 어차피 greedy결과 중탐색 된 ryon배열이 나올 것이라서.. 초기화해놓을 필요는 없을 것 같긴하다.
    answer = None
    ## 2. 매번 case마다 ryon배열을 1개 원소마다 채워서 완성해야한다. ryon 임시배열을 선언해놓는다.
    # ryon_temp = [0] * 11

    ## 3. greedy 탐색을 한다.
    max_diff = 0  # ryan - apeach

    ## 4. greedy를 돌기전에, [case별 ryon배열]을 완성하기 위해, case를 먼저 만든다.
    ##    각 과녁당, 1이 들어와있으면, ryon이 화살을 더 많이 쏴 이긴 상태로 가정하고 만든다.
    ## => 1을 10개를 채운다. 원래는 11자리이지만, [10 ~ 1 0] 중에 오른쪽에서부터 10을 만족하니까, 1까지 10개만 하고
    ##    0은 점수에 반영안되므로 경우의수를 찾아보지 않는다?
    ##   + 00000000 은 ryon이 이길 수 없는 경우이므로, 000000000001 부터 시작한다.
    for subset in range(1, 1 << 10 - 1 + 1):
        ## 5. subset반복문 내부라면, case1개를 선택한 상태다. -> 조건에 맞는 ryon배열을 만들어보자.
        ##    subset은 for 갯수를 돌면서, 1이면 ryon이겨서 점수up, 0이면 apeach점수up or 점수x을 해줘야한다.
        ##   => [부분집합을 통한 배열생성]은 1개 원소씩 돌면서 배열을 생성한다. => [원소갯수만큼 미리 갈이를 초기화된 배열]이 있어야한다
        ryon, apeach, cnt = 0, 0, 0
        ##   => 부분집합을 통한 배열생송 및 배열비교는, 1개원소씩 돌면서 빈배열에 할당하며 배열생성 -> 비교까지 동시에 한다.
        ##      subset은 bit로서 len은 안되고 직접 길이만큼 0부터 돌면서 원소를 1개씩 완성한다.
        ryon_temp = [0] * 11
        for i in range(10):
            if subset & (1 << i):
                # case별로 원소에 1이 들어왔으면 ryon배열에 할당하여 완성하고, 그 점수도 반영한다.
                # -> 이 때, 화살은 apeach보다 1개 많도록 배정한다.
                ryon_temp[i] = info[i] + 1
                # 배정한 만큼 count 해야한다. 제한이 n으로 걸려잇기 때문에 다 완성하고 나중에 cut해준다.
                cnt += ryon_temp[i]
                # 점수는 해당인덱스의 역인덱스로 산출한다고 했다
                ryon += 11 - 1 - i
            else:
                # apeach가 이기면, ryon배열은 화살을 안쏘니 0으로 배정해서 완성하고, apeach의 점수를 올려주는데 조건이 있다.
                ryon_temp[i] = 0
                # apeach가 이긴 경우는, ryon은 0으로 고정이고, apeach의 점수를 올릴테지만, apeach도 0인 경우에는 점수를 안올린다.
                if info[i]:
                    apeach += 11 - 1 - i
        ## 이제 subset을 1자리씩 돌면서, 마지막원소를 제외한 ryon_temp를 생성 / 점수채우기를 했다.
        ## max_diff greedy를 위해서 점수를 diff를 구하고, 비교해서 업뎃한다.
        ## => 그 전에 ryon배열의 11번째 원소는 직접 완성해주기로 했다. (쓰고 남은 경우가 발생해서 휴지통 자리로서 밀어넣을 수 있는 경우)
        ## => 그 전에, 이미 ryon이 사용한 cnt가 n개를 넘어서면 탈락이다. 다음 subset->다음ryon배열을 완성해서 비교해야한다.
        if cnt > n: continue
        ##    쓰고 남은만큼 ryon_temp[11]에 화살을 다써줘야한다. 점수에는 반영이 안되고, 남을 수 있어서 이렇게 구성했다.
        ## (cnt <= n)의 상황 => 차이를 내서 남은만큼 11번째 원소, 0점과녁에 넣어서 ryon_temp를 완성시킨다.
        ## => 0개라도 넣어줘야하니, 이렇게 구성하면 된다. (남았으면 넣어준다?ㄴ) 작거나 같은상황이면 0도 할당해도 되면 그대로 할당
        ryon_temp[10] = n - cnt
        ## 완성된 diff(r-a) 및 해당배열 상태에서는  greey 업뎃
        # if ryon - apeach > max_diff:
        ## 추가로 max를 만족하는 여러개를 추가조건에서 1개더 고른다면 if == max를 조건을 추가하고 거기서 만족시 업뎃해준다.
        if ryon - apeach == max_diff:
            ## 뒤에서부터 2개의 배열을 동시에 봤을 때, val이 큰 것이 나오는 순간 그놈으로 선택
            ## 현재 max와 동일한값배열 vs 직전까지의max
            ## => 현재가 채택되는 경우만 업뎃하면 된다.
            for i in range(len(ryon_temp) -1 , 0 -1, -1):
                if ryon_temp[i] > answer[i]:
                    max_diff = ryon - apeach
                    answer = ryon_temp[:]
                    ## 순서대로 보다가 발견되면 break를 탐색을 끝내야한다.
                    break
                # else:
                ## <=를 동시에 보면 안된다. == 인  경우는 다음앞쪽index를 봐야하므로
                ## == > 맨뒤에 배치해서 continue없이 넘어가게 한다.
                elif ryon_temp[i] < answer[i]:
                    ## 업뎃없는 상황이라고 그냥 넘기면 순서대로 탐색의 장점x 이미 끝났은 탐색을 멈춰야한다.
                    break
        elif ryon - apeach > max_diff:
            max_diff = ryon - apeach
            answer = ryon_temp[:] # 원래 for속 지역변수 컬렉션의 할당은 복사안해도 되긴하다.

    print(max_diff, answer)

    if max_diff == 0: print(-1); exit()
