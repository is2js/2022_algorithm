import sys 
 
input = sys.stdin.readline 
 
 
if __name__ == '__main__':
    ## 외벽점검: https://school.programmers.co.kr/learn/courses/30/lessons/60062
    n = int(input().strip())
    weak = list(map(int, input().split()))
    dist = list(map(int, input().split()))

    ## my)
    ## 몇명을 선택할지 모르고, 순서는 안중요하므로 조합이다.. => 순서 중요하다
    ## => 어떤 친구를 먼저 시작했느냐에 따라, 정복된 취약점 등이 달라서 다른 경우기 때문에 순열이다.
    ## 시작점을 선택하는 것은 경우의 수??
    ## 각 지점마다 있고없고를 bit로 나타낼 순 있는데,  / 도는 방향도 state값으로 나타내야한다?

    #### 개념
    # 1. 친구의 시작위치는, 취약지점에서 시작해야한다.(취약지점 없는 곳을 이동하는 것은 의미가 없어서)
    # 2. 친구는 최소한으로 써야하기 때문에, 다 할 것이 아니라, 가장 멀리갈 수 있는 친구들부터 써야한다 (정렬도 해줬었음..)
    # 3. 1에서부터 4인 친구가 5로 갈 때, 반시계방향도 생각할 수 있지만,
    #    1->반대를 생각할진 몰라도, 5->1의 구간은 똑같기 때문에 반시계를 생각할 필요는 없다. => 진행방향은 시계방향으로 일단 고정하고 시작한다.

    # 4. 모든 친구들을 순열로 하나씩 쓴다. -> dist배열의 순열을 구해서 하나씩 다 시도한다
    # => dist == 친구들을 순열로 구성해서, 어느친구들부터 출발할지에 따라 모든 경우의 수를 나열한다
    # => 굳이, dfs로 시작할 필요없다? 일단 다 나열해놓고, case1~2개를 생각해본다.
    #    MinCnt = INF로 두고 1234 부터 4321까지 다 시도한다.
    #   https://raw.githubusercontent.com/is3js/screenshots/main/image-20221012144717621.png
    # 5. 문제는, 출발취약지점1에서 시작해서, 중간에서 끝났다면, 다음친구는 그부터가 아니라, 다음 취약지점부터 시작하게 해야한다 한다
    # => 이미 정복된 weak를 제외한 그 다음 순서의 weak에서부터 출발
    # https://raw.githubusercontent.com/is3js/screenshots/main/image-20221012144802494.png
    #  -> 하다가 남은게 있으면, 다음친구를 사용하며, 다음 취약점에서 시작해야한다
    # https://raw.githubusercontent.com/is3js/screenshots/main/image-20221012144930696.png

    # 6. 친구출발 순서(dist순열)에 따라, 또 경우의 수가 생기는 것은, 취약지점(weak)의 사용순서이다.
    #   1부터 시작할지, 5부터시작할지.. 또 다르다.
    # https://raw.githubusercontent.com/is3js/screenshots/main/image-20221012145315677.png
    # https://raw.githubusercontent.com/is3js/screenshots/main/image-20221012145347228.png
    # https://raw.githubusercontent.com/is3js/screenshots/main/image-20221012145419960.png

    # 7. 예제2번
    # https://raw.githubusercontent.com/is3js/screenshots/main/image-20221012145653329.png
    # https://raw.githubusercontent.com/is3js/screenshots/main/image-20221012145709302.png
    # https://raw.githubusercontent.com/is3js/screenshots/main/image-20221012145753524.png

    # https://raw.githubusercontent.com/is3js/screenshots/main/image-20221012145942685.png








