import sys

input = sys.stdin.readline


## 서로소 집합구조, UnionFind의 재귀 구현의 문제점
# -> find_parent의 재귀호출이, 최악의 경우, v개의 node를 다 뒤져야해서 매번 O(V)로 작동하게 된다.
#   ex>  1<-2<-3<-4<-5

## 개선: 직접적인 부모가 아니라, 재귀를 통해 찾은 root node를 현재node의 값으로 업데이트 in 재귀귀
# => 재귀에서 거슬러 올라가면서, 재귀를 타고나와 종착역에서 거슬러 올라갈 때,
#    종착역에서 반환한 root_node를 값으로 할당
def find_parent(parent_table, node):
    if parent_table[node] == node:  # root node
        return node

    parent = parent_table[node]

    # return find_parent(parent_table, parent)

    # (1) 종착역의 값을 꼬리재귀로서 계속 연쇄반환해서 값만 반환하는게 아니라, 그 사이 트랜잭션
    # (2) 종착역의 값으로, parent_table을 업데이트 해주고, 반환
    parent_table[node] = find_parent(parent_table, parent)
    # (3) 종착역에서 찾은 값으로, 나의(node)의 부모(parent_table[node])도 종착역으로 업데이트
    #     -> 그리고 그 종착역 값을 반환
    #      -> 다음 직전 재귀에서도, 반환되는 종착역 값 in 테이블 으로 자신의 값(직접 부모)을 종착역으로 업데이트
    #   => 종착역 값을, 현재 자신(node)의 값으로 계속 업데이트시키고 반환시킬 수 있다.
    return parent_table[node]


def union_parent(parent_table, first_node, second_node):
    # 각각의 부모node를 찾을 때, 거슬러 올라가서 root node를 찾아야한다.
    # -> table에 부모 조회시, 직접적인 부모만 나오므로, 재귀를 통해 거슬러 올라가서 찾아야한다.
    first_parent = find_parent(parent_table, first_node)
    second_parent = find_parent(parent_table, second_node)

    # 둘 중에 root node가 더 작은 값을 가질 경우, [최종 root node]가 가리키는 방향을 바꾼다.
    # -> **원래node의 부모 값을 바꾸는게 아니라, **각 root node 중 1개가 [자신이 아닌 다른 node]를 가르키게 한다!!
    if first_parent < second_parent:
        parent_table[second_parent] = first_parent
    else:
        parent_table[first_parent] = second_parent


if __name__ == '__main__':
    ## 서로소 집합의 이용: 무방향 그래프내 싸이클여부 판별
    # cf) 방향그래프는 DFS로 싸이클판별
    # 1. 각 간선마다 find_parent를 통해 루트노드를 확인
    #    (1) 루트노드가 다르면 union(합집합)연산을 통해 같은 집합을 만듦
    #     -> node값이 더 큰 놈을 작은놈의 부모로 만든다?!
    #    (2) 루트노드가 같다면 싸이클이 발생한 것으로 판단
    # 2. 모든 간선 다 합집합때렸는데, 싸이클 발생하지 않았으면, 싸이클 없다고 판단
    # ex>
    # 1-2, 1-3 -> 2-3을 find_parent해서 비교했을 때 같으면, 싸이클 발생
    ### 예제 코드
    v, e = map(int, input().split())

    parent_table = [0] * (v + 1)  # 1~second node의 부모테이블 -> 초기 부모는 자기자신으로 초기화
    for i in range(1, v + 1):
        parent_table[i] = i

    ## 문제에 주어지는 모든 간선들에 대해 union 연산을 수행
    # for _ in range(e):
    #     node, b = map(int, input().split())
    #    # 두 node의 최종부모인 root node를 찾아서, 더 큰 부모가 작은 부모를 가리키게 한다.
        # union_parent(parent_table, node, b)

    # print('각 원소가 속한 집합: ')
    # for i in range(1, second + 1):
    #     print(f"{i} -> {find_parent(parent_table, i)}")

    ## union연산을 통해, [무방향 그래프에 한해] 싸이클 발생여부 판단
    has_cycle = False
    for _ in range(e):
        a, b = map(int, input().split())
        # (2) union전에, 각각의 root_node를 확인하여, 같은 집합에 속해있다면,
        # -> 싸이클을 가지는 것으로 판단한다
        # -> 1-2, 1-3은 같은 부모를 가지더라도 싸이클이 아니다.
        # -> 2-3을 했을 때, 같은 부모를 가진다면, 싸이클 발생이다.
        # --> 최초에는 자신을 루트노드로 가지니, 같아질 일이 없다.
        # --> 한번 업뎃한다면, 더 작은값의 부모를 가지게 될 것이다.
        # --> 만약, 1/1 2/1 상태로 다시 한번 1 2 간선이 등장한다면, 싸이클 아님에도, 같은 부모를 보게 될 것이다.
        #    하지만, [무방향 그래프]는 [2개 node사이에는 1개의 간선]만 존재한다
        # --> 즉, 같은 집합 속 root node랑 다시 union할일은 없으니
        #################
        #  [무방향 그래프]로서 [1번은 자기자신-> 집합 속 root_node]로 테이블값 업뎃]이후의 상황으로서
        #  부모가 같다면, [같은 집합 속에서의 간선]이므로   => 싸이클이 존재하는 것이다.
        #################
        if find_parent(parent_table, a) == find_parent(parent_table, b):
            has_cycle = True
            break

        # (1) 간선 속 2개의 node를 유니온 연산하여, parent_table에 root_node를 부모로 명시하여
        # -> 같은 값을 가지면, 같은 집합으로 판단한다.
        union_parent(parent_table, a, b)

    if has_cycle:
        print("싸이클이 발생하였습니다.")
    else:
        print("싸이클이 존재하지 않습니다.")

