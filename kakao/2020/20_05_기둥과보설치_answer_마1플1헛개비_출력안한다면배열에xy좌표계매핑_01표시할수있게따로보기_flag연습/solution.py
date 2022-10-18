import sys

input = sys.stdin.readline

def check_pillar(x, y):
    ## 5. (1)그 좌표가 y가 0인 바닥이라서 설치할 수 있다.
    # if y == 0:
    #     return True
    ## 6. 또, 설치할 수 있는 경우는? 바로아래가 기둥시작점이 있으면 설치할 수 있다.
    if y == 0 or Pillar[x][y - 1]:
        return True
    ## 7. 또, 바로왼쪽에 보시작점이 있으면 설치할 수 있다.
    # if Bar[x-1][y]:
    #     return True
    ## 8. 근데, -1을 다는 순간, 좌표계가 음수가 될 수 있기 때문에 x>0검사를 해줘서and 통과해야한다.
    ##    위에서 y-1은, y==0가 아닐대의 조건이 포함된 것이므로 검사안해줘도 됬었다.?? (주어진 값은 0~양수)
    ##    => 0부터 시작하는 인덱스에 => -1표시가 나온다면, 0만 아니면 되므로 > 0 을 체크해준다.
    # if x > 0 and Bar[x-1][y]:
    #     return True
    ## 9. 보의 한쪽끝에 있어도 되니, 보의 왼쪽끝에 있어도 된다 => 보는 시작점에서 오른쪽으로 나아가니
    ## => 보의 시작좌표에 있어도 된다는 말이다.
    if (x > 0 and Bar[x - 1][y]) or Bar[x][y]:
        return True
    ## 10. 그외에는 기둥설치할 수없으므로 False반환한다(if 성공조건시에만 early return 그외처리는 맨마지막에 return)
    return False


def check_bar(x, y):
    ## 16. 보 바로 밑에 기둥(시작점)있으면 설치가능 (보의 시작점에 기둥끝)
    # if Pillar[x][y-1]: # my) -> -1이 나온 순간, y가 0부터 시작하는지보고, 0부터 가능하면 조건을 달아준다.
    # if y > 0 and Pillar[x][y-1]:
    #     return True
    ## 17. 보의 오른쪽 아래에 기둥(시작점)이 있어도 가능하다.(보의 오른쪽에 기둥끝이 잇는 것)
    # if (y > 0 and Pillar[x][y-1]) or Pillar[x+1][y-1]:
    #### 18. +1이 나올때도 범위체크를 해야한다. x의 가동범위는 0~5이므로 x+1이 6이 안되려면 x+1 < 6 x<5의조건이 있어야한다
    # if (y > 0 and Pillar[x][y-1]) or Pillar[x+1][y-1]:
    # if (y > 0 and Pillar[x][y-1]) or (x < 6 and Pillar[x+1][y-1]):
    #### 19. 왼쪽범위검사는 힘들지 몰라도 [+1 검사에 대한, 배열 오른쪽에는 헛개비를 실시간추가] 가능하다.
    #### => 전체배열의 크기를 +1 더줘서, 헛개비 0 을 만들어놓으면, x+1은 항상 indexerror안나는 범위가 된다.
    #### => 오른쪽 헛개비는 항상 0이게 되어, 건축물이 없는 상황으로서, 거기에 기둥 잇는 조건에 위배되어 결과에 영향을 안주게 된다.
    #### => Pillar, Bar의 우측에 헛개비를 주고 오자.
    if (y > 0 and Pillar[x][y - 1]) or Pillar[x + 1][y - 1]:
        return True
    ## 21. 양쪽에 보가 있는 경우 => 왼쪽에 보시작점 && 오른쪽에 보 시작점
    ## => -1은 우리가 0부터쓰는 이상 헛개비를 못주므로, 검사해야한다.
    if x > 0 and Bar[x - 1][y] and Bar[x + 1][y]:
        return True

    ## 나머지는 다 보를 설치할 수없으니
    return False


