import sys 
 
input = sys.stdin.readline
sys.setrecursionlimit(100_000)


def quick_sort(numbers, src_index, dst_index):
    # (2) 기본적으로 정렬매서는 1개는 일단 바로 반환하도록 만들어야하며,
    #     종착역이다. -> index로 배열을 짤라 처리하므로, 원본배열이 아니라 index로 len==1을 만들어야한다.
    if src_index >= dst_index:
        # swap으로 전역변수 배열을 처리하므로 반환값은 없다.
        # print(lst)
        return

    # (3) 이제 [처리구간의 0번째인덱스]를 pivot_index로
    #     그다음부터는 src_index / 맨끝은 end_index로 간주하고
    #     while문을 엇갈리기 전까지 돌린다.
    pivot = src_index
    left = src_index + 1
    right = dst_index
    while left <= right:
        # (4) 왼족부터는 pivot위치의 값보다 큰 값을 찾는다.
        #     [가장 가까운 원소]를 찾을 때는 while 찾기직전까지 + 시킨다.
        #     -> 인덱스 탐색은 끝범위를 전제에 둔다.
        while left <= dst_index and numbers[left] <= numbers[pivot]:
            left += 1
            # 현재 left는 [가장 빠른] pivot보다 큰 값 찾은 상태다.
        ######## right의 움직임의 끝범위는 src가 아니라 src+1까지이다.
        #######  src에는 pivot이 위치하고 있으므로 >=로 검색하면   pivot보다 작은 값이 아니라 같은 값으로서 pivot을 검색하게 된다.
        while right > src_index and numbers[right] >= numbers[pivot]:
            right -= 1

        # (5) 각각을 찾았으면 swap한다. 근데 엇갈리기 전까지 swap이고, 엇갈리면 pivot과 작은값(right)을 swap한다.
        if left > right :
            numbers[right], numbers[pivot] = numbers[pivot], numbers[right]
        else:
            numbers[left], numbers[right] = numbers[right], numbers[left]

    # (6) 현재 엇갈릴 때 까지 [pivot보다 작은값] pivot [pivot보다 큰값] 만들어놓은 상태다.
    # -> 재귀를 통해서, 나눠진 부분들을 처리하도록 한다.
    # right는 pivot 값위치이므로 -1과 +1로 나눠서 처리하게 한다.
    quick_sort(numbers, src_index, right - 1)
    quick_sort(numbers, right + 1, dst_index)


