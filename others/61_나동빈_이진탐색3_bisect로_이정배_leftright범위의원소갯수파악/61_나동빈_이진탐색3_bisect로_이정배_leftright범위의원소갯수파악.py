import sys

input = sys.stdin.readline


def count_by_range(lst, left_value, right_value=None):
    right_last_index_plus_1 = bisect_right(lst, right_value if right_value else left_value) # 1개만 주면, left_value의 갯수가 나오게 처리한다.
    left_first_index = bisect_left(lst, left_value)
    # 갯수는 dst - start + 1이지만, end에 이미 +1이 된 상황이라서, 빼기만 하면 된다.
    return right_last_index_plus_1 - left_first_index


if __name__ == '__main__':
    ## 이진탐색3: bisect 라이브러리 구현
    # 참고 및 예제소개 블로그: https://11001.tistory.com/71?category=983191
    # bisect_left(a, x): 정렬순서유지하며 배열a에 x를 삽입할 가장 왼쪽 인덱스(해당요소 인덱스, 여러개라라면 맨 왼쪽자리) 반환
    # bisect_right(a, x): 삽입할 가장 오른쪽 인덱스(해당요소 + 1, 여러개라면 마지막요소 +1 자리)을반환
    #     ↓ bisect_left(a, 4) -> 맨 왼쪽 index
    # 1 2 4 4 8
    #         ↑ bisect_right(a, 4) -> 맨 오른쪽 + 1 index
    from bisect import bisect_left, bisect_right, bisect

    lst = [1, 2, 4, 4, 8]  # 이미 정렬된 배열(중복 포함)

    print(bisect(lst, -1))  # 0 -> 순서를 유지하며 탐색후 -> 없는 것도 삽입해야할 자리를 반환해준다.
    print(bisect_left(lst, -1))  # 0 -> 순서를 유지하며 탐색후 -> [없는 것도 순서에 맞는 삽입 자리]를 반환해준다.
    # => 즉, 없는 것을 탐색해도 None이 아닌 답이 나온다.
    print(bisect_left(lst, 4))  # 2 -> 여러개 존재하면 left는 맨 왼쪽요소의 index를 반환해준다.
    # => 탐색용도로 쓸 수 있는 것은 left
    print(bisect(lst, 4))  # 4
    # => 여러개 존재할 경우 left로는 해결안된다.
    print(bisect_right(lst, 4))  # 4 -> 여러개 존재한다면, right는 맨오른쪽 + 1을 반환해준다.
    # => 중복 원소가 존재할 경우도 있으니, 1개 박인지를, right로 확인도 해야한다. right - 1(막 요소 + 1) = left(현 요소)이면, 원소는 1개이다.
    print(bisect_left(lst, 1) == bisect_right(lst, 1) - 1)  # True

    ## 즉 탐색이 아니라, lgN으로 이정배에 실제삽입 or 시작 + 마지막index+1의 차이로 해당원소의 갯수를 구할 수 있다.
    # -> 범위탐색을 left, right_value로 할 것인데, 만약 없는 원소를 포함시킨다면?
    # -> 123334489, [-1, 3] -> 0 4위치까지  갯수 b-a+1인데 이미 4위치는 +1된 상황이라서 b-a만으로 그 앞에꺼까지 갯수..?
    # -> [4,5] -> 첫4위치 + 8자리 -> 44만...
    # => [이정배]에서 [left ~ right 범위에 있는 데이터 갯수]를 출력하고 싶다면, bisect right - left를 쓰면 된다.
    lst = [1, 2, 3, 3, 3, 4, 4, 8, 9]

    print(count_by_range(lst, -1, 3))
    print(count_by_range(lst, 4))


    def count_by_range(lst, left_value, right_value=None):
        right_last_index_plus_1 = bisect_right(lst,
                                               right_value if right_value else left_value)  # 1개만 주면, left_value의 갯수가 나오게 처리한다.
        left_first_index = bisect_left(lst, left_value)
        # 갯수는 dst - start + 1이지만, end에 이미 +1이 된 상황이라서, 빼기만 하면 된다.
        return right_last_index_plus_1 - left_first_index
