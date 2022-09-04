import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## 정렬
    # (1) 선택정렬
    # -> [처리되지 않은 범위(처리될때마다 범위1씩감소)] 중 가장 작은 데이터를 선택
    # -> 범위내에서 맨 앞과 데이터와 바꾸기
    # -> 바꾼 맨앞원소를 제외하고, 나머지 처리되지않는 범위들에서 반복
    # -> 마지막 원소는, 처리되지 않는 범위가 1로서 바꿀 맨앞도 없으므로 처리하지 않아도 된다.
    # => 마지막원소 제외 모든 원소들에 대해for N, 처리되지 않는 범위(N-i) 중 가장작은원소 탐색 for(N-k)
    # => O(N^2)
    numbers = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    # (1) i는 [처리되지 않은 범위의 맨 앞자리]를 의미한다.
    for i in range(len(numbers)):
        # (2) 제일 작은 것을 i번재 원소라고 가정하고
        #     -> greedy로 [i+1 ~ 끝]까지 제일 작은 원소의 index를 탐색한다
        index_of_min_value = i
        for j in range(i + 1, len(numbers)):
            # (3) 작은 값이 나타날때마다 그 index를 저장한다.
            if numbers[j] < numbers[index_of_min_value]:
                index_of_min_value = j
        # (4) greedy를 통해 찾은 최소값의 인덱스와, 맨 앞자리의 값을 swap하여 앞으로 옮긴다.

        # temp = lst[i]  # (4-2) / 덮어쓰기대상의 값을 위에서 저장해놓는다.
        # lst[i] = lst[index_of_min_value] # (4-1) 덮어써야하는데 (둘 중에 아무거나로)
        # lst[index_of_min_value] = temp # (4-3) 덮어쓰는놈에 대해 temp 값을 덮어쓰면 된다.
        # (4-4) python은 한번에 value swap이 가능하다.
        numbers[i], numbers[index_of_min_value] = \
            numbers[index_of_min_value], numbers[i] # 바꿀놈을 위치만 바꿔서 할당해주면 된다.

    print(numbers)




