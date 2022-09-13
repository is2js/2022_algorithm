import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## 구간합 -> 특정 구간의 모든 수를 합하는 것
    # ex> 10 20 30 40 50  -> 2~4번째수까지의 합 20+30+40 =90
    # => 구간합을 여러번 구해야한다면?

    ## 문제: 구간 합 빠르게 계산하기
    # N개 정수 수열 + M개의 Query정보
    # -> 각 쿼리는 left, Right로 구성됩니다.
    # -> 각 쿼리에 대하여 [Left, Right]구간에 포함된 데이터들의 합을 출력해야합니다.
    # 수행시간 제한은 O(N + M)입니다.
    # N개의 데이터에 대해, M번의 쿼리left ~ right를 새롭게 구간합을 구하려고 한다면, O(NM)이 될 것이다.

    # 접두사합 Prefix Sum -> 배열의 맨 앞ㅇ부터 특정위치까지의 합을 미리 구해놓는 것(객체to필드)
    # => 미리 O(N)으로 구간을 돌면서, 미리 접두사합을 사전에 결과를 기록해놓고, 그것을 이용하는 방법
    # (1) P배열에 N개의 수 위치 각각에 대하여 접두사합을 O(N)으로 미리 계산해놓는다.
    #    -> 0번째 인덱스에는 시작특이점으로서 0을 넣어놓는다?!
    # (2) P[Right] - P[Left-1]
    n = 5
    data = [10, 20, 30, 40, 50]

    # (1) 접두사 합(Prefix sum) 배열 계산
    # -> 매번 누적값이 필요하므로 (1) 누적합 가변변수 (2) 그때마다 저장할 배열 or 빈리스트
    sum_value = 0
    # prefix_sum = [0] * (n + 1)
    prefix_sum = [0] # 시작특이점 객체. 구간은 1번구간부터 시작할 것임.

    # for i in range(len(lst_2d)):
    for number in data: # 해당 수만 누적하고, 그때까지의 누적합을 append만 하면 되므로, index가 아닌 data로 돌린다.
        # (2) 매번 누적변수에 누적하고
        sum_value += number
        # (3) 그때까지의 구간합으로서 저장한다.
        # prefix_sum[i + 1] = sum_value
        prefix_sum.append(sum_value)

    print(prefix_sum[4] - prefix_sum[3 - 1])
