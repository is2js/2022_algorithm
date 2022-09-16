import sys

input = sys.stdin.readline


def heap_sort(iterable):
    h = []
    result = []
    for value in iterable:
        # 1. 최대힙을 구현하고 싶다면, 우선순위 데이터에 -를 달고 넣어, 작은 값이 제일 뒤에 위치하게 시킨다
        #    제일 큰값은 제일 앞에 위치하게 된다.
        pq.heappush(h, -value)
        # scoville.heappush(h, value)
    for _ in range(len(h)):
        # 2. 작은 것부터 꺼내고 난 뒤, -를 달아 부호를 원상복귀시키면, 결국, 제일 큰 값이 먼저 나오게 된다.
        result.append(-pq.heappop(h))
        # result.append(scoville.heappop(h))
    return result


if __name__ == '__main__':
    import heapq as pq

    pass
