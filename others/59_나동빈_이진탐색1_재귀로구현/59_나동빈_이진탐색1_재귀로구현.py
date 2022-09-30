import sys

input = sys.stdin.readline


def binary_search(lst, target, srt_index, end_index):
    # (3) ### 정렬은 len==1일때가 바로반한이지만, index로 탐색은, [못 찾을 때 == not (src <= dst)]인
    # -> src > dst return None의 [찾을 수 없음]도 따로 처리해줘야한다.
    # -> [이진탐색 재귀의 2번째 종착역]
    if srt_index > end_index:
        return None
    # (4) 찾을 수 있는 node의 [1번재 종착역], mid중간점의 값 == target시 그 index인 mid의 반환이다.
    # -> 양끝인덱스 합의 절반 -> 가운데 or 왼쪽이다.
    mid_index = (srt_index + end_index) // 2
    if lst[mid_index] == target:
        return mid_index

    # (lst[mid_index] < target   or   lst[mid_index] > target)
    # (5) 자신의 처리로서, 종착역에 안걸렸다면, 2가지 경우의 수로 node를 각각 뻗어줘야한다.
    # (5-1) target이 lst[mid_index]보다 작은 범위에 있는 경우, mid보다 왼쪽범위를 탐색하게 한다.
    if target < lst[mid_index]:
        return binary_search(lst, target, srt_index, mid_index - 1)  # end자리를 mid-1로 변경해서 탐색

    # (5-2) target이 lst[mid_index]보다 큰 범위에 있는 경우, mid보다 오른쪽 범위를 탐색하게 한다
    #  -> 같은 경우는 종착역으로서 위에서 걸러진다.
    # (target > lst[mid_index] )
    return binary_search(lst, target, mid_index + 1, end_index)  # srt자리를 mid+1로 변경해서 탐색

if __name__ == '__main__':
    ## 이진탐색: [이정배]에서 [index3개]를 활용하여 탐색범위를 절반씩 좁혀가며  데이터 탐색
    # -> 탐색 범위를 정해줘야한다. 시작,끝점 -> 중간점 -> target과 비교하여 재귀를 절반범위로 택1하여 node를 뻗어나간다
    # -> 중간에 2개가 있다면 그냥 왼쪽꺼 사용하도록 // 사용
    # -> (1) 중간점 vs 찾는 값 비교 -> (2)  중간점기준으로 한쪽만 탐색하도록 시작점or끝점을 이동
    # => 단계마다 범위를 2로 나누어 O(lgN)
    # => 배열은 그대로두고, [경우의수에 따라 index만 바꿔서 처리하는 start]를 뻗어나가면서 target index 찾아 반환하는 [재귀]로 해결한다.
    # => start/dst 파라미터로 -> 자신의 처리에서 mid를 만들어 처리하는 [재귀]로 해결할 수 있다.

    ## 1. 재귀를 통한 start, dst 파라미터 변경
    n, target = map(int, input().split())
    # (1) 이미 정렬된 배열에 1개의 target value를 탐색하는 문제여야한다.
    lst = list(map(int, input().split()))

    # (2) 이진탐색은 이정배를 그대로 두고, src/dst 인덱스를 바꿔가며
    # -> mid중간점을 통해 절반씩 줄여서, 1개의 target index를 반환하는 꼬리재귀형식이다.
    # binary_search(lst, target, srt_index, end_index)
    print(binary_search(lst, target, 0, n - 1))