import itertools
import sys
from collections import defaultdict

input = sys.stdin.readline

if __name__ == '__main__':
    ## 방문길이: https://school.programmers.co.kr/learn/courses/30/lessons/49994
    dirs = input().strip()

    ## (1) 이미 정해진 경로의 탐색은 dfs bfs아니다 -> visited도 필요없다(1방향으로 나아감)
    ## => 대신, 좌표계로 매핑한 행렬의 개념은 next좌표의 유효성검사에 쓰일 수 있으니, 범위는 확인해놔야한다
    ## command별 좌표이동은 매핑해준다.

    commands = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1),
    }

    ## (2) 미리 정해진 경로를 따라가면서, 정점좌표를 지나가면서, edge를 기록하기 위해 graph를 만든다.
    ## -> curr_node를 가변변수로 초기화해놓고, next_node를 직접 curr로 업뎃하며 진행
    ##    (i, i+1은 반복문에서 curr를 자동 업뎃)
    ## -> 직후와의 비교는 queue를 이용해도 되지만, 기준마다 직후들 여러개 pop or 순서대로 쌓기용아니면 curr직접업뎃 순회로 대체하자.
    ## 1) (0~양수)숫자node면 -> 인접 2차원 빈행렬
    ## 2) 숫자아니면(좌표튜플, 문자열) -> 인접 빈defaultdict(lst)
    ## 3) 비용 등이 없이 다음node1개만 value면 -> 인접 빈defaultdict(set)
    graph = defaultdict(set)

    ## (3) 좌표계를 행렬로 바꿔서 생각하되, 2차원배열을 생성할 필요없이
    ## => 시작좌표로 정해진 경로를 탐색한다
    ##    -5~ 5 좌표계 -> 행렬 range(2*5+1) by 2*5+1
    ## =>  시작좌표 0,0 -> 행렬 (k,k)

    ## (3) 지나온 경로를 순회하며 좌표를 탐색하되,
    ## => curr, next를 묶어서 보기 위해 => curr가변변수에 초기값넣고 next로 로직처리후, curr = next기준업뎃해줘야한다
    ##    curr, next를 한꺼번에 만나서 -> 방문경로를 처리한다.
    curr_node = (5, 5)
    # i기준이 아니라 i + 1기준이므로, 끝에[:-1]안해줘도 된다. i,i+1이라면 index는 그전까지 처리
    for command in dirs:
        delta = commands[command]
        next_node = curr_node[0] + delta[0], curr_node[1] + delta[1]
        if not (0 <= next_node[0] <= 2 * 5 + 1 - 1 and 0 <= next_node[1] <= 2 * 5 + 1 - 1): continue
        ## (5) 이제 curr, next를 같이보면서 순회할 수 있다면, [curr -> next의 edge]를 graph에 등록한다.
        ## a -> b를 등록하되, [create전 dict라는 db의 중복검사]를 해야한다.
        ## db(dict edge) 저장은 중복되더라도, [i+1 -> i 로의 업데이트는 지속]되어야한다.
        ## => curr, next없뎃은 continue된다면, i -> i+2로 업뎃되어 순차적용이 안된다.
        ##    유효성검사( <- 막히면 ↑로 올라가는 좌표이동)이라  그렇게할 수 있어도,
        #     로직상 부가저장의 중복검사는 무시되기만 하고, 업데이트를 방해해선 안된다.
        ## => 업데이트를 통한 curr,next동시순회가 되려면,
        ##    if 부가처리 실패시 continue (X) => [if 부가처리 가능시: 부가처리만 -> 로직 지속 ]으로 처리해야한다.

        ## (6) 정보저장하되, 이미 db에 들어간 정보면 pass하고 저장하도록 if 중복검사pass : 실행
        ## => 이 때, edge의 방향성이 의미가 없을 땐 [(1) 중복검사도 양방향 -> (2) 저장도 양방향 -> (3)카운팅시 전체세고 //2]으로 한다.
        ##    혹은 (1) 방향성으로 저장 -> (2) 카운팅시 [순서 바꿔도 동일하면 카운팅안함] 해야하는데 복잡하다
        ## => edge의 갯수를 셀 땐 //2해줘야한다.
        ## => dict에 저장전엔 중복검사하자. and defaultdict(컬렉션) 중복검사시에는 key부터 먼저 있는지 검사하자
        ##   key검사안하고 바로 default라고해서 바로 검사하면, defualtdict는 빈컬렉션을 그 때 생성해버린다.

        ## [or는 먼저검사에 대해 false] == 반대로 ~ 하더라도일 때 default값 or 추가검사를 해주는 역할을 한다
        # if (curr_node not in graph or next_node not in graph[curr_node]):# and \
                # (next_node in graph or curr_node not in graph[next_node]):

        ## (7) set defaultdict면, 양방향 중복검사를 생략해도 된다.
        graph[curr_node].add(next_node)
        graph[next_node].add(curr_node)


        ## (4) 공통 업데이트 로직을 미리 작성해둔다. -> 이것이 등장하는 순간부터는
        ##    while도 greedy도 아니지만, 다음것을 curr로 업데이트하며 매번 curr, next를 보려면 for문이라도 직접 필수 업뎃로직이 맨아래 추가된다.
        ##    유효성통과한 로직을 -> [if 저장용로직 실패시: continue를 하면 안된다.]
        curr_node = next_node


    # print(graph.values())
    # print(len(graph))

    ## 각 node마다 양방향 다 저장해놨기 때문에, unique한 방문edge의 갯수는 / 2하면된다.
    ## (5) dict의 values()는 value가 컬렉션일 때, 2차원배열로 나온다.
    ##    모든 갯수는 평탄화해서 세야한다.
    # print(len(list(itertools.chain(*graph.values()))) // 2)
    print(len(list(itertools.chain.from_iterable(graph.values()))) // 2)