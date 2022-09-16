import sys

input = sys.stdin.readline
sys.setrecursionlimit(100_000)


def spair(numbers, N,
          select_count=0, used_bit=0, result=[]):
    # print(select_count)
    # if select_count == N and bin(used_bit).count('1') == 10:
    if select_count == N:  # 종착역의 조건을 stack변수외에 추가조건을 까다롭게 주면, 종착역을 지나쳐버릴 수 있따!!!!!!!!!
        # if bin(used_bit).count('1') == 10:
        if used_bit == (1 << 10) - 1:
            # print(result)
            # print(bin(used_bit))
            # return [result]
            return 1
        else:
            # 종착역에 추가조건이 붙을 경우, 추가조건 만족못하면 종료시켜야지 안건너띈다?!
            # return None
            return 0

    # total_result = []
    total_count = 0
    if select_count == 0:
        for i in range(1, 9 + 1):
            # if bin(used_bit).count('1') < 10 and used_bit & (1 << i):
            #     continue
            # if select_count >=5 :
            #     print(result)

            # if select_count == 0 and i == 0:
            #     continue
            # if select_count != 0 and abs(result[-1] - numbers[i]) != 1:
            #     continue

            # print(result)
            temp_result = spair(numbers, N,
                                select_count + 1, used_bit | (1 << i), list(result + [numbers[i]]))
            # 종착역에 내부 추가조건을 만족못하는 경우, else return None을 걸음. -> 반환값 집계 처리 안되게
            # if temp_result:
            #     for answer in temp_result:
            #         total_result.append(answer)
            # if temp_result:
            total_count += temp_result
    else:
        prev_number = result[-1]
        next_numbers = prev_number + 1, prev_number - 1
        for n in next_numbers:
            if n not in numbers:
                continue
            # if used_bit & (1 << n):
            #     continue
            temp_result = spair(numbers, N,
                                select_count + 1, used_bit | (1 << n), list(result + [n]))
            total_count += temp_result
            print(result)

    # return total_result
    return total_count % 1_000_000_000


if __name__ == '__main__':
    ## boj 계단수: https://www.acmicpc.net/problem/1562
    # 풀이블로그: https://peisea0830.tistory.com/56
    N = int(input().strip())

    numbers = list(range(10))
    print(spair(numbers, N))
