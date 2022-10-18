import sys

input = sys.stdin.readline


def match(arr, key, rot, row, col):
    ## 8. 정사각행렬의 key크기는 미리 저장해놓고 시작한다.
    n = len(key)
    for i in range(n):
        for j in range(n):
            ## 9. 회전index 0은 회전이 없는 상태다. row, col을 시작좌표해서 그대로 key를 복사한다
            ## => 큰영역 0, lock반영돌기1에  key의 값들을 += 누적더하여,복사한다.
            ##    돌기가 겹치면 2가 된다.
            if rot == 0:
                arr[row + i][col + j] += key[i][j]
            ## 10. 90도 회전하는 경우, [첫행으로 어디행or열이 시작되어야하는지]하면 된다.
            ##  => key의 0번째 열이 역순으로 첫행에 와야한다. (cf) 역순인덱스는 len-1-i or python -(i+1) 이다)
            ##  [row자리 생각] 생각1: (시작) 0행 자리에 n-1행이 와야하고 -> 생각2: (진행) 0행에서 열값이 증가할 수록(col(j)가 진행될 수록), 행이 올라간다(row는 ↑ 거꾸로 진행된다.)
            #   =>   n-1(초기값)  - j (어차피i,j는 0부터 시작이라 초기값 맞추기 생각은 없이, 부호만 생각하면 된다.)
            ##  [col자리 생각] (시작)0열 자리에 0열이 와야하고 [0]-> (진행) 행값이 증가할수록 다음열을 봐야한다 -> [0+i]
            elif rot == 1:
                ## my) (0,0)시작자리 대신 초기값 (n-1,0)으로 시작한다.
                ##     열이 진행될때마다(변수) -> [행](index)이 거꾸로 간다[n-1  -j]
                ##     행이 진행될때마다(변수) -> [열]은 정상진행된다 [0   +i]
                arr[row + i][col + j] += key[n-1-j][i]
            ## 11. 180도 회전하는 경우
            ## [1] (0,0)자리에 (n-1,n-1)이 와야한다 => key[n-1 +?][n-1 +?]
            ## [2] ??에 대해서, 열이 진행할때마다 -> [열]이 거꾸로 진행된다. -j => [열]은 [초+][초 -j]
            ## [3] ??에 대해서, 행이 진행될때마다 -> [행]이 거꾸로 진행된다. -i => [행]은 [초-i][초+?]
            ## => 앞이 i, j를 변수를 결정하고 -> 뒤가 어느index에 놓일지를 결정한다.
            elif rot == 2:
                arr[row + i][col + j] += key[n-1 -i][n-1 -j]
            ## 12. 270회전은 반시계 90도와 같다
            ## => [1] 어디가 (0,0)으로 와야하는지를 생각한다. (0,n-1)이 (0,0)으로 와야한다.
            ##   열 진행시 -> 행이 증가한다[0 + j]
            ##   행 진행시 -> 열이 감소한다[n-1 -i]
            elif rot == 3:
                arr[row + i][col + j] += key[j][n-1 -i]


def check(arr, offset, n):
    ## 14. arr에서 초기좌표가 offset, offset, 길이는 n인 lock영역을 돌면서 1로만 구성되는지 확인한다.
    for i in range(n):
        for j in range(n):
            ## 하나라도 1이 아니면 탈락 => flag안걸리고for문을 다돌면 성공
            if arr[offset + i][offset + j] != 1:
                return False
    return True


