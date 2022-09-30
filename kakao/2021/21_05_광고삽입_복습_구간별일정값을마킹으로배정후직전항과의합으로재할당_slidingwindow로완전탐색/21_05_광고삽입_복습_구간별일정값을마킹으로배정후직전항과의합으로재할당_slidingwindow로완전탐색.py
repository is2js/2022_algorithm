import sys

input = sys.stdin.readline


def convert(time) -> int:
    hh, mm, ss = map(int, time.split(':'))

    return hh * 60 * 60 + mm * 60 + ss


if __name__ == '__main__':
    ## 광고삽입: https://school.programmers.co.kr/learn/courses/30/lessons/72414
    play_time = input().strip('\n')
    adv_time = input().strip('\n')
    logs = [input().strip('\n') for _ in range(5)]

    ## 광고시간이 정해져있는 window로 sliding window를 1초마다 탐색해야하므로
    ## => 1초별 index매핑을 해준다.
    ##    0~1초 => 0으로 매핑된다.
    ##    초단위 매핑은 index + 1로 해줘서 0,1로 만들고 시작한다.

    ## 시분초 문제는 최소단위로 변경해서 춘다.
    play_time = convert(time=play_time)
    adv_time = convert(time=adv_time)

    ## 초를 index에 매핑할 때는 + 1개 더 주고 한다.
    play_seconds = [0] * (play_time + 1)

    for log in logs:
        slog, elog = log.split('-')
        srt_time = convert(slog)
        end_time = convert(elog)

        ## 초단위 매핑해서, [구간별 일정값]을 표시하려면
        # => 1~3 => 1,2까지만 값이 들어가면 된다.
        ####  여러 구간이 마킹될 때는, 시작(index) ~ 끝(다음index)을 마킹해놓고
        #### [직전과의 합을 통해 구간별 일정값을 유지]할 수 있다.
        # -> 등장하는 구간별로, 1씩 시청자가 증가한다.
        play_seconds[srt_time] += 1
        play_seconds[end_time] -= 1

    #### 구간별 일정값 마킹한 것은 다 마킹하고, 직전항과의 합을 재할당한다
    #### => 재할당 & 직전은 index(1번째원소부터)로 접근한다.
    for i in range(1, len(play_seconds)):
        play_seconds[i] += play_seconds[i - 1]

    #### 구간별 일정값들이 누적합을 통해 적용된 상태에서
    #### 광고시간을 sliding winodw로 1초마다 완전탐색 해야한다.

    #### slingding window는 curr = next 업뎃처럼 첫번째항을 미리 구해놓고
    #### window 바깥부터 1칸씩 이동하면서, window만큼 직전의 원소를 빼줘야한다.
    curr_sum = sum(play_seconds[:adv_time])
    #### 직전항을 이용한 순회에서, greedy하려면, 초기값을 curr초기값으로 넣어준다.
    max_sum = curr_sum
    max_srt_idx = 0
    for i in range(adv_time, len(play_seconds)):
        curr_sum = curr_sum + play_seconds[i] - play_seconds[i - adv_time]

        if curr_sum > max_sum:
            max_sum = curr_sum
            max_srt_idx = i - adv_time + 1

    # print(max_srt_idx, max_sum)
    ## // 3600 -> 분초는 날리겠다는 말
    ## // 60 -> 초는 날리겠다는 말 => % 60  분 살리겠다는 말
    ## % 60 => 초만 살리겠다는 말
    print(f"{max_srt_idx // 3600:02d}:{max_srt_idx // 60 % 60:02d}:{max_srt_idx % 60}")
