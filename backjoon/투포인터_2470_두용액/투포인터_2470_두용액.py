import sys

input = sys.stdin.readline

if __name__ == '__main__':
    # 두 용액:  https://www.acmicpc.net/problem/2470
    # 배열에서  두 수의 [합] 이 0에 가까운 것
    # -> 교환법칙 성립문제 -> 조합 -> 조합은 2~3개 정도는 투포인터로 풀어야 빠르다.

    N = int(input().strip())
    numbers = list(map(int, input().split()))
    # 1) 투포인터는 작으면 start+=1 크면 end-=1을 조정하기 위해 배열을 정렬해놓고 돌린다.
    numbers.sort()

    # 2) 투 포인터는 start, end를 가변변수로 직접 지정하고 -> while str < end로 돌리면서 둘중에 하나를 업데이트한다.
    start_index = 0
    end_index = len(numbers) - 1

    prev_abs_sum = float('inf')
    prev_answer = []
    while start_index < end_index:
        case_sum = numbers[start_index] + numbers[end_index]
        if abs(case_sum) < prev_abs_sum:
            prev_abs_sum = abs(case_sum)
            prev_answer = [numbers[start_index], numbers[end_index]]
            if case_sum == 0:
                break
        if case_sum > 0:
            end_index -= 1
            continue

        start_index += 1

    print(*prev_answer)