import sys 
 
input = sys.stdin.readline


class Node:
    def __init__(self, value=None, prev=None):
        self.value = value
        self.prev = prev

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value!r})"


class NodeList:

    def __init__(self, node=None) -> None:
        self.head = node if node else Node(None)

    def add(self, value: int):
        self.head = Node(value, self.head)

    def merge(self, value: Node):
        value.prev = self.head
        # self.head = value
        # return self
        return NodeList(value)

    def remove(self, value):
        curr = self.head
        prev = None
        while curr.prev:
            # 1) 시작인 나를 삭제해야한다면, 시작하는 데코객체를 직전꺼로 옮기면 된다.
            if curr.value == value:
                self.head = curr.prev
                return True
            # 2) 중간에 있는 것을 삭제해야한다면, [다음타자]로 업데이트하되, 덮어쓰기 전에 [현재타자를 직전타자]로 저장을 해놓고 처리한다
            # curr = curr.prev

            # prev = curr
            # curr = curr.prev

            # 현재타자를 반복문내에서 매번 저장(할당)해놓는다면, 업데이트변수 되며 변수재활용을 위해, 반복문위에 선언해놓는다.
            # prev = None while ~
            prev = curr
            curr = curr.prev
            # next = curr.prev로 쓰면 된다.
            if curr.value == value:
                # 3) curr을 무시하고 prev <-> next를 연결해서 삭제한다.
                #    이 때, 연결이 끊어지지 않게 뒤에것은 [앞에 것을 prev필드에 갖고 태어나게] 해야한다.
                #    prev(curr) / curr(curr.prev) / curr.prev(curr.prev.prev)
                #    prev(curr.prev) / curr.prev
                prev.prev = curr.prev
                return True
        return False

    def reverse(self):
        # 1) prev데코객체는, 업데이트하면서 연결된 객체들의 동치식으로서 재귀호출이 가능하고, 파라미터를 통해 업데이트가 가능하다
        # 반복문으로 도는 것이 아니라, deco객체를 재귀메서드의 파라미터로 호출하며 업데이트하면서 재귀를 돈다.
        curr = self.head

        # 2) prev데코객체를 외부에서 재귀로 돌 때, 시작객체를 넣어주고, 파라미터에서 다음객체로 업데이트 한다.
        # self.reverse_helper(curr)
        # def reverse_helper(self, curr):
        #     self.reverse_helper(curr.prev)

        # 3) prev데코객체는 1개로만 연결되어있어 변하는 파라미터 변수를 반환하는 꼬리재귀가 가능하다.
        # -> 돌면서, prev필드에 역순으로 저장하고, 역순으로 완성된 Prev데코객체를 반환받도록 한다.
        # -> 시작head를 넣어줘야주고, 꼬리재귀에서는 해당 결과값파라미터를 반환해줘야한다.
        # --> 시작특이점객체부터 시작해서, 하나씩 Prev데코객체를 만들자?!
        new_prev = Node(None)
        #self.reverse_helper(curr, new_prev)
        # def reverse_helper(self, curr, new_prev):
        #     # 4) 데코객체를 도착 끝을 시작특이점객체로 지정하면, .prev에 None이 차있는 것으로 한다.
        #     if not curr.prev:
        #         return new_prev
        #
        #     # 5) 꼬리재귀라고 확정지었으면, 자신의 끝처리는 return이다.
        #     return self.reverse_helper(curr.prev, new_prev)
        # 6) 꼬리재귀는 호출후 1개의 값을 반환해줄 것이므로, 그 값을 이용한다.
        #   -> reverse를 위해 self.head에 역순prev데코객체를 넣어준다.
        # self.head = self.reverse_helper(curr, new_prev)
        return NodeList(self.reverse_helper(curr, new_prev))

    def reverse_helper(self, curr, new_prev):
        # 시작특이점객체는 반환하는 용도로 쓰인다.
        if not curr.prev:
            return new_prev
        # 7) 데코객체가 head부터 ~ 시작특이점도착시 반환하므로, 그 동안 new_prev를 만들어준다.
        # (1) curr과 .prev에 있는 직전타자를 순서를 바꾼 뒤, new_prev에 넣어준다.
        #    curr -> 기존 new_prev를 .prev에 넣어서 다음타자를 만들어 업데이트한다.
        #    그전에 curr.prev에 있는 것을 꺼내서 [그 재귀로 들어갈 다음타자]가 될 준비를 해놔야한다.
        next = curr.prev # 1) 재귀를 타는, 다음타자를 보존해놓는다
        curr.prev = new_prev # 2) [현재타자curr]는 [기존 new_prev를 .prev에 안고서] 새 new_prev가 되게 한다
        # 3) 이미 보존된 상태니, curr를 데코객체로 재활용하기 위해 , .prev만 기존new_prev를 안고 태어나게 해야한다.
        new_prev = curr # 4) 기존new_prev를 안고 있는 curr(value는 그대로씀)을 새로운 new_prev데코객체로 업데이트한다

        # (2) 다음 curr은 next가 되어야한다.
        # return self.reverse_helper(curr.prev, new_prev)
        return self.reverse_helper(next, new_prev)

    def __repr__(self):
        curr = self.head
        string = ""
        while curr.prev:
            string += str(curr) + (", " if curr.prev.prev else "")
            curr = curr.prev

        return string

    def get_head(self):
        return Node(self.head.value, self.head.prev)

    def get_head_value(self):
        return self.head.value

    def next(self):
        return NodeList(self.head.prev)

    def has_next(self):
        return self.head.prev


def solution():
    node_list_1 = NodeList()
    node_list_1.add(5)
    node_list_1.add(3)
    node_list_1.add(1)

    node_list_2 = NodeList()
    node_list_2.add(6)
    node_list_2.add(4)
    node_list_2.add(2)


    def merge_two_node_list(list1, list2):
        merged_list = NodeList()
        # 1) 새롭게 발생항하는 merged_list도 1추가할 때마다, 해당node로 이동시킬 수 있다.
        # 2) .get_node()를 정의하고, 현재이 node를 반환해주도록 작성한다.
        # list1_curr = list1.get_head()
        # list2_curr = list2.get_head()
        # while list1_curr.prev and list2_curr.prev:
        while list1.has_next() and list2.has_next():
            # if list1_curr.value < list2_curr.value:
            if list1.get_head_value() < list2.get_head_value():
                # merged_list.add(list1_curr.value)
                merged_list.add(list1.get_head_value())
                # list1_curr = list1_curr.prev
                list1 = list1.next()
                continue
            # merged_list.add(list2_curr.value)
            # list2_curr = list2_curr.prev
            merged_list.add(list2.get_head_value())
            list2 = list2.next()

        # 3) 둘 중에 남은 것을 [ False가능성 A or 기본값B]로 처리해서
        #    A가 시작특이점이면, next로 업데이트된 B를 가져와서
        #    merge_curr의 다음것으로 B(아직남은)를 붙인다.
        # left_head = list1_curr if list1_curr.prev else list2_curr
        left_list = list1 if list1.has_next() else list2
        # print(left_list)
        return merged_list.merge(left_list).reverse()

    merge_two_list = merge_two_node_list(node_list_1, node_list_2)
    print(merge_two_list)

    print(node_list_1)
    print(node_list_2)


if __name__ == '__main__':
    solution() 
