import sys 
 
input = sys.stdin.readline 
 
 
if __name__ == '__main__':
    ## 트리 기본 개념:가계도와 같은 계층적인 구조를 표현하는 자료구조
    # root node / leaf node(단말노드, 자식필드? 자식 node가 없는 node)
    # 크기: node의 총 갯수
    # 깊이: root node(0)로부터 거리
    # 높이(height) : 깊이 중 최대값
    # 차수(degree) : 자식방향 간선의 갯수 (자식node의 갯수)
    # 트리의 크기N(node갯수) -> 전체 간선의 갯수 N-1 (싸이클없는 트리)
    
    ## 이진 탐색 트리(binary search tree)
    # -> 이진 [탐색]이 동작하도록 고안된 효율적인 탐색 자료구조
    # -> 특징: 왼sub < 부모 < 오sub 로 크기가 구성는 것이 특징
    #    (1) 부모node보다 왼쪽 자식node가 더 작다
    #    (2) 부모node보다 오른쪽 자식node가 더 크다.

    ##  만드는 방법 생략. 탐색(조회)하는 방법 설명
    #          30
    #        /    \
    #       17     48
    #     /  \     /  \
    #    5    23  37  50
    # -> 이진 탐색 트리가 이미 구성되어있다고 가정하고 데이터 조회(37) 과정을 살펴보자.
    # (1) root node(30)부터 방문해서 탐색 -> 30 < 37 => 오른쪽 방문 => [왼쪽은 방문안하도록 배제]
    # (2) 48 vs 37 => 왼쪽 방문
    # (3) 37 => 탐색 종료

    # 이진탐색트리는 이진탐색이 가능한 형태로 고안된 tree자료구조 중 하나
    # -> 이상적인 경우, lgN(절반씩 배제)로 탐색된다.
    # -> 좌우로 균형이 잡힌 tree구성시 가능한 이상적일 때만 가능.

    ## 트리 순회 방법(Tree traversal)
    # 전위순회(pre-order) -> 부->왼(달릴때마다끝까지)->(종착역)오
    # 중위순회(pre-order) -> 왼(달릴때마다끝까지)-->부->오
    # 후위순회(pre-order) -> 왼->오->부


    ## 이진탐색트리 구성과, 순회하기
    #  노드정보
    #  7
    # A B C
    # B D E
    # C F G
    # D None None
    # E None None
    # F None None

    n = int(input().strip())

    # (1) 자신의 data, 및 왼sub의 data, 오sub의 data를 인자로 받아 구성된다.
    # -> input으로 들어오는 정보는 자식들의 left/right정보까진 없이 들어오므로
    # -> 필드에는 left_node가 아닌 left_data만 저장해놓고, 인접dict에서 뽑아쓴다.
    class Node:
        def __init__(self, data, left_data, right_data):
            self.data = data
            self.left_data = left_data
            self.right_data = right_data

    # (2) # 인접dict  key: data / value: data + left_data + right_data(input)으로 구성된
    tree = {}
    for _ in range(n):
        data, left_data, right_data = input().strip().split()
        # 받은 node번호들은, Node객체의 필드로 간다. left/right 필드에 Node객체를 바로 넣지 못하는 상황
        # -> next정보가 들어와서 tree에 next객체로 넣어놓을 예정이므로, next_value -> 나중에 tree에서 next_node객체를 뽑아쓰면 된다.
        # (3) None으로 자식이 없을 경우는 None으로 필드를 자치하도록 객체를 생성해서 매핑한다.
        if left_data == 'None':
            left_data = None
        if right_data == 'None':
            right_data = None
        # 인접dict에는 부모Node로서 자식들은 data(not node)로 가지는 Node객체를 생성하여 매핑해준다.
        tree[data] = Node(data, left_data, right_data)

    # (4) main에서 전역 메서드를 통해, 전역변수 [인접dict tree]를 활용해서
    # -> root node(tree['root'])부터 입력받아 순회한다.
    # -> 직접적으로 필드로 node들이 연결된 상황은 아니다. -> 인접dict로 통해서 node로 치환해서 연결시켜 호출한다.
    def pre_order(parent_node: Node):
        # (4-1) 전위순위는 들어온 부모node를, 다음 각 stack마다 맨첨에 처리되도록 재귀호출 전에 처리하게 한다.
        print(parent_node.data, end=' ')

        # (4-2) 왼sub를 재귀로 갈 수 있는 만큼 깊게 간다. 가면서 자신이 부모로서 먼저 처리되면서 갈 것이다.
        # -> 대신 필드에 존재해야만 가능하다.
        # -> 필드에 존재한다면, tree(인접dict)에 매핑되어있는 실제 Node객체로 변환해서 호출해줘야한다.
        if parent_node.left_data:
            pre_order(tree[parent_node.left_data])
        # (4-3) 왼쪽으로 갈만큼 다 같으면 오른쪽node로 가서 처리한다.
        if parent_node.right_data:
            pre_order(tree[parent_node.right_data])

    # (5) 중위 순회 -> 부모 자신의 처리가 가운데
    def in_order(parent_node):
        if parent_node.left_data:
            pre_order(tree[parent_node.left_data])

        print(parent_node.data, end=' ')

        if parent_node.right_data:
            pre_order(tree[parent_node.right_data])

    # (5) 후위 순회 -> 부모 자신의 처리가 오른쪽까지 다 가고 난 뒤 처리
    def post_order(parent_node):
        if parent_node.left_data:
            pre_order(tree[parent_node.left_data])

        if parent_node.right_data:
            pre_order(tree[parent_node.right_data])

        print(parent_node.data, end=' ')

    # (6) 각 순회 메서드에 root node인 A를 넣어준다.
    pre_order(tree['A'])
    print()
    in_order(tree['A'])
    print()
    post_order(tree['A'])






    pass 
