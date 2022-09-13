import sys

input = sys.stdin.readline
sys.setrecursionlimit(100_000)

def find_parent(node):
    # root start, 집합의 대표는 자기자신이 부모이다. 초기화 된 이후 안바뀐다.
    if node == parent_table[node]:
        return node
    # 그게 아니라면, 재귀를 통해서 계속 찾아나서야한다.
    # start -> parent_table[start]로서 찾아나서기
    # return find_parent(parent_table[start])

    # 그냥 찾아서 반환하지말고, 종착역의 root부모를 반환하면서
    # -> 재귀를 타는 node들 모두 value(부모)값을 root_node로 변경해주고 반환해주자
    # -> 경로압축으로서 검색이 빨라진다.
    root = find_parent(parent_table[node])
    # root를 현재node의 parent값으로서 업뎃해주고 돌아가자
    parent_table[node] = root # 종착역의 대표값을 내 대표값으로 업뎃후 직전재귀에게 돌려주기
    return root


def union(first, second):
    # 직접적인 부모가 아니라, 재귀를 해서라도, root 부모를 찾아서 비교해야한다.?!
    # -> union : 같은집합에 넣는다 -> 한쪽을, root(대표)node를 똑같은 것으로 만들어야한다.
    # -> union시 거쳐야하는 find를 정의하면
    # -> find시 최종대표값을 찾고 돌아오면서, 다 root(대표)값을 부모값으로 업데이트 해주면
    # -> 다 돌고 난뒤 table에서 쉽게 root를 꺼낼 수 있기 때문이다.(지금은 안됨)
    # first_parent = parent_table[first]
    # second_parent = parent_table[second]
    first_parent = find_parent(first)
    second_parent = find_parent(second)

    #### 그냥 왼쪽으로도 밀 수 있지만,
    # parent_table[first] = second_parent
    ### 주의) node의값이 작은 것을, 집합의 대표로 간주하자.(not 대표값 비교)
    # if first_parent <= second_parent:
    if first <= second:
        ### 주의) 한쪽의 대표값의 부모를 바꿔줘야한다. (not 현node의 대표값에 대입 -> but 한쪽 대표의 대표값에 대입)
        # parent_table[second] = first_parent
        parent_table[second_parent] = first_parent
    else:
        # parent_table[first] = second_parent
        parent_table[first_parent] = second_parent


def process():
    method, u, v = map(int, input().split())
    if method == 0:
        union(u, v)
    else:
        print("YES" if find_parent(u) == find_parent(v) else "NO")

if __name__ == '__main__':
    n, m = map(int, input().split())
    # parent_table = [0] * (n + 1)
    # for index, _ in enumerate(parent_table):
    #     parent_table[index] = index
    ### index값으로 초기화는 한방에 할 수 있다.
    parent_table = [i for i in range(n+1)]

    for _ in range(m):
        process()

