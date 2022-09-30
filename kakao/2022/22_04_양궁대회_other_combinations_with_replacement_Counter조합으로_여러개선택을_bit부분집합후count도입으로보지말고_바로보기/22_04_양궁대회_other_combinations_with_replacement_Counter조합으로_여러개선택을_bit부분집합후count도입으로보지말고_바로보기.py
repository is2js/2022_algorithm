import itertools
import sys
from collections import Counter

input = sys.stdin.readline

if __name__ == '__main__':
    ## 양궁대회: https://school.programmers.co.kr/learn/courses/30/lessons/92342
    n = int(input().strip())
    info = list(map(int, input().split()))

    ## 중복조합 + Counter로 O,X가 아닌 여러번 뽑는 경우의수 처리하기
    ## -> n번 쏘는 과녁 -> n개까지 중복 선택이 가능하다.
    max_diff = 0
    # max_subset = []
    ## greedy업뎃전에, 기본값을 인덱싱해서 비교하는ㄱ ㅕㅇ우도 있으니
    ## 배열이라면, 기본값과 동일한 갯수로 미리 맞춰주자.
    max_subset = [0] * 11
    for subset in itertools.combinations_with_replacement(range(10 + 1), n):
        # print(subset) # (0, 0, 0, 0, 0)
        ## 중복해서 뽑은 것을 Counter 씌운다면, 원소: 뽑힌 갯수가 나온다.
        ryan = Counter(subset)
        temp = [0] * 11
        for score, count in ryan.items():
            temp[10 - score] = count
        # print(temp)

        ## 2개의 배열 -> 1개는 배열(index), 1개는 dict(key)로 매핑된 것을
        ## -> 숫자이기 때문에 index이자 key로 동시에 매핑가능하고 접근가능하니, 각각 접근해서 비교한다.
        ## dict에는 i <-> info에는 index로서 역수로 매핑되어있다.
        ryan_score = apeach_score = 0
        for i in range(len(info)):
            if temp[i] > info[i]:
                ryan_score += 10 - i
            # else:
            #     if info[i] > 0:
            ## 배반 중에 1가지라면 else-배반중1가지-if로 주자.
            elif info[i] > 0:
                apeach_score += 10 - i
        diff = ryan_score - apeach_score

        if diff == max_diff:
            for i in range(10, 0 - 1, -1):
                # print(temp[10], max_subset)
                if temp[i] > max_subset[i]:
                    max_subset = temp
                    max_diff = diff
                    break
                elif temp[i] < max_subset[i]:
                    break
        elif diff > max_diff:
            max_diff = diff
            max_subset = temp

    ## greedy 기준값이 업뎃 안됬다-> 발견안됬다->
    if max_diff:
        print(max_subset)
    else:
        print(-1)
