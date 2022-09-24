import sys
from collections import Counter

input = sys.stdin.readline


def dfs(apeech_sum, n,
        count, sum, visited):
    if count == n:
        if apeech_sum < sum:
            return [visited]
        else:
            return False

    # print(count, sum, visited)

    total_result = []
    for k in range(0, 10 + 1):
        new_visited = list(visited)
        new_visited[k] += 1

        result = dfs(apeech_sum, n,
                     count + 1, sum + k, new_visited)
        if result:
            total_result += result

    return total_result


def calculate_score(info, count_arr):
    arr_sum = 0
    for idx, count in enumerate(count_arr):
        if count < 0: continue
        apeech_count = info[::-1][idx]
        if apeech_count > 0:
            if count > apeech_count:
                arr_sum += idx
            else:
                arr_sum += 0
            continue
        arr_sum += idx * count
    return arr_sum


if __name__ == '__main__':
    n = int(input().strip())
    info = list(map(int, input().split()))

    ## 어피치의 합
    apeech_sum = sum([index * count for index, count in enumerate(info[::-1])])
    # 44
    visited = [0] * 11

    l = dfs(apeech_sum, n, 0, 0, list(visited))
    # print(*l, sep='\n')

    ## 이제 sum이 가장 큰 놈(들)을 골라야한다.
    # max_i_arr = None
    ## => greedy의 기준이 아닌 겨과값이 2개이상 나올 수 있다면 미리 배열로 받아두자.
    ## => 일반 value기준 greedy 탐색은 앞에 최대값이 나오면, 뒤에 한번더 나와도 무시된다(크질 않으니)
    ##    (1) 최대기준값만 먼저 찾고 -> (2) 최대기준으로 최대값(배열)을 원하는대로 뽑자.
    ## cf) 최대기준만 찾는답면, 직전최대값을 하한으로 두는 max로 업뎃으로 처리하면 된다.

    if len(l) == 0:
        exit()

    max_sum = float('-inf')
    for count_arr in l:
        # arr_sum = sum([idx * count for idx, count in enumerate(count_arr) if count > 0])
        ## 이 때, apeech랑 동일 위치에있다면, 최대 k점 밖에 못가져간다...
        ## 계산을 할 때, 어피치에 count가 있다면, 해당count보다 많을 경우, k점만, 아닐 경우, 못가져간다.
        arr_sum = calculate_score(info, count_arr)
        max_sum = max(max_sum, arr_sum)

    print(max_sum)
    max_arr = []
    for count_arr in l:
        # arr_sum = sum([idx * count for idx, count in enumerate(count_arr) if count > 0])
        arr_sum = calculate_score(info, count_arr)
        if arr_sum == max_sum:
            max_arr.append(count_arr)

    if len(max_arr) < 2:
        print(max_arr)
        exit()

    ## 최대값을 가지는 배열이 2개이상일 경우 -> 제일 낮은 idx가 많은 것을 선택한다.
    ## -> 다음 비교를 위해, 순서대로 미리 구해놓고 정렬해놓는다.

    ## 인덱스의 갯수를 세고, 낮은 것이 제일많은 것?
    for id, count_arr in enumerate(max_arr):
        ## 배열별로 min idx -> count를 찾고 -> 최소값으로 유지하기 위해, 둘다를 가변변수로 두고 탐색?
        ## 비교 기준이 다음것로 바뀔 수 있으니까 준비는.. idx별 count를 준비
        ## -> 보통같으면 dict comp로 저장하는데, 최소값 및 차선값을 위한 정렬해야하므로, tuple로 2개를 매핑
        idx_of_count = [(idx, count) for idx, count in enumerate(count_arr) if count > 0]
        print(idx_of_count)
