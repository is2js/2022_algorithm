import math
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    # 백준 1774: https://www.acmicpc.net/problem/1774
    v, e = map(int, input().split())

    # node가 좌표라면, node번호(index) -> 좌표(tuple, 값)이 매핑되는 배열이 필요하다.
    # -> 만약 객체라면 필드로..
    # -> 배열인데, node번호가 0부터 시작하지 않으면, 0번에 빈 값을 채우고 시작하는게 좋다. 좌표값이면 (0,0)으로 채우고 간다
    gods_coord = [(0, 0)]
    for _ in range(v):
        row, col = map(int, input().split())
        gods_coord.append((row, col))

    # 최소신장트리(MST) by 크루스칼(간선비용sort + find+continue + continue)를 만드려면
    # -> 비용기준으로 sorting된 간선정보가 필요하다.
    # -> [좌표 node]는 이미 비용이 안에 내포 되어있다.
    # -> 4개의 node -> 4C2개의 edge 중에 4-1 3개만 뽑히도록 해야한다. 일단 4C2로 만들면서, 비용을 계산하여 edge정보를 만든다.

    # 간선정보의 기록은, graph인접행렬 or 인접빈행렬 or dict에 저장하면 된다.
    # -> 이미 주어진 간선정보는 최소비용트리에 계산안되도록 cost 0으로 미리 추가해놓고 -> 이미 차있으면 건너띄게 해야한다.
    # -> 인접빈행렬을 준비해서 처리하자. -> [ node수 + 1만큼 빈배열을 가진 row]를 만들어주면 된다.
    graph = [[] for _ in range(v + 1)]
    # 이미 연결된 통로는 cost를 0으로 인접행렬에 저장한다.
    for _ in range(e):
        u, v = map(int, input().split())
        # 인접행렬 기록시 [양방향이 default임을 기억]하자.
        # 인접빈행렬 기록시 [append]로 하나씩 기록해야함을 기억하자.
        # 인접빈행렬에 cost까지 포함 기록시, (cost, v)의 튜플로 기록함을 기억하자.
        graph[u].append((0, v))
        graph[v].append((0, u))

    # 최소신장트리를 만드려면, 모든node를 연겨랗는 edge정보가 존재하고 그 사이에서 n-1개만 최소비용순으로 & 싸이클없도록 구성해야한다.
    # -> 좌표로 주어지는 node는 내부에 이미 간선정보를 포함하고 있으며
    # -> [combination을 이용해서, nC2개의 간선정보(u->v 양방향) 및 cost(u,v의 좌표배열에서 계산)]까지 만들어낸다.
    numbers = list(range(1, v + 1))  # 조합을 만들어낼 숫자배열
    connections = list()  # nCk개의 튜플을 특정원소 기준으로 정렬할 수도 있어서 list로 모음.

    def combination(prev_cnt, prev_position, selected_tuple):
        if prev_cnt == 2:
            # N개 중 k개를 모았으면, 그때까지의 tuple을 반환한다 -> 모은 tuple로 추가 작업하여 추가결과를 append할 수도 있음
            a, b = selected_tuple
            # 인접행렬 기록전에, 이미 존재하는지 검사 -> u or v 아무거나 1개만 해도 된다.
            # -> 존재한다면, 그 정보(cost 0으로 이미 연결된 간선)을 MST용 간선정보로 모은다.
            for cost, v in graph[a]:
                if v == b:
                    # mst용 간선정보는 [ (cost, u, v)의 tuple들]로 구성되도록 만든다.
                    connections.append((cost, a, b))
                    return # 이미 연결된 정보가 있었다면, 밑에서 cost를 직접 계산할 필요 없이 종료한다.

            # node마다 배열에 매핑된 좌표를 통해 2개 node사이의 cost를 계산한다
            a_coord, b_coord = gods_coord[a], gods_coord[b]
            cost = math.sqrt(math.pow(a_coord[0] - b_coord[0], 2) + math.pow(a_coord[1] - b_coord[1], 2))

            connections.append((cost, a, b))
            return None

        if prev_position == len(numbers):
            return None

        # numbers 중 첫번째 수 선택한 root_node / 선택하지 않은 root_node
        combination(prev_cnt + 1, prev_position + 1, tuple(selected_tuple + (numbers[prev_position],)))
        combination(prev_cnt, prev_position + 1, tuple(selected_tuple))
        return None

    combination(0, 0, ())
    ## 조합을 통해 생성된 간선정보들은, sort()를 통해 비용오름차수능로 정렬한다.
    # -> 애초에 우선순위힙에 넣어다가 하나씩 빼도 될 것 같지만, NlgN으로  둘다 동일하다.
    connections.sort()


    ## 최소비용트리(MST)를 건설하기 위해서는 (1) 비용순edge정보 외에 (2) union/find_parent메서드/를 위한 parent_table이 필요하다
    # -> node(index)별 root_node(value)를 매핑한 배열이다.
    parent_table = [i for i in range(v + 1)]

    def find_parent(a):
        if a == parent_table[a]:
            return a

        root = find_parent(parent_table[a])
        parent_table[a] = root
        return root

    def union(a, b):
        pa = find_parent(a)
        pb = find_parent(b)
        if a < b:
            parent_table[pb] = pa
        else:
            parent_table[pa] = pb

    ## 간선을 비용순으로 돌면서, MST트리를 건설한다(싸이클생길 node들은 건너띈다)
    mst_cost = 0
    result_edges = []
    for edge in connections:
        cost, u, v = edge
        if find_parent(u) == find_parent(v):
            continue
        union(u, v)
        mst_cost += cost
        result_edges.append(edge)

    ## 소수점 잘라서 출력은 f-string을 이용한다.
    print(f"{mst_cost:.2f}")



