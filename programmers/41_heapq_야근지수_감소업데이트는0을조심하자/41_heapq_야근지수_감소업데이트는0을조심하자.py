import heapq
import sys
 
input = sys.stdin.readline 
 
 
if __name__ == '__main__':
    ## 야근지수: https://school.programmers.co.kr/learn/courses/30/lessons/12927
    works = list(map(int, input().split()))
    n = int(input().strip())
    # 업뎃할때마다 가장 큰 것을 다시 뽑아야한다.
    # 업뎃 -> 다시 -1해서 삽입하는 것.

    works = [-x for x in works]
    heapq.heapify(works)

    for _ in range(n):
        max_work = heapq.heappop(works)
        ## 감소 업데이트는 0을 조심하자
        max_work = -(-max_work - 1)
        if max_work > 0:
            max_work = 0
        heapq.heappush(works, max_work)

    print(sum(x**2 for x in works))
