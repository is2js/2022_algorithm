import sys
from collections import deque as dq

input = sys.stdin.readline


def find_start_direction_and_move_count(q, value):
    position = q.index(value)
    mid_index = (0 + len(q) - 1) // 2
    if position <= mid_index:
        # return 'left', position
        # => 회전횟수는 0일 떄, 1번 rotate시키고 1이라면, 0/1 2번 rotate시켜야하므로  [차이갯수]로서 [index차이 + 1]해줘야한다.
        # return 'left', position + 1
        # => 0번위치까지 이동횟수는 index번이다.
        return 'left', position
    # => 오른쪽에서는 0번index까지 위치시킬려면 endindex까지 이동횟수 + 1번 더 rotate해야한다.
    # return 'right', len(q) - 1 - position
    return 'right', len(q) - 1 - position + 1


if __name__ == '__main__':
    ## index 앞에서 가까운지 뒤에서 가까운지 판단하기
    # lst = list(range(1, 10 + 1))
    # # print(lst)
    # # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #
    # # 7의 앞에서부터 거리 vs 뒤에서부터의 거리
    # # -> 가운데를 기준으로 왼족에 있는지 vs 오른쪽에 있는지 보면 된다.
    # # (1) si + ei // 2  :  가운데 or 왼쪽이다.
    # mid = (0 + len(lst) - 1) // 2
    # # (2) 7의 index를 뽑는다.
    # target = lst.index(7)
    # if target <= mid:
    #     print("왼쪽 또는 가운데라서, 앞에서부터 출발")
    # else:
    #     print("가운데보다 오른쪽, 뒤에서부터 출발")
    # 왼쪽 또는 가운데라서, 앞에서부터 출발

    ## bj: 회전하는 큐 : https://www.acmicpc.net/problem/1021
    N, M = map(int, input().split())
    positions = list(map(int, input().split()))
    q = dq(list(range(1, N + 1)))
    total_move_count = 0
    ## 문제에서는 rotate전 index를 주는데, index는 바뀌므로, value로 기억했다가, .index(value)로 회전후 index를 찾아야한다.
    values = [q[x - 1] for x in positions]
    for value in values:
        direction, move_count = find_start_direction_and_move_count(q, value)
        q.rotate(move_count * (-1 if direction == 'left' else 1))
        # => rotate횟수 - 1 =  0번에 위치까지 위치시키는 횟수
        # 01* => rotate횟수는 3번해야지 완료되나, [문제요구 move횟수는 2번]
        total_move_count += move_count if direction == 'left' else move_count
        # => popleft 횟수는 카운팅 안한다
        q.popleft()

    print(total_move_count)
