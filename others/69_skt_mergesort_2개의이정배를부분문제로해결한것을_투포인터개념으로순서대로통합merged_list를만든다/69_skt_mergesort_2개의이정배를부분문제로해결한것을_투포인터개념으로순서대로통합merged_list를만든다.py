import sys 
 
input = sys.stdin.readline


# merget_sort 중 자신의처리 이정배2개를 합치는 로직을 따로 함수로 뺌
def merge(sorted_first, sorted_second):
    # (5) 이정배2개의 two pointer는 -> 통합 list에 정렬하면서 append한다.
    merged_lst = []

    first_index = 0
    second_index = 0
    # (6) 둘다 and로 인덱스 범위를 벗어나지 않은 상태까지 업뎃하여, 둘중에 하나 or 둘다 끝날때까지 처리한다.
    while first_index < len(sorted_first) and second_index < len(sorted_second):
        # (7) 한족이 작다면 먼저 append하고, index를 한칸 업뎃한다.
        if sorted_first[first_index] < sorted_second[second_index]:
            merged_lst.append(sorted_first[first_index])
            first_index += 1
        else:
            merged_lst.append(sorted_second[second_index])
            second_index += 1
    # (8) 둘중에 한개가 index범위를 넘어선 상태 -> [남은 것을 몽땅] 돌면서요소append(x) -> 인덱싱하여 extends += 한다.
    # -> 넘어섰더라도 len()에 index가 위치한 상태이므로, 비교해서 올린다.
    # -> 둘다 끊났떠라도, 한쪽의 빈 list가 extends되니 상관없다.
    merged_lst += sorted_second[second_index:] if first_index == len(sorted_first) else sorted_first[first_index:]
    return merged_lst


def merge_sort(lst):
    # (2) 재귀를 통한 정렬은 종착역이 1개이하로 남았을 때 그대로 반환하는 것
    if len(lst) <= 1:
        return lst

    # (3) 자신의 처리 때, 들어온lst를 left/right로 2개로 쪼개고, 투포인터로 merge한다.
    mid = len(lst) // 2  # mid or right
    left = lst[:mid]
    right = lst[mid:]

    # (4) 부분문제로 나누어서 각각 을 처리 후
    # -> quick -> pivot을 가운데두고 합한다 left + [pivot] + right
    # -> merge -> 정렬된 left, right를 [정렬된 2배열의 two pointer merge]를 한다.
    #   => [2배열 two pointer는 각각이 정렬된 배열일 때 가능]하다
    #   => 길어지니 메서드로 빼서 처리한다. -> 여기서 merge(lst1, lst2)는 자신의처리 내부로직임을 기억하자.
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    return merge(sorted_left, sorted_right)
 
if __name__ == '__main__':
    ## merge sort
    lst = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

    # (1) quick정렬([pivot] 보다 작lst, 큰lst)처럼, stack변수가 lst자체다.
    print(merge_sort(lst))


