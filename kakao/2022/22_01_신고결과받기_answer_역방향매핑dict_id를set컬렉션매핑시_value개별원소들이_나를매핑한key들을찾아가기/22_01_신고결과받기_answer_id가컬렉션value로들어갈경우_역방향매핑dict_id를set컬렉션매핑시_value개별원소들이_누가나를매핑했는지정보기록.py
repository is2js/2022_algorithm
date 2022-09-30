import sys 
 
input = sys.stdin.readline 
 
 
if __name__ == '__main__': 
    ## 22-01-신고결과받기: https://school.programmers.co.kr/learn/courses/30/lessons/92334
    id_list = input().split()
    report = []
    for _ in range(int(input().strip())):
        report.append(input().strip())
    k = int(input().strip())

    #### [개념] id 역방향 매핑 dict : [컬렉션으로 원소들 매핑시, 각 value원소들로 나를 매핑한 key들 다시 찾아가기] 위한 용도
    ####                 => 목적을 위해 매핑당한 value가 key와 동일한 id type일 때, [나를 신고매핑한 놈들을 역으로 알 수 있디]
    ####
    ####               신고-> 매핑은 단일 방향성인데, 매번 역방향을 매핑해놓아 ->↘ 누가 나를 신고매핑햇는지 거꾸로 추적가능하게 해준다.
    ####               이 때, id로서 set으로 add해서 unique한 id들로 카운팅해야한다
    #### 그림설명: https://raw.githubusercontent.com/is3js/screenshots/main/image-20220921003217881.png


    ## report hash a->b 중복허용안되는 것에 대해서, hash의 value를 set을 이용한다
    ## result hash: b->a 신고한 사람을 value에 set으로 저장한다. 이 또한, 중복허용 안하고 unique한 id 1개씩만 담는다.
    ## -> 누가 정지시켰는지, 거꾸로 찾아가기 위한 dict(join용?) 확인하는 용도로 역관계를 또 hash에 저장해준다.

    report_hash = {}
    result_hash = {}

    for r in report:
        user, bad = r.split()
        ## hash는 등록전 중복검사 대신 key별 [최초 hash]검사 해야한다.
        ## [최초일때만] if 확인될시 : 작동 -> 그 밑으로는 기본작동
        if user not in report_hash:
            report_hash[user] = set()
        ## [최초건 아니건]
        report_hash[user].add(bad)

        #### 신고매핑 역방향 dict (누가 나를 신고햇는지 매번 set에 id를 모아 알 수 있다)
        if bad not in result_hash:
            result_hash[bad] = set()
        ## [최초건 아니건]
        result_hash[bad].add(user)

    #### 유저마다 유효한 신고당한놈들 count를 저장할 매핑 배열
    #### 순회할 원소마다 답이 필요하다면 -> 정답기록 배열 및 index접근을 하자
    answer = [0 for _ in range(len(id_list))]

    ## 유저마다 확인해서 -> answer를 채워야하니, for value가 아니라 for idx로 돌려야한다
    ## => 기록할 매핑배열이 있다면, value부터 돌리지 말고, index로 돌리자.
    for i in range(len(id_list)):
        user = id_list[i]
        ## 정답을 채울 때, 예외로 먼저 채울 수 있는 것 부터 채운다
        ## -> 신고한 적이 없는 사람은, hash에 등록도 안되어서 answer 0이다

        #### hash의 조건 확인하기
        #### hash는 조회전에, key존재검사부터 하자.
        #### hash는 삽입전에, 최초key검사 -> 필요시 중복검사
        if user not in report_hash:
            # answer[i] = 0  # 신고안했다면, answer가 0이다. 미리 0 초기화하니 skip하면 된다.
            continue

        ## 여기까지 왔다면, user는 신고를 한 상황이고, 그 사람들이 정지되었는지 확인한다.
        for bad in report_hash[user]:
            #### value를 역방향 dict에 넣어, 누가 신고매핑햇는지 or  몇명이나 신고매핑햇는지 확인한다.
            #### 역방향dict는 필수이므로 조회전 key존재검사를 할 필요는 없다
            if len(result_hash[bad]) >= k:
                ## 신고한 bad유저별로 조건만족시 +1씩 해주면 된다.
                answer[i] += 1

    print(answer)



