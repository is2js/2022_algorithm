import sys

input = sys.stdin.readline

if __name__ == '__main__':
    # boj 세 용액: https://www.acmicpc.net/problem/2473
    # 세 수의 합 -> 배열에서 2개이상의 원소를 나열하는 경우의 수 -> 순열or조합
    # -> 합 문제 ==교환법칙성립(순서영향x) ==조합으로 나열
    # 조합을 재귀로 풀면 O(N) + O(선택 N) * O(선택X N) -> 시간초과긴 하다.
    # => 조합 문제는 순서와 상관없기 때문에
    #    [주어진 배열순서가 고정되어있다고 가정]하고 푼다
    #    [순회시 1번 확인한 뒤로는 안돌아간다] -> 재귀에서는 pos가 무조건 증가 pos+1 업데이트 된다
    #                                    -> 반복문에서는 i선택 후 -> i+1부터 탐색한다
    #    조합문제에서, 2~3개는 투포인터로 풀자! -> 시간 더 절약한다.
    #               재귀는 안뽑은 재귀도 포함되고, 종착역에서 예외처리해주니, 훨씬 더 오래 탐색한다
    N = int(input().strip())
    numbers = list(map(int, input().split()))

    # 교훈) 조합/투포인터는 이미 순서가 고정되었다고 가정하기 때문에, 미리 정렬해줘도 좋다.
    numbers.sort()

    # 전체반복문에서, 만족하는 배열을 저장할 것임
    answer = [] # lst라고 꼭 append안해도 됨. 빈lst로 초기화해놓고, 재할당 업데이트 해도 된다.
    min_of_absolute_sum = float('inf')

    # 교훈) 3개뽑는 투포인터는 i, i+1 -> range(N-2):처럼,
    # -> 돌아가는 포인터2개를 빼고 제외하고 바깥을 돌린다.
    for i in range(N - 2):
        # 교훈) 투포인터는 i+1이 1개 + 끝에서 출발하는 1개 2개로 구성되어어서 반대방향으로 온다.
        srt_index = i + 1
        end_index = len(numbers) - 1

        first_value = numbers[i]

        # 교훈) 투포인터는, start < end로 만나기 직전까지 돌린다.
        while srt_index < end_index:
            # 문제에서 요구하는 것은 3값의 합 abs의 최소값 찾기다.
            current_sum = first_value + numbers[srt_index] + numbers[end_index]
            # 당시의 값들도 알아야하기 때문에 min()메서드 업데이트는 안된다.
            if abs(current_sum) < abs(min_of_absolute_sum):
                min_of_absolute_sum = abs(current_sum)
                answer = [first_value, numbers[srt_index], numbers[end_index]]

            # 교훈) 요구사항을 찾기위한 업데이트 와중에 , 무조건 정답이 찾아진다면
            # -> 가변변수에 업데이트 해놨으면, 밑에서 if + break;로 처리하면 된다.
            # --> 미리 정렬해놓고 시작해서 [작은 순서대로 찾고 있고, 찾으면 바로 break]할 수 있게 된다.
            if current_sum == 0:
                break

            # 교훈) 투포인터의 업데이트는 각각 경우를 나눠서 1개씩 업데이트되어야
            #      나머지는 고정된 상태로 1칸씩만 움직여 case를 만든다.
            # (1) 아직 합이 음수라면, 키워서 0에  가도록 -> 작은 것을 키우도록 srt를 오른쪽으로 땡긴다
            if current_sum < 0:
                srt_index += 1
                continue
            # (2) 합이 양수라면, 작아지도록 -> end를 앞으로 땡겨 줄인다
            end_index -= 1

    print(*answer)




    pass