def can_delete(x, y):
    ## 24. 해당좌표 삭제할 때, 우르르 무너질 수 있는 범위는 ↱ ↔ ↰ 6개가 다이다.
    ## => 기둥이 위로 솟기 때문이다.
    ## => 6개의 점에 대해서, 앞서 구현한 존재가능여부 check_pillar, check_Bar를 이용해서
    ## => 모두 다 살아남지 못하면 삭제가 불가능하다.
    ## => 행렬단위로 탐색하니까, for x범위  for y범위 따로 생각해서 준다.
    for i in range(x - 1, x + 1 + 1):
        for j in range(y, y + 1 + 1):
            ## 25. 확인할때도, 기둥이 있을때만 && 기둥이 존재할 수 있는지 확인한다.
            #### => 우리는 일단, 삭제를 해둔 상태이며, 그 상태일때 존재할 수 있는지 없는지를 보는 것이다.
            ####    만약 먼저 삭제 안했다면, [삭제상태에서 -> 주위가 무너지는지]를 확인못한다.
            ## (if flag 하나라도) 원래 존재하는데, 존재할 수 없게 되면, 삭제불가능이다. -> early retun False
            if Pillar[i][j] and check_pillar(i, j) == False:
                return False
            if Bar[i][j] and check_bar(i, j) == False:
                return False
    ## 다돌았는데도 안걸리면 성공이다
    return True


