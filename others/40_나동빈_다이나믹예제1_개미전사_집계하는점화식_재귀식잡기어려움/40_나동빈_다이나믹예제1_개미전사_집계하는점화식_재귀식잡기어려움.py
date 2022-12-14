import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## 개미전사
    # -> 첫 줄에 식량창고 갯수
    # -> 2 줄에 저장된 식량 k개 =>
    # -> 인접해서 뽑을 수 없는데, 개미전사가 얻을 수 있는 식량 최대값
    # ex> 1 3 1 5
    # ai -> i번째 식량창고까지의 최적의 해 (순열이 아니므로 고정된 순서로 빽없이 진행)
    # ========> 순서대로 주어진 창고배열을 쪼개어서, f(n)을 만든다.
    #           요구사항은 둘째치고, 4개의 창고 = f(4)로 생각한다.
    #           고정된 것이 아니라 0부터 연속된 문제라고 생각하는 습관
    # a0 a1 a2 a3
    # 1   3  3  8
    # =========>  i번째를 털때를 생각하여 재귀식을 만들어본다.
    #    i-2개   [i-1]  i     => i-1을 털면 i를 털 수 없다.
    #      [i-2] i-1   [ i ]  => i-2을 털면 i를 털 수 있다.
    # => 인접이 금지된 경우, 2가지 부분문제(i-1선택, i-2선택)를 고려하면 i번재 창고를 선택할지/말지여부를 결정할 수 있게 된다.
    # => i번째의 최대식량은?  i-1를 턴 최적의해  -> i못텀 or  i-2를 턴 최적의해 -> i텀
    # ==> 이 2가지 부분문제 중 최대값을 구해야한다.
    # ==> 가능한 2가지 부분문제중 최대값을 구하면, 현재의 최대값이 된다.
    # ==> 단순, 재귀식(f(n-1) + f(n-2))이 아니라, greedy한 재귀식이 된다.(f(n-1) , f(n-2) max)
    # ==========> ai = max(ai-1, ai-2 + ki) ki는 i번째 창고의 식량값
    # my) ai-1은.. i-1번째를 턴 경우일까? i-1을 안털었을 수도 있다?
    #    => i-1을 안털었으면 i-2는 무조건 털엇다 => ai-2
    # + 한칸 이상 떨어진 식량창고는 항상 털 수 있으므로 i-3는 고려할 필요없다,.?!
    # i -> i-1에서 오는 것 중  i-1 식량 선택x or i-2에서 오는 것 중 i-2를 털었을 경우만 해당하는데..

    # my) ai는 2가지 경우의 수를 가진다
    # (1) i번째가 선택안되는 경우 -> a(i-1)과 동일하다
    # (2) i번째가 선택되는 경우 -> i-1는 무조건 선택못한다 -> ki + a(i-2)까지의최대값을 더하는 경우와 동일하다
    # => 2가지 경우의 수 중 max를 선택하면 a(i)가 풀린다.
    # => 부분문제로 푸므로 분할정복이다.
    # => i-1, i-2로 깍여내려가는 문제는, 부분문제가 무조건 중복된다 -> 다이나믹 2가지 중 1가지 선택
    # => 재귀+메모의 탑다운보다는, 반복문+dp테이블의 보텀업을 활용하자.
    ####### 초항을 생각해보면
    # 1 -> 그냥선택 / 1 3 -> 둘중에 큰 것 선택 /
    # 1 3 1 -> 1 1 or 3 ==> 3번째 것을 포함하느냐vs안하느냐로 경우가 나뉘며, 그 중에 큰 것을 골라야한다.
    #  포함하면 1 + 3번째거 , 포함안하면 1 3 중 큰 것 고르는 것과 동일하다.
    # => my) 한칸띄는 인접문제는, 점화식 부분문제를 알아볼 때, i번째 포함 vs 불포함의 경우의 수에서 max의 요구사항을 따진다.
    n = int(input().strip())
    meat_lst = list(map(int, input().split()))

    d = [0] * (n)
    d[0] = meat_lst[0]
    d[1] = max(meat_lst[0], meat_lst[1])

    for i in range(2, n):
        # ai = max(ai-1, lst[i] + ai-2)
        d[i] = max(d[i-1], meat_lst[i] + d[i-2])

    print(d[n-1])

    pass
