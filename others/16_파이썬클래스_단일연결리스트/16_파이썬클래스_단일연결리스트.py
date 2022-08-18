import sys

input = sys.stdin.readline


class Node:

    def __init__(self, data, next=None):
        self.data = data
        # [1] 필드는 다음node를 기억한다. 안주면 기본값이 되게 한다.
        self.next = next

    # [2] node를 추가한다면, 시작특이점 객체에 add한다.
    def add(self, node):
        # [3] 현재node의 필드에, 다음node가 없는 경우 == linkedlist의 끝인 경우
        #     필드에 바로 넣어주면 된다.
        if self.next is None:
            self.next = node
        # [4] 만약, 필드에 다음node가 들어가있다면
        #     -> 필드 속 다음node정보를 이용해, 끝까지 간 다음,
        #     -> 필드 속 다음node가 없는 맨 끝node일때. 비로소 add한다.
        # my) prev데코객체처럼, 직전node를 필드에 넣고 다음node를 생성하는 것이 아니므로
        #   -> 현재node가 맨끝이라는 보장이 없게 되어,
        #   -> 맨끝이 아닐 경우, 반복문으로 끝까지 가야한다.
        else:
            # [6] 변수(필드)에 객체를 저장하게 되면, 객체의 위치값이 저장되게 된다.
            #     그걸 다시 변수에 할당하면, 그 객체의 위치값이 저장되어 소통이 된다
            #     x = 객체 -> y = x -> 1개의 객체를 같이 건들인다.
            curr = self.next
            while curr.next:
                curr = curr.next  # next필드 속 다음node를 꺼내 현재가 된다.
            # [5] 다 이동했으면, 맨끝node에 왔다면 add할 node를 필드에 추가한다
            curr.next = node

    def select(self, index_):
        # [9] linekdlist에서 메서드 작동 기준은 head이다.
        #   그리고 탐색은 1번째 요소부터 지역변수로 받아놓고, while로 한다.
        #  -> 맨끝은 .next에 암것도 안들어가있다.
        # curr = self.next
        # while not curr.next:
        #     curr = curr.next
        # [10] 이 때, 인덱싱은 0일 땐 첫번째 원소가 나와야하고
        #    i일 땐, i번재 next를 타야한다.
        curr = self.next  # head(시작특이점)이후의 원소로 시작한다.
        # 0 -> 0, 1-> 1번, i -> i번 next를 쳐야한다
        # 이 때, while문으로 카운팅하는 것은 비효율적 -> 지역변수 추가됨
        # -> 정해진 횟수를 반복할 땐, while문 말고, for문을 쓰자
        # -> 끝까지 + 횟수가 아닌 조건까지 가야할 땐, while문을 쓰자.
        for _ in range(index_):
            curr = curr.next
        return curr.data

    def delete(self, index_):
        # [12] linkedlist에서 메서드 작동 기준은 head이며, 시작을 0번째 요소로 한다
        curr = self.next
        # i번째를 삭제하려면, i번재 이전node로 먼저 가야한다.
        for _ in range(index_ - 1):
            curr = curr.next
        # (1) 삭제연결은 이전node.필드 = 다음node 이므로
        #     덮어쓰여지는 이전node.필드 == 삭제node위치값을 보존한다
        #    temp  = overwritten (덮어쓰여질 정보의 보존은 대각위에서 하자)
        #            /
        #          /
        #    overwitten = k
        target = curr.next
        # (2) 이제 이전node.필드에 다음node를 연결하자
        #    -> 다음node정보 역시, 덮어쓰여질 위기의 temp값의 필드에 있었다.
        curr.next = target.next
        # (3) 이제 보존된 객체를 del로 삭제한다.
        # del target
        # my) 삭제 안해주고 반환해도 될 것 같기도?? 카운팅?? 객체라면, 복사해서??
        # (4) 삭제안하고 그냥 반환하면(어차피 연결이 컬렉션을 통한 연결은 없어서 자유로운 객체 -> 반환해도됨)
        #  => 삭제시 del삭제 안하면 pop이다.
        # => [컬렉션에 속한 객체]가 아니라면, 객체는 그냥반환해도 된다.
        # => [컬렉션에 속한 객체라도, 외부조작을 위해(카운팅)서라면 객체 그냥 반환하기도]
        return target

    def print_node(self):
        # [13] 메서드의 기준시작은 head가 된다.
        # -> 끝까지 탐색을 하는 경우, add처럼,
        # -> 미리 head의 필드에 다음이 없는 것은 아닌지
        if self.next is None:
            print("there is no node except head")
            return
        # 기준은 head지만, 탐색은 업데이트되어야하므로, 첫번째 원소부터 한다.
        curr = self.next
        # my) next데코객체는, 맨마지막이 종료특이점이나 마찬가지다(.next필드 =None)
        # 1) 탐색 끝 범위에 특이점 객체(필드None)가 존재할 경우, 업뎃결과가 none이 아닌 객체다
        #    -> 마지막까지 돌 수 있다.
        #    -> next데코객체는, head유지에 마지막이 자동 특이점객체로서
        #    -> 만약, 끝처리를 원한다면, 내부에서 필드검사로 해준다.
        while curr:
            # 특이점 객체용
            if not curr.next:
                print(f"{curr.data}asdf")
                # curr = curr.next
                # continue
                # 공통 업데이트로직이 있다면, if continue는 쓰지 않고 return이나 else를 쓴다.
                # => while문에서는 마지막 공통업뎃문 때문에 early continue 못쓴다.
                # => 근데, 마지막이라도 업데이트를 해야 while조건문에 걸려 더이상 진행안하게 된다.
                # => 마지막이 확실하다면, break,나 early return을 쓴다.
                # => next데코객체는 끝 특이점객체가 datat가 들어있으니, 사용해야한다.
                break
            print(f"{curr.data}", end=" ")
            curr = curr.next

    def insert(self, index_, node):
        curr = self.next
        # [15] 해당index까지 필드로 객체 업뎃을 i-1번을 하여
        #      예비 [이전node]로 간다.
        for i in range(index_ - 1):
            curr = curr.next
        # 새로온놈을 예비이전node.필드에 넣기 전에 기존 정보를 보관한다
        # / 형태로 선언된다.
        temp = curr.next
        curr.next = node
        # 그담에 새로운놈의 필드에 그 다음놈(temp에 보관중)을 연결해준다.
        node.next = temp


