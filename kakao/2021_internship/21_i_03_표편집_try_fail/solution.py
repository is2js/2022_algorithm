import sys

input = sys.stdin.readline


def execute_z(data, stack, cursor):
    print(data, stack)
    popped_data, popped_index = stack.pop()
    if popped_index <= cursor:
        cursor += 1
    data.insert(popped_index, popped_data)

    ## 삭제된 stack 속 인덱스에서 [나보다 같거나 앞에것이 복구]되는 순간부터는
    ## => 삭제된 것의 index도 밀어줘야한다?
    for i, (d, c) in enumerate(stack):
        if popped_index <= c:
            stack[i] = (d, c + 1)
    print(data, stack)

    return cursor


def execute_c(data, stack, cursor):
    stack.append((data.pop(cursor), cursor))
    if cursor == len(data) - 1:
        cursor -= 1

    ## 삭제되는 순간, 나보다 같거나 앞에것이라면..??
    ## => 나보다 작을 때만 당겨준다.
    ## => data에 다른게 추가될 때는, 나보다 작거나 같은 곳에 추가시 밀기
    ##    data에 다른게 삭제될 때는, 나보다 작을때만 삭제시 당기기
    ##      -> 내위치랑 같은놈이 삭제된다면.. 그자리 insert는 동일하다..
    ##      -> 내위치랑 같은 놈이 추가된다면, insert는 밀린다.
    ##삭제된 것의 index를 당겨줘야한다
    for i, (d, c) in enumerate(stack):
        if cursor < c:
            stack[i] = (d, c - 1)

    return cursor


if __name__ == '__main__':
    ##표 편집:https://school.programmers.co.kr/learn/courses/30/lessons/81303
    n, k = map(int, input().split())
    cmd = []
    for _ in range(9):
        cmd.append(input().strip())

    cmd_map = {
        'U': lambda x, y: x - y,
        'D': lambda x, y: x + y,
    }

    data = list(range(0, n))
    stack = []

    cursor = k
    answer = ''
    for c in cmd:
        ## 옵션이 달릴 수 있으나.. 첫번째는 동일유형이면 나중에 startswidth로?
        if c[0] in ['U', 'D']:
            c, count = c.split()
            cursor = cmd_map[c](cursor, int(count))
        elif c[0] == 'C':
            # stack.append(data.pop(cursor))
            cursor = execute_c(data, stack, cursor)
        else:
            cursor = execute_z(data, stack, cursor)

    stack_ = [k for d, k in stack]
    for i in range(n):
    ## stack에 남아있는 경우, Z를 한 것처럼, 1개씩 꺼내면서 인덱스 조정되게 해서 비교해야한다...
        if i in stack_:
            answer += 'X'
            cursor = execute_z(data, stack, cursor)
        else:
            answer += 'O'



    print(answer)






