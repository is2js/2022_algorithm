import sys
from collections import defaultdict

input = sys.stdin.readline

if __name__ == '__main__':
    ## 실패율: https://school.programmers.co.kr/learn/courses/30/lessons/42889
    N = int(input().strip())
    stages = list(map(int, input().split()))

    stage_try = defaultdict(int)
    stage_complete = defaultdict(int)

    for comp_stage in stages:
        stage_try[comp_stage] += 1

        for i in range(1, comp_stage):
            stage_complete[i] += 1

    stage_total = defaultdict(int)
    fail_rate = defaultdict(float)
    for i in range(1, N + 1):
        stage_total[i] = stage_try[i] + stage_complete[i]
        if stage_total[i]:
            fail_rate[i] = stage_try[i] / stage_total[i]
        else:
            fail_rate[i] = 0

    result = []
    for stage, rate in fail_rate.items():
        result.append((stage, rate))

    print([stage for stage, rate in sorted(result, key=lambda x: x[1], reverse=True)])


