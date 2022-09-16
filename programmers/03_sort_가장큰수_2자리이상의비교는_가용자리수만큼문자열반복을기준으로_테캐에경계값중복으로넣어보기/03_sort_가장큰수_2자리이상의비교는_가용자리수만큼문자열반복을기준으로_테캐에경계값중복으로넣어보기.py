import heapq as pq
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    numbers = list(map(int, input().split()))
    # (1)가장 앞자리 숫자가 큰 것을 골라낸다.
    # -> 앞 자리 1글자를 가져오려면 string으로 변환해서 첫번재를 가져오는 것이 최고다.
    # -> 그 custom한 순서대로 가져오려면, sort lambda를 활용한다.
    # sorted_lst = sorted(map(str, numbers), key=lambda x: (x[0], int(x)), reverse=True)
    sorted_lst = sorted(map(str, numbers), key=lambda x: int((x * 4)[:3 + 1]), reverse=True)

    ## 이 조건이 없으면 테케 1개 걸린다.
    # => 테캐확인은 경계값을 중복해서 넣어본다!
    # if sorted_lst[0] == '0':
    #     print('0')
    #     exit()

    print(''.join(sorted_lst))
    # (2) 문제는 30과 34, 3 중에 34 > 30 > 3를 골라내야한다.
    # -> 34와 30은 정렬기준에 int(x)를 넣으면 되지만..
    # -> 30 + 3 보다 3 + 30이 더 크다.
    # => gg

    # (3) 요구사항에 [원소는 1000이하]라고 했다 + [후보 수를 넣으면, 그 뒤로는 더 작은 수]밖에 못온다.
    #     34 + 첫자리가  3이하이면서, 그 뒤로는 더 작은 수들이 붙는다.
    #     -> 34 3x(3이하)
    #     -> 30 34(x)
    # => 암기: 큰 수를 만드려면,
    #     (1) 1자리면 첫자리만 비교하고 끝낼 수 있으나
    #     (2) 2자리 이상의 수들이 비교되면, 문제요구사항에서 maximum자리수가 주어지니
    #         34 -> 3434|34가 최대이므로 그 이하 / 30 -> 3030이 최대
    #         343 -> 3433|43이 최대
    #         342 -> 3423|42이 최대
    #         => 숫자문자열을 반복하되 maximum자리수까지 짤랐을 때,그 때 큰 값이, 가장 큰 수를 만든다.
    #         3   -> 3333|33
    #         30  -> 3030|30

    pass
