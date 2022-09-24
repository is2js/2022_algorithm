import sys
from collections import deque, defaultdict

input = sys.stdin.readline


def dfs(dirs, visited, row, col):
    stack = []
    ## stack은 넣기전에 방문체킹(중복 추가제거)만하고, 자신의 처리에서 방문체킹(중복 기존제거) + 방문표시한다
    # if visitied[row][col]: continue
    stack.append((row, col))

    coords_of_dir = defaultdict(list)
    counter = 0


    while stack:
        c_row, c_col = stack[-1]

        ## 종착역(다음 탐색 못하는 조건) +
        ## continue가 아닌, 중간break지점!!!!!!!!!!
        ## continue는 [현재node -> 다음node가 없는 것]이어서, [stack에 쌓아둔 다음node로 진행(back후 새 경로)]
        ## break는 [더이상 다른경로도 불가능한 상황]으로 stack에 쌓아둔것과 무관하게 스탑
        if len(dirs) == 0:
            stack.pop()
            break


        # if visited[c_row][c_col]: continue
        ## 방문 체킹(블러킹) -> 재방문 안된다. -> 더이상 진행이 안된다.
        ## 방문을 막지말고, 방문안했으면 ryan +=1
        ## => 생각해보니, [방문(좌표)]을 했더라도, 다른방향에서 간다면, [방문했떤 길]이 아니기 때문ㅇ
        poped_dir = dirs.popleft()
        d_row, d_col = dir_of_move[poped_dir]
        if not visited[c_row][c_col] or (visited[c_row][c_col] and (poped_dir not in coords_of_dir[(c_row, c_col)])):
            counter += 1

        visited[c_row][c_col] = True
        print(c_row, c_col, stack)

        # visited[c_row][c_col].append((d_row, d_col))

        print(dirs)

        n_row, n_col = c_row + d_row, c_col + d_col
        # if not (0 <= n_row <= len(visitied) - 1 and 0 <= n_col <= len(visited) - 1): continue
        if not (0 <= n_row <= len(visited) - 1 and 0 <= n_col <= len(visited) - 1): continue
        # if visited[n_row][n_col]: continue
        stack.append((n_row, n_col))
        coords_of_dir[(n_row, n_col)].append(poped_dir)

    ## dirs길이에 따른 break가 생겼으므로 남은 것 처리해줘야한다?
    ## => 더이상 못가니 따로 해줄필욘 없다?!

    return counter - 1 # 시작좌표는 방문과 무관하게 안친다?!


if __name__ == '__main__':
    ## 방문길이: https://school.programmers.co.kr/learn/courses/30/lessons/49994
    dirs = input().strip()
    ## (1) 일단 음수의 좌표를 가지고 있지만, 길이만큼 생성한다. 시작좌표는 (4,4)
    ##     -5 0 5 총 11개
    visited = [[False] * 11 for _ in range(11)]
    dir_of_move = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1),
    }

    ## 순서대로 좌표탐색하되, 갈 수 있으면 길이다. 1번 진입시마다 +1인데,
    ## -> 방문체크시 continue가 아니라 카운팅을 안한다
    ## -> 경계넘어서면 카운팅을 안한다
    ## dir으로 1번만 가게 한다면, queue를 이용해서 앞에서부터 뺀다?
    dirs = deque(dirs)
    print(
    dfs(dirs, visited,
        4, 4)  # 1개의 경로(꼬리재귀)라면 누적결과값없으 자신이 집계해서 반환한다?!
    )