import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## max값 greedy할 때, 뒤에 나타난 max값도 처다보기
    lst = [1, 5, 4, 3, 2, 5, 4, 5]

    ## (1)일반적인 greedy 탐색은 가장 먼저 등장한 원소만 바라보고, 그 이후로 같아도 업데이트 안된다.
    max_i = 0
    max_value = float('-inf')
    for i, value in enumerate(lst):
        if value > max_value:
            max_i = i
            max_value = value

    # print(max_i, max_value) # 1 5

    ## (2)동일한 기준값이 max로 등장했을 때, 여러개를 모아두고 싶다면?
    #   => 발견시마다 초기화되어, 뒤에 같은 값이 나타나면 모아줄 [배열 가변변수] 추가
    ## =>  (0)모아둘 빈 배열을 만들고
    #      (1) 새로운 max가 나타날 땐, 배열을 초기화하는 과정을 추가해준다.(그 이후로 모아야함)
    #      (2) 기존if는 elif의 배반조건문으로 -> if max == value:의 조건문을 추가한다음, 같은게 나타나면, append한다.
    #      (3) max발견이후 max와 동일할 것이 나타날 땐, 배열에 담아두기
    max_i = 0
    max_value = float('-inf')
    max_i_arr = []
    for i, value in enumerate(lst):
        if value == max_value:
            max_i_arr.append(i)
        elif value > max_value:
            max_i = i
            max_value = value
            max_i_arr = [i]

    # print(max_i_arr, max_value) # [1, 5, 7] 5

    ## (3) greedy 탐색시, 여러개 등장(뒤에 ==한 조건추가)할 때, [max시 업뎃]+ [같은max라면 추가조건 만족시 새로운 것으로 업뎃]하기
    ## => 같은 max값이 여러개 등장한다면(if == 로 추가 살피기)
    ##    idx가 늦은 뒤에 것을 선택한다( if == 조건에서 idx비교해서, idx큰 것으로 새로 업뎃)
    ## -> 모아둘 것 아니고, 바로 확인후 업뎃한다면, 배열에 모아둘 필요 없다
    max_i = 0
    max_value = float('-inf')
    for i, value in enumerate(lst):
        if value == max_value:
            if i > max_i:
                max_i = i
                max_value = value
        elif value > max_value:
            max_i = i
            max_value = value

    # print(max_i, max_value) # 7 5

    ## (4) 배열의 집계를 greedy한다면  -> 기준값 및 원본배열를 저장하기
    lst = [
        [1, 0, 1, 2, 0],  # 4
        [1, 0, 1, 1, 1],  # 4
        [1, 0, 1, 1, 0],  # 3
        [1, 1, 1, 1, 0],  # 4
    ]
    max_arr = []
    max_sum = float('-inf')
    for i, arr in enumerate(lst):
        sum_of_arr = sum(arr)
        if sum_of_arr > max_sum:
            max_sum = sum_of_arr
            max_arr = arr  # 매번 바뀌는 반복문 변수 arr는 깊은복사 안해도 된다.

    print(max_sum, max_arr)  # 4 [1, 0, 1, 2, 0]
    # => 첫번재 발견되는 것이 그대로 남는다.

    ## (5) sum max를 만족하는 배열을 모아서 집계할 것 아니라
    ##  => 그자리에서 if == 를 추가 뒤에 나오는 sum max의 배열을
    #      바로  비교해서 조건만족시 업뎃한다면, 모아두는 배열 변수(새업뎃시 초기화, == 만족시 모아두기)는 필요없다
    max_arr = []
    max_sum = float('-inf')
    for i, arr in enumerate(lst):
        sum_of_arr = sum(arr)
        if sum_of_arr == max_sum:
            ## 현재 2배열(기존max배열, 현재 max와 같은 기준값을 가진 배열)을 index로 동시에 탐색하면서
            # index를 뒤쪽부터 역순으로 살펴보면서, 더 value가 큰 arr를 선택한다.
            # value가 같으면 앞으로 넘어가고, 동시에 같은 index를 봣을 때, value가 더 큰게 나오는 놈이 선택
            for i in range(len(arr) - 1, 0 - 1, -1):
                ## max가 같아서 새롭게 등장한 놈이 추가조건을 만족하면 업뎃을 똑같이 해줘야한다.
                if arr[i] > max_arr[i]:
                    max_sum = sum_of_arr
                    max_arr = arr
                    ## 뒤에서부터 순서대로 본다면, 만족시 업뎃하고 break로 끊어야한다.
                    break
                ## 기존 max배열이 조건에 부합한다면, 업뎃없이 바로 끊어야한다.
                elif arr[i] < max_arr[i]:
                    break
                ## 마지막 배반으로서 같다면, 다음 앞쪽 index를 보러 가야한다.
                ## 맨마지막에 배치해서, continue안해도 자동으로 넘어간다.

        elif sum_of_arr > max_sum:
            max_sum = sum_of_arr
            max_arr = arr

    # print(max_sum, max_arr) # 4 [1, 0, 1, 1, 1]

