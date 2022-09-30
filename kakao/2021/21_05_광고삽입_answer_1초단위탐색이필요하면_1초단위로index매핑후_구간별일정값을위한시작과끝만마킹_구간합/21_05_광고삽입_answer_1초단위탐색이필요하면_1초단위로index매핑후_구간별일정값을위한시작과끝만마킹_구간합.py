import sys 
 
input = sys.stdin.readline


def convert(time):
    h, m, s = time.split(':')
    # 시간은 60분이고 -> 분은 60초다
    return int(h) * 60 * 60  + int(m) * 60 + int(s)


if __name__ == '__main__':
    ## 광고삽입: https://school.programmers.co.kr/learn/courses/30/lessons/72414
    play_time = input().strip('\n')
    adv_time = input().strip('\n')
    logs = [input().strip('\n') for _ in range(5)]

    ## 1. 변환함수 부터 작성
    play_seconds = convert(time=play_time)
    adv_seconds = convert(time=adv_time)

    ## 2. 광고시간1초단위 탐색을 보고, 1초단위로 총 시간을 쪼개서 처리하기
    ## => 시간을 index로 매핑할 땐, 미리 index1개를 더써서, 그 초를 넘겼을 때의 연산에 대비한다.
    total_seconds = [0] * (play_seconds + 1)

    ## 3. log를 보면서, [시작과 끝시간만 마킹]을 해주면, 나중에 1회 순회로 구간별 1초단위 값을 일괄처리할 수 있다.
    for log in logs:
        slog, elog = log.split('-')
        start = convert(slog)
        end = convert(elog)
        ## 4. 1초단위처리에서, [구간별 일정값]d은, 시작과 끝을 마킹해서 나중에 일괄처리한다.
        ## => 해당초를 넘어서는 순간부터 value가 적용된다는 의미이며, 직전과의 연산을 통해 구간 전체에 나눠준다
        total_seconds[start] += 1
        total_seconds[end] -= 1

    # print(total_seconds)
    ## 4. 직전과의 합을 구해야하므로, index를 첫번째는 건너띄고 1부터 [구간별일정값을, 직전과 합으로 적용]해볼 것이다.
    ## -> idx가 있다면, 직전값과의 연산은 for i 로 curr, next 자동업뎃이다.
    for i in range(1, len(total_seconds)):
        total_seconds[i] += total_seconds[i-1]
    # print(total_seconds)

    ## 5. 일정idx(광고시간seconds)간의합이 1칸씩 이동하므로, 구간합 알고리즘을 적용한다 + greedy까지
    ## => (1) 첫번째 구간의 sum을 구해놓고, (2) 반복문은 +1한 cursor == 직후의 원소가 i가 되도록 돌린다
    #                  sum( arr[:window길이]) => range(window길이, ) 부터 돌린다.
    #         012k(3)   => curr_sum + arr[window길이](직후) - arr[k-window길이]
    #         윈도우길이를 3이라고 치면, 012를 먼저 구해놓고, 3부터 원소1개씩 직후로서 더하고 / 3-3 =0(직전구간의 시작)을 뺀다
    #  012345  마지막에서부터 2번째   len()-1-2 == 마지막인덱스-2 == 5 -2 == 현재인덱스- 번째
    #        [0 12]3 -> 3에서부터 윈도우길이번째 => 3 - window길이
    ## => 직전과의 연산은 0번째를 현재의 값을 미리 구해놓고 1번째원소부터 돌린다.
    ## => 1번째의 idx는 움직이는 구간의 길이부터 시작하면 된다 (0~179 미리 구함) -> range(180, 끝까지 1칸씩)
    ## => greedy에서는 최대합일 때의 idx를 찾아야므로 해당 가변변수도 선언한다.
    # (1) 앞쪽 첫번째구간의 sum을 미리 구해둔다.
    curr_sum = sum(total_seconds[:adv_seconds])

    max_sum = curr_sum
    max_idx = 0
    # (2) window바로 직후의 index부터 시작하여 직후원소로 취급하고, 직전원소는 arr[i - 윈도우길이만큼뒤로]로 사용한다
    ## -> 값의 계산에서는 index1개 추가한 것은 계산에 넣지 않기 때문에 끝index - 1까지 돈다
    for i in range(adv_seconds, play_seconds):
        curr_sum = curr_sum + total_seconds[i] - total_seconds[i - adv_seconds]

        if curr_sum > max_sum:
            max_sum = curr_sum
            #### 광고시작시작은, 1~n초면, 1을 기록해야한다.
            #### 현재 window의 끝에 i가 물려있기 때문에, i에서 - windw길이만큼 간상태에서 +1을 해야 windwo시작부분이다.
            ##       0[123] ->  윈도우직전 = 3 - 윈도우길이
            ##              -> 윈도수시작 = 3 - 윈도우길이 + 1
            max_idx = i - adv_seconds + 1

    # print(max_idx) # 5459
    ## 시작 초를 시분초로 바꿔서  반환해준다.
    ## => 시분초 형태를 00을 붙여허 해야한다면 0으로 2칸을 채우도록 02d를 넣어주도록 formmating하면 된다.
    # hh, r = divmod(max_idx, 3600)
    # mm, ss = divmod(r, 60)
    # answer = f'{hh:02d}:{mm:02d}:{ss:02d}'
    # 01:30:59
    answer = f'{max_idx//3600:02d}:{max_idx//60 % 60:02d}:{max_idx % 60:02d}'
    print(answer)




