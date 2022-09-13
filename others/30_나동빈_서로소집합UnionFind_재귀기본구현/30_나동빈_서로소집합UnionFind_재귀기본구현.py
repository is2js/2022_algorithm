import sys

input = sys.stdin.readline


def find_parent(parent_table, node):
    # 재귀를 통해 table을 거슬러 올라가도록 업뎃하는데, 최종 root node는 index(start)와 value(부모node)가 같다
    if parent_table[node] == node:
        return node

    # 자신의 parent를 현재node로 업뎃해서 넣어주면 된다.
    parent = parent_table[node]
    return find_parent(parent_table, parent)


def union_parent(parent_table, first_node, second_node):
    # 각각의 부모node를 찾을 때, 거슬러 올라가서 root node를 찾아야한다.
    # -> table에 부모 조회시, 직접적인 부모만 나오므로, 재귀를 통해 거슬러 올라가서 찾아야한다.
    first_parent = find_parent(parent_table, first_node)
    second_parent = find_parent(parent_table, second_node)

    # 둘 중에 root node가 더 작은 값을 가질 경우, [최종 root start]가 가리키는 방향을 바꾼다.
    # -> **원래node의 부모 값을 바꾸는게 아니라, **각 root start 중 1개가 [자신이 아닌 다른 start]를 가르키게 한다!!
    if first_parent < second_parent:
        parent_table[second_parent] = first_parent
    else:
        parent_table[first_parent] = second_parent


if __name__ == '__main__':
    ## 서로소 집합 -> 합집합 연산 Union / 찾기 Find (특정 원소가 어디 집합에 속하는지)
    # -> ex> 2개의 원소가 같은 집합에 속해있는지 판단은 find로 한다.
    # => Union find 자료구조라고도 부름
    # 1. Union을 하면서, 서로 연결된 두 node를 확인
    #  1-1. A와 B의 루트노드를 찾는다.
    #  1-2. A의 루트노트A`를 B의 루트노드B`의 부모노드로 설정
    # 2. 1번을 모든 합집합(Union)연산 처리할 때 까지 반복

    # Union(1,4), Union(2,3), Union(2,4), Union(5,6)
    # 부모node table
    # 자신node 1 2 3 4 5 6
    # 부모node 1 2 3 4 5 6

    # (1) 노드 갯수만큼 부모테이블 초기화(자신의 부모는 자신으로 초기화)
    #    각각이 다른 집합으로 존재
    # (2) 1-4node 합집합 연산 -> 각각의 root node를 찾고, 더 큰 번호의node의 부모를 작은번호node의 부모로 업뎃한다
    #    더 큰 번호가 작은 node를 부모로 가르키게 하는 것이 일반관행
    # 1<-4, 2<-3,
    # (3) Union(2,4)에서 특이점 발생. 4번의 부모가 1이기 때문에, 2<-4가 아니라
    #   -> 부모가 더 큰 node에 대해, 그 node의 부모를 더 작은 부모node로 업뎃한다.
    # 1<-2가 수행되어, 1-4, [1<-2], 2<-3 로 가르키게 된다.

    # (4) 직접적인 부모node만 기록하는 table로서, 3은 2번을 부모로, 4는 1번을 부모로 보고 있기 때문에
    #     [비록 연결은 같은 집합] 1<-2<-3, 1<-4 로 같은 집합으로 보지만,
    #     확인은, 연결확인은 find로 root node까지 가서 확인해야한다.
    #     root node는 자기자신을 부모로 가질 것이다.

    # (5) Union(5,6)  5<-6

    # (6) 연결이 끝나면, [연결성]을 통해, 총 몇개의 집합이 존재하는지 확인할 수 있다.
    # [ 1<-2<-3  1<-4 ]  [5<-6]
    # -> 1개의 rootnode로 구성된 tree형태의 그래프는, 같은 집합으로 다룬다.
    # -> 나눠진 부분집합들은 [서로소 관계]임이 증명된다.

    # (7) 이렇게 구현하면, root node에 즉시 접근은 안된다 ex> 2<-3
    #     root node를 가려면, 부모테이블을 계속 확인하면서, 거슬러 올라가야한다.
    #     -> 재귀적으로 거슬러 올라가야한다.

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

    # parent_table이 union결과 완성되었으니, 각 node가 속한 집합 == root start by find_parent를 통해 찾아 출력한다.
    print('각 원소가 속한 집합: ')
    for i in range(1, v + 1):
        print(f"{i} -> {find_parent(parent_table, i)}")
    # 1 -> 1
    # 2 -> 1
    # 3 -> 1
    # 4 -> 1
    # 5 -> 5
    # 6 -> 5


    # parent table만 출력하면, 직접적인 부모node의 값만 나올 것이다.(속한집합x root nodex)
    print('각 node의 직접적인 부모: ')
    for i in range(1, v + 1):
        print(f"{i} -> {parent_table[i]}")
    # 1 -> 1
    # 2 -> 1
    # 3 -> 2
    # 4 -> 1
    # 5 -> 5
    # 6 -> 5

    def find_parent(parent_table, node):
        # 재귀를 통해 table을 거슬러 올라가도록 업뎃하는데, 최종 root node는 index(start)와 value(부모node)가 같다
        if parent_table[node] == node:
            return node

        # 자신의 parent를 현재node로 업뎃해서 넣어주면 된다.
        parent = parent_table[node]
        return find_parent(parent_table, parent)


    def union_parent(parent_table, first_node, second_node):
        # 각각의 부모node를 찾을 때, 거슬러 올라가서 root node를 찾아야한다.
        # -> table에 부모 조회시, 직접적인 부모만 나오므로, 재귀를 통해 거슬러 올라가서 찾아야한다.
        first_parent = find_parent(parent_table, first_node)
        second_parent = find_parent(parent_table, second_node)

        # 둘 중에 root node가 더 작은 값을 가질 경우, [최종 root start]가 가리키는 방향을 바꾼다.
        # -> **원래node의 부모 값을 바꾸는게 아니라, **각 root start 중 1개가 [자신이 아닌 다른 start]를 가르키게 한다!!
        if first_parent < second_parent:
            parent_table[second_parent] = first_parent
        else:
            parent_table[first_parent] = second_parent

