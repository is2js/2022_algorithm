import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## 파라메트릭 서치 -> 이진탐색 활용해야하는 문제
    # -> 최적화 문제(함수의 값을 최대한 높이거나 낮추는 문제)를 -> 여러번의 결정문제(y or no)로 바꾸어 해결하는 기법

    ## 문제: 떡볶이 떡 만들기
    # 일정하지 않는 떡의 길이 -> 한봉지안에 들어가는 떡의 총길이는 절단기로 잘라서 맞춘다.
    # -> 절단기 높이 H -> 보다 짧은 떡은 짤리지 않는다.
    # ex> 19, 14, 10, 17, 절단기 높이 15 => 15, 14, 10, 15
    # 잘린 떡의 길이는 4, 0, 0, 2cm => 손님은 나머지 6cm를 가져간다. => 잘린떡의 총합이 손님이 가져가는 떡길이의 총합 M이다.
    # => 문제: 요청한 총 길이가 M일 때, 적어도 M만큼의 떡을 얻기 위해, 절단기 높이의 최대값?
    # 2초제한 / 떡갯수N, 요청떡길이 M    N<= 100만 / M <=20억 / H는 0 <= <= 10억의 정수
    # 잘리더라도, 떡 높이의 총합은 항상 M이상이므로, 손님은 필요한 양만큼 떡을 사갈 수 있다.

    ## 문제해결 아이디어 -> 적절한 높이를 찾을 때까지 이진탐색을 반복적으로 수행하여, 높이H를 조정한다.
    #  -> H를 높이면 잘린떡의 길이는 줄어들고, H를 낮추면 잘린 떡의 길이는 늘어난다.
    # => 매번 현재 이 높이로 자르면 조건을 만족할 수있는가? 를 확인 -> 조건만족여부(y/n)에 따라서 탐색범위를 좁혀서 해결
    # ==> ex> M만큼을 못 얻으면 H를 낮추어서 더 많이 잘려나가게 해야한다. => 조건에 따라 탐색범위를 조정하여 이진탐색 수행
    # => 절단기 높이는 0 ~ 10억까지의 정수
    # ==> 10억 -> 선형탐색x => 이진탐색으로 N(10*9)보다 줄여야한다. => 10*7보다 큰 탐색범위는 이진탐색을 떠올려야한다.

    ## 과정
    # (1) 첫 떡 19 -> [자를 대상]의 높이값을 [탐색]한다면, 높이1 -> 1번index가 되도록 -> 0을 끼워서 0 ~ 19까지의 인덱스를 탐색한다고 생각한다.
    # => 첫 떡의 중간점mid_index는 s+e//2로서, 짝수개의 중간왼쪽으로서, 9가 잡힌다.
    # => 이 중간점을 [자를 길이]라고 먼저 준다면, => 나머지 떡들의 길이까지 계산해보면 [10, 6, 1, 8] => 25로서 M6보다 크므로 [중간점9]를 저장한다.

    # (2) M==6보다 크므로, 높이를 더 높여 잘린길이의 합을 줄이도록 업데이트 해본다.
    # => h를 [이진탐색 중간점]으로서 탐색한다면, [중간점h를 이동시키는 방법은 src or end를 mid주위로 올겨 mid를 다르게 업데이트]해야한다.
    # => h를 높이려면, 시작점을 기존 h +1로 옮겨야한다.
    # 시작점 10: 끝점 19 -> 중간점 = 14 -> 잘린 떡 [4, 1, None, 3] => 6보다 크다. => 중간점 h14 저장

    # (3) 또 이진탐색으로 중간점+ 1으로 시작점을 높인다. => 2 -> 기록하지 않는다.
    # (4) 중간점을 낮추기 위해서(왼쪽으로 이동)는, end를 안쪽으로 당겨야하므로 mid-1자리로 옮긴다 => 15, 16 => 중간점 15 => [4, 2 ]=> 6 기록

    ## my) 배열의 index가 아닌 값자체를 배열로 본다면, 0~[19value]까지 걸어두고 확인할 수 도 있으나 -> O(N)이 걸린다.
    #      자를 높이를 이진탐색의 lst[mid] -> value탐색이 아닌 [조건에 맞는 mid_index]를 구하는 식으로 이진탐색해나간다.
    #      이 때, end의 초기값은, 가장 긴 떡으로 해야, 거기서부터 줄여나갈 수 있다.

    ## 이정배 속 target value탐색이 아닌 [value를 이정배로 보고,조건에 맞는 mid_index를  이진탐색으로 찾기]
    # => [이진탐색을 통한 조건에 맞는 mid_index는 종착역없이 진행되어 가장 마지막에 최적의 중간점]으로 저장될 것이다.
    #    왜냐면, 조건 cut_sum >= m  vs cut_sum <  m 을 번갈아 진행되면서, cut_sum == m에 가깝도록 [이진탐색범위가 점점 좁아지기 때문]
    n, m = list(map(int, input().split()))
    lst = list(map(int, input().split()))

    # (1) 반복문 이진탐색은 src, end를 while안에서 업뎃하기 때문에, 미리 초기화
    srt_index = 0
    # (2) value를 배열로 보고 이진탐색할 땐, 0부터, value까지를 index로 둔다(n-1아님)
    # -> 특히, 여러개의 value에 대해 적용한다면, 제일 긴 value를 end_index로 줘야한다.
    end_index = max(lst)

    # (3) 이진탐색은 while문 + stack변수인 src/end_index로 하고, 내부에서 mid를 만들어 업데이트한다.
    # -> 종착역이 있으면 내부에서 if로 걸면되고, 없으면 다 돈다.
    result = 0 # python은 누적계산이 아니라면, 가변변수 없이 반복문 내에서 선언한 변수도 바깥에서 쓸 수 있다.
    while srt_index <= end_index:
        mid_index = (srt_index + end_index) // 2 # 중간점이자 자르는 높이
        # (4) 이진탐색시, src/end로 정해진 자를높이h(mid)를 통해, 잘린 떡의 길이를 합하여 비교한다.
        # -> 자르는 높이(mid_index)보다 긴 것에 대해서만 잘라서 누적하니, 필터링으로서 list comp를 활용한다.
        cut_sum = sum(x-mid_index for x in lst if x >= mid_index)

        # (5) 잘린 떡의 총합이 m보다 작으면, 자르는 높이mid를 낮추기 위해 dst -> mid - 1 로 안쪽으로 당겨서 mid를 낮춘다.
        # -> 반대는 srt를 안쪽으로 당겨서 mid를 높인다.
        if cut_sum < m:
            end_index = mid_index - 1
        # (6) cut_sum >= m일때는, 그 때의 높이를 지역변수에 저장한다.
        # => [이진탐색을 통한 조건에 맞는 mid_index는 가장 마지막에 최적의 중간점]으로 저장될 것이다.
        #    왜냐면, 조건 cut_sum >= m  vs cut_sum <  m 을 번갈아 진행되면서, cut_sum == m에 가깝도록 [이진탐색범위가 점점 좁아지기 때문]
        else:
            result = mid_index # 조건을 만족하는 자르는 높이H는 매번 덮어쓰기하다보면, 이진탐색의 좁혀진 범위가 최적화되어가며 마지막 값이 최적 중간점이 된다.
            srt_index = mid_index + 1

    print(result)