import sys

input = sys.stdin.readline

if __name__ == '__main__':
    # 대중소 괄호 짝 맞추기 : https://chaelinyeo.github.io/%EC%BD%94%ED%85%8C/Level01%EB%8C%80%EC%A4%91%EC%86%8C%EA%B4%84%ED%98%B8%EC%A7%9D%EB%A7%9E%EC%B6%94%EA%B8%B0/
    s = input().strip()

    # (5) 확인대상원소별 정답 매핑dict
    correct_parenthesis = {
        ']': '[',
        ')': '(',
        '}': '{',
    }

    # (1) 배열을 탐색하되, 먼저 나와야해서 확인용 node가 되는 것들을 stack에 저장한다.
    stack = []
    for x in s:
        # (2) 확인 주체로서 진입해야할 node들은 stack에 저장한다.
        ## 1글자씩으로 구성된 문자열이면 배열대신 문자열seq를 쓰자.
        if x in '[{(':
            stack.append(x)
        else:
            # (3) 확인 대상 원소들은, 진입된 stack에서 peek으로 꺼내서 검사완료되면 pop해야한다.
            # -> 꺼내기 전에 존재 검사부터 한다.
            if not stack:
                print(False)
                break

            # (4) 이제 진입된 stack node를 peek으로 꺼내서, 현재의 확인대상 원소들을 확인한다.
            # ] -> [ , ) -> ( , } -> { 가 맞는지 검사해야한다.
            # => 올바른 정답을 미리 매핑해놓되, 숫자가 아니므로 문자열index는 dict에 매핑해두자.

            # (5) 확인대상은 stack의 peek을 보고 확인해야한다.
            peek = stack[-1]
            # (5-1) 확인O : stack에서 확인용 node를 pop으로 삭제 -> 직전node로 간다. / 배열탐색도 다음원소로 가야한다.
            # (5-2) 확인X : flag처리해서 실패해야한다.
            # => pop 후에는 직전node 및 다음배열원소로 넘어가야한다. (맨끝에 위치 or continue)
            if correct_parenthesis[x] == peek:
                stack.pop()
            else:
                # (6) 하나라도 틀리면 flag처리된다.
                print(False)
                break
    else:
        # (5) 배열원소들을 다 검사했는데, stack에 확인용 node가 남았을 경우, 모자란 것이므로 처리해준다.
        # -> stack도 비워져있으면 모두 통과다
        # => true false삼항연산자는 True가 되도록 바꾸고 조건문만 넣어주자.
        # print(False if stack else True)
        # print(True if not stack else False)
        print(not stack)