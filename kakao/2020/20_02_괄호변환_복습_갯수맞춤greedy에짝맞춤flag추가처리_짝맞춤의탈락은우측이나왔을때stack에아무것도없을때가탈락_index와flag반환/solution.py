import sys

input = sys.stdin.readline


def parse(p: str):
    ## 4. 현재 p 탐색로직에 [짝 맞춤by stack]도 추가해서, 쪼개는index외 [짝맞춤여부 flag도 추가해준다.
    ## => 탐색하며, 하나라도 실패시 [탈락 검사]이면 True로 초기화해놓고, if flag시 False를 반영한다.
    correct_parenthesis = True
    my_stack = []
    ## 2. 2개의 서로다른 괄호의 갯수를 세면서 p를 탐색한다. (투포인터가 아니므로 while X)
    left_count = 0
    right_count = 0
    for i in range(len(p)):
        if p[i] == '(':
            left_count += 1
            ## 4-1. 짝맞춤에선 왼쪽이라면 stack에 넣어주고
            my_stack.append(p[i])
        else:
            right_count += 1
            ## 4-2. 짝맞춤에선 오른쪽이 나오면 pop한다.
            # my_stack.pop()
            #### 6 짝맞춤에서 [flag처리는 오른쪽 것이 나왔을 때, pop할 왼쪽이 없으면 탈락]이다.
            #### => 이것만 검사하는 것이 아니므로, True로 초기화하는 부분만 없다면, breka없이 그냥 두면 된다.
            if not my_stack:
                correct_parenthesis = False
            else:
                my_stack.pop()
        #### 3. 카운팅을 최초로 하고나서부터, 갯수가 같아지는 순간
        #### =>  마지막괄호 + 1 index를 반환하여, u, v를 나눈다.
        # p: ()))((()
        # u: ()  ))((():v
        #        2
        if left_count == right_count:
            # return i + 1
            ## 7. flag로직이 추가되었다면, 그것도 같이 tuple로 반환한다.
            return i + 1, correct_parenthesis

    ## 8. [반복문 내부 if flag return/break]라면, 끝처리도 해줘야한다.
    ## -> 문제에서는 무조건 if에 걸린다고 했지만, 디버깅용으로 return해준다.
    return 0, False


def convert(sub_u: str):
    temp = ''
    for c in sub_u:
        if c == '(':
            temp += ')'
        else:
            temp += '('
    return temp


def solution(p: str):
    if len(p) == 0:
        return ''

    v_start_index, correct = parse(p)
    u = p[:v_start_index]
    v = p[v_start_index:]
    if correct:
        return u + solution(v)

    # return "(" + solution(v) + ")" + convert(u[1:-1])

    ## 10. 재활용할 일이 없으면, [index순회 seq재할당-변환]하기 위해, index로 순회하면서 확인하여 변환한다
    answer = "(" + solution(v) + ")"
    # for i in range(1, len(u) - 1):
    #     if u[i] == '(':
    #         u[i] = ')'
    #     else:
    #         u[i] = '('

    ## 11. 이어 붙일거면 순회하면서, 그냥 확인하고 += 해준다.
    for i in range(1, len(u) - 1):
        if u[i] == '(':
            answer += ')'
        else:
            answer += '('

    return answer

if __name__ == '__main__':
    ## 괄호변환: https://school.programmers.co.kr/learn/courses/30/lessons/60058
    p: str = input().strip()

    if len(p) == 0:
        print('')
        exit()

    ## 1. 괄호의 갯수가 같은 것 중 가장 짧은 것을(같아지는 순간 끝)을 찾아내서 -> 쪼개야한다
    ## => index로 발견할테니, 나누는 인덱스 중 오른쪽껏 시작index를 반환해준다.
    # print(p)
    # print(parse(p)) #(2, True)

    ## 8. parse가 반환해주는 짝맞춤 여부에 따라 다른 처리를 한단다.
    v_start_index, correct = parse(p)
    # if correct:
    #     print(p[:v_start_index], )
    ## 9. 결과물 중 1개가 부분문제가 되면, 모든 과정을 메서드로 정의해서 재귀로 만든다.
    print(solution(p))
