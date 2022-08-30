import sys

input = sys.stdin.readline


# (7) 자식index, 자기자신이 부모value로 되어있는 node를 parent_table에서 찾으면, root_node(집합 대표)
# -> 아니라면 재귀를 통해서 찾아올라가되, 찾고나면, 경로압축을 위해 재귀역행하면서,
#    종착역직전부터 ~시작까지 연결된 node들의 부모값을 종착역 root_node로 변경해준다
def find_parent(parent_table, node):
    if node == parent_table[node]:
        return node

    parent = parent_table[node]
    # return find_parent(parent_table, parent)
    parent_table[node] = find_parent(parent_table, parent_table[node])
    return parent_table[node]

# (8) 둘 중 1개node의 대표값(root_node)를 반대쪽으로 만들어주는 작업
# -> 먼저 각각의 root_node를 find_parent로 찾아야한다.
def union(parent_table, first, second):
    first_parent = find_parent(parent_table, first)
    second_parent = find_parent(parent_table, second)
    # 무작위로 한 곳을 반영해도 되지만, 자식node(index)가 작은 곳을 root node로 취급해준다.
    if first < second:
        parent_table[second_parent] = first_parent
        return
    parent_table[first_parent] = second_parent
    return



if __name__ == '__main__':
    ## 최소신장트리 by 크루스칼 알고리즘
    # 모든 node를 포함하는 & 일부간선만활용한 & (싸이클없는그래프인)트리를 만듦
    # -> 모든 node가 연결되어있지만, 일부간선만 사용해도 된다는 점에서
    # ex> 모든 node가 연결되어야하는 상황

    # 최소비용으로 구성되는 신장트리
    # ex> N개의 도시가 있는데, 두 도시다시에 도로를 놓아, [전체 도시가 서로 연결]되도록 하는 경우
    # -> 이동경로가 반드시 존재하도록 도로 설치

    # 알고리즘 : 크루스칼 알고리즘
    # -> 간선을 하나씩 확인하면서, 최소신장트리에 포함시킬지 여부를 판단하는데
    # (1) 간선을 비용 기준, 오름차순으로 정렬
    # (2) 간선 하나씩 싸이클 발생시키는지 여부를 확인한다.
    # -> 싸이클발생여부는 통괴되었다면 2 node를 union하여 같은 집합(같은 root_node)에 속하도록 후처리해줘야한다.
    # -> 그래야 다음 것이 필터링 될 정보를 구축해나갈 것이다.
    # (3) 싸이클이 발생하지 않으면, union하여 이후 간선정보들의 cycle판단 정보를 만들고,
    #    최소신장트리를 만드는 result edges에 append한다.
    #      4
    # 23/      |13
    # 6 --25-- 7   => 6과 7의 간선을 확인할 땐, 이미 같은 집합에 속해있으므로 연결시 싸이클 발생하므로 연결안한다.
    # (4) 완성 후, 포함된 간선들의 cost만 합하면, [모든 node를 최소비용으로 잇는 최종 비용]이 된다.
    # cf) 최소신장트리에서 node의 총 간선의 갯수 = node수 -1
    #    -> 싸이클이 없는, tree가 가지는 특징

    ## 성능분석
    # 간선을 오름차순 하는 부분이 가장 큰 시간복잡도를 요구하므로 E개의 간선 정렬의 시간복잡도와 같다
    # => python sort()는, 힙정렬/퀵정렬?처럼 O(NlogN)의 시간이 소요된다.

    v, e = map(int, input().split())
    # (0) 최소신장트리를 구성하는 edge수 == node -1이므로,
    #  -> input되는 edge는 이것보다 많아야지 골라서 최소비용 순으로 싸이클을 안만드는 edge들을 선택할 수 있다.

    # (1) 싸이클여부판별용 unionfind 구현을 부모테이블
    # -> 소속집합이자 집합의 대표(rootnode/부모)를 자기자신으로 초기화
    parent_table = [i for i in range(v + 1)]

    # (2)  간선정보를 받고, tuple의 첫번째요소(정렬기준)으로 배치하는 배열 만들기
    # -> 정렬기준만 람다 지정해줘도 될 듯하다.
    edges = []
    for _ in range(e):
        a, b, cost = map(int, input().split())
        edges.append((cost, a, b))
    # (3) 간선들을 비용 오름차순으로 정렬
    edges.sort()
    # (4) 비용이 작은 간선 순으로 탐색하되, 싸이클 여부가 발생안하는 간선들만 모은다
    result_edges = []
    mst_cost = 0
    for edge in edges:
        cost, a, b = edge
        # (5) 싸이클 발생시키는 같은 집합 node들끼리의 간선이면 건너띈다.
        if find_parent(parent_table, a) == find_parent(parent_table, b):
            continue
        # (6) 싸이클 발생시키지 않는 최소비용 간선은
        # ->    최소신장트리 간선으로 추가 전, union하여 2간선을 이어주어,
        #       parent_table에 같은 root_node를 가지는 집합이라고 명시한다
        #       이 작업을 해줘야 (5)에서 걸린다.
        union(parent_table, a, b)
        result_edges.append((cost, a, b))
        mst_cost += cost

    print(mst_cost, result_edges)
