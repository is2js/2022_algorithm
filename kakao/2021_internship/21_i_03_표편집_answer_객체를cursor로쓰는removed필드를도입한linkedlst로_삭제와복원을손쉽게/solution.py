import sys

input = sys.stdin.readline


class Node:
    def __init__(self, number):
        self.removed = False
        self.prev = None
        self.next = None
        self.number = number

    def __repr__(self):
        # return f"Node [ {self.removed}]"
        return f"Node [{self.number}, {self.removed}]"

if __name__ == '__main__':
    ##표 편집:https://school.programmers.co.kr/learn/courses/30/lessons/81303
    n, k = map(int, input().split())
    cmd = []
    for _ in range(9):
        cmd.append(input().strip())

    #### (1) [삭제시에도 cursor가 유지]되는 배열을 처리하기 위해서는
    #### => prev/next이외에 removed필드를 가지는 Node class를 정의하고
    ####    각 필드는 None으로 초기화한다.
    #### (2) Node배열을 만든다. linkedlist class까진 정의하지 않나보다.
    # nodes = [Node() for _ in range(n)]
    nodes = [Node(_) for _ in range(n)]

    #### (3) prev/next link는 직접 초기화해준다(linkedlist아닌 경우)
    #### => link는 2개의 node를 비교해야하니 [curr, next] 혹은 [i-1, i]로 반복문을 돌려서 처리한다.
    ####  cf) 2개의 배열-> zip -> curr, next => 첫번째 가변변수 curr 초기화후 [1:]부터 시작 => curr = next 수동 업뎃
    ####      1개의 배열 -> i-1, i => 가변변수 필요없고, for i range(1, )부터 시작하여, 자동 업뎃
    #### => 직전꺼 오른쪽, 다음꺼 왼쪽만 처리해주면
    ####     0번째는 왼쪽 안해도됨(head = None)
    ####     n-1번째는 오른쪽 안해도됨(tail = None)이기 때문에
    ####     [양끝의 처리를 안해도 된다면] => [직전꺼오른쪽/다음꺼 왼쪽] 단위로 link를 업데이트한다.
    for i in range(1, n):
        nodes[i - 1].next = nodes[i]
        nodes[i].prev = nodes[i - 1]

    # print(list(enumerate(nodes)))

    #### (4) linkedlist의 cursor는  node배열을 인덱싱해서 [객체를 가리키게]한다
    #### => cursor를 index가 아닌 객체로 유지한다.
    curr = nodes[k]

    #### (5) 복원 -> stack을 사용한다.
    my_stack = []

    #### (6) 명령어처리 -> x or xy 인데 첫번째[0]만 확인하면 어떤 것인지 알 수 있다.
    #### => 뒤에 숫자가 나온다면, [i:]형태로 슬라이싱해서 여러단위 숫자도 처리되게 한다.
    # -> my) 나는 가운데 공백을split()으로 처리해서.. 자동으로 묶여서 나왔었는데...
    for str in cmd:
        if str[0] == 'U':
            x = int(str[2:])
            #### (7) U는 그냥 curr에 담긴 객체를 prev링크타고 올라간 객체를 cursor에 할당해주면 된다
            #### => linkedlist는 여러번 이동해야한다면, 여러번 link업뎃해주면 도니다.
            for _ in range(x):
                curr = curr.prev
        elif str[0] == 'D':
            x = int(str[2:])
            for _ in range(x):
                curr = curr.next
        elif str[0] == 'C':
            # print(curr)
            #### (8) 삭제는 실제pop대신, 현재 curr객체를 append만 해준다.
            my_stack.append(curr)
            curr.removed = True
            #### (9) 위아래 link 업데이트
            #-> 일단 타고가서 각각의 객체를 keep해둔다.
            up = curr.prev
            down = curr.next
            #-> 타고가서keep해둔 node는 특이점 검사를 해야한다.
            if up: # 직전이 시작특이점 아닐 때 == curr가 첫node아닐때
                ## link필드들을 건너띄어서 연결해준다.
                up.next = down
            if down: # 다음이 끝특이점 아닐 떄 == curr가 마지막node아닐때 == 다음이 있을 때
                down.prev= up
            #### (10) curr stack -> removed 마킹 -> link업뎃이후에는
            #### => cursor역할인 curr가 가리키는 객체를 아래행으로 바꿔준다.
                #### 10-1 curr 마지막 node아닐때만, 삭제후 바로 다음인 down을 curr가 가리키기 한다.
                #### 다음이 잇는 경우니까, 그 다음을 curr가 가리키게 한다.
                curr = down
            else:
                #### 10-2 down없다 = 다음없다= 마지막행이다. -> curr는 바로 위를 가리켜야한다.
                curr = up
        #### (11) Z 복구인 경우
        else:
            #### stack 리얼pop(실제 뽑아서 넣은 것은 아니지만, 객체주소는 연결되어서, pop해서 조작하면 된다.)
            # => pop해서 받으면, nodes에 있는 node객체가 조작된다?!
            # => stack에 배열 속 객체를 가져와 append하면
            # => stack은 객체참조용 저장소가 된다. (값이 아니라 객체append시)
            # -> 배열의 값이 아니라 객체로 복원을 구현하는 이유..?!
            # removed 마킹제거
            node = my_stack.pop()
            node.removed = False
            #### [복구될 놈의 위아래node] link 업뎃을 위한 객체 뽑아두기
            # -> 자신은 removed=True만 해주고, prev/next는 삭제되기 전 그대로 유지된 상태다
            # => [복원은 위아래node의 link만 removed된 나와 연결해주면, 삭제된 node link가 복구]된다.
            # -> 삭제할때, stack에 추가했지만, 배열에 있는 것과 동일한 객체이며
            #    삭제전 가리키던 위아래node link가 prev, next의 필드에 그대로 살아있다.
            up = node.prev
            down = node.next
            # 복원된 node가 첫행/마지막행일 수도 있으니 항상 검사한다.
            if up:
                up.next = node
            if down:
                down.prev = node
            # 복원은 curr를 옮기지 않고 그대로 둔다. 마지막행이라도

    #### (12) 이제 node배열을 가지고 있으니, 순회하면서 removed에 따라 O/X를 넣어주면 된다.
    #### => 삭제후 복원을 쉽게하기 위해 node객체 + stack에 객체주소append를 쓴다.
    #### => 삭제후 cursor가 이동되는 경우, cursor를 맨마지막에 link만 따라 수정해주면 되므로 linkedlist를 쓴다
    ####    linkedlist는 [복원시 삭제된link기억->prev/next node 특정쉬움 -> 삭제후 복원편리/cursor이동 자유로움]이 무기다
    #### => 사실상 removed는 가짜 삭제된 것들(이자 복원가능성)을 필터링하기 위해, 반드시 필요하다
    answer = ''
    for i in range(n):
        if nodes[i].removed:
            answer += 'X'
        else:
            answer += 'O'
    print(nodes)
    print(answer)
