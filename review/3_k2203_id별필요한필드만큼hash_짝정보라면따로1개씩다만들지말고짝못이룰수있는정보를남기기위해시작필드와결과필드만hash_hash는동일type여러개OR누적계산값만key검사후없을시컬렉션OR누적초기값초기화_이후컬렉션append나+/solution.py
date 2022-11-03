import math
import sys

input = sys.stdin.readline


def convert_min(hhmm):
    hh, mm = hhmm.split(':')
    return int(hh) * 60 + int(mm)


if __name__ == '__main__':
    ## 주차요금: https://school.programmers.co.kr/learn/courses/30/lessons/92341
    fees = list(map(int, input().split()))
    records = []
    for _ in range(int(input().strip())):
        records.append(input().strip())

    ## 짝 등장시 계산 후 삭제되는 && 짝 없는 것들만 남게되는 DB용 hash
    ## hash에 id마다 1개 정보만 저장하되,
    # 2번째가 들어오면 계산하고 삭제되는 hash

    ## 시작과 끝은 각각 따로 입력된다.
    ## DB: 시작 -> row의 시작필드에 시간입력 / 끝 -> 같은row의 끝필드에 시간입력 / 끝이 비었다면 23:59로 처리하는데 / 끝필드 - 시작필드 계산
    ## 알고: id별 hash에 시작정보 입력 / id별 hash에 끝정보입력? in collection? 을 하게 되면
    ## => id별 계산결과도 거기에 추가해야하며
    ##    id별 짝 안맞는 것들은 where로 순회하면서 처리해야한다.

    ## id별 필요한 필드만큼 저장hash(역hash) 를 만들되, 짝정보의 경우 1개 hash만 만들어서, 존재확인후 처리한다.
    intime_hash = {}
    result_hash = {}

    for r in records:
        # print(r.split())
        # ['06:00', '0000', 'IN']
        # ['06:34', '0000', 'OUT']
        ## 짝정보는 시작정보만 시작_hash에 저장한다.
        time, id, inout = r.split()
        ## 저장시 1type 여러개 저장의 누적저장이라\면, id존재안하는 최초 초기화해줘야하는데
        ##  1개 필드값만 저장한다면, 바로 저장한다.
        # intime_hash[id] = time

        if inout == 'IN':

            ## 계산용 값필드는 미리 변환하고 저장하자. 시간 계산은 최소단위로 변환해놓기
            intime_hash[id] = convert_min(time)

            ## 계산hash는 누적필드라 한번 초기화해놓고 => += 누적계산으로 넣어준다.
            ## => id별 누적필드 초기화
            if id not in result_hash:
                result_hash[id] = 0
        else:
            ## out정보가 들어왔다면, in정보와 함께 계산하고, 짝 안맞는 것만 남긴다.
            result_hash[id] +=  (convert_min(time) - intime_hash[id])
            del intime_hash[id]


    ## 짝 안맞아서 intime_hash에 남아있는 것들 처리
    for id, intime in intime_hash.items():
        result_hash[id] += (convert_min("23:59") - intime)

    ## items()는 튜플이라 sorted만 하면 알아서 앞에것(key)부터 오름차순이다.
    answer = []
    for id, minute in sorted(result_hash.items()):
        if minute <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((minute - fees[0] )/ fees[2]) * fees[3])


    print(answer)




