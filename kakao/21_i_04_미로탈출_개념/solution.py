import sys 
 
input = sys.stdin.readline 
 
 
if __name__ == '__main__':
    #### 개념
    ## trap밟을 때 역방향 인접 빈행렬을 만드는 것보다는
    ## => 고정된 인접행렬을 만들고, 행렬을 \ 기준 반전된 index로 뽑아쓰면, 따로 역방향graph를 안만들어도 된다.
    ##    그렇다면 양방향graph로 저장하면 안되나? 3->2정보시 2->3추가???
    ##  => trap발동상태에 따라... 2->3은 못가야하는데, graph for문 돌릴 때, 2->3까지 찍혀버리니 안된다.
    ##  단방향이면서 + trap상태시 사용시 \대각선 반전index

    ## graph가 인접list(원하느 것에 원하는value만 딱딱입력가능)가 아니라
    ## -> 대칭index를 위해 인접행렬을 쓴다면, (원하지 않는곳은 INF, 0으로 초기화)해야한다.
    ## => 자기자신은 0으로 초기화, 표현되지 않는 곳은 INF로 초기화한다.

    #### 방문여부는 visited[node]가 아니라, trap별 발동state__bit를 [traps_state_bit]까지 2차원index로써서 방문여부를 저장한다
    #### => visited[node][state_bit] => [node별] [모든traps별 발동O/X여부] => 2차원index는 traps의 갯수만큼 부분bit를 형성 -> range( 1<<len(traps) )
    ### => index매핑이라면, 모든 경우의 수의 갯수만큼 0부터 매핑시켜놨어야함~!

    #### 함정node의 갯수가 최대 10개라고 표현했기 때문에, bit로 표현할 수 있다.
    #### 다익스트라는 pq에 (cost, node)만 넣는데, 여기서는(cost, node, state_bit)의 상태까지 추가해서 관리한다.
    #### => dfs의 stack파라미터 상태관리를, bfs/다익에서는 pq에 넣는 tuple에 cost외 state도 추가한다.
    #### => node별 trap 발동 여부를  node별로 bit에 매핑하는 것이다.

    #### cost 1 00(2)로 방문한 것과
    #### cost 1 01(2)로 방문한 것은 다르다. node별.. trap발동상태별 방문여부이므로
    # ![image-20220930130129941](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220930130129941.png)
    #
    # ![image-20220930130503332](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220930130503332.png)
    #
    # ![image-20220930130518014](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220930130518014.png)
    #
    # ![image-20220930130604637](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220930130604637.png)
    #
    # ![image-20220930130613984](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220930130613984.png)
    #
    # ![image-20220930130723748](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220930130723748.png)
    #
    # ![image-20220930130738852](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220930130738852.png)
    #
    # ![image-20220930131437421](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220930131437421.png)
    #
    # ![image-20220930131453822](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220930131453822.png)
    #
    # ![image-20220930131601955](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220930131601955.png)
    #
    # ![image-20220930131627397](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220930131627397.png)
    #
    # ![image-20220930131643599](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220930131643599.png)
    #
    #
    #
    # ![image-20220930131847218](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220930131847218.png)
    #### -> (1)현재node가 발동 중이면, graph를 대칭index로 써서 다음것을 찾아야한다.
    ####    => 주의해야할 것은, 도착지점도 trap발동상태인지를 확인해야한다.
    #### -> (2)도착node도 발동 중이라면?, 대칭index를 graph를 써서 자식들을 탐색해야한다.
    #### =>  현재node가 trap발동중이든 vs 도착node시 node가 trap발동중이든
    ####     둘 중 1개node라도 불이 들어와있으면, 대칭index graph를 써야한다.
    ####     but 둘다 켜진 상태면 원래graph
    # ![image-20220930132601294](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220930132601294.png)
    #
    # ![image-20220930132609470](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220930132609470.png)
    #
    # ![image-20220930132625396](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220930132625396.png)
    #
    # ![image-20220930132657119](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220930132657119.png)

    #### 그렇다면, 2개 node 모두 XX이거나 OO면 => 같은 bit상태라면 원래 graph
    ####                  서로 다르면 => 대칭index graph를 쓰면 된다.
    # ![image-20220930132916459](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220930132916459.png)
    #
    # ![image-20220930132952734](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220930132952734.png)
    #
    # ![image-20220930132957065](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220930132957065.png)
    #
    # ![image-20220930133006333](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220930133006333.png)
    #
    # ![image-20220930133014694](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220930133014694.png)
    #
    # ![image-20220930133121983](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220930133121983.png)
    #
    # ![image-20220930133133899](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220930133133899.png)
    #
    # ![image-20220930133144398](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220930133144398.png)
    #
    # ![image-20220930133155523](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220930133155523.png)
    #
    # ![image-20220930133232758](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220930133232758.png)
    #
    # ![image-20220930133240772](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220930133240772.png)
    #
    # ![image-20220930133249224](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220930133249224.png)
    #
    # ![image-20220930133302048](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220930133302048.png)
    #
    # ![image-20220930133310154](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220930133310154.png)
    #
    # ![image-20220930133319456](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220930133319456.png)
    #
    # ![image-20220930133516214](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220930133516214.png)
    #
    # ![image-20220930133525690](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220930133525690.png)
    #
    # ![image-20220930133536532](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220930133536532.png)
    pass 
