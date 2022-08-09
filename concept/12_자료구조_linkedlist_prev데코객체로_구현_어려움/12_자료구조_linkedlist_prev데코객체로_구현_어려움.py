import copy
import sys

input = sys.stdin.readline


# https://www.geeksforgeeks.org/python-program-for-reverse-a-linked-list/


# sort 관련https://stackoverflow.com/questions/19217647/sorted-linked-list-in-python

class Node:
    def __init__(self, value, prev=None):
        self.value = value
        self.prev = prev

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value!r})"


class NodeList:
    def __init__(self, node=None):
        self.head = node if node else Node(None)

    def add(self, value):
        self.head = Node(value, self.head)

    def insert(self, prev_value, value):
        current_node = self.head
        if current_node.value == prev_value:
            self.add(value)
            return

            ## 나와, 다음것 사이에 추가한다면, 미리 시점이동해서 처리한다.
            # while current_node.prev:
            #     next = current_node
            #     current_node = current_node.prev
            #     if current_node.value == prev_value:
            #         new_node = Node(value)
            #         new_node.prev = current_node
            #         next.prev = new_node
            ## 출력상으로 다음차례에 삽입되려면... 나와 <-> 다음 것 사이가 아니라
            #  나 <-> 이전 것 사이에 삽입해야한다.
            #  즉, 시점이동 안해도 된다?
        print(self)
        while current_node.prev:
            if current_node.prev.value == prev_value:
                new_node = Node(value)
                ## 나는 new_node를 prev로 물고 태어나는 다음타자다.
                ## --> 조심 -> 연결할 앞에 것들부터 먼저 연결해주고, 뒤에것을 연결해줘야한다?
                ## --> [앞쪽에 있는 new_node부터 prev필드를 채워 완성해놓고 -> 다음 것(current_node)에 물려줘야한다]
                ## 안그러면 똑같은 것으로 업데이트된다.
                ####잘못된순서
                # current_node.prev = new_node
                # -> prev필드가 미완성된 new_node를 먼저 넣어준다.
                # -> 이 순서로 가면 # current_node.prev가 new_node로 바뀐 상태다.
                # -> .prev로 보이지만, 객체가 있다. 그 객체를 안쓰고 먼저 덮어버리면 안된다.
                # new_node.prev = current_node.prev ->
                ###
                new_node.prev = current_node.prev # 1) .prev속 node인 앞에꺼부터 덮어쓰기 전에 먼저 갖다 쓰고
                current_node.prev = new_node      # 2) 업데이트해준다
                print(f"{prev_value}의 다음 node로 {value} node를 추가했습니다.")
                return
            current_node = current_node.prev
        return


    def __repr__(self):
        current_node = self.head
        result = ""
        # while current_node.prev: # 보통은..특이점객체에 도달하면 멈춤
        while current_node:  # 특이점객체 진입허용 -> NULL로 출력
            result += self.get_repr(current_node)

            current_node = current_node.prev

        return result


    def get_repr(self, current_node):
        # [특이점 객체의 이전것일 때]
        if current_node.prev is None:
            # return str(current_node)
            ## 특이점객체의 이전것일 때 -> 콤마제거 대신 NULL추가?
            return "NULL"
        return str(current_node) + ", "


    def reverse(self):
        # 역순Prev데코객체가 될 업데이트 변수
        # -> 첫값은 객체가 아니라 저장안되고, 다음부터 객체가되어 필드에 저장된다.
        prev = Node(None)
        current_node = self.head
        ## 특이점객체Node( ?, None)를 쓴다면, 무조건 prev필드로 검사한다.
        while current_node.prev:
            temp = current_node.prev

            # 마지막prev데코객체의 value를 시작value로 활용하여
            # value는 그대로, prev만 역순으로 가는 prev데코객체를 만든다
            # 이 때, prev필드값은 None으로 시작되어 업데이트된다.
            # -> value 4부터 3, 2, 1을 채운 Prev데코객체가 된다.
            # -> prev필드 초기None부터, current_node로 업데이트해나간다
            #    외부에서넣어줄 다음 value와 prev객체는 재활용된다.

            # 1) None을 .prev로 가진 새로운 역순prev 특이점객체 완성
            current_node.prev = prev
            # 2) current_node를 이용하여 prev필드에 prev를 집어넣어 완성했으면,
            #    현재역순prev데코객체를 덮어쓴다.
            prev = current_node

            current_node = temp

        # 3) 각 prev필드마다 역순으로 저장된 current_node재활용 데코객체는
        #   list의 head로 주면 된다.
        self.head = prev
        ## 값객체를 변수에 할당한 순간.. deepcopy안한다면.. 덮어쓴다


    def reverse_helper(self, current_node, prev):
        if not current_node.prev:
            return prev
        temp = current_node.prev
        current_node.prev = prev

        return self.reverse_helper(temp, current_node)


    def reverse_recursive(self):
        current_node = self.head
        prev = Node(None)

        self.head = self.reverse_helper(current_node, prev)


    # ## value를 탐색하여 삭제
    def remove(self, value):
        current_node = self.head

        while current_node.prev:
            # 1) 삭제할 본인이라면.. 나(self.hdea)를 삭제해야하는데
            #    다음 것 -> self.head로 덮어써버리면 된다
            if current_node.value == value:
                self.head = current_node.prev
                print(f"{value}노드가 삭제되었습니다.")
                return

            # 2) 내 다음 것을 삭제한다면 현재 <-> 다다음을 연결하되
            #    current를 다음것으로 엄데이트하기 전에,
            #    [어차피 다음것 if조사할 거, 미리 업데이트 하되, 현재 것을 덮어쓰기 전에 next로 빼놓으면]
            #    next <-(curr)-> prev(curr.prev)를 연결하면 된다.

            # current_node = current_node.prev
            next = current_node
            current_node = current_node.prev
            if current_node.value == value:
                # 나(next)와 다다음것(current_node.prev)를 연결한다.
                # 무시하고 연결해서 삭제한다.
                next.prev = current_node.prev
                print(f"{value}노드가 삭제되었습니다.")
                return

        print("삭제할 요소가 없습니다.")
        return


    def update(self, before_value, after_value):
        current_node = self.head
        while current_node.prev:
            if current_node.value == before_value:
                current_node.value = after_value
                print(f"{before_value} -> {after_value} update")
                return
        print("there is no value")


    def sort(self, reverse=False):
        current_node = self.head
        lst = []
        while current_node.prev:
            lst.append(current_node)
            print(current_node)
            current_node = current_node.prev
        lst.sort(key=lambda node: node.value, reverse=reverse)
        return [Node(None)] + lst


def solution():
    ## linked list 구현
    ## https://velog.io/@yeseolee/python-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%97%B0%EA%B2%B0%EB%A6%AC%EC%8A%A4%ED%8A%B8Linked-List-feat.LeetCode

    node_list = NodeList()
    node_list.add(2)
    node_list.add(3)
    node_list.add(4)

    print(node_list)
    node_list.reverse_recursive()

    print(node_list)
    node_list.remove(4)
    print(node_list)
    node_list.remove(2)
    print(node_list)
    node_list.remove(3)
    print(node_list)

    node_list.update(3, 5)
    print(node_list)

    node_list = NodeList()
    node_list.add(5)
    node_list.add(2)
    node_list.add(7)
    #
    node_list.insert(2, 3)
    print(node_list)


if __name__ == '__main__':
    solution()
