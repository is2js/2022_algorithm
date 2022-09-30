import sys

input = sys.stdin.readline

if __name__ == '__main__':

    ## 가짜삭제후 복구(by 삭제를 위한 stack)가 가능한 [정해진 길이 + cursor]의 node list
    ## => 모든 커맨드가 아닌, [삭제(C)만 undo(Z)대상으로 보므로, 삭제undo용 stack이 필요]하다
    ##    모든 커맨드는 커맨드패턴에서 이렇게 한다. 대신 add발생시, 움지이던 현cursor이후로 stack 싹다 removed후(stack[:cursor + 1]) add되어서 cursor  redo대상(커맨드1칸 전진)들 사라짐
    ## => 삭제에 대한 redo를 구현할라면, undo대상들을 stack에 저장해놓고, redo시 꺼내서 do(C)하면 된다.
    n, k = map(int, input().split())
    cmd = []
    for _ in range(11):
        cmd.append(input().strip())


    ## 1. node class 정의
    class Node:
        def __init__(self, data):
            self.data = data
            self.removed = False
            self.prev = None
            self.next = None

        def __repr__(self):
            return f"{self.__class__.__name__}[{self.data!r}, {self.removed!r}]"

    ## 2. node list 생성
    node_list = [Node(i) for i in range(n)]

    ## 3. node link 초기화
    # -> i-1의 next, i의 prev끼리 연결하여, 0번재/마지막 원소는 prev/next가 None
    for i in range(1, len(node_list)):
        prev = node_list[i - 1]
        curr = node_list[i]
        prev.next = curr
        curr.prev = prev

    ## 4. linked list의 cursor는 curr에 객체할당 및 link를 타고 움직인다.
    curr = node_list[k]

    ## 5. 삭제후 복구를 위한 가짜 삭제된 객체주소저장용 stack
    stack_for_undo = []

    ### redo를 위해 추가 진행 1###
    # undo된 목록들을 stack에 순서대로 저장해, 최근것부터 redo를 위한 stack을 만든다 #
    stack_for_redo = []
    ###########################


    ## 6. U(prev)/D(next)/C(delete)/Z(undo) 정의
    # U 2 / D 3 / C / Z => /R로 redo추가해보기
    for s in cmd:
        # 1) 'U', 'D'의 이동은 link를 1개씩 타고 n번 움직인다.
        if s[0] == 'U':
            for _ in range(int(s[2:])):
                curr = curr.prev
        elif s[0] == 'D':
            for _ in range(int(s[2:])):
                curr = curr.next
        # 2) 'C'의 삭제는 가짜삭제로서
        # (1) curr객체의 removed마킹 + stack에 삭제된 객체로서 주소 저장
        # => # link연결이 끊겨 GC에 들어가기 전에,  다른데 자료구조에 저장하여 연결해놓기
        # (2) prev/next객체 보유하고 -> if 객체존재시(0/마지막원소는 없을 수 있음) -> 삭제된 node를 제외하고 서로 연결
        # (3) if next 존재시 link연결외에 + curr(cusror객체)를 next로 옮기기
        # (4) if next 존재안할시 -> curr(cursor객체)를 prev로 옮기기
        elif s[0] == 'C':
            # print('C', stack_for_undo, stack_for_redo)
            curr.removed = True
            stack_for_undo.append(curr)
            curr_prev = curr.prev
            curr_next = curr.next
            if curr_prev:
                curr_prev.next = curr_next
            if curr_next:
                curr_next.prev = curr_prev
                curr = curr_next  #
            else:
                curr = curr_prev  #
        elif s[0] == 'Z':
            # print('Z', stack_for_undo, stack_for_redo)
            # 3) 복구는 삭제보다 더 쉽다. removed 클리어 + stack에서 pop해서 삭제된 객체 사용하기
            # -> 복구는 삭제와 달리, cursor이동이 전혀없다.
            # my) stack이 존재할 때를 먼저 확인해야할 듯
            node = stack_for_undo.pop()

            ### redo를 위해 추가 진행 2###
            # -> undo되는 것들을 최근순으로 redo stack에 append한다.
            # 참고 cursor로 redo하기: https://raw.githubusercontent.com/is3js/screenshots/main/image-20220811121544292.png
            # java: https://github.com/imcts/code-spitz/blob/64cf34a914ddf1883e08a7c6b52fa318ee2dd147/codespitz84/src/listen4/command/CommandTask.java
            stack_for_redo.append(node)
            #############################

            node.removed = False
            node_prev = node.prev
            node_next = node.next
            if node_prev:
                node_prev.next = node
            if node_next:
                node_next.prev = node
        elif s[0] == 'R':
            if not stack_for_redo:
                print("삭제후 복구된 것이 없습니다.")
                continue
            # print('before R', stack_for_undo, stack_for_redo)
            # print(node_list)
            node = stack_for_redo.pop()
            ## 삭제후 복구되었던 node를 다시 삭제해야한다.
            # -> 과정은 C랑 동일할 것 같아서.. 복붙
            # -> 객체 주소만 가지고 있다가 다시 삭제하는 것이다..
            node.removed = True
            stack_for_undo.append(node)
            node_prev = node.prev
            node_next = node.next
            if node_prev:
                node_prev.next = node_next
            if node_next:
                node_next.prev = node_prev
                node = node_next  #
            else:
                node = node_prev  #
            # print('after R', stack_for_undo, stack_for_redo)
            # print(node_list)

    # before R [Node[4, True]] [Node[7, False], Node[1, False]]
    # [Node[0, False], Node[1, False], Node[2, False], Node[3, False], Node[4, True], Node[5, False], Node[6, False], Node[7, False]]
    # after R [Node[4, True], Node[1, True]] [Node[7, False]]
    # [Node[0, False], Node[1, True], Node[2, False], Node[3, False], Node[4, True], Node[5, False], Node[6, False], Node[7, False]]
    # before R [Node[4, True], Node[1, True]] [Node[7, False]]
    # [Node[0, False], Node[1, True], Node[2, False], Node[3, False], Node[4, True], Node[5, False], Node[6, False], Node[7, False]]
    # after R [Node[4, True], Node[1, True], Node[7, True]] []
    print(curr, node_list)
    # CCZ 전
    # [Node[0, False], Node[1, True], Node[2, False], Node[3, False], Node[4, True], Node[5, False], Node[6, False], Node[7, True]]
    # Node[3, False] [Node[0, False], Node[1, True], Node[2, False], Node[3, False], Node[4, True], Node[5, False], Node[6, False], Node[7, True]]
    # Node[6, False] [Node[0, False], Node[1, True], Node[2, False], Node[3, True], Node[4, True], Node[5, False], Node[6, False], Node[7, True]]

    pass
