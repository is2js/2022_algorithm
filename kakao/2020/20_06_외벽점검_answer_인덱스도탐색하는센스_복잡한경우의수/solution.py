import sys
 
input = sys.stdin.readline 

import itertools
 
if __name__ == '__main__':
    ## 외벽점검: https://school.programmers.co.kr/learn/courses/30/lessons/60062
    n = int(input().strip())
    weak = list(map(int, input().split()))
    dist = list(map(int, input().split()))

    ## 1. 추적지점의 갯수를 계속 사용하므로 변수로 빼놓는다.
    weak_size = len(weak)
    ## 2. 공간이 원형이므로 10->1의 거리3을, 101112 -> 13으로도 볼 수 있다.
    # => 10에서 1갈때의 거리를 쉽게 구하기 위해선, 1바퀴를 더 extend해놓는다.
    # => 각 weak값에다가 구간인덱스를 늘려주는 개념으로 + n을 해준 weak를 한번 더 더한다.
    weak = weak + [w + n for w in weak]
    ## 3.
    min_count = float('inf')

    ## 4. 순열로 만들어진 취약지점들을, 모든 경우의수마다, 처음부터 시작하기 위해서, 갯수로 -> index를 돌려 순서대로 출발시킨다.
    for start in range(weak_size):
        ## 5. 시작이 정해진 weak위치에서, 또 매번 dist를 순열로 탐색한다
        #### => cnt제한 등 조건이 있는 순열이 아닐 땐, api로 순열을 처리한다.
        for d in itertools.permutations(dist, len(dist)):
            ## 6. 끝나기전까지 사용된 탐색갯수를 변수로 미리 빼놓는다. -> 현재부터 시작하니 1로 cnt한다
            cnt = 1 # 누적
            ## 7. 끝나기전까지 탐색하는사람마다, 탐색대상인 weak에서의 pos를 자기가 이동한만큼 index를 이동시켜줘야한다.
            ##    A배열 탐색시, B배열의 index를 onepointer로 이동하려면, index를 가변변수로 업데이트 해줘야한다.
            pos = start # 위치 업데이트 # 탐색 cursor 원포인터 # 현재친구의 시작점
            ## 8. 이제 친구를 1명씩 쓴다.
            # for i in range()
            ## => 모든 취약지점이 방문되었는지 여부를 알기 위해선, 하나하나씩 거리를 측정해봐야한다.
            ## => 현재친구의 시작위치는, 이미 취약지점에 올라간 상태에서, 거기서 시작하므로 방문할 필요가 없다
            ##    index 1부터 시작해서 -> 모든 취약지점을 n-1까지 index를 돌게한다?!
            for i in range(1, weak_size):
                ## 9. 다음에 방문해야할 위치는, 시작점에서 i만큼 진행한 index값으로 잡아야한다..?! 인덱스의 +1씩 증가..
                next_pos = start + i
                ## 10. 1에서 시작해서 5까지 갈 수 있는지를 거리를 봐야한다.
                diff = weak[next_pos] - weak[pos]
                ## 11. 현재 친구가 갈 수 있는 거리는 d에 있다.
                ## => cnt는 1이지만, 첫번재 친구가 사용할 index는 cnt - 1의 0이다.
                if diff > d[cnt - 1]:
                    ## 12. 만약 1에서 다음거리 5까지를 못갔따면, 5에서 새로운 친구를 출발시켜야한다.
                    ## => 다음 친구의 시작위치pos를 next_pos로 업뎃시키면 된다.
                    pos = next_pos
                    ## 13. 친구를 한번더 쓴 것이므로, +=1
                    cnt += 1
                    ## 14. 만약, diff를 넘어선 상황이라면?, 위 조건에 안걸리고 5->6을 거쳐 7까지 갈 수 있는 상태다
                    ## => 사용친구 명수인 cnt가 늘어나지 않은 상태로, 위 조건에 걸릴때까지 i가 업뎃된다.
                    ## => 즉,pos=5cnt2에서,  next_pos가 조건에 안걸리느 6skip 후, diff조건에 걸리는 10이 next_post가 될떄까지 i만 증가한다

                    ## 15. 하지만, 입력값에 따라서, 친구가 부족할 수도 있다
                    # => 문제조건에 모든 친구를 투입해도 점검안되면 -1 반환
                    ## => 이럴 때는, 친구를 사용할만큼 사용하되, dist에 제시된 친구명수를 넘어가면,
                    ##    탈락으로 매번 체크한다.
                    if cnt > len(dist):
                        break
            ## 16. for문이 끝나면, 초과된 상황에서 끝난 것은 아닌지 확인해야한다.
            # -> 초과안된상황이라면 min_count 업뎃 => 초과된상황이면 업뎃 안되고 INF그대로 있을 것이다.
            if cnt <= len(dist):
                min_count = min(min_count, cnt)


    ## 17. 모든 탐색을 다돌았는데, min_count가 한번도 업뎃안됬으면, [모든 경우가 다 초과]되어 업뎃 한번도 안됨
    ## => 업뎃한번도 안된 것을 flag로 처리한다
    if min_count == float('inf'):
        print(-1)
        exit()
    print(min_count)