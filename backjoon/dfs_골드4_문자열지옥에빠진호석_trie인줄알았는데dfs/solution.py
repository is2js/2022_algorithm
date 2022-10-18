import sys

input = sys.stdin.readline


def dfs(node, y: int, x: int, cur):
    # 문자열의 길이는 최대 5이므로 종료
    if cur == 5:
        return

    # node.count += 1 # => root node부터 문자열의 부모node에 카운팅하면, start_with_count다.
    if board[y][x] not in node.children:
        node.children[board[y][x]] = TrieNode()
    node = node.children[board[y][x]]
    # node.count += 1 =>  char에  자신node부터 카운팅하면, 방문횟수다?
    node.count += 1

    for dy, dx in DELTA:
        ny = (y + dy) % N
        nx = (x + dx) % M
        dfs(node, ny, nx, cur + 1)


if __name__ == '__main__':
    ## 문자열 지옥에 빠진 호석: https://www.acmicpc.net/problem/20166
    # => https://velog.io/@boorook/Python-%EB%B0%B1%EC%A4%80-20166-%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%A7%80%EC%98%A5%EC%97%90-%EB%B9%A0%EC%A7%84-%ED%98%B8%EC%84%9D-%EB%AC%B8%EC%A0%9C-%ED%92%80%EC%9D%B4
    # => starts_with문제가 아닌... 방문횟수 문제?
    N, M, K = map(int, input().split())
    board = [list(input().strip()) for _ in range(N)]
    ## 1. 일단 막 움직이는 board에서 dfs로 경우의수를 만들며 종착역 길이 5개짜리 문자열 모든 경우의 수를 찾는다.
    ## 2. 5개짜리 문자열을 trie에 insert하고, 주어진 K개의 문자열로 만들 수 잇는 문자열의 갯수를 판단한다

    ## 시작점이 없는 dfs는, 여러개의 시작점 dfs로서, 경우의수를 반복문으로 만들어서 호출한다.
    DELTA = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1),)

    ## => 5개짜리 단어들을 먼저 다 탐색한 후 -> 다시 insert하는 것보다
    ##    insert할때도 어차피 1글자씩 보게 된므로,
    ##    dfs시작 -> depth늘어날때마다 next로 업데이트하면서, 자신의 처리에서 cnt도 같이한다.?
    class TrieNode:
        def __init__(self):
            self.count = 0
            self.children = dict()

        # def insert(self, string):
        def insert(self):
            curr = self
            # for char in string:
            #     curr.count += 1
            #     if char not in curr.children:
            #         curr.children[char] = TrieNode()
            #     curr = curr.children[char]
            # curr.count += 1
            for i in range(N):
                for j in range(M):
                    dfs(curr, i, j, 0)

        def search(self, query):
            curr = self
            print("total:", curr.count)

            for char in query:
                if char not in curr.children:
                    return 0
                curr = curr.children[char]
                print(char, curr.count)
            return curr.count




    root_node = TrieNode()
    # words = set()
    # words = []
    # for row in range(N):
    #     for col in range(M):
    #         dfs(board, row, col, 0)
            # print("check")
            # print(words)

    # for word in words:
    root_node.insert()

    # print(words)
    for _ in range(K):
        print(root_node.search(input().strip()))



