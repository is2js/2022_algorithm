import sys 
 
input = sys.stdin.readline 
 
 
if __name__ == '__main__':
    ## 운송트럭: https://daekyojeong.github.io/posts/Algorithm1/
    max_weight = int(input().strip())
    specs = []
    for _ in range(2):
        name_and_weight = input().split()
        weight = int(name_and_weight[1])
        specs.append([name_and_weight[0], weight])
    names = list(input().split())

    print(list(zip(*specs)))
    # zip(*언패킹 2차원배열)로, name들끼리 , weight끼리 모았지만
    # [('toy', 'snack'), (70, 200)]
    # 그것을 다시 언패킹해서 dict에 넣으면 안되고 -> dict(zip()에 넣어야한다.
    # print(dict(*list(zip(*specs))))
    # 각 배열을 언패킹해서 1차원배열 순서대로 넣어야지. dict(zip( 1차원배열들 순서대로, ))

    ## 그럴겨면list로 풀지말고 바로 dict, zip(  names, 가격즈))를   *언패킹해서 만들자.
    print(dict(zip(  *  zip(*specs)          )))
    # {'toy': 70, 'snack': 200}

    ## 뭐야.. dict()는 dict(zip()없이도.. 2차원배열의 각 개별원소 순서대로 첫번재를 key, 나머지를 value로 저장하네..
    # print(dict(specs))

    ## 2개 원소를 가진 2차원배열을 dict comprehension도 가능하다.
    # -> 2개의 원소 중 데이터변형을 하면서 dict로 매핑할 때 쓴다.
    # dict_comp = {i: int(j) for i, j in specs}
    # print(dict_comp)



    weight_of_name = dict(zip(*zip(*specs)))
    ## => 누적하기 전에, 300을 넘어서는 순간,  count + 1하고, sum_ 0으로 초기화한 뒤, 더해야한다.
    weight_sum = 0
    count = 1
    for name in names:
        curr_weight = weight_of_name[name]
        if weight_sum + curr_weight > max_weight:
            count += 1
            weight_sum = 0 + curr_weight
        else:
            weight_sum += curr_weight
    print(count)

    # 단 1차원요소가 2개일따만 가능하다.
    print(dict([["toy", 70], ["snack", 200]]))
    # {'toy': 70, 'snack': 200}
    # print(dict([["toy", 70, 100], ["snack", 200, 100]]))
    # ValueError: dictionary update sequence element #0 has length 3; 2 is required

    ## 2차원배열의 원소들이 각 2개씩일 땐 바로 dict()로 변환가능하다
    ## but [원래부터 따로 있었떤 배열] or [순서만 가진 배열을, 문자열 매핑하여 key에 넣어주고 싶을 때]
    #     문자열배열을 순서대로 만들어서 dict(zip())으로 매핑하자.
    # if len(composite) == 2:
    #     graph = dict(zip(list('yn'), composite))
    # else:
    #     graph = dict(zip(range(1, len(composite) + 1), composite))

