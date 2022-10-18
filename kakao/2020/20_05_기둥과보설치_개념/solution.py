import sys 
 
input = sys.stdin.readline 
 
 
if __name__ == '__main__':
    ## 기둥과보설치: https://school.programmers.co.kr/learn/courses/30/lessons/60061
    n = int(input().strip())
    build_frame = [list(map(int, input().split())) for _ in range(8)]

    #### 개념
    ## 1. 기둥은 위로 바닥위or보의한쪽끝부분or기둥위, 보는 오른쪽으로 -> 기둥위or양쪽끝이 다른보와 연결
    ## 2. n이 5로 주어졌으면, 우리가 쓸 수 있는 좌표는 012345로 6개다
    ## 3. 건축물이 존재할 수없는 상태면, 건축물을 삭제를 해야한다.
    ## 4. 각 모서리를 좌표로 나타내야하며
    ##    기둥과보를 같은평면에 기둥0보1로 놓는 것보다는, 각각에 평면에 따로 표현하는 것이 더 좋다
    ##     기둥평면에 기둥있으면 1 없으면0  / 보평면에 있으면1 없으면 0
    ##    => 각각의 조건을 확인해야하므로, 각각의 평면에 0과1로 나타낸다.
    ##    좌표평면에 기둥/보를 나타날때는, 시작좌표에 1로 나타낸다
    ##  https://raw.githubusercontent.com/is3js/screenshots/main/image-20221009145727870.png
    ## (4,2) 자리에 보를 시작하는데 오른쪽에 기둥이 있으니 설치할 수 있다.
    # https://raw.githubusercontent.com/is3js/screenshots/main/image-20221009150122425.png
    ## (3,2) 자리에 보를 시작하는데,  시작자리/오른쪽자리 모두 보가 있으므로 가능하다
    ## 5. 맨 마지막에는 기둥배열+보배열을 동시에 확인하면서, 답으로 써준다.
    ## https://raw.githubusercontent.com/is3js/screenshots/main/image-20221009150240258.png
