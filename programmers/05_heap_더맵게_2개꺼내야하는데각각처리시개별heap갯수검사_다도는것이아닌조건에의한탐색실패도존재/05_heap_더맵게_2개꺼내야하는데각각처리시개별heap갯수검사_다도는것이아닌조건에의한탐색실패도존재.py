import heapq
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    scoville, K = list(map(int, input().split())), int(input().strip())
    ## [매번] 꺼낼때마다 낮은 우선순위를 유지하여 꺼내야한다.
    # -> list기반 이진힙
    heapq.heapify(scoville)

    count = 0
    # 2개를 꺼내야한다면, len() >=2를 조건을 줄 수 있지만,
    # => 1개꺼내고 검사하고 1개 더 꺼낸다면, 각각 꺼낼때마다 검사해야한다.
    while scoville:
        first = heapq.heappop(scoville)
        if first >= K:
            print(count)
            break
        ## 2번째를 꺼내야할 때도, 길이 검사하기 안되면 종료?(X) -> continue로 해서 1번째꺼 검사가 이루어지게 해야한다.
        # -> 1개만 남은 상황이라면, 그 위쪽에 1개꺼내서 확인하는 로직을 거치게 해야한다.
        # -> 추가: fisrt <K 상항에서 남은 갯수가 없으면, 탐색실패하여 종료다
        ## => 다돌아도 못찾으면 else:탐색실패
        #  => 중간에 조건만족 못하면 if break 탐색실패
        if not scoville:
            # continue
            # 탐색 실패로 인해 종료
            print(-1)
            break
        second = heapq.heappop(scoville)
        new = first + (second * 2)
        heapq.heappush(scoville, new)
        count += 1
    else:
        print(-1)