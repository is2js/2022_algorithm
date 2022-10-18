import sys 
 
input = sys.stdin.readline 
 
 
if __name__ == '__main__':
    ## 블록이동하기: https://school.programmers.co.kr/learn/courses/30/lessons/60063

    #### 개념
    ##  문제는 1,1부터 우리는 0,0부터
    ## 시작은 0,0  0,1로 시작
    ## 회전축은 왼쪽이 될수도, 오른족이 될 수도 / 회전할때 모서리부분은 0이 되어야 회전 가능 /
    ## => 최단시간 문제라서 bfs를 활용할 것이고, 상하좌우 이동 + 같은 1초 걸리는 회전도 같이 진행될 것이다.
    ##   회전 조차, 다음 움직임 중 1개
    ## => 1칸이 아니라서, 위치정보 저장이 까다롭다. => 2개이상의 좌표를 동시에 방문체크할 땐, 방향성이 필요하다.
    ## => 각 칸에 중심을 바라보는 방향성을 준다.
    #     https://raw.githubusercontent.com/is3js/screenshots/main/image-20221016144237529.png
    ## => 1칸씩 방문이라면, board와 똑같은 n by n 의 visited array를 잡지만
    ##    각 칸마다 방향성을 잡아서 n by n 에 차원을 하나 더 잡아서 [n][n][4]개의 visited array를 사용한다.
    ##   => 각 좌표[n][n]마다 [방문여부 && 방향성을 기록][4]하는 것 => up 0 / right 1  down 2 left 3
    #     https://raw.githubusercontent.com/is3js/screenshots/main/image-20221016145253805.png
    ##   => 각 방향성마다, 4개의 좌표평면[n][n]이 생기는 개념이다.
    #     https://raw.githubusercontent.com/is3js/screenshots/main/image-20221016145356925.png
    ## [n][n][4]는 n by n 이 4개씩 생긴다고 볼 수 있다.
    ## => 원래는 [i][j]각 좌표마다 0123 4개의 저장공간이 생긴다고 봤었는데
    ##    반대로.. [4]개의 [n][n]좌표가 존재한다고 생각할 수도 있다. => [n][n]를 묶어서, 행렬별 4개의 공간이 생긴다.

    ## 예시 시작
    # ![image-20221016145444688](https://raw.githubusercontent.com/is3js/screenshots/main/image-20221016145444688.png)
    #
    # ![image-20221016145850643](C:\Users\is2js\AppData\Roaming\Typora\typora-user-images\image-20221016145850643.png)
    #
    # ![image-20221016145918372](https://raw.githubusercontent.com/is3js/screenshots/main/image-20221016145918372.png)
    #
    # ![image-20221016145938509](https://raw.githubusercontent.com/is3js/screenshots/main/image-20221016145938509.png)
    #
    # ![image-20221016145952245](https://raw.githubusercontent.com/is3js/screenshots/main/image-20221016145952245.png)
    #
    # ![image-20221016150543008](https://raw.githubusercontent.com/is3js/screenshots/main/image-20221016150543008.png)
    #
    # ![image-20221016150633314](https://raw.githubusercontent.com/is3js/screenshots/main/image-20221016150633314.png)
    #
    # ![image-20221016150652133](https://raw.githubusercontent.com/is3js/screenshots/main/image-20221016150652133.png)
    #
    # ![image-20221016150700813](https://raw.githubusercontent.com/is3js/screenshots/main/image-20221016150700813.png)
    #
    # ![image-20221016150732746](https://raw.githubusercontent.com/is3js/screenshots/main/image-20221016150732746.png)
    #
    # ![image-20221016150745908](https://raw.githubusercontent.com/is3js/screenshots/main/image-20221016150745908.png)
    #
    # ![image-20221016150759532](https://raw.githubusercontent.com/is3js/screenshots/main/image-20221016150759532.png)
    #
    # ![image-20221016150809322](https://raw.githubusercontent.com/is3js/screenshots/main/image-20221016150809322.png)
    #
    # ![image-20221016150816362](https://raw.githubusercontent.com/is3js/screenshots/main/image-20221016150816362.png)
    #
    # ![image-20221016150829748](https://raw.githubusercontent.com/is3js/screenshots/main/image-20221016150829748.png)
    #
    # ![image-20221016150836703](https://raw.githubusercontent.com/is3js/screenshots/main/image-20221016150836703.png)
    #
    # ![image-20221016150849165](https://raw.githubusercontent.com/is3js/screenshots/main/image-20221016150849165.png)
    #
    # ![image-20221016150904955](https://raw.githubusercontent.com/is3js/screenshots/main/image-20221016150904955.png)





   pass
