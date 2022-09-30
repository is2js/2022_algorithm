import sys 
 
input = sys.stdin.readline


def traversal(sales, node):
    # visited, graph가 있는 탐색은 조건이 없다면 종착역이 없다.(알아서 못뻗고 사망)

    global cost
    ## 4. 자신의 처리에서, sale정보 -> cost O/X에 기록한다.
    ##    ex> depth도 자신의처리에서 기록한다. cf) parent_table은 자식들처리에서 기록한다.
    cost[node][0] = 0
    cost[node][1] = sales[node]

    ## 5. 자신의 처리가 끝난 leaf node는 종착역 처리해줘야한다.
    ## =>  순열, 조합 등의 [파라미터에 입력하는 누적결과값 변수] -> 자신의처리 X -> [stack 변수]넘어서면 [바로 종착역]
    ##     [자신의 처리에서 입력하는 global변수] -> [자신의 처리 끝나면 종착역 명시]
    ##     => ex> leaf node 등 마지막 지점까지 계산을 해야하면, 자신의 처리 끝나고 종착역을 명시하자.

    #### => graph가 있어도, [자식들처리for문 이후 이후 (집계 or greedy연계) 자신의 끝처리]를 하는 경우가 있으므로
    ####    반드시 종착역 명시하자.
    if not graph[node]:
        return

    ## 10. 자식들 중 참여O비용( - 참여X비용)이 가장 적은 것을 찾기
    # -> 이미 부모X-자식들모두X로서 누적된 상황이므로, 참여시킬 자식1개를 최소값으로 찾되, 자식참여X의 차감만큼만 더해주면 된다.
    min_extra_cost = float('inf')

    ## 6. 자식들 순회
    for child in graph[node]:
        traversal(sales, child)
        ## 7. for 자식들 재귀호출 바로 밑은 leaf node가 자신의 처리를 마친 것이다.
        ## => 여기서부터 누적할 수 있다.
        ## => 전역변수 cost에 leaf node가 값을 확정지었으므로,
        ##    바로 위 node는 leaf node자식들마다의 집계처리를 할 수 있다.
        ## => 개별자식마다 return된 상태(global cost)를 가지고 연산한다면, for문 자식바로 아래에서 확인하자.

        ## 8. [타고올라가는 상황 == 자식재귀 끝나고 난 뒤]라면 => 자식또한 자식의 자식에게 누적된 상황이라고 생각하자.
        ## => 자식참여X vs 참여O의 누적비용 중 작은 것을 택하여, 부모의 X/O2가지 경우 모두에 누적한다.
        if cost[child][0] < cost[child][1]:
            ## 부모가 2가지 경우의 수가 있으므로, 각각 모두 누적해야한다.
            cost[node][0] += cost[child][0]
            cost[node][1] += cost[child][0]
            ## 9. 문제는, 부모X 인데 자식들 모두 all X로 누적되느 경우다. => 한번이라도 자식O가 나온다면 누적비용 0이 되어야함.
            ## => 부모X-all자식X를 처리하기 위한 추가비용(최소비용의 자식 1개만 선택)
            ## => 이 경우를 예외처리 하기 위해서는,
            ## => for를 돌고 있는 와중에, 차식들 중 참여비용이 가장 작은 것을 greedy 가변변수로 찾아야한다.
            ## => 더욱이, [이미 참여X비용이 부모X에 더해진 상황]이므로, 참여O로 바꿨을 때의 차이만큼만

            ## 11. greedy를 통해, 자식들 중 (참여비용-이미누적된참여X비용)이 가장 작은 경우 찾기
            ## => 참여X비용이 더 작은데서만 찾아야한다.
            ## => 이미 최소값을 택하는 상황인데.. 참여X가 더 크는 순간 [해당 자식은 참여X가 선택이 안되서] 나가리가 되기 때문이다.
            min_extra_cost = min(min_extra_cost, cost[child][1] - cost[child][0])

        else:
            cost[node][0] += cost[child][1]
            cost[node][1] += cost[child][1]
            ## 12. for자식들 if else에서.. 하나라도 참여해는 경우만 else를 방문한다.
            ## => 참여O가 더 작은 자식이 발견되는 순간 => 그 경우의 수가 선택되므로 =>
            ##    부모입장에서는 X - X를 고려할 필요가 없게 된다.
            ##   => X-X예외처리를 위한 추가비용을 0으로 재할당해야한다. (더 작은비용이 안나올 듯?)
            min_extra_cost = 0 # 사실상 가장 작은 값이라 더이상 업데이트 안된다.

    ## 13. 부모X- all 자식X를 처리하기 위한 추가비용(최소비용의 자식 1개만 선택)을 부모X에 누적해준다.
    ## 끝처리인데, return누적(꼬리재귀 or 집계재귀)가 아니라 global로 처리한다면 딱히 return해줄 필요 없다.
    cost[node][0] += min_extra_cost










