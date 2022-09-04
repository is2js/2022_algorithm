import sys 
 
input = sys.stdin.readline





if __name__ == '__main__':
    lst = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

    def quick_sort(lst):
        # (2) 종착역으로서 배열이 1개가 되면, 그냥 반환한다.
        #    -> 배열이 아무것도 없을 때도 바로 종료한다.
        if len(lst) <= 1:
            return lst

        # (3) 자신의처리로서, 맨앞원소는 pivot원소로 빼고, 나머지를 가지고,
        #     listcomp로  필터링하여, pivot보다 큰/작은 배열을 각각 만든다.
        pivot = lst[0]
        tail = lst[1:]

        left = [x for x in tail if x <= pivot]  # 정렬 속에 pivot과 같은 값이 있을 수 있으니 포함해서 작은것이라고 가정한다.
        right = [x for x in tail if x > pivot]

        # (4) 각 분할된 부분문제를 자식node로서 재귀호출한 뒤, pivot을 가운데로 넣고, 1개의 배열로 집계해서 반환한다.
        return quick_sort(left) + [pivot] + quick_sort(right)

    # (1) 인덱스를 조정하는 재귀가 아니라, 배열자체를 분할하여 꼬리재귀(자식node집계가 정렬된 배열 합치기)로 퀵정렬한다.
    print(quick_sort(lst))
