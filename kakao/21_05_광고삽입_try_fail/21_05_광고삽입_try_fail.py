import itertools
import sys
from collections import defaultdict

input = sys.stdin.readline


def convert(time):
    hh, mm, ss = map(int, time.split(":"))
    return hh * 3600 + mm * 60 + ss


def r_convert(seconds):
    hh, r = divmod(seconds, 3600)
    mm, ss = divmod(r, 60)
    return ":".join(map(str,[hh, mm, ss]))


if __name__ == '__main__':
    ## 광고삽입: https://school.programmers.co.kr/learn/courses/30/lessons/72414
    play_time = input().strip('\n')
    adv_time = input().strip('\n')
    logs = [input().strip('\n') for _ in range(5)]

    # 각 시간을 초로 변환하기
    play_time = convert(play_time)
    adv_time = convert(adv_time)
    logs = [list(map(convert, log.split('-'))) for log in logs]
    # print(logs)
    # [[4815, 6314], [2431, 3600], [1550, 2909], [5459, 6809], [5864, 7350]]

    ## log에 찍힌 srt, endtime를 section별 to로 하여 구간을 만든다.
    sections = [0] + sorted(itertools.chain.from_iterable(logs))
    if play_time != sections[-1]:
        sections += [play_time]
    # [0, 4815, 6314, 2431, 3600, 1550, 2909, 5459, 6809, 5864, 7350, 7435]

    ## 각 구간별로 직전의to와 비교해서 카운트를 세자.

    section_count = defaultdict(int)

    prev_to = 0
    # count = [0] * (len(sections) - 1)
    for log in logs:
        srt_time, end_time = log
        for section_index, curr_to in enumerate(sections[1:]):
            ## 착수하려면 1) 내 구간하한(prev_to)이 들어오는 상대하한보다 더 커야 착수 시작
            #           2) 내 구간하한이(prevo_to)이 들어오는 상대상한보다는 작아야 착수 시작(내 구간상한은.. 알아서 상대상한 vs 내상한으로 짜름)
            #             => 구간처리기의 다음구간으로 갔는데도,
            #             => 내 구간상한조정은 알아서 함.
            # if prev_to <= srt_time:
            if prev_to <= srt_time or prev_to >= end_time:
                prev_to = curr_to # 필수 업뎃구간은 continue전에 넣어줘야한다
                continue
            upper_bound = curr_to if end_time > curr_to else end_time
            lower_bound = prev_to
            print(srt_time, end_time , '|' ,  prev_to, curr_to ,'|' , lower_bound, upper_bound)
            ## 들어오는 놈의 상한과 내 하한이 같을 수 도 있다 -> 구간처리하면 1-1 = 0으로 되지만.. 구간이 아닌 튜플로 처리한다면.. 남긴 남는다.
            ## => 계산할땐 어차피 구간기준으로 한다면 cut 당할 듯.
            section_count[(lower_bound, upper_bound)] += 1

            prev_to = curr_to

    # print(sorted(section_count.items()))
    # [((2431, 2909), 1), ((2909, 3600), 1), ((5459, 5864), 1), ((5864, 6314), 2), ((6314, 6809), 2), ((6809, 7350), 1)]

    play_of_section = {}
    ## 이제 각 구간x누적횟수만큼 계산하며 string으로 변환
    for section, count in sorted(section_count.items()):
        # section은 시작시간으로만 표시

        play_of_section[r_convert(section[0])] = (section[1] - section[0]) * count

    print(play_of_section)
    # {'0:40:31': 478, '0:48:29': 691, '1:30:59': 405, '1:37:44': 900, '1:45:14': 990, '1:53:29': 541}
