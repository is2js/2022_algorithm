import sys

input = sys.stdin.readline


if __name__ == '__main__':
    ## 짝지어 제거하기: https://school.programmers.co.kr/learn/courses/30/lessons/12973#:~:text=%EC%A7%9D%EC%A7%80%EC%96%B4%20%EC%A0%9C%EA%B1%B0%ED%95%98%EA%B8%B0%EB%8A%94,%EC%A0%9C%EA%B1%B0%ED%95%98%EA%B8%B0%EA%B0%80%20%EC%A2%85%EB%A3%8C%EB%90%A9%EB%8B%88%EB%8B%A4.
    # -> 직전과 검사하여 제거해야하므로 stack을 쓴다.
    s = input().strip()
    stack = []

    for x in s:
        ## (2) 확인 주체만 존재한다면, if 로 확인해서 즉시 append 후 continue로 다음 원소로 넘어간다
        ## => 모든 순회원소들을 다 확인 후 모으되, 확인되면 주체와 대상을 같이 날려서 모은다.
        #     성공 -> 확인주체 -> pop / 확인대상 -> not append로   동시에 같이 날아가야한다.
        ## (3) if stack에 확인 주체가 진입된 순간부터는, 현재원소x와 비교해야한다.
        # if stack:
        #     peek = stack[-1]
        ## (4) if stack 존재하면서 if 확인 성공시 -> peek pop하고 x not append한다
        #                           확인 실패시? -> x를 append하고 넘어간다
        ##  (5) else 실패시 append -> 뒤에 모든 원소 대상이라 모으니 append
        ##    => 중복이므로 성공시 continue하고 끝내면 else는 필요없이 공통과정이라 생략한다
        ##    => else가 없는 중첩if(if stack, if 확인조건)은 조건문을 합쳐준다
        if stack and x == stack[-1]:
            # 직전과 같으면, 현재와 직전만 제거하고, append없이 다음배열로 넘어가도록 continue를 날린다
            stack.pop()
            continue

        ## (1) 일단 append하고, 2번째부터 검사하게 한다.
        ## (6) stack이 빈상태던지 or 확인실패던지 둘다 append되어야하는 것이 공통이므로
        ##     if확인성공을 제외하고 공통 과정이 되게 한다
        ##    => 확인성공은 continue가 있으니 아래로 안내려온다. 그외 상황(확인 실패 or not stack) 공통이다.
        # if not stack:
        stack.append(x)

    # (7) 다돌았는데 stack에 append되었다면, 직전과 짝을 못맞춰진 것이다.
    else:
        print(1 if not stack else 0)