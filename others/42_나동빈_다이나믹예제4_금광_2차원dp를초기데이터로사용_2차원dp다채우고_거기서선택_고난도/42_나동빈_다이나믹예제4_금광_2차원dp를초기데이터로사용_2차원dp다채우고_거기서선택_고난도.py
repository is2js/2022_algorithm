import sys

input = sys.stdin.readline


def process():
    # ######### 내 풀이
    # n, m = map(int, input().split())
    # lst_2d = list(map(int, input().split()))
    # # 열의 갯수만큼 구간을 만들고, 구간index * 열의갯수 + 현재열수로 해당구간의 요소들을 컨트롤 할 수 있다?!
    # board = []
    # for i in range(len(lst_2d) // m):
    #     board.append(lst_2d[i * m: (i + 1) * m])
    #
    # # f(i) = k(i번재열 3택1) + f(i-1)
    # # => 무조건 택1이 아니라, 제한이 있다. 만약, 맨 아래나 맨위에서 정답이 나온 경우, 다음열의 반대끝은 선택할 수 없음.
    # # => f(i)를 결정짓는 경우의 수를 나누어서 생각한다. 0행택 / 1행택 / 2행택 .. / m-1행택
    # # => 저것들을 f(i-1)의 부분문제로 생각해야한다. 0과 m-1행의 값을 k로 택한 경우, 2가지f(i-1), 그외에는 3가지f(i-1)의 경우가 생긴다.
    # # => 3가지 경우로 하되, 저것들을 에외처리시켜야한다.
    # # => 또한, 3가지 방향이 존재하므로, 열만 변수화시킬게 아니라 행도 변수화해서
    # #    dp table또한, 행을 포함한 2차원 dp테이블을 만들어야한다.
    # # f(i) = k가 맨위의 행인 경우 -> f(i-1) : f(1, i-1) or f(2,i-1) => f(0, i-1)을 제외시킨다. => 그 경우만 부분문제 대신 0으로 두고, max시킨다?!
    # #        k가 맨아래 행인 경우 ->          f(m-2, i-1) or  f(m-3,i-1) => f(m-1,i-1)을 제외시킨다 => 그 경우만
    # #
    # d = [0] * m
    # # 점화식에 i-1이 존재하므로 0번은 채우고, 1번부터 하자.
    # d[0] = max(board[x][0] for x in range(n))
    #
    # for i in range(1, m):
    #     for x in range(n):
    #         k = board[x][i]
    #         d[i] = max(d[i], k + d[i - 1])
    #
    # print(d)

    ###### 강의 풀이
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    ## (1) dp table을 2차원으로 생성하기 위해 빈 list를 만든다.
    # -> row별 받을 것이므로, 빈 list에 x list를 append하여 행렬을 만든다
    dp = []
    ## (2) 2차원dp는 dp table이자, data행렬이다.
    # -> 초기데이터를 다 넣어놓는다.
    # => 각 dp가 max갚을 찾도록 초기데이터보다 더 커질 것이기 때문에, 최소값이 들어가있다고 보면 된다.(0열 제외)
    # -> m개씩 끊어서 append하는 방법은 array[index : index + m]로 1개의 row를 잡고 구간의첫째항인 index를 m개씩 높여가면 된다.
    # -> 내 방법이 더 좋다 len//구간갯수 -> 0부터 시작하는 구간index ->  구간index * m + 열인덱스(0~m-1)로 반복문속에서 각 구간데이터 다 접근
    index = 0
    for _ in range(n):
        dp.append(data[index:index + m])
        index += m
    # 이미 초기항들이 dp.테이블에 차있어서 추가로 채울 필요는 없다.

    ## (3) 다이나믹 프로그래밍 시작(0열은 현재 값이 최대값이다. 1열부터 시작한다)
    # -> f(i,j) = row반복문k + f(왼위i-1,j-1) + f(왼i,j-1) + f(왼아래i+1,j-1)
    #            이 때, row가 0행이거나, n-1행일 때는, 각각, 왼위와 왼아래에서 못온다 -> 식에서 0으로 치환해서 막아주기
    # => 택1재귀식에다가, 2차원으로서 조건까지 걸려있는 문제이다.
    # (3-1) 구하고 싶은 dp열인 m-1열까지 dp를 채워나가도록 돌린다.
    for col in range(1, m):
        # (3-2) row를 돌리면서 k를 선택하되, 0/n-1은 왼위/왼아래는 최대값찾는데 보탬이 안되도록 0을 걸어주면 된다.
        # -> 일단 각 k에 대해 3가지 경우의수를 먼저 만든다
        # => 연쇄업뎃이 아니라, 경우 하나하나를 만들어야지 -> if조건에 따라 무시할 수 있는 상황?!
        for row in range(n):
            k = dp[row][col]
            # (3-3) 선택한 row별 k에 따라, 왼쪽에서 오는 3가지 경우 중, row가 0 or n-1일 때는 제외시키기 위해
            # => 각 부분문제들만 변수화 시킨다.
            left_up = dp[row - 1][col - 1] if row != 0 else 0  # 첫번째 행일 경우, 부분문제 left_up은 0으로 대체하고, max시 사라지게 한다.
            left_down = dp[row + 1][col - 1] if row != n - 1 else 0  # 첫번째 행일 경우, 부분문제 left_up은 0으로 대체하고, max시 사라지게 한다.
            left = dp[row][col - 1]
            # (3-4) 1개 k에 대한, 각 부분문제들을 모아 택1한다.
            # -> 초기값 + 부분문제들로 전해온 값 택1
            dp[row][col] = dp[row][col] + max(left_up, left, left_down)
    # 각 row별 k마다 최대값을 만드는 k + 부분문제를 해결하면서, 0~n-1까지 다돌았으니
    # dp m-1열 전체가 다차있는 상황이다.
    # (4) m-1열에 있는 k 중에서 가장 큰 것을 다시 뽑아야한다.
    # => 아~~ 2차원dp는, 해당 line의 경우의수를 먼저 다채우고,그 중에서 뽑으면 되는 구나...
    print(max (dp[row][m-1] for row in range(n) ) )


if __name__ == '__main__':
    ## 금광
    # nxm크기의 금광, 0열에서부터 다음열의 값중 택1하여 m-1열까지 1개씩 금광을 선택해 금의 최대크기 산출
    # T
    # 매 T마다 n m / 거기에 차있는 금광의 갯수
    # ai = i번째열 중 택1 + ai-1
    for _ in range(int(input().strip())):
        process()
