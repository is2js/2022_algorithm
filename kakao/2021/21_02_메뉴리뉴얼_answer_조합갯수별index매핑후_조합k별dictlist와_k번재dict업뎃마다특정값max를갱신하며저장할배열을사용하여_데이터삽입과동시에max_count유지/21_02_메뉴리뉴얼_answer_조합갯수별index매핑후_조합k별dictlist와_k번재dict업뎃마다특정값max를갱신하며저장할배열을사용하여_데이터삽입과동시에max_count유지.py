from itertools import combinations
import sys
 
input = sys.stdin.readline 
 
 
if __name__ == '__main__':
    ## 메뉴리뉴얼: https://school.programmers.co.kr/learn/challenges?order=recent&page=1&partIds=20069
    orders = input().split()
    course = list(map(int, input().split()))

    #### (1) 숫자인 조합갯수k별로 dict를매핑하기 위해
    ## =>  dict list를 만들어 사용한다. k는 2 ~ 10까지 이기 때문에, index매핑하기 위해
    ##    총 n+1개의 배열을 속에 빈dict를 집어넣어서 만든다.
    food_maps = [{} for _ in range(10 + 1)]

    #### (2) 각 조합k별을 index로 매핑한 max_count필드를 매핑하기 위해,
    # index와 동일한 배열을 만든다.
    ## => 개별id -> index, 각 필드 => 새로운배열 or 자료구조(dict)
    max_count = [0] * 11

    #### (3) orders를 순회하며 처리
    for order in orders:
        #### 문자열에 대한 뽑는 갯수k는 2부터 문자열의 길이까지 뽑을 수 있으니,
        #### k별로 쪼개서 조합을 탐색한다. 이 때, foodmap과 max_count에 기록해야하니 k별 매핑한 인덱스로 순회한다.
        for k in range(2, len(order) + 1):
            #### 조합은 뽑기전에 정렬하고 뽑자 -> api는 튜플리스트를 반환 -> map의 key에는 string으로 바꿔서 넣어준다.
            for subset in combinations(sorted(order), k):
                #### 튜플은 ''.join으로 string으로 변환해서 카운팅하기 쉽게 1개의 값으로 한다
                key = ''.join(subset)
                #### 현재 조합갯수k -> food_map의 그룹기준이자 max_count의 집계대상그룹을 index로 매핑해놨었다.
                # -> 이미 등록된 적이 잇으면 +=1 counting해준다.
                if key in food_maps[k]:
                    food_maps[k][key] += 1
                    #### k개조합마다, 데이터가 추가될때마다, 매핑된 max_count[k]를 max업데이트해준다.
                    #### greedy를 값만 처리할 경우, 값1개저장공간 = max(값1개저장공간, 새로운 값)로만 업데이트
                    max_count[k] = max(max_count[k], food_maps[k][key])
                ## 최초카운팅이라면 1로 초기화
                else:
                    food_maps[k][key] = 1
                    #### max_count는 현재 count 2개이상만 필요하므로, 1개짜리는 업데이트 안해도된다.

    #### (4) k개 조합마다, foodmaps[k]에는 조합별:count를, max_count[k]에는 k개조합별 최대값을 매핑해놓은 상태다.
    ####    이제 문제에서 주어지는 course(조합갯수)마다, max_count[]갯수와 동일한 것을 다 뽑아온다
    answer = []
    for num in course:
        for subset, count in food_maps[num].items():
            ## 최소 value가 2이상이면서 && max_count[k]랑 동일한 것만 골라낸다.
            if count >= 2 and count == max_count[num]:
                answer.append(subset)

    print(sorted(answer))

