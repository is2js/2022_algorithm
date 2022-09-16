import sys
from datetime import datetime, timedelta
from functools import reduce
from operator import add

input = sys.stdin.readline

if __name__ == '__main__':

    times = list(map(lambda x: datetime.strptime(x, "%H:%M"), input().split(", ")))
    pair = 2
    # 시작시간/종료시간을 2개씩 끊어서 배열로 저장한다.
    # -> 구간인덱스로 돌리면서, 각 구간별원소에 접근할 수 있게 된다 -> 끝시간-시작시간의 차이를 구할 수 있다.
    study_times = []
    for section in range(len(times) // 2):
        srt_time = times[section * 2 + 0]
        end_time = times[section * 2 + 1]
        study_time = end_time - srt_time
        # => 공부시간이 5분미만이면 배제한다.
        if study_time < timedelta(minutes=5):
            continue
        # => 공부시간이 1시간45분을 넘어서면, 상한으로서 넘어서도 1시간 45분으로 한다.
        study_time = min(study_time, timedelta(hours=1, minutes=45))
        study_times.append(study_time)

    total_study_time = reduce(add, study_times)
    # seconds is the number of seconds within a day, which is in [0, 86399]. total_seconds is the entire timedelta converted to seconds, and can be any value, for example 604800.0 for one week, or 0.1 for 100 milliseconds.

    # (1) 3600으로 나눠서 몫(시간), 나머지(분초)를 먼저 받는다.
    hours, remainder = divmod(total_study_time.seconds, 3600)
    # (2) 분초 남아있는 것을 60으로 나눠서 몫(분), 나머지(초)로 나눈다.
    minutes, seconds = divmod(remainder, 60)

    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
    # 02:20:00

    td = timedelta(weeks=3, days=1, hours=2, minutes=30, seconds=50)
    print(td.total_seconds())  # 95450.0 => 1일 이상의 시간을 float로 반환한다
    print(td.seconds)  # 9050 # => 일반 seconds는 1day미만의 시간(86400 -1)까지를 int로 반환한다

    # (1) 단위별로 해당단위보다 크면, 큰 단위부터 해당단위를 나눈 몫(해당단위 값), 나머지(그 아래단위)로 나누어 해당단위값을 챙긴다
    # -> 우연히.. dict에 저장했는데 큰 단위부터 갔다.. 순서에 의지하는 list에 단위값들을 순서대로 매핑해야한다.
    # periods = {
    #     'year': 60 * 60 * 24 * 365,
    #     'week': 60 * 60 * 24 * 7,
    #     'day': 60 * 60 * 24,  # month는 달마다 달라서 처리안한다. 한다면, 30일로..
    #     'hour': 60 * 60,
    #     'minute': 60,
    #     'second': 1,
    # }
    # month는 달마다 달라서 처리안한다. 한다면, 30일로.).
    periods = [
        ('year', 60 * 60 * 24 * 365),
        ('week', 60 * 60 * 24 * 7),
        ('day', 60 * 60 * 24),
        ('hour', 60 * 60),
        ('minute', 60),
        ('second', 1),
    ]

    total_seconds = int(td.total_seconds())
    # value_of_periods = dict()
    value_of_periods = []
    for period, unit in periods:
        if total_seconds >= unit:
            # (1) 해당단위보다 크거나 같을 경우, 몫을 value로 가지면서, 나머지하위단위들을 total_seconds에 업뎃해서 할당한다.
            value, total_seconds = divmod(total_seconds, unit)
            # (2) period이름과 그 값을 챙긴다. -> 원한다면 fstring으로 포맷을 맞춰 챙긴다.
            # value_of_periods[period] = f"{value:02d}" if period in ['hour', 'minute', 'second'] else value
            string_time = f"{value:02d}" if period in ['hour', 'minute', 'second'] else value
            value_of_periods.append((period, string_time))

    print(value_of_periods)


    # {'week': 3, 'day': 1, 'hour': '02', 'minute': '30', 'second': '50'}
    # [('week', 3), ('day', 1), ('hour', '02'), ('minute', '30'), ('second', '50')]

    ## 함수화
    def time_interval_to_string(srt_time, end_time=None) -> list:
        periods = [
            ('year', 60 * 60 * 24 * 365),
            ('week', 60 * 60 * 24 * 7),
            ('day', 60 * 60 * 24),
            ('hour', 60 * 60),
            ('minute', 60),
            ('second', 1),
        ]

        if end_time and srt_time > end_time:
            end_time, srt_time = srt_time, end_time

        time_delta = end_time - srt_time if end_time else srt_time
        total_seconds = int((time_delta).total_seconds())

        value_of_periods = []
        for period, unit in periods.items():
            if total_seconds >= unit:
                # (1) 해당단위보다 크거나 같을 경우, 몫을 value로 가지면서, 나머지하위단위들을 total_seconds에 업뎃해서 할당한다.
                value, total_seconds = divmod(total_seconds, unit)
                # (2) period이름과 그 값을 챙긴다. -> 원한다면 fstring으로 포맷을 맞춰 챙긴다.
                # value_of_periods[period] = f"{value:02d}" if period in ['hour', 'minute', 'second'] else value
                string_time = f"{value:02d}" if period in ['hour', 'minute', 'second'] else value
                value_of_periods.append((period, string_time))
        return value_of_periods


    print(time_interval_to_string(timedelta(days=3, seconds=5)))
    # [('day', 3), ('second', '05')]
    for time in study_times:
        print(time_interval_to_string(time))
        # [('minute', '30')]
        # [('hour', '01'), ('minute', '45')]
        # [('minute', '05')]
