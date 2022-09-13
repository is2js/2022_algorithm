import sys

input = sys.stdin.readline


def solve(f_h_count, f_v_count, srt_row, srt_col, end_row, end_col):
    # if f_h_count + f_v_count == 2 * k:
    # (3) 카운팅  총합으로 차지한다면, 각각 k번이 아니라 2k-2 + 2번으로 종착역이 마련될 수 있다.
    # -> 카운팅을 나눠서 하는 이유가 있다.
    if f_h_count == k and f_v_count == k:
        # (2) 종착역은 1개의 점이며, h가 들어갈 위치는 값으로 대신한다.
        # -> 업데이트되는 어느 좌표 중 시작점 or 끝점 어느 것을 써도 1개의 점인 상태다. 값을 넣어준다.
        paper[srt_row][srt_col] = h
        # (4)
        # - R D D R
        # 0 0 0 0
        # 0 0 0 0
        # 0 0 0 0
        # 0 0 0 3 <-- 2**k크기의 paper를 다 접고나면, 1개의 좌표(문제상 단위행렬)에 h값이 박힌다.

        # - L U U L
        # 3 0 0 0 <--
        # 0 0 0 0
        # 0 0 0 0
        # 0 0 0 0
        return

    #  자신의처리 -> 택1연산의 재귀에서는, 업데이트 변수만 처리해서 넘겨주고, 자신의 처리는 없다.
    #           -> 종착역도 자신의 처리는 없게되어, 직전에서 모든 처리가 끝난다?!
    # 0부터 시작하는 카운트변수가 있다면, 특정배열에서 꺼내는 순서와 매핑할 수 있다.
    fold = folds[f_h_count + f_v_count]  # 카운팅 순서대로 나온다 (count는 1씩 증가해야한다)

    # 택1연산으로서, 해당방법에 맞게 변수들을 업데이트하여 다음재귀를 호출한다.
    # -> D로 접으면, row좌표가 달라지고, col좌표는 그대로이다.
    # -> 접으면, 절반보다 1칸 더 가는 위치에 있어야한다. -> s+e//2 + 1
    if fold == 'D':
        solve(f_h_count, f_v_count + 1, (srt_row + end_row) // 2 + 1, srt_col, end_row, end_col)
        # (5) 2k번 접히면, 1개의 좌표로 이동되는데, 여기서부터 재귀를 빽하는 부분은 [펴는 행위]가 된다.
        #     택1연산 'D'이후 back했다면, [종착역 처리(종점에 h할당)이후 'D'에 대한 역 연산]이 이루어진다.
        #     -> 위쪽 방향으로 해당좌표에 h`를 찍어야하는데, h3 -> h`1로 찍혀야한다.
        #        0->2, 1->3, 2->0, 3->1 로 매핑되면서 위쪽에 찍어야한다.
        #     => D 역연산(unfold)에 대한 값을 매핑해야한다.
        #     => U, R, L 역연산(unfold)에 대한 값을 매핑해야하므로, 매핑dict를 먼저 정의하고 오자.
        # (7)
        h_candidates = unfold_values[fold]  # 펴서 찍을 좌표에 대입할 값 h_candidates 의 후보값들
        # (8) 종착역으로 직전으로 생각하면, 현재 업데이트(인자) 전 파라미터들은, 접히기 전 펴진 상태이므로
        #    -> 이 파라미터를 이용해서, 펴진 상태를 처리해야한다.
        #  => 일단, 종착역 직전인지 / 직전의 직전인지 ~ 최초 호출 상태인지를 stack결정변수로 결정해야한다.

        ### 다 하고보니.. [기존시작좌표 기준, 처리해야할 좌표 수]를 만드는 것이었다.

        ## 종착역 직 전(인자 속 변수들은 이미 마지막연산)이라면, +1개 좌표찍기       -> k-1 == f_h_count 일 때,
        ## 종착역 직직 전이라면, +2개 좌표찍기     -> k-2
        ## 종착역 직직직 전이라면, +4개 좌표찍기    -> k-3
        ## 최초 호출이라면(인자 속 변수들은 1번째 연산),  + 2**(k-1) , 1부터 2씩 등비수열.. [총 k개]
        # => [종착역 직전의 재귀호출 아래]에는 [업데이트 인자가 아닌 파라미터를 쓴다면, 마지막 연산이 이루어지는 곳]의 상황이며
        # => 여기서 마지막 연산이, 최초호출부는 첫번재 연산이, 종착역 기준의 k번 이루어진다.
        # => 'D'의 경우, f_v_count가 종착역(2) 직전인 1일 것이며, 최초는 0일 것이며, 총 2번 연산(0으로, 1으로)이 이루어진다
        # => 파라미터를 쓴다면, 종착역직전(2-1, k-1) ~ 최초호출(1-1, 0) 직전의 인자가 사용된다.
        # => 정의부는, 0부터 ~ k-1로 연산이 이루어지고, k는 마킹만 하는 종착역이다.
        # => k-1 일 때, +1 h`마킹 -> 다음은 + 2개 h`마킹 해야한다면
        # -> 첫항1, 등비2, 갯수k개의 등비수열이라서, -> 2**(k-1)로 하면될 것 같지만,
        #    n = 0부터 시작이라면, 일반항을 2**k로 잡고 k=0~n-1까지 돌리면 된다.
        # [2**k for k in range(0, k-1 + 1)]
        # -> 이것을 역순으로 빨아야지, 재귀에 적용되므로 => Range를 역순으로 뽑게 한다.
        # [2 ** k for k in range(k - 1, 0 - 1, -1)]
        # -> 이제 stack결정변수이자, 0부터 처리하는 카운팅변수가 순서에 맞게 뽑아쓰기 위해
        # -> 전역변수 배열로 선언하고, count변수로 하나씩 순서에 맞게 뽑아 쓸 수 있게 한다.
        # unfold_count = [2 ** k for k in range(k - 1, 0 - 1, -1)]
        # (10)
        # print(fold, f_v_count, unfold_count[f_v_count])
        # R 1 2
        # D 1 2 -> 종착역 직전에는 1개가 아니라 2개..
        # D 0 4
        # R 0 4
        # 2**i 를 0부터,, k-1까지가아니라, k까지의 역순을 때리니
        # 1(0), 2(1), 4(2) -> 4,2,1 이 나온 상황이고,
        # 재귀안에서는 2 직전인, 1 -> 0 순으로 index르 락져, 1을 무시하고 2->4가 나오게 된다.
        # 그게 아니라, 횟수에 따라 1, 2 만 나와야하므로,,, 다시 수정했따.
        for moving_row in range(unfold_count[f_v_count]):
            # 2 ->4 를 0,1    0,1,2,3으로 돌리면서 직전의 srt_row에 +@ 될 좌표로 사용한다.
            # 모든 열을 다 돌면서, D의 반대인
            for col in range(srt_col, end_col + 1):
                # 접히기 전 row로 돌아가서, 거기서부터 1개, 거기서부터 2개씩 내려가며 처리해줘야한다.
                # paper[srt_row + x][y] = f"check{f_v_count, unfold_count[f_v_count]}"
                # -> 직전좌표기준으로, 참조할 좌표를 확인한 뒤,
                # -> 직전좌표는 start을 index0으로 생각하고 식을 작성하면 된다.
                # ->  대칭 좌표 [len - 1 - 대칭index] = 마지막index - 대칭index
                # paper[srt_row + x][y] = paper[end_row - x][y]
                # -> 이제 각 stack마다, 참조 값h에 따라 stack에 맞게 매핑해주는 h_candidates를 사용해주면 된다.
                paper[srt_row + moving_row][col] = h_candidates[paper[end_row - moving_row][col]]

    elif fold == 'U':
        solve(f_h_count, f_v_count + 1, srt_row, srt_col, (srt_row + end_row) // 2, end_col)

        for moving_row in range(unfold_count[f_v_count]):
            for col in range(srt_col, end_col + 1):
                # 직전stack의 좌표(이미 펴진상태)가 기준이 된다. /srt_는 0으로 생각한다.
                h_candidates = unfold_values[fold]
                paper[end_row - moving_row][col] = h_candidates[paper[srt_row + moving_row][col]]




    elif fold == 'R':
        solve(f_h_count + 1, f_v_count, srt_row, (srt_col + end_col) // 2 + 1, end_row, end_col)

        for row in range(srt_row, end_row + 1):
            for moving_col in range(unfold_count[f_h_count]):
                h_candidates = unfold_values[fold]
                paper[row][srt_col + moving_col] = h_candidates[paper[row][end_col - moving_col]]
    else:  # L
        solve(f_h_count + 1, f_v_count, srt_row, srt_col, end_row, (srt_col + end_col) // 2)

        for row in range(srt_row, end_row + 1):
            for moving_col in range(unfold_count[f_h_count]):
                h_candidates = unfold_values[fold]
                paper[row][end_col - moving_col] = h_candidates[paper[row][srt_col + moving_col]]


if __name__ == '__main__':
    ## 종이접기: https://www.acmicpc.net/problem/20187
    # -> 사각형이 줄어든다 == 분할정복 -> 재귀
    # -> 가능한 연산들 중 택1 -> 재귀내에서 if문으로 1가지만 택해서 나아간다
    # -> 접었다가 다시 편다 -> backtracking으로서, 다음재귀호출 후 아래 연산이 있다.
    # -> 다접으면 1by1정사각형이 나오는데, 이것을 2by2행렬로 보지않고, 1개의 점으로 본다.
    #    0123는 좌표로 보지 않고 1개의 값으로 본다.

    k = int(input().strip())
    folds = input().split()
    h = int(input().strip())  # 1by1정사각형의 좌표가 아니라, 1개 점(좌표) 속의 값으로만 본다.

    # (6)
    unfold_values = {
        # 0, 1, 2, 3의 역연산시 매핑되는 값
        'D': [2, 3, 0, 1],
        'U': [2, 3, 0, 1],
        'R': [1, 0, 3, 2],
        'L': [1, 0, 3, 2],
    }

    # (9) stack 스택 변수에 맞게, 뽑아 쓰는 [펼 때, 찍어야하는 좌표 갯수]
    unfold_count = [2 ** i for i in range(k - 1, 0 - 1, -1)]
    # print(unfold_count) #  [4, 2, 1]
    # -
    # 2번 접는다면, k==2가 종착역이라서, k==1일 때, 1이 나와야한다
    # k==0일 때, 2개 나와야한다.
    # unfold_count = [2 ** k for k in range(k, 0 - 1, -1)]
    # print(unfold_count) # [4, 2, 1] # 각 방향별 k번 접는데,

    # (1) stack결정변수는, 총 2k번 접으면 종착역 -> 접는 횟수가 stack결정변수인데
    #   -> 통합해서 카운팅한다면, 2k-2 + 2번으로 재귀가 굴러갈 수 있기 때문에
    #     나눠서 k번, k번 카운팅되도록 해서 종착역을 and로 잡아야 재귀가 굴러가더라도 제대로 멈춘다.
    #     + 택1연산마다, 세로로 접기도하고, 가로로 접기도 하는데, 현 상황을 알려주기 위해, 나눠서 conting해야한다.

    #     택1해서 node를 시작하므로, roo에서는 자신의 처리가 없다.
    #     전역변수 paper에, 종착역일 때 단위행렬에 점을 찍고, 백트래킹하면서, 계쏙 찍는다.
    #    -> 업데이트변수는 접힌 사각형의 시작좌표/끝좌표들이다. (start_row, end_row, start_col, end_col)
    #       나는 tuple(X) -> 업뎃어려움 -> 순서만 start_row, start_col, end_row, end_col
    #       0,0부터 끝좌표는 2**k-1, 2**k-1 인데=> 2**k를 N으로 변수로 만들어서 쓴다.
    N = 2 ** k
    paper = [[0] * N for _ in range(N)]
    #    -> 택1연산에서는, root_node에선 자신의 처리없이, if분기로 각 case마다 재귀를 걸어준다.
    solve(0, 0, 0, 0, N - 1, N - 1)

    for row in paper:
        print(*row)