if __name__ == '__main__':
    ## (3) 퀵정렬: 데이터와 상관없이 표준적으로 사용하는 정렬알고리즘
    # -> 가장 많이 사용되며, 병합정렬과 같이 표준정렬 라이브러리의 근간 알고리즘
    # -> python 표준라이브러리 정렬은 quick sort가 아니라 merge와 insert 조합해서 만든 Tim sort로 구현되어있어서 최악일때도 O(n log n)을 보장합니다
    # (1) 기준데이터(0번째원소)를 고르고,
    # (2) 처리되지않은범위의 [왼쪽부터는 기준보다 큰값 찾기 -> ] vs [ <- 오른쪽끝에서는 기준보다 작은 값 찾기]를 찾아나선다.(작은게 앞으로 오도록 바꿀 swap예정)
    # (3) 그 swap후 각각+1, -1 index하여, 더 안쪽범위를 탐색한다. (순서는 중요치않고, 기준값을 가운데 있다치고, 기준데이터보다 작 -> 큰으로 순서없이 swap으로 모으는 중)
    # (4) src, end_index가 서로 엇갈리는 순간에는, [ 1<-(from dst) -> 6(from start) ] 2개를 swap하는 것이 아니라
    #    -> 맨 안쪽 2놈빼고는 다 정렬된 상태이므로,[작은 값]과 [0번째원소pivot]의 자리를 바꿔,
    #    -> pivot을 가운데에 위치시킨다.   1 ~~~~~~~ pivot 6(start부터찾은 마지막 pivot보다 큰값) ~~~~~~
    #    -> pivot을 가운데 놓고 [pivot보다 작은범위의 데이터들(정렬x)] + [ pivot ] + [ pivot보다 큰 범위의 데이터들(정렬x)]
    #   => 1번 수행할때마다, [정렬해야할 범위가 절반]이 된 것들로 나눠진다.
    #   => 이것을 재귀를 통해 종착역 1개 남을때까지 절반씩 나누면, 결국엔 정렬된 것이 돌아온다
    #   => 분할partition -> 재귀

    #   => 이상적인 경우, 분할이 절반씩 일어난다면, O(NlgN)
    #   => depth의 높이가 lg2N이 된다.  -> 너비는 총 N개라서  -> 높이x너비 = O(Nlg2N)이 된다.
    #      1234      -> 4  너비 N4
    #  [12]   [34]    ->2     => 높이 lg2(4) = 2
    #  [1][2] [3][4]  ->1

    #   평균 NlgN이지만, **최악의 경우, N^2이 될 수 있다. => 절반 분할이 아니라,
    #   => pivot이 제일 작은 값이라면, [pivot] [    pivot보다 더 큰값들만 ]  => 정렬범위가 절반이 아니게 된다.
    #   => 그냥 N개를 정렬하는 것과 똑같아진다 => N^2
    #   ==> pivot을 0번째 원소로 잡을 때, 그게 이상적으로 절반을 나눠준다면 O(NlgN), 편향분할이라면 O(N^2)
    #   ==> 표준라이브러리는, 하이브리드 형식으로 퀵+분할 -> NlgN을 보장되도록 설계되어있다.

    def quick_sort(numbers, src_index, dst_index):
        # (2) 기본적으로 정렬매서는 1개는 일단 바로 반환하도록 만들어야하며,
        #     종착역이다. -> index로 배열을 짤라 처리하므로, 원본배열이 아니라 index로 len==1을 만들어야한다.
        if src_index >= dst_index:
            # swap으로 전역변수 배열을 처리하므로 반환값은 없다.
            # print(lst)
            return

        # (3) 이제 [처리구간의 0번째인덱스]를 pivot_index로
        #     그다음부터는 src_index / 맨끝은 end_index로 간주하고
        #     while문을 엇갈리기 전까지 돌린다.
        pivot = src_index
        left = src_index + 1
        right = dst_index
        while left <= right:
            # (4) 왼족부터는 pivot위치의 값보다 큰 값을 찾는다.
            #     [가장 가까운 원소]를 찾을 때는 while 찾기직전까지 + 시킨다.
            #     -> 인덱스 탐색은 끝범위를 전제에 둔다.
            while left <= dst_index and numbers[left] <= numbers[pivot]:
                left += 1
                # 현재 left는 [가장 빠른] pivot보다 큰 값 찾은 상태다.
            ######## right의 움직임의 끝범위는 src가 아니라 src+1까지이다.
            #######  src에는 pivot이 위치하고 있으므로 >=로 검색하면   pivot보다 작은 값이 아니라 같은 값으로서 pivot을 검색하게 된다.
            while right > src_index and numbers[right] >= numbers[pivot]:
                right -= 1

            # (5) 각각을 찾았으면 swap한다. 근데 엇갈리기 전까지 swap이고, 엇갈리면 pivot과 작은값(right)을 swap한다.
            if left > right:
                numbers[right], numbers[pivot] = numbers[pivot], numbers[right]
            else:
                numbers[left], numbers[right] = numbers[right], numbers[left]

        # (6) 현재 엇갈릴 때 까지 [pivot보다 작은값] pivot [pivot보다 큰값] 만들어놓은 상태다.
        # -> 재귀를 통해서, 나눠진 부분들을 처리하도록 한다.
        # right는 pivot 값위치이므로 -1과 +1로 나눠서 처리하게 한다.
        quick_sort(numbers, src_index, right - 1)
        quick_sort(numbers, right + 1, dst_index)

    ## 일반적인 로직에 따른 구현
    numbers = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


    ## (1) 재귀로 구현하며, 각 자식node를 반반씩 뿌릴 때, src/dst가 달라지므로
    ## 재귀 메서드의 인자로 주고 들어간다.
    quick_sort(numbers, 0, len(numbers) - 1)

    print(numbers)
