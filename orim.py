# https://jinomadstory.tistory.com/43
import sys
import random

sys.setrecursionlimit(2_000_000_000)


def simulator(level, cost, try_count, wanted_level):
    if level == wanted_level:
        return cost, try_count

    event = random.choices(['성공', '유지', '실패'], weights=강화_확률[level])[0]

    temp_total_cost = 0
    temp_total_count = 0

    if event == '성공':
        result = simulator(level + 1, cost + 회당_가격, try_count + 1, wanted_level)
        if result:
            temp_cost, temp_count = result
            temp_total_cost += temp_cost
            temp_total_count += temp_count

    elif event == '유지':
        result = simulator(level, cost + 회당_가격, try_count + 1, wanted_level)
        if result:
            temp_cost, temp_count = result
            temp_total_cost += temp_cost
            temp_total_count += temp_count

    else:
        result = simulator(level if not level else level - 1, cost + 회당_가격, try_count + 1, wanted_level)
        if result:
            temp_cost, temp_count = result
            temp_total_cost += temp_cost
            temp_total_count += temp_count

    return temp_total_cost, temp_total_count


def reinforce(목표_강화_수치_, 목표강화별_시뮬_수_):
    global count
    result = []
    for level in range(목표_강화_수치_):
        cost_per_level = 0
        count_per_level = 0
        for _ in range(목표강화별_시뮬_수_[level]):
            cost, count = simulator(0, 0, 0, level + 1)
            cost_per_level += cost
            count_per_level += count
        expected_count = count_per_level / 목표강화별_시뮬_수_[level]
        expected_cost = cost_per_level / 목표강화별_시뮬_수_[level]

        result.append((level + 1, 목표강화별_시뮬_수_[level], expected_count, expected_cost))

    print(f'{"인첸레벨":>4s},{" 시뮬 수":>4s},{"기대시도횟수":>17s},{"기대금액":>17s},{"직전과의 차이":>17s}')
    prev_exp_cost = 0
    for i, (wanted_level, simul_count, ex_count, exp_cost) in enumerate(result):
        print(
            f'{wanted_level:>6d},{simul_count:>7d},{ex_count:>20.3f},{exp_cost:20.3f},{exp_cost - prev_exp_cost if prev_exp_cost else 0 :20.3f}')
        prev_exp_cost = exp_cost


if __name__ == '__main__':
    목표_강화_수치 = 8

    회당_가격 = 7_434

    강화_확률 = (
        # (성공, 유지, 실패)
        (0.45, 0.55, 0.00),  # 0 -> 1강
        (0.40, 0.58, 0.02),
        (0.30, 0.67, 0.03),
        (0.20, 0.75, 0.05),
        (0.10, 0.75, 0.15),
        (0.04, 0.75, 0.21),
        (0.02, 0.75, 0.23),  # 6 -> 7강
        (0.01, 0.75, 0.24),  # 7 -> 8강
    )

    목표강화별_시뮬_수 = [
        1_000,  # 0 -> 1강 :  최대 2000회
        1_000,
        1_000,
        1_000,
        1_000,
        1_000,
        1_00,    # 6 -> 7강 :   100회를 여러번 해보면서 감잡는 게 좋을 듯
        1_00,
    ]

    reinforce(목표_강화_수치_=목표_강화_수치, 목표강화별_시뮬_수_=목표강화별_시뮬_수)
