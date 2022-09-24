import bisect
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## 순위검색: https://school.programmers.co.kr/learn/courses/30/lessons/72412
    info = [input().strip() for _ in range(6)]
    query = [input().strip('\n') for _ in range(6)]

    #### 정해진종류의 field는 새로운배열이 아니라, 배열의 차원에 매핑할 수 있으며
    ### 각 정해진value별로-> 차원에서의 index1개에 매핑하므로
    ### dict로 차원별 index를 미리 매핑해놓는다.

    #### field별 정해진 종류의 문자열 -> index로 매핑하려면 dict에 따로 저장해놓고 매핑하기
    #### string -> 다차원배열을 위한 index매핑은 dict로 한다.
    #### => field종류별, line을 바꿔서, 숫자index로 매핑해준다.
    ###     각각 다른차원이므로, field별 index중복은 상관없다.
    word_map = {
        '-': 0, 'cpp': 1, 'java': 2, 'python': 3,
        'backend': 1, 'frontend': 2,
        'junior': 1, 'senior': 2,
        'chicken': 1, 'pizza': 2
    }

    #### 정해지지 않은 field는 따로 배열을, 나올수 있는 다차원의 인덱스를 그대로 쓸 수 있도록
    #### 그 갯수만큼 배열로 가지게 한다.
    # => 앞에서 나올 수 있는 경우의 수4*3*3*3중복될 수 있으면 2차원배열로 생성한다.
    #### => 앞의 경우의수별로
    score_list = [[] for _ in range(4 * 3 * 3 * 3)]

    #### info의 정보로 테이블을 만들어야한다.
    for string in info:
        words = string.split()
        #### 이제 word -> index로 변환해야한다.
        #### => 다차원 -> 1차원 투플로의 매핑은 각 자리수마다, 뒤에 남은 자리의 경우의수를 모두 곱해서 생성한다.
        arr = (
            word_map[words[0]] * 3 * 3 * 3,
            word_map[words[1]] * 3 * 3,
            word_map[words[2]] * 3,
            word_map[words[3]],
        )
        #### score는 따로 뽑아준다.
        score = int(words[4])

        #### 이제 각 field별 -(상관없음)에 해당하는 것도 중복해서 score를 채워놓기 위해
        #### 2222 16가지를 부분집합을 bit로 나타낸다
        for subset in range(1<<4):
            #### score_list에 사용할 index를 0으로 초기화한 뒤
            idx = 0
            #### 각 원소별로 확인하도록 돌아준다
            for i in range(4):
                #### O로 선택된 경우 => arr[]의 i번째 인덱스에 매핑된 것을 포함시켜준다
                #### => 다차원을 1차원으로 으로 매핑하기 위해서는
                ####    0번재index*333 + 1번째index*33  + 2번째index*33 + 3번째index 형태로 만들어내며
                ####   arr에    [0]         arr[1]        arr[2]         arr[3]으로 매핑되어있으니
                ####  [-]로서 불이꺼진 경우에는 매핑된index가 0이라서 아예 idx에 안더해줘도, [-]에 해당하는 idx가 뽑힌다
                if subset & (1 << i):
                    idx += arr[i]
            #### subset마다 만들어진 다->1차원 index를 score_list에 score로서 append로 저장한다.
            #### => 총 16개번 score가 16개의 데이터에 append된다.
            ####    java/- backend/- junior/- pizza/- 150
            #### =>각 field별 상관없다고 날린 경우까지 다 추가해놓는다.
            score_list[idx].append(score)

    #### 모든 지원자마다 16개씩 score가 중복append된 상황이라면
    #### score를 나중에 binary서치할 수있게 미리 정렬을 해둔다.
    for i in range(4*3*3*3):
        score_list[i] = sorted(score_list[i])

    #### query를 처리해서 answer를 만들어낸다.
    answer = []
    for string in query:
        words = string.split()
        #### 이제 각 지원자query별 idx를 계산해야한다. -> 그래야 score를 확인할 수 있다.
        #### => and가 달렸어도 다 정해진 form이므로, idx만 바꿔서 뽑아내면 된다.
        idx = word_map[words[0]] * 3 * 3 * 3 + \
              word_map[words[2]] * 3 * 3 + \
              word_map[words[4]] * 3 + \
              word_map[words[6]]
        score = int(words[7])

        #### 이제 score_list에 저장된 [이정배 score들] 중에 score이상인 것을 찾기 위해,
        #### score이상인 것의 갯수를 찾을 때, 이진탐색을 한다.
        #### ex> 100 200 300 -> 50이상은요? -> idx 0을 반환 -> 3 - 0
        ####     100 200 300 -> 100이상은요? -> idx 0을 반환 -> 3 - 0
        ####     100 200 300 -> 150이상은요? -> idx 1 -> 3 -1 => 2명
        ####     100 200 300 -> 200이상은요? -> idx 1 -> 3 -1 => 2명
        ####     100 200 300 -> 300이상은요? -> idx 2 -> 3 -2 => 1명
        ####     100 200 300 -> 350이상은요? -> idx 3 -> 3 - 3 => 0명
        #### => len() - 1 - left_value_idx + 1 => [len - left_idx]
        ###  => [더 큰 것의 right => len)]- left_value_idx
        more_than_count = len(score_list[idx]) - bisect.bisect_left(score_list[idx], score)
        answer.append(more_than_count)


    print(answer)

