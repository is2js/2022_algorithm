import sys

input = sys.stdin.readline


## (4) 커스텀 Stack은 기본적으로 push/pop/size를 가진다.
class MyStack:
    def __init__(self):
        self.lst = list()

    def push(self, x):
        self.lst.append(x)
        return x

    def pop(self):
        return self.lst.pop()

    def size(self):
        return len(self.lst)

    def __repr__(self):
        return f"{self.lst!r}"


## (2) stack2개로 popleft를 구현하는 queue
class EmptyException(Exception):
    pass


class FullException(Exception):
    pass


class MyQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        ## (3) stack2개로 구현하는 커스텀queue는, 필드에 stack 2개를 가지고 있다.
        self.stack1 = MyStack()
        self.stack2 = MyStack()

    ## (5) queue는 기본적으로 push / pop(left)/ size를 가진다.
    # => 여기서 stack2개로 pop을 popleft로 구현하는 것이 핵심이다.

    ## (6) 메인queue는 stack1이다. stack2는 popleft구현에만 쓴다.
    def size(self):
        return self.stack1.size()

    ## (7) 문제요구사항에 queue의 max_size는 queue의 push제한을 만든다.
    def push(self, item):
        try:
            ## push의 갯수 제한 -> 해당 자료구조의 용량 제한이다.
            if self.stack1.size() == self.max_size:
                raise FullException
            self.stack1.push(item)
            return item
        except FullException:
            print('queue의 용량이 가득찼습니다')
            return False

    ## (8) pop은 stack1 전체를 pop -> stack2에 원래배열 역순으로 담아놓았다가
    #    => stack2를 pop하면 원래배열의 popleft가 된다.
    def pop(self):
        ## (10) 모든 과정에서 발생한 Exception을 try, except로 처리한다.
        # -> 예외가 발생하면, return False한다.
        # => 그냥 놔두면 프로그램이 꺼진다. 잡아서 return까지 해줘야한다
        try:
            # 꺼낼때는 갯수검사를 한다.
            if self.stack1.size() == 0:
                # (9) 커스텀 Exception은 Exception클래스를 상속해서 만든다.
                raise EmptyException
            ## [1] stack1을 역순으로 처음부터 끝까지 pop해서 stack에 담아야한다.
            # while self.stack1:
            ## => list가 아니라 객체기 때문에 비어있어도 항상 True이므로
            #  => 직접 stack ls까지 가거나 len으로 비교한다.
            # while self.stack1.lst:
            while self.stack1.size():
                self.stack2.push(self.stack1.pop())

            ## [2] stack2에서 1개만 pop하면, popleft 1개만 하는 것
            first_item = self.stack2.pop()

            ## [3] 다시 stack2에 있던 것들(원래배열을 역순으로 넣고 첫번째꺼만 pop남은 것들)
            #  다시 pop해서 stack1에 역순으로 담는다. 432 -> 234
            while self.stack2.size():
                self.stack1.push(self.stack2.pop())

            ## [4] stack1복구가 완료되면 꺼낸 것만 반환한다.
            return first_item
        except EmptyException:
            return False

    ## (12) 추가로 queue의 상태(main stack1)을 보여주자
    def __repr__(self):
        return f"{self.__class__.__name__}({self.stack1.__repr__()!r})"


if __name__ == '__main__':
    ## 최대 용량이 정해진 FIFO 큐 클래스: https://abluesnake.tistory.com/50
    # 그림: https://rollingsnowball.tistory.com/94?category=929338
    ## [1] queue를 stack2개로 구현할 수 있다.
    # -> 원래배열을 stack pop으로 역순으로 탐색하면서,
    # -> 그것을 다른 stack에 집어넣으면, 원래stack역순저장하며 + pop으로 최근버려진부터 역순으로 가져올 수 있다
    # => 즉, [모두 pop한 것을 담는 stack2]을 쓰면,
    #       (1) 원래 배열(stack) 역순으로 저장 + (2) 역순으로 다넣고 다시pop하면, 원래 배열(stack)의 앞쪽부터 pop(popleft)가 된다.
    #     + (3) redo는 [unoo로 일부pop해서 undo]한 것을 저장했다가, [redo로 최근undo한것부터 다시do]할 수 있다
    # => 이 때, pop한것을 담는 stack2가 용량이 미리 정해져있다면
    #    원래배열의 역순으로 k개까지만 역순저장 -> pop시 원래배열의 뒤에서부터k깨지만 popleft되는 효과가 생긴다.

    # stack1(n) : (확인주체가 되는 것들의)최근것 부터 역순으로 꺼내고 싶어 저장한다.
    # stack2(k):  stack1에 pop된 것들을 뒤에서부터 최근순으로 담지만, 갯수가 n보다 작아
    #             원래배열의 역순저장이지만, stack1(n)의 뒤 에서부터 k개만 담을 수 있다.
    #            => stack1에서 pop된 것을 다 담았다면, stack1의 역순으로 구성되어
    #            => pop하는 순간 원래stack의 popleft가 구현되는 것이다.

    #  stack1:  1 2 3 4

    #  stack1:  1 2 3
    #                /
    #               /
    #             /
    #  stack2:  4

    #  stack1:  1 2
    #               |
    #               |
    #              /
    #  stack2:  4 3

    ## 참고 -> 한쪽 길이가 다를 때
    #  stack2: 4
    #  pop     3
    #  stack2:
    #  pop     3 4 => 원래배열 순서지만, stack2의 받을 수 있는 용량이 적으면, 뒤에서부터 k개까지만 pop된다.

    ## 한쪽의 길이가 같거나 그 이상이 가능할 때(일반적인 경우)
    #  stack1:
    #  stack2:  4 3 2 1
    # => stack2를 내부에서 pop하면, stack1의 popleft가 구현되는 것과 같다.
    #  stack2 : 4 3 2  => pop  1
    #  stack2 : 4 3    => pop  1 2

    n, max_size = map(int, input().split())
    # (1) 커스텀queue의
    my_queue = MyQueue(max_size)
    for _ in range(n):
        command = input().strip()  # 1개도 있고 2개도 있다면, 일단은 쪼개지 않는다.
        # => 1개 짜리들을 모두 직접 검사하고 else라면, split()해서 나눈다.
        if command == 'POP':
            print(my_queue.pop())
        elif command == 'SIZE':
            print(my_queue.size())
        ## => 1개짜리들이 아닌 경우는 else로 처리한다. len으로 확인해도 상관없긴 하다.
        else:
            # PUSH item
            command, item = command.split()
            my_queue.push(int(item))
        print(command, my_queue)
