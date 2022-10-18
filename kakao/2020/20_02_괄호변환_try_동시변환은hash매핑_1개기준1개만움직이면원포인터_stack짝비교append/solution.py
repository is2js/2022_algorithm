import sys

input = sys.stdin.readline


def check_count(p, i):
    curr_p = p[:i + 1]
    return curr_p.count('(') == curr_p.count(')')


def check_right(u):
    stack = []

    # 0) 짝이 맞는지 볼땐, stack에 기존배열을 1개씩 append하면서, 직전과 검사한다.
    for c in u:
        # 2) 있으면 직전과 검사한다. -> 실패시 탈출
        # if stack and stack[-1] == c:
        # 2-2) 짝만 맞다 -> ) (도 맞다고 치는 중... 그러면 안됨.. (부터 와야한다.
        if stack:
            if stack[-1] == '(' and c == ')':
                # 앞에 (가 있고, 나는 )면  (는pop하고 나)는 append안하고 skip하여 다음것
                stack.pop()
                continue
            # if stack[-1] == '(' and c == '(':
                # 앞에 (가 있는데, 나도 (면 쌓아두어야한다.

            if  stack[-1] == ')':
                # 앞에 )가 있을 일이 없다. 짝의 2번재는 (와 맞쳐서 pop시키는 역할 -> 있으면 탈락
                return False


        # 1) 아무것도 없을 땐 올리고 본다.
        stack.append(c)
    # 3) 다 짝이 맞아서 실패가 없었으면 통과
    else:
        return True


def recur(p):
    if not len(p):
        return ""  # return

    # 포인터를 기점으로 검사는 +1칸에서 시작해서 1칸씩 가면서 검사? 투포인터? -> 기준은 0에서 안움직이니 원포인터
    u = ''
    v = ''
    for i in range(1, len(p)):
        if check_count(p, i):
            u = p[:i + 1]
            v = p[i + 1:]
            break
    # print(f"u: {u}, v: {v}")
    if check_right(u):
        return u + recur(v)

    else:
        ## 순차변형하면... 엉킨다.
        ## -> 일괄변형 by dict mapping
        # print("not right u")
        return "(" + recur(v) + ")" + ''.join([replace_map[x] for x in u[1:-1]])


if __name__ == '__main__':
    ## 괄호변환: https://school.programmers.co.kr/learn/courses/30/lessons/60058
    p = input().strip()

    replace_map = {
        '(': ')',
        ')': '(',
    }
    ## 1. 균형잡힌 -> 갯수가 같아지면 바로 split해서 u, v로 나눈다.
    # -> i, i-1을 보는게 아니라, 현재부터k개를 호다가 걸리면 바로 break
    # -> 더이상 안쪼개야하니까 갯수같으면 바로 break
    # -> 도는데 갯수 같은 것...을 탐색하기도 전에 0개면.. out
    print(recur(p))
