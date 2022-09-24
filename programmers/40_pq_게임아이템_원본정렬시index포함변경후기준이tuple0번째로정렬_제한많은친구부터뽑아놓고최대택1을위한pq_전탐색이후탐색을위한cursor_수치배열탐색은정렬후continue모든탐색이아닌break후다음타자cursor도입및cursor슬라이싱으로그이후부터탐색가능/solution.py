import heapq
import sys
from collections import deque

input = sys.stdin.readline

if __name__ == '__main__':
    ## 게임아이템:  https://chaelinyeo.github.io/%EC%BD%94%ED%85%8C/Level03%EA%B2%8C%EC%9E%84%EC%95%84%EC%9D%B4%ED%85%9C/
    # 입출력: https://daekyojeong.github.io/posts/Algorithm27/
    healths = list(map(int, input().split()))
    items = []
    result = []
    for _ in range(int(input().strip())):
        item = list(map(int, input().split()))
        items.append(item)
    ## (2) 최솟값 만들기는 1:1매칭 가장 최소값은 한쪽가장작 x 한쪽가장큰 순서대로 누적합이었다.
    ## 최대값을 만들려면, 한쪽에는 공격력관련이 없으니, 1x한쪽가장큰의 누적합이 되어야한다.
    ## => 즉, 무기중에는 가장 공격력 높은 것을 우선순위로 써야한다.

    ## (2) [제한이 가장 심한] 체력 낮은사람부터 쥐어줘야한다.
    healths.sort()
    ## (3) 모든item들을 순회하며,자신이 쓸 수 있는 것 중(if검사), 가장 공격력 높을 사용해야한다.
    ##     items를 미리 공격력 순으로 정렬내놓고 -> 1개씩 순회하여, 가장 빠른 것을 선택해도 되고

    ## (4) item을 정렬해야하는데, 원본순서(index)를 기억해야하므로 변형하여 정렬한다.
    ## -> 정렬기준은 [체력이 높은 순]으로 [순회시 빨리 끝나게]한다.
    ##    사람별로, 체력제한이 걸리면, 그 뒤로는 안보고 끝내게 한다.
    # => tuple에 정렬기준을 맨앞에 두면, key를 지정안해도 된다.
    # print([(needed_hp, attack, num) for num, (attack, needed_hp) in enumerate(items, start=1)])
    # [(100, 30, 1), (30, 500, 2), (400, 100, 3)]
    new_items = [(needed_hp, attack, num) for num, (attack, needed_hp) in enumerate(items, start=1)]
    new_items.sort()

    ## (9) 모든 사람들이 사용가능한 우선순위 창고
    pq = []
    ## (12) item을 1번만 뽑기 위한 pointer
    # item_cursor = 0
    new_items = deque(new_items)
    result = []

    ## (5) health배열은 체력낮은사람부터 -> items들을 순회한다.
    for health in healths:
        ## (6) 제한이 가장 많은사람부터, 자신이 할 수 있는 만큼만 탐색한다
        # for item in new_items:
        ## (11) 이미 탐색한 것들이후로 탐색하기 위해, cursor부터 시작한다
        # for item in new_items[item_cursor:]:
        while new_items:
            # needed_hp, attack, num = item
            needed_hp, attack, num = new_items[0]
            ## (7) 돌아가면서 사용가능한 것만 append한다.
            ##     오름차순으로 정렬되어있으므로, 검사에 걸리면 종착역으로 break다.
            ##     (만약, 순서가 정렬안되어있다면, continue로 모두 건너띄면서 확인해야했다)
            if health - needed_hp < 100:
                break  # continue
            ## (8) 체력순으로 [내 제한]까지, 사용가능하다면,
            ##    공통 창고 우선순위큐에 [사용가능한 item]들을 attack순으로 저장한다.
            ## => 사람마다 갈수록 뽑을 수 있는 것이 많으므로 [삽입이 일어나는 우선순위 정렬]인 우선순위큐를 이용한다
            ## => attack뿐만 아니라, num도 같이 저장한다.
            new_items.popleft()
            heapq.heappush(pq, (-attack, num))
            ## (10) new_items 중에서 [제한 많은 놈들]이 지금껏 뽑아놓은 것들 이후로 검색할 수 있게
            ## item탐색마다 srt_cursor를 저장해놓는다.
            ## => 중복탐색 금지를 위한 원포인터
            # item_cursor += 1
        ## (13) 자기가 공통창고에 넣어놓은 것 중 가장 attack이 높은 것을 뽑는다.
        ## => pop전에는 무조건 검사하고 해야한다.
        ##    없어서 못쓸 수 도 있다.
        if pq:
            opposite_attack, num = heapq.heappop(pq)
            ## (14) 사용하여 pop한 것을 저장한다.
            result.append(num)

    print(result)