import sys 
 
input = sys.stdin.readline 
 
 
if __name__ == '__main__':
    ## 순위검색: https://school.programmers.co.kr/learn/courses/30/lessons/72412
    info = [input().strip() for _ in range(6)]
    query = [input().strip('\n') for _ in range(6)]

    #### 개념
    #### => 처리하지 않는 -에 대해서는 미리 구성을 해놓고, 그때그때 처리하지 않고, 한번에 찾아서 처리하게 한다
    # 그림: https://raw.githubusercontent.com/is3js/screenshots/main/image-20220922175856508.png
    # => 경우의수는 4 x 3 x 3 x 3 = 108 + 점수
    # => 이미 field별로 올 수 있는 경우의 수가 정해져있다.
    # => 이미 정해진 경우의 수는 각 field별 배열의 1차원에 저장할 수 있다.
    #    사람(index)별 아무거나 저장가능한 field -> field별로 배열 추가
    #### 사람이 아니라, 이미 정해진 종류의 field -> 배열의 차원마다 1개씩 field씩 & index마다 정해진value를 매칭 -> 다차원indexing == 이미 정해진 1사람
    #### 4차원배열에 이미종류가정해진field를 1차원씩 저장한다.
    # -> 그림: https://raw.githubusercontent.com/is3js/screenshots/main/image-20220922180857144.png
    # java backend junior pizza 150
    #  2     1      1      2
    #### 혹은 1차원배열에 각 case를 108개를 나누어서 계산되도록 변환 -> index에 매핑해놓을 수도 있다
    # -> https://raw.githubusercontent.com/is3js/screenshots/main/image-20220922181031258.png

    #### 종류가 정해지지 않은 점수field -> 마지막차원에 넣어주는데
    #### 희한하게..  각 종류가 정해진 필드에 대해, 각각이 O -의 모든 경우에 미리 150을 넣어둔다?????
    # -> 지원자별로 각field에 대해 O/X로만 생각하면, 2x2x2x2의 16case별로 모두 150점을 넣어둔다?
    # -> https://raw.githubusercontent.com/is3js/screenshots/main/image-20220922181405282.png
    # case1: - - - - 150 => - - - -로 가서 마지막차원 배열에 150을 을 넣는다
    #      => 값이 있음에도 4개field 모두를 - 라 생각하고 - - - - 에 150을 넣는다
    # case2: - - - pizza 150 => 이것도 넣어준다
    # case3: - - junior - 150 => 이것도 넣어준다
    # => 원래value뿐만 아니라, 각 - 일 때도 중복으로 값을 넣어둔다
    # case4: - - junior pizza 150 => 이것도 넣어준다
    # => 하나하나를 원소로 생각하고 있고없고의 집합으로 생각하면, 모든 부분집합 모든 경우의 수로서 지원자별 0000 1111 의 원소4개의 모든 부분집합으로 생각할 수 있다.
    # case15: java backend junior - 150
    # case16: java backend junior pizza 150
    #### 이렇게 미리 넣어둠으로써, 어떠한 query가 들어오더라도, index로 찾아가면
    #### score배열 list만 bs하면 된다
    #### 만약, - 없이 테이블을 만들어놓는다고 하면, -에 대한 별도연산으로 시간이 오래걸린다.
    #### => 없을 수도 있는 - 도 미리 테이블에 포함시켜 경우의수를 만들어놓고
    ####    미리 중복이지만 점수를 insert해놓는다면, 한번의 indexing으로 찾을 수 있따.

    #### my) -는 없음이 아니라, 상관없다는 말이다. 상관없는 case에 대해서도 미리 구성을 해놓으면, 검색시 걸리게 된다.




