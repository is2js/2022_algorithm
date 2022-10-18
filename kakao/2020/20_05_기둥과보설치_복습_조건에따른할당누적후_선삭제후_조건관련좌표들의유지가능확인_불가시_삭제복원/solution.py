import sys

input = sys.stdin.readline


def check_pillar(x, y):
    if y == 0 or Bar[x][y] or (x - 1 >= 0 and Bar[x - 1][y]) or (y - 1 >= 0 and Pillar[x][y - 1]):
        return True
    return False


def check_bar(x, y):
    ## 8. +1 인덱스가 등장한 순간에는, 배열의 오른쪽에 헛개비를 줘도 되는지 생각한다.
    ## => 0으로 없는 것으로 시작하면 상관없다.
    if (y - 1 >= 0 and Pillar[x][y - 1]) or Pillar[x + 1][y - 1]:
        return True
    if (x - 1 >= 0 and Bar[x - 1][y]) or Bar[x + 1][y]:
        return True
    return False


def can_delete(x, y):
    ## 11. x,y를 지울수 있으려면, ↑기둥 →보의 성격을 생각하면,
    ##    ↓방향에는 영향을 미치지 않고,  ←는 가능성이 있다.
    ## => (x,y)포함 주위6개 좌표가 유지될 수 있는지를 check_pillar, check_bar로 다 확인해서
    ##   하나라도 실패시 탈락이다
    for i in range(x - 1, x + 2):
        for j in range(y, y + 2):
            # if not check_pillar(i, j) or not check_bar(i, j):
            ## 12. 6개 좌표에 대해서, 건축물이 존재할때만 검사해야한다.
            if (Pillar[i][j] and not check_pillar(i, j)) or (Bar[i][j] and not check_bar(i, j)):
                return False
    return True


if __name__ == '__main__':
    ## 기둥과보설치: https://school.programmers.co.kr/learn/courses/30/lessons/60061
    n = int(input().strip())
    build_frame = [list(map(int, input().split())) for _ in range(8)]

    ## 1. 선분은 무시하고, 시작점을 기준으로 좌표평면에 나타낸다.
    ## 2. 출력할 예정이없다면, 좌상단시작 행렬 대신, 좌하단시작 좌표로 매핑해서 쓸 수 있다.
    ## 3. 조건에 맞는 할당(점 복사)를 하는데, 종류가 2개면, 0기둥1보가 아니라 각각이 [1/0 있고없고]로 나타내고 싶다면, [종류별 개별평면]에 나타낸다.
    ## 4. 시작점을 제외하고 길이가 5 -> index차이가 5 -> 끝좌표는 0
    ## => 좌표계는, 1칸당 좌표가 아니라, 모서리당 좌표 => 좌표차 == 길이 == window는 시작점제외한 차이가 5 => 인덱스차이가 5 -> 시작index + 5 == 끝index이다.

    ## 5. 조건에 따라 복사하기 위해, 좌표별 기둥이 있고1/없고0를 나타내기 위한 행렬
    # Pillar = [[0] * (1 + n) for _ in range(1 + n)]
    # Bar = [[0] * (1 + n) for _ in range(1 + n)]
    ## 9. +1 인덱스를 처리하기 위해 헛개비를 1개씩 준다.
    Pillar = [[0] * (n + 2) for _ in range(n + 2)]
    Bar = [[0] * (n + 2) for _ in range(n + 2)]

    for x, y, kind, cmd in build_frame:
        ## 6. 기둥or보별 -> 설치or삭제를 해야하므로 kind를 먼저 탐색? 2x2경우의수라서 상관없다?
        # 조건에 따른 설치
        if cmd == 1:
            if kind == 0:
                ## 7. 조건에 따른 할당은 if check 해놓고 할당한다.
                if check_pillar(x, y):
                    Pillar[x][y] = 1
            else:
                if check_bar(x, y):
                    Bar[x][y] = 1
        # 조건에 따른 제거
        else:
            if kind == 0:
                ## 10. 조건에 따른 설치가 누적된 상태에서 삭제를 함부러 할 수 없다.
                ## => 삭제시 -> 기존 조건에 따른 설치가 유지되는지 확인해야한다.
                ## => 이럴 때 쓰는 것이 (1) 미리 삭제를 해놓고 -> (2) 관련된 설치 건축물들이 유지여불ㄹ [설치가능여부checker]를 재활용하여 확인후 -> (3) 유지안되면서 삭제못해서 복원을 해야한다.
                ## => 설치가능여부check_XXXX() 사용하기 위해서, can_delete()를 작성하고, if not can_delete()시 복원한다
                # if can_delete():
                Pillar[x][y] = 0
                if not can_delete(x, y):
                    Pillar[x][y] = 1
            else:
                Bar[x][y] = 0
                if not can_delete(x, y):
                    Bar[x][y] = 1

    ## 13. 개별평면에 설치여부를 0/1로 해놨으니 종합한다.
    ## => 정렬의 우선순위 높은 것부터 순회하며 종합한다 x>y>기둥>보
    ##    헛개비index를 빼고 2개행렬에 대한 공통인덱스로 순회한다.
    answer = []
    for x in range(n + 1):
        for y in range(n + 1):
            if Pillar[x][y]:
                answer.append([x, y, 0])
            if Bar[x][y]:
                answer.append([x, y, 1])

    print(answer)
