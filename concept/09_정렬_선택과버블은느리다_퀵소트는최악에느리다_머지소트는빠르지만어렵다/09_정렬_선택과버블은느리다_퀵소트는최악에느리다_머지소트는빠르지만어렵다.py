import sys
from typing import List

input = sys.stdin.readline


def solution():
    ## 정렬
    # 1. 선택정렬: i를 돌면서 -> i+1~끝까지 비교하여 더작은값찾을시 왼쪽으로 swap
    #    i로 N을 돌면서, i+1~끝까지 다시 N을 도는 2중포문 -> O(N^2)은 느리다.
    # 2. 버블정렬: i를 돌면서 -> i+1~끝까지 비교하며 큰값은 오른쪽으로 swap
    #    i로 N을 돌면서, i+1~끝까지 다시 N을 도는 2중포문 -> O(N^2)은 느리다.
    # ==> 선택/버블은 N^2으로 느리다.

    # 3. 퀵소트
    #    배열의 첫번째원소를 p로 잡아놓고
    #    배열을 p보다 작거나 같은 + p + p보다 큰 그룹으로 나눈 뒤
    #    재귀를 통해, 각 그룹을 배열로 하여 -> 갯수가 p1개가 남을때까지,
    #       작은그룹을 왼쪽으로 두고 p  큰그룹을 오른쪽으로 정렬한 배열을 더한다
    # -> depth마다 배열의 사이즈가 작아지도록 업데이트된다.
    # -> depth마다 2개의 배열로 나눠져서, 재귀를 수행한 뒤, a배열 + [p] + b배열을 만든다.
    # -> 종착역에선 원소1개배열이 반환되니, 직전엔 [a] + [당시p] + [b] -> [a, p, b]가 반환된다.
    # --> 결국, [a1,p1,b1] + [p3] + [a2,p2,b2] 가 더해져 직전으로 가니.. 순서가 정렬된다
    # ---> 재귀에 의해 O(2N) -> O(N)이 될 것이다.

    # ==> 퀵 소트는, 최악(역순정렬&p를 맨첫값)의 경우 NN이 될 수도 있다.

    # array -> left_side로 업데이트 , right_side로 업데이트되며 진행되는데,
    #          결국엔 정렬되어서 반환되면, 합쳐진 array가 된다.
    def quick_sort(array):
        if len(array) <= 1:
            return array

        ## 현재arry의 처리
        pivot = array[0]
        tail = array[1:]

        # 자식들 호출직전까지가.. 자신의 처리
        # -> 자신을 p보다 작/큰그룹으로 나누는 것이 자신의 처리
        left_side = [x for x in tail if x <= pivot]
        right_side = [x for x in tail if x > pivot]

        ## 나눠진 것들로 자식들호출
        ## return있는 재귀라면,
        # 자식들 동적트리순회가 아니다.
        # 자식들로 나눴지만, 빽하면서 1개의 값으로 돌려준다.
        # 자식들이 자신의처리를 하고 난 뒤, 종착역에서 어떤값을 돌려줄 지 보고
        # -> 종착역에서 돌려주는 값을 이용해 최종반환할 것을 정한다.
        return quick_sort(left_side) + [pivot] + quick_sort(right_side)

    print(quick_sort([5, 4, 2, 3, 1]))

    # [1, 2, 3, 4, 5]


    ## 4-2.
    def merge(left_lst, right_lst):
        ## 자식들로부터 반환된 1개짜리배열 2개를 merge해서 끝처리를 한다.
        ## 2개의 배열 투포인터로 동시에 돈다.
        merged_list = []
        i, j = 0, 0

        # 2개의 배열을 동시에 돌릴땐, and로 둘다 유효한범위를 때린다.
        while i < len(left_lst) and j < len(right_lst):
            # 둘다 0부터 시작하므로 각각 포인터를 올려간다.
            # i+=1
            # j+=1

            # 대소비교해서, 작은 것을 append하고 포인터를 올린다.
            # 한쪽이 다 작다면 한쪽만다 append될 것이다.
            # 1개짜리 배열들부터 생각하면, 이미 정렬된 상태라고 가정한다.
            # 부분문제는 이미 정복(정렬)된 상태라고 가정한다.
            if left_lst[i] < right_lst[j]:
                merged_list.append(left_lst[i])
                i += 1
                continue
            merged_list.append(right_lst[j])
            j += 1

        # A and B에서 한쪽이 다돌아서 not A로 빠져나왔다면,
        # 나머지를 싹다 append해주면 된다.
        # > 다돌았다 == 끝index넘어섰다.
        if i == len(left_lst):
            merged_list += right_lst[j:]
        if j == len(right_lst):
            merged_list += left_lst[i:]

        return merged_list

        pass

    ## 4. 머지소트
    #    재귀의 종착역은 array 원소갯수가 1개인 것은 퀵소트와 동일한데
    #    재귀 속 divide_conquer로서 또다른 재귀가 돈다.
    # 2개의 배열을 merge할 때, 4개짜리 배열을 미리 대기시켜놓고, 투포인터로 넣어줘야한다.
    # 즉, 메모리할당이 많아진다.
    # 머지 소트는 정렬 문제에서 메모리가 넉넉할 때 쓴다.
    # 퀵 소트는, 최악(역순정렬&p를 맨첫값)의 경우 NN이 될 수도 있다.
    # 4-1.
    def merge_sort(my_lst: List):

        ## 종착역에서 값을 반환해준다 -> 동적트리순회가 아닌 [자식들은 빽하며 하나의 값으로 반환] 예상
        if len(my_lst) < 2:
            return my_lst

        ## 자신의 처리

        # divide and conquer
        # len는 마지막인덱스 + 1
        # len//2 -> 0123 짝수개라면 4//2 -> 2 -> 가운데 오른쪽 index
        #  [:len//2] -> 첨 ~ 가운데서 왼쪽까지
        #  [len//2:] -> 가운데서 오른쪽부터 ~ 끝
        #        -> 012 홀수개라면 3//2 -> 1 -> 가운데 index
        # ==> len//2는  가운데거나(홀수)  가운데서 오른쪽꺼다.
        left_half = my_lst[:len(my_lst) // 2]
        right_half = my_lst[len(my_lst) // 2:]

        # 자신의처리에서 index기준으로 절반으로 나눈다.

        # 절반을 나눈 자식들이 다음stack으로 가서 절반을 나눌 것이다.
        # -> 절반나눈것이 종착역의 1개 요소 list를 반환한다고 생각
        # -> 1개짜리배열 반환받은 것으로 merge를 때려서 최종반환한다?

        ## 아직 자신의 처리가 안끝났다. 반환받은 1개짜리배열 2개로 merge해서 끝낸다.?
        ## -> 자식들호출하여 끝난 뒤 처리 ->
        ## 자신의 끝처리
        return merge(merge_sort(left_half), merge_sort(right_half));

    print(merge_sort([5, 4, 3, 2, 1]))

    pass




if __name__ == '__main__':
    solution()
