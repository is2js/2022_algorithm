import sys
import heapq as pq
input = sys.stdin.readline


def heap_sort(iterable):
    # (1) lst기반 이진 힙으로 우선순위큐를 구현한다.
    h = []

    # (2) 모든 원소를 완전이진트리인 heap에 N * lngN으로 넣으면 내부 자동 최소힙 오름차순 정렬된다.
    for value in iterable:
        pq.heappush(h, value)

    # (3) 우선순위큐(완전이진트리 min heap)에서 꺼내기N * lgN만 하면
    # -> 오름차순으로 root node에서 제거되어, 정렬된 상태이다.
    result = []
    for _ in range(len(h)):
        result.append(pq.heappop(h))

    return result


if __name__ == '__main__':
    ## 우선순위 queue
    # ex> 넣고 가치가 높은 것부터 꺼내고 싶은 경우
    # (1) list에 넣은 뒤 -> 가장 갚이 큰 데이터 찾아 -> 꺼내기
    # => 삽입O(1) 뒤에 연달아넣음, 삭제(N) 찾아서 꺼내야한다.
    # (2) heap으로 구현
    # => 삽입O(lgN) 삭제빼는것 O(lgN)
    # => N개의 데이터를 넣으면 자동으로 힙정렬 O(NlgN)

    ## 우선순위큐를 위한 heap 자료구조
    # -> [완전 이진 트리]의 일종
    # (1) heap은 항상 root node를 제거하는 방식으로 자동
    # (2) heap 종류 2가지
    #   (2-1) 최소 힙=> root node를 가장 작은 값으로 유지
    #   (2-2) 최대 힙=> root node를 가장 큰큰값으로 유지

    # (3) 완전 이진트리: root -> 왼sub -> 오sub start 순으로 차례로 데이터 삽입되는 트리
    # (4) 최소 힙 구성 함수: min_heapify()
    # -> 상향식과 하향식으로 구성할 수 있는데, 상향식만 살펴본다.
    # => root-왼sub-오sub순으로 삽입할 때, 부모로 거슬러 올라가면서
    #    매번 상향식으로 부모와 비교하며, 부모가 더 작다면 swap한다.
    #     3
    #   /   \
    #  5     9
    # / \
    # 6   [4]
    #     3
    #   /   \
    # [4]     9
    # / \
    # 6   [5]
    # => heapify를이용하면 O(lgN)으로 힙 성질을 유지할 수 있다.
    # => 완전이진트리를 따르면 -> 부모쪽으로 거슬러 올라 갈 때 최악에도 lgN을 유지
    #     3
    #   /   \  => 2번째 swap
    #  4     9
    # / \    /  => 1번째 swap
    # 6   5 [2]  -----> 새로운 데이터는 depth만큼만 swap해도 부모까지 올라가며, depth는 N개의 데이터에 대해 lgN으로 구성된다.

    ## 힙에서 원소 삭제
    # (1) root node가 먼저 날아간다. -> 상수시간
    #    (2)
    #   /   \
    #  4     3
    # / \    /
    # 6   5  9
    # (2) 가장 마지막 node인 9를 root node로 상향식으로 올린다 -> 상수시간
    #     9
    #   /   \
    #  4     3
    # / \    /
    # 6   5  ( )
    # (3) 마지막node였던 9를  [하향식]으로 heapify()를 수행한다
    # -> 오sub순 - 왼sub(역순)으로 비교해서, 더 작은 자식과 위치를 바꾼다. -> O(lgN)

    lst = [3, 5, 1, 23, 5]

    print(heap_sort(lst))


    def heap_sort(iterable):
        # (1) lst기반 이진 힙으로 우선순위큐를 구현한다.
        h = []

        # (2) 모든 원소를 완전이진트리인 heap에 N * lngN으로 넣으면 내부 자동 최소힙 오름차순 정렬된다.
        for value in iterable:
            pq.heappush(h, value)

        # (3) 우선순위큐(완전이진트리 min heap)에서 꺼내기N * lgN만 하면
        # -> 오름차순으로 root node에서 제거되어, 정렬된 상태이다.
        result = []
        for _ in range(len(h)):
            result.append(pq.heappop(h))

        return result


    pass
