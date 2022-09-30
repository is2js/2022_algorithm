import sys

input = sys.stdin.readline


## 2. removed는 다 False로 초기화
##   link들은 모두 None으로 초기화해서, 주어지지 않으면 특이점 객체로 간주한다
class Node:
    def __init__(self, data):
        self.data = data  # 번호로 식별하기 위한 필드
        self.removed = False
        self.prev = None
        self.next = None

    def __eq__(self, other):
        return self.data == other.data

    def __repr__(self):
        return f"{self.__class__.__name__}[{self.data!r}, {self.removed!r}]"


if __name__ == '__main__':
    ##표 편집:https://school.programmers.co.kr/learn/courses/30/lessons/81303
    n, k = map(int, input().split())
    cmd = []
    for _ in range(9):
        cmd.append(input().strip())

    ## 1. 삭제후, 다시 끼워넣기를 하는 가짜삭제의 경우, [removed마킹 + 삭제객체 주소 stack 보관]의 linkedlist를 쓴다.
    # => 삭제한 node라도, 그 삭제시 link가 살아있는 체로 stack에 객체주소가 보관되어있어 복구가 쉽다.
    node_list = [Node(i) for i in range(n)]

    ## 3. lst로 모으는 node list는 for 직접 i-1, i번째로 돌면서, link를 연결해줘야한다.
    ##  => 1번째원소next부터 && 좌측(curr)은 .next만 /우측(next)은 .prev만 link를 연결해주면
    ##     0번째원소의 좌측prev는 None특이점  / 마지막원소의 우측next는 None특이점으로 연결된다.
    #      Nonde 0<->1  1<->2  ... n-2 <-> n-1 None
    # -> index로 접근안하고 value로 i-1, i를 본다면,
    #    (1) 초반curr=[0]번째원소로 초기화 + (2) 반복문 마지막에 curr = next로 업뎃해줘야한다.
    # curr = node_list[0]
    # for next in node_list[1:]:
    #     curr.next = next
    #     next.prev = curr
    #     curr = next
    # => 할 수만 있다면(1칸씩 움직이며, 배열안에 순서대로 있다면
    #    linkedlist의 i-1, i연결은 for i의 index로 자동+1칸씩만 움직이면서 처리
    for i in range(1, n):
        node_list[i - 1].next = node_list[i]
        node_list[i].prev = node_list[i - 1]

    ## 4. linkedlist의 cursor는 현재객체를 할당해주고 -> link를 타고 횟수만큼 curr = curr.link를 반복해서 움직인다.
    # -> index가 아니라 객체로 앞뒤객체와 비교되니, cursor 대신 curr를 써준다.
    curr = node_list[k]

    ## 6. 가짜삭제(removed마킹)을 위한 stack
    my_stack = []

    for str in cmd:
        c = str[0]
        # print(curr, node_list)
        if c == 'U':  # 앞으로  cursor 이동
            for _ in range(int(str[2:])):  # 현재자리부터~ 슬라이싱 활용
                curr = curr.prev
        elif c == 'D':  # 뒤로  cursor 이동
            for _ in range(int(str[2:])):
                curr = curr.next
        elif c == 'C':  # 현재 cursor의 객체 가짜삭제
            ## 5. 삭제는 (1) removed마킹 후 객체주소 stack append 쌓는 것이다.
            ## => 이 때, 객체주소만 복사되서 stack에 append될 것이다.
            curr.removed = True
            my_stack.append(curr)
            ## 7. 삭제는 (2) 앞/뒤객체 keep해놓고, 각 각채를 특이점검사 후 link조절해준다
            ##    =>    (3-1) 뒤 객체가 존재하는 경우, link조절 + cursor도 같이 뒤 객체로 옮겨줘야한다.
            ##          (4) 뒤 객체가 존재하지 않는 경우(curr가 마지막), link조절X ->  앞객체로 cursor를 옮겨주면 된다.
            curr_prev = curr.prev
            curr_next = curr.next
            if curr_prev:
                curr_prev.next = curr_next
            if curr_next:
                curr_next.prev = curr_prev
                curr = curr_next
            else:
                curr = curr_prev
        else:  # 직전 삭제된 객체(stack poo에 객체주소) 복구하기
            ## 8. 복구는 (1) stack.pop으로 살릴 객체의 주소를 가지고 와 -> removed마킹을 clear해준다.
            node = my_stack.pop()
            node.removed = False
            ## 복구도 (2) [삭제마킹전에도 소유하고 있던 link로] 앞뒤객체 확보후 -> 특이점 검사후 link 조절한다.
            ## => 복구시는 cursor(curr)가 움직이 않으니, [뒤객체 존재유무]를 따지지 않는다.
            node_prev = node.prev
            node_next = node.next
            if node_prev:
                node_prev.next = curr
            if node_next:
                node_next.prev = curr

    answer = ['X' if node.removed else 'O' for node in node_list]
    print(''.join(answer))
