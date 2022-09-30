import sys

input = sys.stdin.readline


def is_valid(ch):
    ## 각 유효한 문자는 배반(return값다름)이 아니더라도 return같다면, or 연결대신 위아래로 나눠서 검사해줘도 된다.
    ## => 배반이라면 if elif로 나눠서 하거나 or 항상 위아래로 나눠서 해야한다.
    ## 유효한 경우에만 True 나머지 else는 False로 체킹한다.
    if ch.isalnum():
        return True
    if ch in ['-', '_', '.']:
        return True
    ## 배반인 경우, 위쪽이 아닌 경우,는 반드시 나눠서 다른 값으로 return
    return False


if __name__ == '__main__':
    ## 신규아이디 추천: https://school.programmers.co.kr/learn/courses/30/lessons/72410
    new_id = input().strip()

    answer = ''
    ## 문자열을 1개씩 필터링 + 변환까지만 처리한다.
    is_last_dot = False # 3-2-1
    for ch in new_id:
        #### (1)문자열이 유효한지 확인하는 is_valid메서드를 구현한다
        ##  => 유효한경우 True, 배반나머지False return하는 메서드 생성
        ##  => 바깥에서 유효하지 않다면 continue로 스킵
        #### 정규표현식: new_id = re.sub('[^0-9a-z-_.]', '', new_id)
        if not is_valid(ch=ch): continue


        #### 유효한 경우(배반)
        ## (2) 소문자로 변환
        ch = ch.lower()
        #### (3) 마침표 -> 현재가 마침표인데, 그게 처음인지 어떻게 확인할까?
        #### 정규표현식 new_id = re.sub('[.]+', '.', new_id)
        ####  (3-1) [원본 필터링 재배열 누적 중 처음에 올 것인지 아닌지]는 누적 결과값을 이용
        # -> 아직 answer에 append된게 없다면, 현재.는 첫번째 마침표후보다 -> skip
        if ch == '.':
            #### 3-2-3 flag체크하며 처리된 1번째 마침표이후, 또 마침표가 나왔을 때 skip by flag
            #### => 마침요이면서, 직전에 마침표가 들어온 경험이 있다면 is_last_dot = True로 불들어온 상태면, 스킵
            # if len(answer) == 0:
            if len(answer) == 0 or is_last_dot:
                continue
            #### (3-2) 재배열 누적 순회 중 연속된 것의 확인은? => flag로 최초 1번만 불키고 허용하고, 불켜지면 skip
            #### 먼저 처음인것을 스킵했으니, (처음이 아닌 -> 중간or끝)의 마침표상태다
            #### flag를 두어서 -> 1번이라도 등장했다면 -> if flag: continue로 스킵해주면
            #### flag: False일 대, 체크+append 후, 2번째 마침표부터 필터링한다
            is_last_dot = True # 3-2-2, 처음자리가 아닌 마침표가 최초 1번 등장할때 체크
            ## => 이후로 append 1번은 된다.
        #### 3-2-4 현재들어온  마침표가 아닌 경우에는, 마침표 연속이 아니므로 flag를 clear해줘야한다.
        else:
            is_last_dot = False
        #### (3-4)마지막 마침표를 처리하기 위해서는, 일단 문자열길이가 확정되어야한다.
        # -> 원래 문자열이 마침표가 끝이 아니였는데 요구사항대로 짤라주다 보니까 마침표로 바뀌는 경우가 존재한다
        #### => 길이가 변하는 것의 끝처리는 , 길이 부터 처리하고 마지막원소 처리한다.
        answer += ch

    if len(answer) >= 16:
        answer = answer[:15]
    #### 문자열의 끝처리는 endswith로 확인해서 처리한다.
    #### 문자열의 뒤쪽 삭제는 슬라이싱을 이용한다.
    #### 정규표현식 new_id = new_id.strip('.')
    if answer.endswith('.'):
        answer = answer[:-1]

    #### 빈문자열이라면 소문자a를 대입한다.
    if len(answer) == 0:
        answer += 'a'

    #### 문자열길이 2이하면, 마지막문자열을 반복
    # -> 마지막문자열을 저장해두고 횟수만큼 반복문을 돈다.
    #### 정규표현식 while len(new_id) <= 2: new_id += new_id[-1]
    if len(answer) <= 2:
        ch = answer[-1:]
        ## 원하는 곳에 도달하고 싶다면 while 반대조건, for if반대조건으로 반복문 직후 조건을 건다
        while len(answer) < 3:
            answer += ch


    print(answer)