import sys 
 
input = sys.stdin.readline 
 
 
if __name__ == '__main__':
    ## 메뉴리뉴얼: https://school.programmers.co.kr/learn/challenges?order=recent&page=1&partIds=20069
    orders = input().split()
    course = list(map(int, input().split()))

    #### 입력에서 WXA처럼 순서가 정렬되어있지 않다
    #### => 조합을 풀어낼 때는, 미리 순서를 정렬하여 고정시켜 풀자

    #### 개념
    # 그림: https://raw.githubusercontent.com/is3js/screenshots/main/image-20220922144413510.png
    # 각 주문당 nC2, nC?조합을 만들고 ->
    # 주문갯수(숫자->index)별 value에 food_maps(menu:누적count) / max_count(배열)를 매핑할 것이다.
    # foodmap은 key = menu, value = 누적count로 저장
    # => foodmap을 누적하면서, 매번 현재index(course갯수)에 대한 max값을 확인해서 업데이트한다
    # => foodmap을 추가할때마다, 그 전체에 대한 max_count를 greedy로?
    #그림: https://raw.githubusercontent.com/is3js/screenshots/main/image-20220922145259047.png

    # 조합은, api없이 순서고정해놓고, 재귀호출 2node로, 앞에서부터position별로 선택O/X로 조합을 만들어낼 것이다.
    ## => api는 뽑는갯수k를 지정해줘야하지만, 재귀로 찾아나가면 선택하고 안하고에 의해 알아서
    ##    1개도선택X ~ 다 선택한 경우의수를 다 탐색하게 된다.

    ## index별(조합단품갯수k) foodmaps + maxcount가 맾이되어있는데
    ## => 문제에서 주어지는 course의 조합수 -> index -> foodmaps를 순회하면서 max_count와 동일한 count를 가진것들을 다 골라낸다.
    ## => max_count1개만 추출하는 게 아니라, 같은 여러개를 탐색해야한다면,
    ##   (1) 누적저장시 max_count를 실시간으로 max_count를 업뎃하며 구해놓는다.
    ##   (2) 구해진 max_count를 기준으로, 처음부터 순회하여 같은 것을 골라낸다
    ## => 만약 이렇게 안한다면 저장 -> max_count구하기 -> max_count와 같은 것들 다 골라내기 3번의 과정이 생긴다.
    #### => 처음부터 create(삽입)해야한다면, 삽입하면서 집계값을 미리 구해놓고 => 집계값과 같은 것들을 1번만 순회해서 골라내자
    # https://raw.githubusercontent.com/is3js/screenshots/main/image-20220922145943295.png

    ####
