import itertools
import sys
from collections import defaultdict

input = sys.stdin.readline

if __name__ == '__main__':
    ## 방문길이: https://school.programmers.co.kr/learn/courses/30/lessons/49994
    dirs = input().strip()
    ## 좌표계를 행렬로 나타내려면, 0부터 시작하고, k까지 양수로 있으면, 1사분면은 k(1~k) + 1(0) by k+1이다.
    ## => 음수까지 해야한다면, 0을 제외한 양쪽 2k + 0을포함한 1로 해서 2k+1이다.

    ## -> board에 value를 사용하는 것이 아닌 이상, dfs탐색에는 board가 직접적으로 필요없다
    ## => [dfs탐색에는 배열]이 필요한 경우는, [방문체크하거나 value를 사용하는 경우]이다.

    visited = [[False] * (2 * 5 + 1) for _ in range(2 * 5 + 1)]

    dir_of_move = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1),
    }

    ## node별 방문경로가 정해져있다면 -> 각 현재node -> 다음node로 가는 graph(인접행렬, 인접dict)를 만들 수 있다.
    ## => a -> b 를 기억해야하는데 b <- a는 중복으로 카운팅 하지 않는다.
    #    경로의 갯수마다 count +=1 인데,
    ## => [경로 저장]은 [graph]를 만들되, [방향을 고려해야하는지 생각]한다.

    ## 경로가 1개로 이미 정해져있다면, dfs로 가능한 여러경로를 검색하는 것이 아니다
    # -> 경로의 순서별로 반복문을 돌려서 처리하면 된다.
    # -> 이미 정해진 경로를 따라가면서 graph(node연결관계)를 기록하되, 역방향은 중복으로 친다.
    ## => graph를 인접빈행렬이 아닌, 인접빈set으로 만든다.

    ## node가 숫자라면, index매핑의 인접행렬, 문자열or 좌표(튜플값이지만, 숫자는아님) 등은 인접dict로 처리한다.
    # graph = [set() for _ in range(2 * 5 + 1)]
    graph = defaultdict(set)

    ## 현재좌표 와 다음좌표 with dirs를 비교하려면,
    ## => 숫자는 i -> i+1을 쓰면 되지만, 직후와의 비교는 queue를 쓰면 될 것 같다.
    ##         val -> (->매핑dirs) next_val를 뽑아내서 queue 에서 매번 기준을 정해서 뽑아내도 되지만,
    ##         반복문으로 기준 다음좌표로 넘어갈때마다, 기준 가변변수를 선언해 업뎃해줘도 된다.
    ## => curr 를 바꾸고시팓면, 초기curr를 반복문위에 + for문으로 비교대상 돌리기 + 마지막에 curr업뎃하기
    ##   최대값, 최소값 greedy처럼, 다음원소를 기준으로 업뎃시키면서
    #    [for i 반복문 -> i, i+1처럼, i기준 반복문 자동업뎃, i+1다음거 자동업뎃] 대신
    #    [for 원소 반복문 -> curr 초기값으로부터 현재로 직접업뎃, next 직접 업뎃]으로
    #   현재를 기준으로 매번 다음것과 비교한다. [curr직접업뎃으로 매번 다음원소와 비교]
    # print(curr_coord + (1, 0))  # (4, 4, 1, 0)
    ## => 좌표튜플은 한번에 연산시 extends로 내부값 통째로 업뎃은 못한다.. 각각 쪼개서 해야함.
    # print(tuple(map(sum, zip(curr_coord, (1, 0))))) # (5, 4)


    ## queue-popleft으로 빼면서 돌지말고, for로 1개씩 앞에서 접근할 수 있다.
    ## queue는 직후만 비교x -> 기준마다 직후들을 반복해서 비교 or bfs처럼 순서대로 여러개 쌓아두고 -> 넣어준 순서대로 나가는 저장용도

    ## i, i+1이 아니라, curr, next비교라면, next -> curr로 직접업뎃 시켜주기 위해, 가변변수를 만들어서 쓴다.
    curr_position = (5, 5)
    # for dir in dirs[:-1]:
    ## => i로 돌린다면, index1개 적게까지 진행되어야하지만
    ##    dir은 next에 대한 정보를 주는 반복문이므로 마지막 종착이 i가 아닌 next이다.
    for dir in dirs:
        d_row, d_col = dir_of_move[dir]
        next_position = curr_position[0] + d_row, curr_position[1] + d_col
        ## 새 좌표는 유효성검사
        # -> curr로 업뎃되기도 전에 넘어가야한다.
        ## => 실패시 업뎃되 해선 안되는 예외처리의 경우는, if실패시continue다.
        if not (0 <= next_position[0] <= 10 and 0 <= next_position[1] <= 10): continue
        ## 등록 중복 검사 (이미 저장된 a -> b)라면, 제낀다.
        ## => deafultdict는 항상 key검사하고 조회한다! 안그러면 set() list()기본형이 들어가서 갯수로 세어진다.
        # if (curr_position in graph and next_position in graph[curr_position] )\
        #         or (next_position in graph and curr_position in graph[next_position]):
        #     continue
        ## => 등록 중복되었다면,등록만 제껴야지 이동(좌표이동)까지 제끼면 안된다!!!!!!!

        # if (curr_position in graph and next_position in graph[curr_position] )\
        #         or (next_position in graph and curr_position in graph[next_position]):
        #     continue
        ## 이미 역방향으로 등록되었으면 제낀다?
        # if next_position in graph and curr_position in graph[next_position]: continue

        ##
        # if not (curr_position in graph and next_position in graph[curr_position]):
                # or (next_position in graph and curr_position in graph[next_position])):
            ## 이미 왔던 길이면, 등록안하고 업데이트는 해야한다.
            ## => continue는 밑에 2가지 로직 중 1가지만 skip이 안된다.
            ## => [curr기준 업뎃]  [공통 로직]이 맨 아래 있을 경우, continue를 쓰면 안된다. 혹은 반복되도라도 공통로직(필수로직)은 넣어주고 continue해야한다.
            ## => 아니라면, if 실패 continue가 아니라, continue없이 if 성공시만 비공통로직 실행하고 -> 뒤에 공통로직까지 내려간다.
            # curr_position = next_position
        graph[curr_position].add(next_position)
        graph[next_position].add(curr_position)
            # continue
        # if next_position in graph and curr_position in graph[next_position]:
        #     curr_position = next_position
        #     continue


        ## 검사를 마치고나서는 저장한다.
        # => a->b와 b->a가 다른 것이 아니라 동일한 것이므로
        ##  인접dict에서는 다르게 저장되지만, graph[a] b   graph[b] a
        ##  카운팅은 1개로 되어야한다.
        # print(curr_position, next_position)
        # graph[curr_position].add(next_position)
        ## (0) 인접set으로 a->b를 또 방문하더라도 1번만 저장된다.
        ## (1) 양방향이 아니라 단일방향으로 진행하므로 양방향 저장할 필요가 없다 경로만 기록이다.
        ##    but 양방향으로 저장해주면, 반대방향에서 와도 카운팅안하게 된다 => 방문한 간선의 종류만 카운팅한다면 //2로 해주면 된다.
        ## (2) 단뱡향으로 기록했으나, a->b와 b->a는 동일한 1개로 카운팅해야한다.(방향(단방향)성있게 저장했찌만, edge의 방향성을 무시하고 카운팅)

        # graph[next_position].add(curr_position)

        ## 이제 next를 기준curr로 직접업뎃해줘야, 다음것nn이 n와 비교된다.
        curr_position = next_position






    # print(graph)
    # defaultdict(<class 'set'>, {(4, 4): {(4, 3)}, (4, 3): {(4, 4), (3, 3)}, (3, 3): {(3, 2), (4, 3)}, (3, 2): {(3, 1), (3, 3)}, (3, 1): {(3, 0), (3, 2)}, (3, 0): {(2, 0), (3, 1)}, (2, 0): {(3, 0)}})

    # defaultdict(<class 'set'>, {(4, 4): {(4, 3)}, (4, 3): {(3, 3)}, (3, 3): {(3, 2)}, (3, 2): {(3, 1)}, (3, 1): {(3, 0)}, (3, 0): {(2, 0)}, (2, 0): set()})
    ## (
    ## values()도 각 value들이 1개의 lst로 묶여서 나오므로 개별 원소의 갯수는 못센다
    # print(graph)
    # print(graph.values())
    # dict_values([{(4, 5), (6, 5)}, {(7, 5)}])
    print(len(list(itertools.chain(*graph.values()))) // 2)


    #     for v in vs:

