import sys
from random import random

input = sys.stdin.readline 
 
 
if __name__ == '__main__':

    ##  원소 2개인 배열 -> dict로 매핑
    specs = [["toy", 70], ["snack", 200]]
    # (1) 데이터 변형이 필요없다면, 원소2개씩 가진 2차원배열은 0번재 key, 1번재 value로 바로 매핑가능하다
    print(dict(specs))
    # {'toy': 70, 'snack': 200}

    # (2) 데이터변형하면서 dict로 매핑하고 싶다면, dict comprehension을 쓴다.
    #   2개의 원소를  a: b로 주는 {a:b for a, b in 원소2개 2차원배열} 컴프리핸션이다.
    specs = [["toy", "70"], ["snack", "200"]]
    print({name: int(weight) for name, weight in specs})

    ##  배열1개이며, 길이제한없을 때 -> 매핑문자열배열을 만들어서 dict로 매핑
    # (3) 원소2개씩 주어지지 않고, 만약 value배열만 주어졌다면?
    # => dict(zip( key매핑배열,  value매핑배열))을 이용한다
    specs = [70, 200]
    print(dict(zip(["toy", "snack"], specs)))
    # {'toy': 70, 'snack': 200}

    ## 2개 배열을 직접 만들어서 dict(zip())으로 매핑
    animals = ['cat', 'dog', 'lion']
    sounds = ['meow', 'woof', 'roar']
    print(dict(zip(animals, sounds)))
    # {'cat': 'meow', 'dog': 'woof', 'lion': 'roar'}

    # (5) 프로젝트에 쓸 예시매핑
    # => 순서에 의지하는 compoiste객체에 대해, 문자열을 매핑하되, 길이에 따라 매핑해준다.
    composite1 = ['cat', 'dog']
    composite2 = ['a', 'b', 'c', 'd', 'e']

    composite = random.choice([composite1, composite2])
    if len(composite) == 2:
        graph = dict(zip(list('yn'), composite))
    else:
        graph = dict(zip(range(1, len(composite) + 1), composite))
    print(graph)
    # {'y': 'cat', 'n': 'dog'}
    # {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
