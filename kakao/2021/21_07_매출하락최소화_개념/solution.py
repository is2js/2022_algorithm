import sys 
 
input = sys.stdin.readline 
 
 
if __name__ == '__main__':
    ## 매출하락 최소화: https://school.programmers.co.kr/learn/courses/30/lessons/72416
    sales = list(map(int, input().split()))
    links = []
    for _ in range(9):
        links.append(list(map(int, input().split())))

    #### 개념
    # 예제4번을 보면, 1개의 팀에서 2개의 팀원이 참석해도 괜찮다 -> 나는 팀별visited만 썼다
    #### tree는 재귀호출로 탐색한다 -> 재귀호출이기 때문에 dfs다
    #### 각 leafnode마다 참석O/참석X의 비용을 기록한다.
    #### 각 node별 2가지의 경우를 기록하려면, 배열[node][node별 정해진종류의 경우의수]를 차원에 기록할 수 있다.
    #### ex> cost[7][0] -> 참석했을때의 비용 저장 / cost[7][1] -> 참석했을때의 비용
    #### => leaf node부터 시작해서, 윗방향으로 cost2차원배열을 채워나갈 것이다.
    #### => 지문에는 1부터 시작하는데, 우리는1씩빼서 사용한다
    #### 그림: https://raw.githubusercontent.com/is3js/screenshots/main/image-20220926011058217.png

    #### root node부터 내려가면서 cost배열을 채우되, 누적비용 계산은 leaf node부터 올라가면서 한다?
    #### 그림: https://raw.githubusercontent.com/is3js/screenshots/main/image-20220926011726591.png
    #### leaf까지는 각각의 node가 0, 1인 경우의 수에서 비용만 기입한다.
    #### => leaf node부터는, return해서 돌아가면서 비용을 누적할 것인데
    ####    반환받은 자식node에 대해서,[ 자식이 참석O or 참석X 둘중에 작은 비용]을 더한다.
    ####    그림: https://raw.githubusercontent.com/is3js/screenshots/main/image-20220926012029250.png

    ####   이 때, 자식을return받은 부모node는 책임이 있다.
    ####   => 누적계산은 돌아가면서 윗방향으로 하며, 자식부터 체킹하는데
    ####      (1) 부모가 참석한 경우 -> [자식의 참석여부는 상관없이] 둘중에 최소값만(자식 참석X로 비용0)만 더하면 된다.
    ####                              =>  부모O비용 + 0 / 부모X비용(0) + 0
    ####         하지만 이상태로 있으면, 부모X비용(0) + 0 => 둘다 참석하지 않은 것으로 유지된 상태다.
    ####         그림: https://raw.githubusercontent.com/is3js/screenshots/main/image-20220926021224794.png
    ####      (2) 부모가 참석X인 경우 -> [자식들 중 1개는 무조건 참석]해야한다
    ####                              => 부모X비용(0) + 0 에서 + [차식 참석비용]을 더해줘서 결정해야한다.
    ####         그림: https://raw.githubusercontent.com/is3js/screenshots/main/image-20220926021224794.png
    ####   => 부모참석X비용 = 0 + return되는 자식최소비용(자식X비용) 0 + 자식들 중1개 필참비용(자식O비용)
    ####      부모참석O비용 = cost + return되는 자식최소비용(자식X비용) 0
    ####   my) 재귀가 역방향으로 올라감에 따라 [직접적인 자식비용] 뿐만 아니라 [후손들로부터 누적된 비용]인 (return되는 자식 최소비용 택1)을 해야하나보다

    #### 이제 root node로 올라간다고 치자.
    #### (1) 해당자식의 참석O/참석X비용 중 택1하여 [return되는 최소비용]을 더한다.
    ####   그림:https://raw.githubusercontent.com/is3js/screenshots/main/image-20220926021917837.png
    ####   => 그전의 부모에서 구해진 해를 바탕으로 더 큰(더 위쪽) 부모의 해를 구하고 있기 때문에 DP다

    ####  자식이 3개인 D그룹을 경우 살펴보자.
    ####  (1) 값이 추가될 것이 없는 leafnode는 값이 정해진다.
    ####  (2) 부모node는 각 자식마다, return되는 최소비용을 더한다.(자식들마다 선택X들을 다 더함)
    ####     -> 부모참석O의 경우 확정된다. 부모가 참석한 경우, 자식들은 참석안하는 것이 맞으므로 17 + 000
    ####     -> 부모참석X의 경우, 자식들 다 참석X만 return된 상태 0+ 0+0+0는 아직 해가 구해진 상태가 아니다.
    ####        그림:https://raw.githubusercontent.com/is3js/screenshots/main/image-20220926022248634.png
    ####        -> 첫번재 자식을 참석시킨다면? 14
    ####        -> 2번재 자식을 참석시킨다면? 16
    ####        -> 3번재 자식을 참석시킨다면? 17 이 들어간다
    ####        => 이 경우, 부모참석X + 자식들의 최소비용들 더하기 + [자식들중 참석O시 가장 작은 비용]을 추가로 더해
    ####                    0           000                 + 14가 정해진다
    ####  (3) 부모O: 17, 부모X:0+000+14로 14의 비용이 확정된다.
    ####      그림: https://raw.githubusercontent.com/is3js/screenshots/main/image-20220926022701857.png

    #### 다시 그 부모의 경우를 생각해보면
    ####    부모참석X: 0   0(반대쪽자식)+(위에서구한자식의 최소값)14 + 2명의 자식 들 중 택1 최소값 => 17이 아니라 +3으로 17을 맞춰준다.
    ####   =========> return되는 자식들의 누적최소값 + [ 자식들마다 중 자식참석O - 자식참석X를 비교해서, 그 차이만큼만 더 더해주면] 해당 자식을 참석시키는 경우가 된다.
    ####             A에 참석X에 대해서, B가참석시 (28-13)=15증가 / C가참석시(33-17)=16증가/D가참석시(15-0)으로 D를 참석시키며 + 15를 해줘야한다.
    ####           그림: https://raw.githubusercontent.com/is3js/screenshots/main/image-20220926023107736.png
    ####    부모참석O: 19  0(반대쪽자식)+(위에서구한자식의 최소값)14 -> 끝

    #### my) 탐색시 모든node 중 일부node 조건에 따라 참석 => 모든 node들의 O/X를 기록하되, 조건에 의해 확정되는 node들(leaf node)들부터
    ####     차례대로 dp형식으로 누적해서 올라간다.
    ####  node마다 참석O/X를 기록할 땐, 1차원index엔 node / 2차원index에는 O/X(정해진종류)시의 개별비용을 최초로 기록해놓고
    ####  확정된 node부터 출발하여 -> 다음node에는 직전node의 O/X에 따른 누적계산을 [조건에 맞춰서] 비용을 누적해나간다


    # https://www.youtube.com/watch?v=qilOh6qkDXo&list=PL6YHvWRMtz7DqcupeeJ1FOTXjZmJPu_XC&index=7
    # https://school.programmers.co.kr/learn/courses/30/lessons/72416





