import sys
from collections import deque

input = sys.stdin.readline


# def bfs(s_row, s_col):
def bfs(images):
    ## (1) bfs는 visited든 distance든 상태배열을 가지고 출발한다.
    visited = [[False] * m for _ in range(n)]
    DELTA = ((-1, 0), (1, 0), (0, -1), (0, 1)) # 4방향 좌표탐색을 위한 dir

    ## 색(1~)별 갯수 매핑 배열 ? X 끊기면 따로따로 -> 동적으로 연결한다.
    result = []

    ## (2) bfs는 원래 시작좌표가 정해지고 4방향 탐색하지만,
    ##    여기서는 색이 같은 좌표만 탐색하고 끊긴다 => 시작좌표가 계속 탐색할 수 있게
    ##   => 시작좌표에도 예외적으로 방문체크까지 해준다. (원래는 방문표시 + inqueue)
    for s_row in range(len(images)):
        for s_col in range(len(images[s_row])):
            ## (3) 시작좌표라면 방무체크 생략하고 넣고 갔는데, 여러 시작좌표를 순회한다면 방문체크하고 넣어준다.
            if visited[s_row][s_col]: continue
            ## (2) 테이블 다음은 queue를 만들고, (시작좌표1개시 첫번째 node는 방문체크생략)하고 방문표시 + append하고 pop해서 기준이되어 다음node들 탐색
            visited[s_row][s_col] = True
            q = deque([])
            q.append((s_row, s_col))

            ## (4) 각 시작좌표마다 bfs탐색한 좌표를 카운팅할 변수 -> pop될때마다 +1할 수 있게 한다
            curr_area_counter = 0

            ## (5) queue는 [존재할 때 -> 첫 기준을 빼서] 직후들 or 다음node들을 탐색한다.
            while q:
                row, col = q.popleft()
                # print(row, col)

                ## peek에 있는 직후들과 비교할게 아니라, 꺼낼때마다 카운팅하게 한다.
                curr_area_counter += 1

                for d_row, d_col in DELTA:
                    n_row, n_col = row + d_row, col + d_col
                    ## (6) queue와 무관하게 [이동좌표 검사]  +  [색 같은지 검사]
                    if not (0 <= n_row <= n - 1) or not (0 <= n_col <= m - 1): continue
                    if images[row][col] != images[n_row][n_col]: continue
                    ## (7) inquee전 방문체크 -> 방문표시 -> inqueue
                    if visited[n_row][n_col]: continue
                    visited[n_row][n_col] = True
                    q.append((n_row, n_col))

            ## (8) 매 시작좌표 출발 bfs마다 카운팅을 저장한다.
            result.append(curr_area_counter)

    # print(result)
    return len(result)


if __name__ == '__main__':
    ## floodfill: https://velog.io/@rapsby/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-FloodFill-python
    ## input: https://chaelinyeo.github.io/%EC%BD%94%ED%85%8C/Level03FloodFill/
    n, m = map(int, input().split())
    images = []
    for _ in range(int(input().strip())):
        row = list(map(int, input().split()))
        images.append(row)

    ## [1] bfs는 다음node가 없으면, queue에 안담기고 끊겨버린다. -> while q이후 끝나버린다.
    ##     images board에서 같은 색만 탐색하며 카운팅해야한다
    ##     색이 끊기면, bfs가 끊기므로, => images를 for m for n 으로 하나하나 탐색하면서
    ##     [방문하지 않은 색의 좌표가 나올때마다 =>  매번 bfs 탐색 시작]을 해야한다.
    ## => 시작좌표를 정해놓지 않고, 내부에서 영역별 매번bfs 탐색을 위해 2차원배열을 돈다.
    print(bfs(images))