if __name__ == '__main__':
    ## 기둥과보설치: https://school.programmers.co.kr/learn/courses/30/lessons/60061
    n = int(input().strip())
    build_frame = [list(map(int, input().split())) for _ in range(8)]

    ## 1. 기둥과 보의 정보를 별개로 2차원 배열에 저장해서 각각의 조건을 확인할 수 있게 한다
    ## 2. 인자로 전달할 정보를 줄이기 위해 전역변수로 선언한다

    # Pillar = [[]]  # 기둥
    # Bar = [[]]  # 보

    global Pillar, Bar  # 값을 읽기만 한다면 global안써도 되는데, 재할당 or 값을 입력한다면 global을 써줘야한다
    ## 3. n이 5로 주어져도 0부터 써야해서 n+1로 돌려야한다
    ## => 각각을 0으로 초기화한다.
    # Pillar = [[0] * (n + 1) for _ in range(n + 1)]
    # Bar = [[0] * (n + 1) for _ in range(n + 1)]
    #### 20. 좌표 인덱싱시 +1에 대한 헛개비를 오른쪽에 하나씩 줌 n+1 -> n+2
    Pillar = [[0] * (n + 2) for _ in range(n + 2)]
    Bar = [[0] * (n + 2) for _ in range(n + 2)]
    ####### row, col의 행렬이 아니라 -> 1사평면 좌표계로 사용할 수 있다. 매핑공간만 사용하는 것이다.
    ####### => 출력을 요구하는 문제가 아니면, 2차원배열에 1사평면을 매핑해서 좌표계처럼 사용할 수 있다.

    for x, y, kind, cmd in build_frame:
        ## 종류에 따른 설치/삭제명령부터 확인한다
        #### 설치부터 구현하고 삭제를 구현한다. if 설치가능? 의 check함수가 삭제가능?에 사용되기 때문?
        if kind == 0:  # 기둥
            if cmd == 1:  # 설치
                ## 4. 설치할 수 있는지 check_xxx 슈도메서드를 먼저 작성한다.
                if check_pillar(x, y):
                    ## 만약 설치할 수 있으면, 기둥설치여부를 1로 준다
                    Pillar[x][y] = 1
            else:  # 삭제
                ## 11. 삭제인 경우, 0할당으로  일단 바로 soft delete해놓고 -> canDelete 슈도 check함수를 만든다.
                ## => 이렇게 하는 이유는?
                # Q: 보나 기둥을 먼저 지웠다가 if not candelete 하면 다시 생성해주는 부분이요.  그냥 if candelete 하고 기둥을 지워주니까 에러 뜨더라고요. 왜 그렇게 코드를 짜면  에러가 뜨는지 알 수 있을까요 ?
                # A:
                # checkPillar()하고 checkBar()는 그 위치에 기둥과 보를 설치할 수 있는지 확인해 주는 함수입니다.
                # 특정 위치의 기둥이나 보를 삭제할 수 있는지 확인하는 함수를 따로 만들지 않고,
                # 이미 구현한 checkPillar(), checkBar() 두 함수를 이용해서 canDelete()를 만든 것입니다.
                # canDelete()는 주어진 위치 근방의 기둥과 보가 있을 경우 문제 조건에 맞는지 확인하는 것입니다.
                # 설치할 때는 기둥과 보를 문제 조건에 맞게만 설치하기 때문에, if canDelete()하면 무조건 true만 반환되고 항상 기둥이나 보가 삭제될 것입니다. 따라서 오답이 발생할 수 밖에 없습니다.
                # 제 솔루션에서는 기둥이나 보를 삭제해 보고, 그 상태가 조건에 맞는지 if not canDelete()로 확인해서
                # 문제 조건에 맞지 않다면 삭제할 수 없었던 것이기 때문에 복원해 주는 방식으로 구현한 것입니다.
                ## 문제에서 무조건 존재하는 경우만 삭제명령어가 있다. 현재 위치에 기둥이 서있다는 말이다.
                ## => 구조물이 겹치도록 설치하는 경우와, 없는 구조물을 삭제하는 경우는 입력으로 주어지지 않습니다.
                Pillar[x][y] = 0
                ## 12. check_XXX를 이용하기 위해 canDelete -> if not canDelete로 작성한다.
                ## => 삭제해놓고 -> canDelete로 확인해서 not canDelete삭제할 수 없으면 -> 복원한다.
                ## => my) 삭제해도 나머지것들이 유지되어야 삭제할 수 있다.
                ## => 나머지것들은 check_pillar/check_bar로 확인할 것이다.
                ## => 문제에서는 삭제할 것이 있는 경우에만, 삭제 명령을 준다고 했다.
                ##    이 위치에는 무조건 건축물이 있는 경우
                ## 13.슈도 can_delete를 작성하기 전에 => check_bar도 내부에서 써야하므로
                ##  => 보부터 처리하고 온다.
                if not can_delete(x, y):
                    ## 다시 복원
                    Pillar[x][y] = 1
        ## 14.
        else:  # 보 -> 설치부터 구현한다.
            if cmd == 1:
                # 15. 체크바부터 구현하고 오자.
                if check_bar(x, y):
                    Bar[x][y] = 1
            ## 22. 삭제 -> 먼저 삭제한다.
            else:
                Bar[x][y] = 0
                ## 23. can_delete는 Pillar와 Bar 2개 조건 다 확인하는 것이므로 2개다 공통으로 사용한다.
                if not can_delete(x, y):
                    Bar[x][y] = 1
                    ## can_delete 구현하러 가자.

    ## 25. Pillar와 Board에 존재여부를 다 기록해둔 상태이므로 다시 종합한다
    # return 하는 배열은 가로(열) 길이가 3인 2차원 배열로, 각 구조물의 좌표를 담고있어야 합니다.
    # return 하는 배열의 원소는 [x, y, a] 형식입니다.
    # x, y좌표가 모두 같은 경우 기둥이 보보다 앞에 오면 됩니다.
    ## => 1) x좌표 오름차순 -> 2) y오름차순 순서이므로, 우선순위차원부터 반복문으로 돌린다.
    #     행렬도.. row별 col이다.. x를 빠른것부터 시작하고, 같은x에 대하여 y오름차순할려면, for x for y  순이다.

    # return 하는 배열은 x좌표 기준으로 오름차순 정렬하며, x좌표가 같을 경우 y좌표 기준으로 오름차순 정렬해주세요.
    ## => 같은 x,y에 대해 기둥,보가 모두 있는 경우, 기둥부터 표시하려면 if기둥검사 -> if보검사 순서대로append되게 하면된다.
    answer = []
    for x in range(n + 1):
        for y in range(n + 1):
            if Pillar[x][y]:
                answer.append([x, y, 0])
            if Bar[x][y]:
                answer.append([x, y, 1])

    print(answer)
    pass
