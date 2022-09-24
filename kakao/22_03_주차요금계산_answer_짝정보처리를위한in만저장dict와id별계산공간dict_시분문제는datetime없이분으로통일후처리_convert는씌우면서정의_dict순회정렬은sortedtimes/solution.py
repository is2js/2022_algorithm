import math
import sys

input = sys.stdin.readline


def convert(time):
    ## (1) 하루안의 시:분문제는 분으로 변환한다.
    hh, mm = time.split(":")
    return int(hh) * 60 + int(mm)


if __name__ == '__main__':
    ## 주차요금: https://school.programmers.co.kr/learn/courses/30/lessons/92341
    fees = list(map(int, input().split()))
    records = []
    for _ in range(int(input().strip())):
        records.append(input().strip())

    #### 시분만으로 구성된 문제는 시->분으로 바꿔서 처리한다. end - start 분으로 계산해버리면 된다.

    #### 2개의 자료구조를 유지한다 ==> id별 저장 기록을 위한 hash를 여러개 유지할 수 있다.
    #### (1)id별 입차시 기록을 남기기 위한 intime hash
    ####    시:분으로 이루어져있다면, 분으로 바꿔서 넣어준다.

    #### (2)id별 in시 초기화 -> out시 계산해서 주차시간누적을 위한 result hash
    ####  => my) 짝을 이루는 동떨어진 정보들은,
    ####         in -> 정보hash (시간) 기록 +  짝마다 계산hash초기화
    ####         out -> 정보hash에서 in정보 추출해 계산 -> 계산hash에 기록
    ####                계산된 id는 정보hash에서 삭제
    ####
    ####  => my) in만 기록해놓고, out등장시 삭제해주면
    ####         out안등장한 것들은 in에 그대로 남아있게 되어 예외처리가 가능하다

    ####    1번hash에 들어가는 순간 같이 기록한다.
    ####  => 역방향hash도 마찬가지처럼, 매핑할때마다 history성으로 결과를 기록할 수 있다.
    ####  => id별 누적계산을 할 것이라면, 기록마다 계산하지말고 default값으로 초기화한다

    #### 그림설명: https://raw.githubusercontent.com/is3js/screenshots/main/image-20220921024011153.png

    ## (1) 짝이 존재하지 않을 수 있을 때는 짝정보 중 in만 저장하는 dict와
    ## (2) id별 (누적)계산결과 저장을 위한 dict를 만든다.
    intime_hash = {}
    result_hash = {}

    for r in records:
        time, number, inout = r.split()
        ## (3) srt, end 중 srt만 hash에 저장한다
        if inout == 'IN':
            #### (4) 할당시에도 변환메서드를 씌워서 넣어준다.
            # intime_hash[number] = time
            intime_hash[number] = convert(time)
            #### (5) in이 등장시 out때 계산할 id별계산공간hash를 초기화해준다.
            #### => 최초key검사는 최초에만 이루어지면 되는데
            ####    id별로 여러개의 in이 들어올 수 있기 때문에
            ####    검사하고 초기화해준다.
            ####    [삽입(value할당)이 아니라 초기화]는 최초key검사하고 넣어준다.
            if number not in result_hash:
                result_hash[number] = 0
        else:
            ## out인경우 -> in과 계산해서 누적결과값 공간에 넣어주고, in에서는 지워야한다.(남아있으면 짝 안맞는 것)
            result_hash[number] += convert(time) - intime_hash[number]
            #### (6) 짝이 안맞을 수 있는 것을 잡아내야하 때는,
            ####    => 짝이 맞는 경우는 in 해쉬에서 삭제를 해줘야한다.
            del intime_hash[number]

    ## 누적 주차시간 계산이 끝났는데, in에 짝이 안맞아서 남아있는 것은 23:59로 처리한다.
    for number, intime in intime_hash.items():
        result_hash[number] += 23 * 60 + 59 - intime

    ## answer에 차량번호 오름차순으로 넣어줘야하기 때문에
    ## answer배열의 순서에 맞게, result_hash에서 주차시간을 순서대로 가져와서 넣어줘야한다.
    ## -> 매핑된 정답배열을 위해 index로 탐색해서 처리하면 좋겠지만, dict는 그게 안되므로 value로 탐색하되 미리 정렬해놓고 탐색해야한다.
    #### items()는 튜플리스트이므로 1번째 요소 id가 정렬되서 가져올 것이다.
    answer = []
    for number, time in sorted(result_hash.items()):
        ## 계산들어가기 전에, 총 주차시간이 180분보다 작으면 바로 끝이다.
        if time <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(
                fees[1] + math.ceil((time - fees[0]) / fees[2]) * fees[3]
            )

    print(answer)