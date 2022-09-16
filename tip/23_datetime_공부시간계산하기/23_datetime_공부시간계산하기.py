import sys
from functools import reduce
from operator import add

input = sys.stdin.readline 
 
 
if __name__ == '__main__':
    ## 년원일(소문자) 시분초(대문자)
    # log	result
    # ["08:30", "09:00", "14:00", "16:00", "16:01", "16:06", "16:07", "16:11"]	"02:20"
    # ["01:00", "08:00", "15:00", "15:04", "23:00", "23:59"]	"02:44"
    # HH:MM형태는 시:분을 뜻합니다. 이때 시혹은 분이 한 자리 수라면 왼쪽에 0을 채워 항상 두 자리가 되게 합니다.
    # 제한사항
    # log의 길이는 짝수입니다.
    # 2 ≤ log의 길이 ≤ 1,440
    # log의 원소는 시각을 나타내며 길이는 항상 5입니다.
    # 시각은 항상 시:분을 뜻하는 HH:MM 형태로 주어집니다.
    # 어플리케이션의 기록을 가지고 공부한 시간을 나타내면 다음과 같습니다.
    #
    # 08:30 ~ 09:00, 14:00 ~ 16:00, 16:01 ~ 16:06, 16:07 ~ 16:11
    # 규칙에 따라 실제로 공부한 시간을 구하는 과정은 다음과 같습니다.
    #
    # 공부한 시각(시작 ~ 끝)	공부한 시간(분)	실제로 공부한 시간(분)
    # 08:30 ~ 09:00	30	30
    # 14:00 ~ 16:00	120	105
    # 16:01 ~ 16:06	5	5
    # 16:07 ~ 16:11	4	0
    # 따라서 실제로 공부한 시간은 30 + 105 + 5 + 0 = 140분이고, 140분은 2시간 20분이므로 "02:20"을 return 해야 합니다.

    from datetime import datetime, timedelta
    # (1) 연속된 시작/끝시간 짝을 [::2] 와 [1::2]로 각각 배열에 담을 수도 있지만
    # -> 2개식 pair로 세트로 끊어서 보관한다.
    # times = list(map(lambda x:x, input().split(", ")))
    # print(times)
    # ['08:30', '09:00', '14:00', '16:00', '16:01', '16:06', '16:07', '16:11']

    # (2) string 시간을 -> datetime.str pppp time(문자열, 문자열의형식)으로 변경한다
    # -> 시분초는 %대문자 / 년월일은 %소문자 / 년4자리만 %Y대문자
    times = list(map(lambda x:datetime.strptime(x, "%H:%M"), input().split(", ")))
    # print(times)
    # [datetime.datetime(1900, 1, 1, 8, 30), datetime.datetime(1900, 1, 1, 9, 0), datetime.datetime(1900, 1, 1, 14, 0), datetime.datetime(1900, 1, 1, 16, 0), datetime.datetime(1900, 1, 1, 16, 1), datetime.datetime(1900, 1, 1, 16, 6), datetime.datetime(1900, 1, 1, 16, 7), datetime.datetime(1900, 1, 1, 16, 11)]
    # -> 시:분:초만 입력한 시계는 1900, 1, 1일의 년월일로 고정이다.
    pair = 2
    # (3) 2개씩 끊어서 배열로 저장한다.
    # -> 구간인덱스로 돌리면서, 각 구간별원소에 접근할 수 있게 된다 -> 끝시간-시작시간의 차이를 구할 수 있다.
    study_times = []
    for section in range(len(times)//2):
        srt_time = times[section * 2 + 0]
        end_time = times[section * 2 + 1]
        study_time = end_time - srt_time
        ## -> 시간차이는 timedelta로 존재한다.
        # print(type(study_time))
        # <class 'datetime.timedelta'>
        # print(study_time)
        # 0:30:00
        # 2:00:00
        # 0:05:00
        # 0:04:00
        # => 공부시간이 5분미만이면 배제한다.
        if study_time < timedelta(minutes=5):
            continue
        # print(study_time)
        # 0:30:00
        # 2:00:00
        # 0:05:00
        # => 공부시간이 1시간45분을 넘어서면, 상한으로서 넘어서도 1시간 45분으로 한다.
        # if study_time >= timedelta(hours=1, minutes=45):
        #     study_time = timedelta(hours=1, minutes=45)
        study_time = min(study_time, timedelta(hours=1, minutes=45))
        # print(study_time)
        # 0:30:00
        # 1:45:00
        # 0:05:00
        study_times.append(study_time)

    ## 각 공부시간들을 누적한다. timedelta라서 그냥 다 더해주면 될 듯하다
    total_study_time = reduce(add, study_times)
    # print(total_study_time) # 2:20:00

    ## 기본적으로 timedetla는 시:분:초 표기법이다
    # -> 표기를 다르게(시:분)으로 출력하기 위해서는 format을 변경해 출력해준다.
    # -> 숫자를 특정형식으로 출력하려면 이렇게 한다
    # hour = total_study_time.hours
    # minute = total_study_time.minutes
    ## => timedelta는 hours가 없다 days 와 seconds밖이다.
    ## => timedelta.seconds // 60 : 분
    ## => timedelta.seconds // 3600 : 시간만 -> 나머지 분초 존재
    # (1) 3600으로 나눠서 몫(시간), 나머지(분초)를 먼저 받는다.
    hours, remainder = divmod(total_study_time.seconds, 3600)
    # (2) 분초 남아있는 것을 60으로 나눠서 몫(분), 나머지(초)로 나눈다.
    minutes, seconds = divmod(remainder, 60)
    # f"{변수:[ljust]}"
    # print(f"{hours:>02d}:{minutes:02}")  #02:44
    # print(f"{'bd':^4s}:{minutes:02}")  #02:44
    # bd   :20

    # 타임델타(시간간격)은 formatting적용은 안된다. datetime만 된다.
    # print(f"{datetime.now() :%Y-%m-%d %H:%M}") # 2022-09-13 18:23
    print(f"{hours:>02d}:{minutes:>02d}:{seconds:>02d}")
    # 02:20:00