if __name__ == '__main__':
    ## linked list

    # index기반 데이터들은 [원소 추가/삭제]가 없다면, 효율적이지만
    # -> 처음 or 중간에 삭제/추가된다면, 뒤쪽에 모든 것들이 같이 움직여야한다

    # linked list -> 각자가 다음을 기억하고 있다면
    # -> 처음 or 중간에 [삭제]되더라도,
    #    [이전 사람]만, [필드에 빠진사람 다음사람]을 기억하도록 만 바꿔주면 된다.

    # -> 처음 or 중간에 [추가]되더라도
    #    [앞 사람]은 [필드에 들어온 사람을 기억]하고
    #    [추가된 사람]은 [필드에 다음사람을 기억]하기만 하면된다.

    # my) 단일 연결리스트는, 필드에 다음사람을 기억하기만 하면 된다.
    #     삭제되면, 이전사람의 필드를 수정한다
    #     추가되면, 앞아사람의 필드 수정 + 추가된사람의 필드에 다음사람 추가

    # python은 list자체가 stack이자, linkedlist역할을 하고 있지만,
    # -> node를 값이 아닌 객체로 가지고 싶다면 구현해야한다?!
    # -> node에 기능을 가지는 객체가 되려면 구현해야한다

    # [0] 시작특이점 객체는, data가 None이며,
    #     prev(next)객체또한 None인데 기본값으로 None이 들어가게 한다.
    # -> 시작특이점 객체는, linked list 접근을 위해 생성되는 객체이므로
    #    data가 None이며, 여기에 add를 칠 수 있게 된다.
    head = Node(None)

    # [7] 이제 head로부터 다음node를 add한다.
    #     뭔가 들어있으면 그 끝까지 가서 add한다.
    head.add(Node("구독"))
    print(head.next.data)  # 구독
    head.add(Node("좋아요"))
    print(head.next.next.data)  # 좋아요
    head.add(Node("댓글"))
    print(head.next.next.next.data)  # 댓글

    # [8] i번째 요소 접근에 계쏙.next로 필드속 저장된 객체를 타고 갈 수 없으니
    # select함수를 만든다.
    # print(head.select(2))

    # [11] node삭제는 몇가지 준비과정이 필요하다
    # (1) 핵심은 [삭제될 node가 필드속에 가지고 있떤 다음node]의 정보 -> 이전node의 필드에 담아 연결인데,
    # (2) 조심해야할 것은, [이전node의 필드]에 먼저 덮어써버려 다음node를 연결부터 해버리면
    #                 -> 삭제node에 접근할 수 있는 유일통로인 이전node.필드 속 위치값이 사라져버린다
    #    => my) 연결을 위해 덮어쓰일 변수(이전node의 필드 속 삭제node 위치값)을 보존하라!!!!!!!!
    #    -> [구독]( )   [좋아요]( )    [댓글}( )
    #                           ---->
    #               ---------------->
    #              더이상 [좋아요]( )에 접근 by 이전node의 필드(구독.next)
    #              삭제할node에 접근(구독.next)할 수 있는 유일변수가 사라지게 된다
    # (1) 이전node로 간다
    # (2) 이전node의 필드에 있는 삭제node정보를 보존해놓는다(있다가 덮어쓰기 당함.)
    # (3) 삭제할node의 필드에 있는 다음node정보를 -> 이전node의 필드에 덮어써서 연결시킨다.
    # (4) 보존된 삭제node의 위치값을 통해 삭제한다.
    # print(f"삭제전 1번 index {head.select(1)}")
    # print(f"삭제한 1번 = {head.delete(1).data}")
    # print(f"삭제후 1번 index {head.select(1)}")
    # 삭제전 1번 index 좋아요
    # 삭제후 1번 index 댓글

    # [12] 전체node 출력은 add(head -> 처음부터 끝으로 탐색)을 활용해서 만든다.
    head.print_node()

    # [14] 제일 마지막 insert 역시, delete와 비슷하게 이전node의 필드에 다음 것을 연결하는 것에 집중한다.
    head.insert(1, Node("광고시청"))
    head.print_node()
    # 구독 좋아요 댓글asdf
    # 구독 광고시청 좋아요 댓글asdf

pass
