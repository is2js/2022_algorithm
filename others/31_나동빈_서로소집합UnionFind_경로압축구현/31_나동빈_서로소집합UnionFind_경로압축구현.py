import sys

input = sys.stdin.readline

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


    ### 예제 코드
    v, e = map(int, input().split())

    parent_table = [0] * (v + 1)  # 1~second node의 부모테이블 -> 초기 부모는 자기자신으로 초기화
    for i in range(1, v + 1):
        parent_table[i] = i

    # 문제에 주어지는 union 연산을 수행
    for _ in range(e):
        a, b = map(int, input().split())
        # 두 node의 최종부모인 root node를 찾아서, 더 큰 부모가 작은 부모를 가리키게 한다.
        union_parent(parent_table, a, b)

    print('각 원소가 속한 집합: ')
    for i in range(1, v + 1):
        print(f"{i} -> {find_parent(parent_table, i)}")


    print('각 node의 직접적인 부모: ')
    for i in range(1, v + 1):
        print(f"{i} -> {parent_table[i]}")


    ## 서로소 집합구조, UnionFind의 재귀 구현의 문제점
    # -> find_parent의 재귀호출이, 최악의 경우, v개의 node를 다 뒤져야해서 매번 O(V)로 작동하게 된다.
    #   ex>  1<-2<-3<-4<-5

