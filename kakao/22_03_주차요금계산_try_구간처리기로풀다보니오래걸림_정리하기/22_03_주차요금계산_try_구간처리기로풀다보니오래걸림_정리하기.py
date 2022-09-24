import datetime
import math
import sys
from collections import defaultdict

input = sys.stdin.readline

if __name__ == '__main__':
    ## 주차요금: https://school.programmers.co.kr/learn/courses/30/lessons/92341
    fees = list(map(int, input().split()))
    records = []
    for _ in range(int(input().strip())):
        records.append(input().split())

    ## prev데코 객체 대신, 배열로 매핑
    ##        -> 재귀로 넘어가는게 아니라서 시작특이점 객체가 필요없다?
    # sections = [60 * 180, 60 * 60 * 24]  # 구간별 처리할 to -> timedelta는 초밖에 없다
    sections = [0, fees[0], 60 * 24]  # 구간별 구간 (분)to
    sections_fees = [0, fees[1], fees[3]]  # 구간별 (분당) 요금

    db = defaultdict(list)

    ## db에 id별 정보들 집계
    for time, id, type in records:
        db[id] += [time]

    print(db)
    ## id별 2개씩 끊어서 계산하기 -> 1개로 남았으면, 23:59로 처리하기
    ## id순으로 정렬
    result = []
    for id, times in sorted(db.items()):
        ## db를 뒤질때는 id별로 뒤질 수 있게 출력 걸어주고 시작하자.
        print(f'{id}============')
        total_fee = 0
        # ['06:00', '06:34', '18:59']
        # ['07:59', '19:09']
        # ['05:34', '07:59', '22:59', '23:00']


        ## 2개씩 끊어서 계산하되, 홀수라서 남으면, 23:59를 애초에 더해놓고 짝수처리 되게 한다.
        section_len, mod = divmod(len(times), 2)
        if mod:
            times.append('23:59')
            section_len += 1


        times = [datetime.datetime.strptime(time, '%H:%M') for time in times]
        # time_deltas = []
        ## 개별 inout계산이 아니라, 누적해서 시간을 매긴다
        timedelta_sum = datetime.timedelta(seconds=0)
        for section_index in range(section_len):
            # print(times[section_index * 2 + 0], times[section_index * 2 + 1])
            # time_deltas.append(times[section_index * 2 + 1] - times[section_index * 2 + 0])
            timedelta_sum += (times[section_index * 2 + 1] - times[section_index * 2 + 0])
        # if mod:
        #     time_235900 = datetime.datetime.strptime('23:59', '%H:%M')
        #     time_deltas.append(time_235900 - times[section_index * 2 + 0])
        # print(time_deltas)
        # [datetime.timedelta(seconds=2040), datetime.timedelta(seconds=64740)]
        # [datetime.timedelta(seconds=40200)]
        # [datetime.timedelta(seconds=8700), datetime.timedelta(seconds=60)]

        ## 이제 구간별 처리기로 자신의 구간만큼 처리해서 누적한다
        # for time_delta in time_deltas:
        #     fee_per_inout = 0
        #     minutes = time_delta.seconds // 60
        minutes = timedelta_sum.seconds // 60
        ## 구간처리는 to가 0이 될때까지 거꾸로 들어온다.?
        ## prev데코객체는 직전의 to를 쓸 수 있기 때문에.. i, i+1(curr, next직접업뎃)과 같은 효과다?
        ## 매핑배열을 2개 동시에보기(zip) + 직전도 보기 -> 인덱스로 변경 or curr, next직접업뎃
        prev_section = sections[0]
        prev_fee = sections_fees[0]
        sum_of_fee = 0
        for section, fee in zip(sections[1:], sections_fees[1:]):
            ## 일단 내 구간(prev to보다 작거나, section to보다 크거나 )이 아니면 continue!!!!!!!
            ## => 구간은 자기구간 아니면 continue로 넘기는 로직 필수
            ## => continue로 넘기되 업뎃은하면서 넘어가야한다!!!!!!!
            ##   필수 없뎃 (curr next)이 아래 있다면, if 실패시 contineu(x) -> 성공시만 계산
            # if minutes < prev_section or minutes > section:
            #     continue

            ## 직전의 to는 포함안하면서, 나의 to까지는 해결하자.
            ## (1) 직전의 to보다 크거나 같아야 일을 착수한다.
            ## 보통 0~999 , 1000 부터 끊으니까... 하한을포함하고 상한을 안포함하게 해보자.
            ## => 여기서는 180까지 상한을 포함하니까.. 직전의to보다 커야ㅣ 일 착수

            ## (2) 내가 일을 착수안하더라도, 어차피 구간을 다 도니, 누적계산을 기본값으로 넘겨주자.
            ## => 일단 현재구간의 to후보인 minutes는 하한보다는 커야한다!!!!!!
            print(f'현재구간 {prev_section}< <= {section}')
            if minutes <= prev_section:
                # fee_per_inout += 0
                sum_of_fee += 0

            ## (3) 내가 일 착수하는 하한 < 구간
            # if minutes > prev_section :
            ## => 상한을 일단 두고, [하한을 기준으로 일 착수를 결정]한다
            else:
                ## (4) 상한보다 작거나 같으면 to 후보인 나를 상한으로 쓴다.
                ##     구간to보다 크다! => 구간to을 upper_bound로 쓴다.
                upper_bound = minutes if minutes <= section else section
                # lower_bound = prev_section
                ## (5) 하한은 포함안시킬 경우, lower_bound를 +1시켜야한다? => ㄴㄴ 우리는 차이로 구간을 만들기 때문에, 각 경계의 포함유무는 중요치 않다? 180분이후로 200분까지 -> 20분
                lower_bound = prev_section

                my_section = upper_bound - lower_bound
                print(f"my_section: {lower_bound} ~ {upper_bound}")

                ## 각 구간별 계산 -> sum에 누적
                ## (5) 구간을 계산했지만, upper_bound가 기본요금구간인 180이하면, 일괄 기본요금으로
                ##     upper_bound가 180을 초과했다면, lower도 181부터로서 구간을 넘어선 것이므로, 계산법을 적용한다.
                ## => 어차피 0 ~ 180 구간을 잡아놨기 때문에, 구간처리가 아니더라도 한방에 처리된다?
                ## ->  180이하면, 기본요금 자체만 누적 / 180초과면, 단위분(k) == fees[2] 으로 나눈 값(몫x 나머지를 추산해 올릴 수 있음)을 올림해서 * 요금
                # curr_fee = fee if upper_bound <= fees[0] \

                ## (6) new minutes든 to든 일단 상한을 minutes로 통일된 상태다.
                ## 상한이 기본구간보다 작을때만 계산없이 기본요금으로 처리한다.
                ## => 일 착수를 if minutes > prev_section:가 아닌  (wrong) if minutes >= prev_section:시 했다고 했떠니.. upper_bound도 fee if upper_bound <= 기본요금경계 로 넣은 상태에선
                ##    외우자.. 하한을 넘어서야 일 착수(특이점 0도 넘어서야) -> upperbound교체도 section을 넘어서야 seciontion으로
                ##    기본요금이 있는 구간처리 => 애초에 0 ~ 기본요금 까지 구간을 1개로 제한하고, upper_bound가 기본요금 안쪽이면, 누적시 기본요금 1개로 탁

                curr_fee = fee if upper_bound <= fees[0] \
                    else math.ceil(my_section / fees[2]) * fee
                print(f'{my_section / fees[2]} * fee {fee} -> {math.ceil(my_section / fees[2]) * fee}')
                # fee_per_inout += curr_fee
                sum_of_fee += curr_fee
                print(f'id, minutes, my_section, curr_fee : {id}: {minutes}, {my_section}, {curr_fee}')

            ## curr, next업뎃
            prev_section = section
            prev_fee = fee

        ## 해당in-out별 계산한 요금을 또 합산
        # total_fee += fee_per_inout
        print(sum_of_fee)

        ## id별 요금을 append
        result.append(sum_of_fee)
        # print(id, total_fee)

    print(result)












