import bisect
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## 순위검색: https://school.programmers.co.kr/learn/courses/30/lessons/72412
    info = [input().strip() for _ in range(6)]
    query = [input().strip('\n') for _ in range(6)]

    # (1) 정해진 종류의 field는 index로 매핑하되, map에 적어서 매핑한다.
    # -> 여러개의 field라면, [정해지지 않은 field]를 입력할 수 있게
    # -> 1field 당 정x필드의 index차원에 매핑한다.
    # => 상관없음 값(-)는, 검색시 다 걸리도록, 특정종류가 등장할 때, (-)를 대입한 case에도 같이 넣어준다
    word_map = {
        'cpp': 1, 'java': 2, 'python': 3, '-': 0,
        'backend': 1, 'frontend': 2,  # '-': 0,
        'junior': 1, 'senior': 2,  # '-': 0,
        'chicken': 1, 'pizza': 2,  # '-': 0,
    }
    # (2) 정해진 종류의 field를 K개(차원) 선택할때마다 case는 정해져있다.
    #    그 각각의 index마다(case) 패밍할 [정해지지 않는 필드] 값을 저장할 배열읆 나든다.
    #    K차원으로 만들면, 바로바로 인덱싱할 수 있지만, 관리는 1차원으로 하되
    #   -> 종류1갯수 * 종류2갯수 * 종류3갯수 * 종류4갯수의 총 case == index마다
    #      1차원으로 매핑할 수 있게  1차원 배열에 매핑하며,
    #    그 값이 여러개 나올 수 있으면, 해당 갯수의 빈 행렬을 선언한다.
    score_list = [[] for _ in range(4 * 3 * 3 * 3)]
    for datas in info:
        data = datas.split()
        # (3) 필드 종류별 index를 매핑값->map-> index로 변환한 뒤, 튜플로 보관해 둔다
        # => 이 때, 각 차원별로, 하위차원의 종류갯수만큼을 곱해서 보관해야한다.
        #   ex>  1차원이지만, 2차원으로 생각하기(len//col갯수 range 0 ~n-1 row(상차)인덱스 -> 1차원으로  [row_index] * 하위차원인col갯수 + 하위차원인col번호
        #        상위차원 매핑 인덱스 * 하위차원의 갯수 + 하위차원 매핑 인덱스
        #        상차인덱스 * 하차갯수 * 더하차갯수 + 하차인덱스 *더하차갯수 + 더하차인덱스
        # language_index = word_map[data[0]] * 3 * 3 * 3
        # position_index = word_map[data[1]] * 3 * 3
        # career_index = word_map[data[2]] * 3
        # food_index = word_map[data[2]]

        # (4) 원래는 각 하위차원갯수를 곱한 상태로 누적합을 해야하 index가 왼성되지만
        # => 완성하지 않고 누적하기 직전으로 tuple로 모아둔다.
        # => 상관없음도 같이 동시에 넣어주기 위해, bit로 경우의수를 표현하고
        # => bit는 1자리씩 shift하며 완성하기 때문에
        #    해당자리0(상관없음), 해당자리1(특정종류)가 bit로 표현한 부분집합에 다 올라오기 때문에
        #   확인해서 넣어준다.?
        convert_indexes = (
            word_map[data[0]] * 3 * 3 * 3,
            word_map[data[1]] * 3 * 3,
            word_map[data[2]] * 3,
            word_map[data[3]]
        )
        score = int(data[4])

        # print(data) # ['java', 'backend', 'junior', 'pizza', '150']
        # print(convert_indexes) # (54, 9, 3, 2)
        ## => 차원별index도 1자리씩 가지고 있는다 for bit로 만든 부분집합의 O/X마다 동시처리
        ## => bit는 0번재자리부터 if불들/else불안들을 나누어서 1자리씩 처리하기 때문에
        ##    1자리씩에 해당하는 index를 가지고와 누적합한다
        ##    => 차원index에서 0번index를 사용한다면 안더해진다.
        ##    => 불O: 하위차원곱해진index사용 / 불X: 0번인덱스사용(합없어도 됨)
        ##    => -상관없음은 0에 배정해놓고, 불X -> 0번index -> 누적합에서 안더해도 된다.

        ## 정x필드 score를 제외하고, / 정해진 종류의 field4개에 대해 O/X부분집합을 만든다.
        for subset in range(1 << 4):
            ## 보통 여기서 빈배열을 선언하여, 0번째 자리부터 채워나갈 수 있다.
            ## 각 자리별 배열을 만드는 것이 아니므로,
            idx = 0
            for i in range(4):
                ## 보통 여기서 if불들 else불안들을 나누어서 처리한다.
                ## => 해당자리 불들어왔다면, [하위차원갯수곱해진 차원index]를 누적합해준다.
                ##    불 안들어왔다면, -상관없음의 case로서, 0번인덱스를 사용하여 누적합 안해줘도 된다.
                if subset & 1 << i:
                    idx += convert_indexes[i]
                else:
                    idx += 0

            ## 각 자리별 index를 더했다면, 정해지지 않는 필드 score의 index로 주고
            ## 해당하는 값을 매핑한다. 여러값이 들어갈 수 있으므로 (-), list에 append한다.
            score_list[idx].append(score)
            ## 부분집합을 돌면서, 각자리가 0인 경우(-), 1인경우(정해징종류value)가 다 등장하므로
            ## => 0일때와 1일때 case들은 어차피 마련되어있으며, 그 상태에 따라, index를 달리하여
            ##   똑같은 score를 2번 매핑한다.
            # print(idx, score_list[idx])
            # 0 [150]
            # 54 [150]
            # 9 [150]
            # 63 [150]
            # 3 [150]
            # 57 [150]
    ## score_list는 총 4*3*3*3 정해진종류field들에 의해 만들어진 case마다.
    ## => input되는 value case + 상관없음(-, 차원index 0 )case를 다 score를 집어넣었다.
    ## =>  숫자를 모으는 곳은 다모아서 탐색한다면 => 정렬해놓고, 이진탐색하자.
    ## => 각 원소에 (정렬해서) [재할당하는 순회]의 경우 => index로 or index와 함께 돌린다.
    for i, val in enumerate(score_list):
        score_list[i] = sorted(val)

    answer = []

    for datas in query:
        data = datas.split()
        ## 정종fieldvalue -> 차원index로 매핑풀기
        ## 자리별로 처리할 것이 아니라면, 차원index를 그냥 다 누적더해서 index를 만들면 된다.
        # print(data) # ['java', 'and', 'backend', 'and', 'junior', 'and', 'pizza', '100']
        idx = word_map[data[0]] * 3 * 3 * 3 + \
              word_map[data[2]] * 3 * 3 + \
              word_map[data[4]] * 3 + \
              word_map[data[6]]
        score = int(data[7])

        scores = score_list[idx]
        ## 이진탐색 중 target index뿐만 아니라, ~이상의 값도 bisect_left로 구할 수 있다.
        ## => len - left(, ~이상인값)
        more_than_count = len(scores) - bisect.bisect_left(scores, score)

        answer.append(more_than_count)

    print(answer)
