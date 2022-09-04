import sys 
 
input = sys.stdin.readline 
 
 
if __name__ == '__main__':
    ## LCA(Lowest Common Ancestor): 최소 공통 조상
    # 백준: LCA https://www.acmicpc.net/problem/11437
    # -> 2 node의 가장 가까운 공통 조상이 몇번인지 출력한다
    # -> N 5만, M 1만 -> O(NM)으로 설계해도 통과한다고 한다.
    # 최소 공통 조상 알고리즘
    # (1) 모든 node마다 depth를 계산한다 by dfs
    # (2) LCA(최소 공통 조상)을 찾을 2 node를 매번 확인한다.
    #    (2-1) 두 node의 깊이가 동일하도록 거슬러 올라간다
    #    (2-2) 이후에 부모가 같아질때까지, 반복적으로 부모방향으로 거슬러 올라간다
    # (3) 모든 LCA(a,b) 연산에 대해 2번을 반복한다.

    ## 예시 8과 15
    #                 1
    #                / \
    #              [2]   3      => (3) 부모가 같아질때까지 동시에 거슬러 올라간다.
    #             / |     | \
    #          [4]  [5]   6  7  => (2) depth가 같아진 순간부터, 동시에 거슬러 올라간다.
    #         / |  / |     | \
    #      [8]  9 10 [11]  12 13 => (1)2node 중 짧은 depth로 깊이를 맞춰준다.
    #              / |
    #            14 [15]

    ## 매 쿼리(M)마다 부모로 거슬러 올라가므로, 최악의 경우 O(N) -> O(NM)이 요구되는 코드다.

    # https://www.youtube.com/watch?v=O895NbxirM8&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=16

