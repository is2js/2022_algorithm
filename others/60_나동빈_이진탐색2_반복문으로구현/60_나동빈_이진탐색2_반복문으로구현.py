import sys

input = sys.stdin.readline


def binary_search(lst, target, srt_index, end_index):
    # (2) stack변수인 index들로 만드는 종착역 대신
    # -> while문의 조건으로 [찾지못하는 종착역] 을 대신한다
    # -> 변수가 종착역이 되기전까지 돌게 하면 된다.
    # -> 업데이트변수가 [조건에 따라 2개이상이 업뎃대상]이라면 while문을 쓴다.
    while srt_index <= end_index: # 탐색의 찾지못함 종착역(stack변수 종료)
        # (3) 이진탐색은 업뎃srt,end_index로  mid중간점을 만들어서 처리한다.
        mid_index = (srt_index + end_index) // 2  # 가운데 or 중간왼쪽
        # (4) 2번째 종착역으로서, 중간에 조건을 만족하여 끝나는 종착역은 stack변수 소진 전 반복문 내에서if로 찾아서 끝낸다.
        # stack변수의 소진(srt> end) 해서 끝나는 것이 아니라, 특별한  종착역이 있다면,
        # -> while문 속에서 업뎃되는 변수를 통해 if return으로 처리한다.
        if lst[mid_index] == target:
            return mid_index
        # (5) 재귀의 파라미터 -> 자식호출 순으로 업데이트되는 것을 반복문 속에서 업데이트 시킨다.
        # -> 택 1호출이면, 그에 맞게 if를 쓰면 된다.
        if target < lst[mid_index]:
            end_index = mid_index - 1
        else:
            srt_index = mid_index + 1

    # (6) stack변수가 다 소진되었는데 return안됬으면, 찾지못한 것
    return None

if __name__ == '__main__':
    ## 이진탐색 by 반복문
    # -> 이정배에서 1개의 targetvalue를 탐색할 때 O(lgN)으로 한다.
    n, target = map(int, input().split())
    lst = list(map(int, input().split()))

    # (1) 재귀도 가능하지만, while으로도 srt, end_index를 업데이트하며 mid로 탐색할 수 있다.
    # binary_search(lst, target, srt_index, end_index)
    print(binary_search(lst, target, 0, n - 1))


    def binary_search(lst, target, srt_index, end_index):
        # (2) stack변수인 index들로 만드는 종착역 대신
        # -> while문의 조건으로 [찾지못하는 종착역] 을 대신한다
        # -> 변수가 종착역이 되기전까지 돌게 하면 된다.
        # -> 업데이트변수가 [조건에 따라 2개이상이 업뎃대상]이라면 while문을 쓴다.
        while srt_index <= end_index:  # 탐색의 찾지못함 종착역(stack변수 종료)
            # (3) 이진탐색은 업뎃srt,end_index로  mid중간점을 만들어서 처리한다.
            mid_index = (srt_index + end_index) // 2  # 가운데 or 중간왼쪽
            # (4) 2번째 종착역으로서, 중간에 조건을 만족하여 끝나는 종착역은 stack변수 소진 전 반복문 내에서if로 찾아서 끝낸다.
            # stack변수의 소진(srt> end) 해서 끝나는 것이 아니라, 특별한  종착역이 있다면,
            # -> while문 속에서 업뎃되는 변수를 통해 if return으로 처리한다.
            if lst[mid_index] == target:
                return mid_index
            # (5) 재귀의 파라미터 -> 자식호출 순으로 업데이트되는 것을 반복문 속에서 업데이트 시킨다.
            # -> 택 1호출이면, 그에 맞게 if를 쓰면 된다.
            if target < lst[mid_index]:
                end_index = mid_index - 1
            else:
                srt_index = mid_index + 1

        # (6) stack변수가 다 소진되었는데 return안됬으면, 찾지못한 것
        return None