if __name__ == '__main__':
    ## 매출하락 최소화: https://school.programmers.co.kr/learn/courses/30/lessons/72416
    sales = list(map(int, input().split()))
    links = []
    for _ in range(9):
        links.append(list(map(int, input().split())))

    #### 개념
    ## (1) tree는 순회하며 [1][자신을 기록]할 수 있고, leaf에서 return하면서 값을 누적연산할 수 있다.
    ## -> global 매핑배열에 node별[1차원] 참석여부에 따른 비용[2차원]을 순회하며 기록하되
    ## => [2][return해오면서 자신의 비용 저장공간에  자식들의 비용을 누적]한다.

    ## (2) 팀별 최소1명 참여 & 최소비용 -> 전체 경우의 별 (O<-O(min) O<-X X<-O(min) X<-X최소값을 구하고, XX의 경우를 제거한다.
    ##    실제로 제거하진 않고 부모X <- 자식X 에 대해, 자식들 중 최소 추가비용(참여-비참여)을 더한다.
    ##    -> 자식의 비참여도 비용이 있다. 누적된 상태기 때문이다.(자식의 자식은 참여한 경우)
    ## => 이렇게 X - X의 경우만 처리하면서, 모든 경우를 누적해서 root node로 경우의 수를 다 계산한다.

    ## 1. graph
    graph = [[] for _ in range(len(sales))]
    for link in links:
        u, v = link
        graph[u - 1].append(v - 1)

    ## 2. 각 node별/참여O,X시 비용을 저장할 2차원 배열을 만들고 -> 순회하며 기록한다.
    ##    번호는 1부터 주어지지만, 0부터 쓰기 위해 정보에서 -1하고 쓴다.
    ##   누적되는 2차원 배열의 초기값은 0으로 주면되는데,
    ##   => 2차원index를  0/1 2개의 인덱스를 쓰는 2차원배열은 [0] * 2 == [0, 0]
    cost = [[0, 0] for _ in range(len(sales))]

    ## 3. tree순회는 dfs재귀지만, 명칭은 traversal로 하자.
    ## -> cost의 자신의 비용정보가 있는 sales의 기록을 남겨야하므로, 들고 들어간다.
    traversal(sales=sales, node=0)

    ## 14. traversal(순차:global에 자신기록/역순:자식들O/X에 대해 부모O/X비용 누적)
    ##  => 이 끝났다면, cost 2차원배열에는 0번node에 모든 경우의 수를 누적한 것이 쌓여있다.
    ##  => [0][0] : 0번node가 참석X면서, 자식들 중 1개는 참여된, 최소비용
    ##  => [0][1] : 0번node가 참석O면서, 자식들 중 1개는 참여된, 최소비용
    ##  => 0번이 참여안해도 이미 예외처리가 되어있기 때문에 둘중에 최소값을 처리하면 된다.
    print(min(cost[0][0], cost[0][1]))




