import heapq
import sys
 
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

    healths.sort() # 제한이 많은 것부터 우선적으로 순회
    # 제한과 관련된 원소를 기준으로 오름차순으로 정렬
    # ->  원본의 순서를 기억하기 위해 데이터변형으로 index와 같이 저장
    # -> 제한검사를 오름차순으로 하면, 그 뒤로는 검사안해도 된다.
    items = [(hp, attack, num) for num, (attack, hp) in enumerate(items, start=1)]
    # items.sort()
    # print(items)
    # [(30, 500, 2), (100, 30, 1), (400, 100, 3)]

    pq = []

    items.sort(reverse=True)
    ## [0] 제한 많은 순으로 먼저 순회한다.
    for health in healths:
        # 현재 케릭터가 사용할 수 있는 item을 다 모으고 -> 그 중 greedy를 뽑아야한다.
        # -> for greedy로 max한 것을 골라내고, 택1한 뒤, 그 다음 것은 버려야하는 원포인터이다.
        #    max와 max일때의 num을 찾고, 그 num은 제외시켜야한다면?
        #    [제한 많은 순으로 순회하며 택1 greedy -> 제한 덜한 다음타자가, 다시탐색하지않고 뽑아놓은 것 재활용]가능하려면?
        #    => 재활용을 위한 greedy는 stack pop or 원포인터를 사용해, 다음타자는 그 이후부터 탐색하고
        #       greedy는 global pq를 이용하여, 택1된 것 이외에는 재활용할 수 있게 하기
        #    -> (1) 미리 stack에 꽉채워 역순으로 정렬해놓고, peek으로 가능하면, 택1이 아님에도 pop하여 재활용되는 후보들을 [맨 뒤 제한 낮은것부터 pop] pq에 모아둔다
        #          -> 직전들 = 제한 제일 높은 것들을 찾아가며 가능한 것들 pop하면서 저장 -> pq에 가장 높은것만 뽑아내기
        #          -> 다음타자는 pq는 재활용하면서, pop안된것들만 탐색
        #    -> (2) 미리 오름차순으로 정렬해놓고, cursor의 원포인터로 탐색하며, 가능한대로 pq에 모으기
        #          -> 다음타자는 pq는 재활용하면서, cursor이후부터만 탐색
        #    -> (3) 미리 오름차순 정렬, 원포인터 없이 deqeue로 popleft()하며 택1후보들을 pq에 모으기
        #         https://410leehs.tistory.com/18?category=855737

        ## [1] 역순으로 정렬한 것을 뒤에서부터 가능한 것들을 다 뽑아놓고 pq에 저장하여 택1은 pq로 한다.
        while items:
            needed_hp, attack, num = items[-1]
            if health - needed_hp < 100:
                break # stack이 낮은순부터 찾아보므로, 제한이 걸리면 그 뒤는 안살펴봐도 된다.
            _ = items.pop() # 미리 greedy하지말고 택1 후보들을 모아둔다(다음 타자 재활용)
            ## [2] 다음타자들이 다 쓸 수 있어, 재활용할 수 있게, global pq에 저장해놓고 greedy를 끝낸다.
            # -> 저장할때 attack순으로 오름차순으로저장되어야한다.
            heapq.heappush(pq, (-attack, num))

        ## [3] 사용불가해서 pg에 후보들이 안담겨있을 수 있으니, 확인하고 greedy를 택1한다.
        if pq:
            op_attack, num = heapq.heappop(pq)
            result.append(num)

    print(result)


