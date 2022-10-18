import itertools
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## 외벽점검: https://school.programmers.co.kr/learn/courses/30/lessons/60062
    n = int(input().strip())
    weak = list(map(int, input().split()))
    dist = list(map(int, input().split()))

    ## 1. 친구투입 순서 순열. 친구 수 최소값 -> min greedy 뿐만 아니라, 가장 많이 갈 수 있는 친구부터 투입해야됨.
    ## -> 특정한 조건이 있는 것 아니면, 순열을 dfs로 할 필요는 없다. 전체 경우의수를 다 만들어서 돌자.
    ## 2. weak는 이미 순서가 정해져있으므로, 시작지점만 정하면 되는 [경우의 수 -> for start]
    ## 3. 반시계로 도나, 시계로 도나, 같은 길이를 움직이므로, 시계만 보면 된다.

    ## 4. weak는 환형이라 index => [index % 12(구간별 열의 갯수)]로 변형해서 계산하면, 순환이 된다.
    ##    하지만, 여기선 weak의 순환되어도 그냥 value만 뽑는게 아니라, 거리 차를 구해야한다.
    ##   => 하지만, 여기서는, 10 11 -> 0이 아닌 12 13으로 [다음취약지점과의 거리차]가 중요하기 때문에
    ##   => 3번째 weak(10) -> 0번재 weak(1)와 거리 차를 존재하게 만들기 위해서는, 4번재로서 구간길이를 +시킨 -> 4번째 weak(13)을 만들어줘야한다.
    ## my) 환형이면서, 1바퀴 안에서 거리차를 계산하려면(많아야 넘어서서 1바퀴-자기자신시작이므로)
    ##     arr = arr + [e + 구간길이 for e in arr] 로 연장해서, 1바퀴 이내의 거리차 계산을 하게 한다.
    ## => weak를 변형해야하므로 미리 size를 빼놓는다.
    weak_size = len(weak)
    weak += [e + n for e in weak]

    min_d_count = float('INF')

    ## 5. weak의 시작점은 이미 순서가 정해졌지만, 어느것부터 시작할지의 경우의 수(순열X)
    # for i in range(len(weak)):
    for start in range(weak_size):
        ## 7. 취약지점출발이 정해졌으면, 친구 투입순서를 정한다. 순열로 모든 경우를 보기 위해, permutations를 활용한다
        for d in itertools.permutations(dist, len(dist)):
            ## 8. 시작지점에 대해 curr, next의 weak거리차를 구하고, d[i]가 점검이 가능하면, 1칸씩 더 가야햔다
            ## => [투포인터(현재취약점/다음취약점)에 대해 [2번째 포인터를 조건에 따라 갈 수 있는만큼 +=1씩 진행]해야하므로
            ##    2번재 포인터를 for range(1,) 문안에서 업데이트 시킨다
            ## => [순서대로 진행되는 투포인터]는, 1번째 포인터도 넘어가야하므로 가변변수로 받아놓아야한다
            # 1) 경우의 수 for문 변수와 별개로, 그 지점부터 1개씩 넘어가야하므로, 시작점도 변수로 잡고 돌린다.
            #    one pointer(curr)
            pos = start
            # 2) two pointer는        => for next in range(pos+1, )부터 끝까지 가면 되지만,
            #   [갈 수 있는 만큼]가려면  => for i in range(1, n-1)까지 => 내부에서  next = start + i(1,2...n-1)로 가야한다.
            ##  ===> next_pos는  pos+i가 아니라. start+i로 업뎃한다...?!
            #   => 2번째 포인터를 갈수있는만큼 가기 위해서는, next를 pos + 1부터 확정시작이 아니라, for i  next = pos+i로 조건비교하며 계속 업뎃해야한다.
            #   => 갈수있는만큼 업뎃된 next의 index를 사용해야하기 때문에, next를 for문변수가 아닌 내부업뎃변수로 잡는다.
            # for next in range(pos + 1, weak_size):

            #### 10. 투입된 d_cnt도 누적해서 세어야한다.
            d_count = 1
            # for next_pos in range(pos+1, weak_size):
            for i in range(1, weak_size):
                ## 10-5. next_pos는 가변pos + i가 아니라.. start + i다..
                ##     => pos가 없뎃 + d가 다음놈으로 넘어가더라도 ==>  i와, start+i은 그대로 유지되며, weak의 인덱스를 n-1까지 돌면 끝이다.
                ##     => pos가 감당X의 next_pos로 없뎃되어도, next_pos는 쉬지않고 +1씩 올라간다...
                ##     => 커버O에도 next_pos는 1칸/ 커버X에도 next_po는 1칸씩 올라간다
                ##        시작을, pos=start  / next_pos = start + 1에서 하지만
                ##               pos는 d바뀜에따라시작위치가 바뀌지만 /next_pos는 pos<->next_pos
                #                감당안된 직전next_pos ->  pos  <-> 감당안된 직전next_pos + 1된 next_pos(쉬지않는 next+pos)
                ## my) next_pos는 start+1에서부터 쉬지않고 start를제외한 [그 뒤로 n-1개를 쉬지않고 1순회] 하고 끝난다.
                # => start가 0고정이었다면, next_pos = i -> for next_pos in range(1, n): 으로 출발하지만,
                #    경우의 수에 의해  ->  시작index 자체가 start다. -> 뭐든 [start + ]를 달고 index를 계산해야한다.
                #    => curr/next에서 curr = start,  next = 원래는 1부터 n-1까지  => start시작이라면,   next = start + 1부터 ~ start + n-1까지
                #    =>  for next_post in range( start + 1,  start + n )  or    for i in range(1, n ) -> next_pos = start + i
                next_pos = start + i
                print(pos,next_pos, i, start)

                diff = weak[next_pos] - weak[pos]

                ## 9. next_pos를 어디까지 업뎃할지 조건은, 현재d의 능력에 달렸다.
                ##    d를 뽑는 index도 있어야하는데, [몇번째 d를 쓰는지도 가변변수]로 업뎃되어야한다.
                ## => d_index = 0부터 시작할 수 있지만, d를가 몇명사용되었는지 d_cnt도 [for d 순열경우의수마다 그 내부에서 누적]해야한다.
                ####    현재까지 사용된친구 d_cnt = 1부터 시작,  현재 d_index = 0부터 시작 => 동시에 필요하다면
                ##    [d_cnt = 1부터 세고, index는 cnt -1 로 사용]한다.

                ## 11. 현재d가 감당할수있는 차이면, for문이 그냥 넘어가서 next_pos가 더 커져 -> diff도 더 커지면 된다.
                ##     감당할 수 없을 때 => (1) [d다음놈으로 업뎃 by cnt증가] + (2) next_pos를 d다음놈의시작위치가 되도록 pos로 업뎃하면 된다.
                if d[d_count - 1] < diff:
                    d_count += 1  # 카운트업뎃되면 index도 자동 업뎃 -> d는 다음놈이됨.
                    ## 1개씩 인덱스 직접증가는.. 제한이 있어야한다.
                    if d_count > len(dist):
                        break

                    ## 12. 현재d(d[d_count-1]가 감당안되는 next_pos까지의의 weak는, 다음d의 시작점이 되도록 pos로 업뎃해줘야한다.
                    pos = next_pos


            ## 13. d_count = 1부터 시작해서, 투입된 친구명수를 min없댓하자.
            # 이 때, d_count가 len을 넘어가는 순간 탈락이므로, 그 이내일때만 업뎃한다
            if d_count <= len(dist):
                min_d_count = min(min_d_count, d_count)


    ## 14. 친구를 다 투입해도 점검 못하는 경우도 있다.
    ##  => 이런 경우는, d_count > len  탈락 -> 탈락 아닌 경우에만  greedy min 업뎃 ->  min업뎃 한번도 안한 INF인 경우 모두 탈락
    if min_d_count == float('inf'):
        print(-1)
        exit()
    print(min_d_count)