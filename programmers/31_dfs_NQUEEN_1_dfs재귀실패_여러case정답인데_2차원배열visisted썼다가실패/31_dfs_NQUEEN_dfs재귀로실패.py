import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000_000)


def dfs(n, D,
        k, q_count, coord, visited):

    if q_count == n:
        return 1
    ## q_count가 증가안하는 경우 계속 탐색한다?
    # => 방지하기 위해 nbyn만큼 탐색하면 종료?!
    if k == n**2:
        return 0


    row, col = coord
    ## q_count를 올릴 수 있는지 확인
    # (1) 해당row의 모든 칼럼이 False인지 확인
    is_available = True
    if any(visited[row][i] for i in range(len(visited))):
        is_available = False
    if any(visited[i][col] for i in range(len(visited))):
        is_available = False
    ## 대각선은.. 현재위치에서 (-1, +1) 최대n-1번, (1, -1) 최대
    #                      (-1, -1)         (1, 1) 최대
    #   단 범위 필터링 매번하기
    if any([visited[row - i][col + i] for i in range(n) if 0 <= (row - i) <= n - 1 and 0 <= (col + i) <= n - 1]):
        is_available = False
    if any([visited[row - i][col - i] for i in range(n) if 0 <= (row - i) <= n - 1 and 0 <= (col - i) <= n - 1]):
        is_available = False
    if any([visited[row + i][col + i] for i in range(n) if 0 <= (row + i) <= n - 1 and 0 <= (col + i) <= n - 1]):
        is_available = False
    if any([visited[row + i][col - i] for i in range(n) if 0 <= (row + i) <= n - 1 and 0 <= (col - i) <= n - 1]):
        is_available = False

    return

    print(row, col, visited)

    total_count = 0
    for drow, dcol in D:
        nrow, ncol = row + drow, col + dcol
        if not (0 <= nrow <= n - 1) or not (0 <= ncol <= n - 1):
            continue
        temp = visited[row][col]
        visited[row][col] = is_available
        temp_result = dfs(n, D,
                          k + 1, q_count + is_available, (nrow, ncol), visited)
        visited[row][col] = temp

        if temp_result:
            total_count += temp_result

    return total_count


if __name__ == '__main__':
    ## N-queen: https://school.programmers.co.kr/learn/courses/30/lessons/12952
    n = int(input().strip())

    # (1) 1개의 경로만 탐색하는 꼬리재귀인 경우, stack dfs로 풀 수 있고, 내부에서 visited선언해서 1개만 쓰면 된다.
    # => 하지만, 여러 경로를 다 찾아야하는 재귀인 경우, 1차원은 used_bit, 2차원부터는 무조건 배열을 들고 다녀야한다?!
    visited = [[False] * n for _ in range(n)]

    ## 현재좌표를 선택하면 -> 해당row, col line은 모두 탐색 불가능한 위치가 된다.
    ## 총 4개를 선택해야한다. => dfs로 탐색해나가면서 선택수 ==4를 만족하게 하자
    # dfs(n, q_count, visited, result)
    D = ((-1, 0), (1, 0), (0, -1), (0, 1),)
    print(dfs(n, D,
              0, 0, (0, 0), visited))

    ## 2차원배열(dict포함)은 깊은복사 안되는 구나.
    # => 매 자식마다 변경 후  자식node 뻗거 올라올때 복구해주기
    # a = [[1],[2]]
    # b = list(a)
    # b[0][0] = 3
    # print(a,b)
