import bisect
import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline


def count_by_range(lst, left, right):
    start_index = bisect_left(lst, left)
    end_index_plus_1 = bisect_right(lst, right)
    return end_index_plus_1 - start_index


if __name__ == '__main__':
    ## 이진탐색 예시2: 정렬된 배열에서 특정 수의 갯수 구하기
    # N개의 원소를 포함하고 있는 수열이 오름차순 정렬
    # 이 수열에서 x가 등장하는 횟수를 구하세요
    # ex> 1,1,2,2,2,2,3 -> x=2 -> 4
    # 단, O(lgN)으로 설계하지 않으면 시간초과판정 => 이정배(안되어있으면 NlgN정렬이라 불가)에 이진탐색 수행
    # 찾는 것이 없으면 -1로 출력
    # => 이진탐색으로 첫 요소의 위치, 나머지 1개는 마지막요소의 위치를, 이진탐색 2번으로 해결할 수 있다.
    n, x = map(int, input().split())
    lst = list(map(int, input().split()))

    count = count_by_range(lst, x, x)

    print(count if count !=0 else -1)