if __name__ == '__main__':
    ## 자물쇠와 열쇠:https://school.programmers.co.kr/learn/courses/30/lessons/60059
    key = []
    for _ in range(3):
        key.append(list(map(int, input().split())))
    lock = []
    for _ in range(3):
        lock.append(list(map(int, input().split())))

    #### 개념
    # 1개의 2차원 배열에 좌물쇠 먼저 복사 -> key를 우측하단 1개를 lock의 좌측상단에 걸치는 것으로 시작해서
    # 그림: https://raw.githubusercontent.com/is3js/screenshots/main/image-20221006032611665.png
    # => 겹치는 부분을 원소들의 합으로 파악한다. 돌기 + 돌기라면 2다
    # (1) 겹칠 수 있는 모든 경우를 다 나타낼 수 있는 큰 영역에 2차원 배열을 먼저 만든다.
    # https://raw.githubusercontent.com/is3js/screenshots/main/image-20221006032849576.png
    # (2) 좌물쇠는 큰 영역의 중앙에다가 복사해놓는다.
    # https://raw.githubusercontent.com/is3js/screenshots/main/image-20221006032912824.png
    # (3) 키를 복사해서 놓을때는, 큰 영역에 더하는 형식으로 겹치게 한다.
    # (4) 움직일때마다 90도씩 회전하면서 겹치게 해서 확인한다.
    # (5) 매번 확인할 부분은, 좌물쇠의 영역만 확인하며 빈부분이었던 0이 1로 채워지는지 보면된다. -> 하나라도 2나 0이 있으면 탈락이다.

    ## https://raw.githubusercontent.com/is3js/screenshots/main/image-20221006033750911.png
    ## 1. 큰 영역은 좌상단 0,0 시작이다. 가운데 좌물쇠를 넣으려면
    ## 0,0에서 떨어지는 길이만큼 알아야 lock의 시작좌표를 안다-> offset으로 변수를 잡아놓는다.
    ## => 결국엔 0,0에 key를 놓았을 때, key우측하단에 1개 겹치는 부분
    ##    즉, [key의 마지막인덱스, 마지막인덱스]  => len(key)-1, len(key)-1이 lock의 시작좌표가 된다.
    offset = len(key) - 1  # 0 + len(key) - 1

    ## 2. 모든 경우의수를 만들기 위해, 탐색할 key의 끝좌표를 row, col별 만들어내야한다.
    ## row를 key가 우상단에서 1개 겹칠때까지 내려가야한다. 다 내려갔다고 가정하면,
    ## key의 우상단좌표(0,2)가 (0 + offset(len(key)-1) + len(lock) - 1, 2)까지 내려간다.
    ## https://raw.githubusercontent.com/is3js/screenshots/main/image-20221006035606462.png
    ## my) 현재부터시작하는 window길이값을 더하면, 윈도우바로 바깥이므로 window 끝으로 이동하려면 [현재좌표+window-1]
    ##     좌표이동생각할 때, 현재좌표로부터 window를 그리고, window끝인지/window바깥시작인지를 생각해보자.
    for row in range(offset + len(lock) - 1 + 1):
        ## 3. 열의 좌표도 큰 영역 중 lock과 1개 걸칠때까지 이동했다고 가정하면
        ##    offset + len(lock) - 1 까지 이동한다.
        for col in range(offset + len(lock)):
            ## 4. 이제 매번 90도 씩 돌려봐야한다. -> 총 4번 반복이 필요하다.
            for rot in range(4):
                ## 5. 이제 가장 큰 영역arr을 만들어야하는데, 최대 20/20이므로
                ## => 가로 20|20|20에서 겹치는 부분 1개씩 빼면 58이면 충분하다
                ##   더해서 겹치게 할 것이므로 초기값을 0으로 잡는다.
                arr = [[0 for _ in range(58)] for _ in range(58)]
                ## 6. 좌물쇠lock를 복사해서, 큰영역arr에 넣어놓는다.
                ## => offset만큼 떨어진 위치에 복사해놓는다.
                ##    복사할 lock의 원소들을 돌며, i+offset, j+offset 좌표로 재할당하면
                ##    평행이동시킨 것을 복사하는 개념이다.
                ## => lock은 0,0기준으로 돌고, arr는0,0기준에서 +offset한만큼에 그리면 [평행이동복사]
                for i in range(len(lock)):
                    for j in range(len(lock)):
                        ## my) offset은 i,j순회에 대해 기준점을 0,0에서 os,os으로 이동시켜서 진행하게 해준다.
                        arr[offset + i][offset + j] = lock[i][j]
                ## 7. 매 회전시마다, (1)새로운 큰영역arr 생성 + (2) lock가운데복사해놓고
                ##    -> 방향으로 1칸씩 이동후 / ↓ 으로 한칸 내려간다
                ## => 매번 (1) (2)는, row행을만들고/col을만들고/rotate반복시마다 /매번 arr+lock을 초기화하는 상태로
                ##    match()함수를 통해 회전하여 복사해놓고, 비교한다?! (arr는 lock이 들어간 것)
                ##   => 필요한 모든 것을 for 인자들을 모두 넣어준다.
                ##   => 여기서 [row, col는 움직이는 key의 시작좌표]라 생각한다.
                match(arr, key, rot, row, col)

                ## 13. 현재 arr에 회전된 key까지 올려둔 상태다. => 이제 lock영역만 확인해서 모두 1인지
                ##    혹은 0으로 빈곳은 없은지, 2로 돌기끼리 만난부분이 없는지 check함수로 확인한다.
                ## => for + if 성공flag시만 early return이다.
                ## => 다돌아도 안걸리면.. for문 바깥에서 실패처리한다.
                if check(arr, offset, len(lock)):
                    print(True)
                    exit()
    ## 13-2. for 다돌았는데도 성공못해서 빠져나온 경우 -> False
    print(False)




