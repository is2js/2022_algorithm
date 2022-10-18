import sys 
 
input = sys.stdin.readline


def parse(p: str):
    #### 2. 결과적으로 나올 u,v 중 u가 올잡괄인지 표기하기 위해, correct 변수를 True로 초기화화고
    ####    => 쌍이 맞지않으면 False로 재할당해서 반환한다.
    ####    => 조건에 따라 달라지는 검증값(T/F or None/notNone)은 미리 flag가변변수로 초기화하고 시작한다?!
    correct = True

    ## 3. 짝이 맞는지를 stack이 아닌 count로 처리한다.
    left = 0 # ( 갯수
    right = 0  # ) 갯수
    ## 4. 쌍을 맞출때는 stack 자료구조를 사용한다(undo할 것을 모아둘때도.. 직전들과 비교할때도.. 직전1개만 검사할때도)
    my_stack = []
    ## 5. for문을 p를 1글자씩 돌면서, 문자열 1개씩 처리한다.
    for i in range(len(p)):
        ## 5-1. 열린괄호 처리 -> stack 짝처리는 left만 append한다.
        if p[i] == '(':
            left += 1
            # my_stack.append(p[i])
            my_stack.append("(")
        else:
            ## 5-2. 닫힌 괄호라면 카운팅 후, stack에 짝 확인해야한다.
            ## => 짝맞춤과, 순서맞춤은 별개이므로, 짝맞춤을 위한 counting을 먼저한다.
            right += 1
            #### => right는 left가 stack에 존재해야하므로, stack empty라면 짝이 안맞는 경우다.
            if len(my_stack) == 0:
                #### 5-3. 짝이 안맞으면, return False대신  flag를 false처리한다.
                correct = False
            else:
                # 열린괄호가 있으면 짝맞추면 pop
                my_stack.pop()

        #### 7. left하고 right를 카운팅하는 이유는 [가장 최소길이의 짝]을 발견하기 위해서다
        ####   [left, right 최초로 같아지는 부분] == [가장 짧은 짝]
        #### => 확인할 놈 p[i]처리 직후, 매번 확인한다.
        if left == right:
            #### 8. 가장 작은짝을 발견했다면, [u와 v를 분리하기 위한 position]을 반환한다.
            #### => 분리position은 뒤에것 v의 시작위치로 주면 된다.
            #### => 현재 i까지 처리해서, 짝은 맞추었으니, i + 1을 넘겨주면 된다.
            # return i + 1
            #### 9. 분리위치와 더불어서, 같이 확인한 u의 올잡괄 correct여부
            ####    => 갯수는 같더라도, 순서맞춤이 안될 수 있어서, 순서맞춤여부 correct flag도 같이 반환한다.
            ####    => 순서안맞음 by (뒤")" 차롄데, stack에 짝맞춤용 "("가 없는 상태)을
            ####       갯수맞춤logic에 flag로 더불어서 처리했다.(True -> 1개라도 안맞는 순간 False)
            #### ====> my) 더불어처리는 flag로 하며, 한개라도 안맞는 순간 False라면, True로 초기화해서 처리
            return i + 1, correct
    #### 10. 문제에서 항상 균형잡힌문자열(갯수맞음)만 주어진다고 했으니
    ####      if left == right는 무조건 걸리는 종착역이고, return은 거기만 있어도 된다.
    ####  => 그래도 디버깅용도로 default값을 반환해줘야한다.
    return 0, False


if __name__ == '__main__':
    ## 괄호변환: https://school.programmers.co.kr/learn/courses/30/lessons/60058
    p = input().strip()

    # if len(p) == 0:
    #     print(p)
    #     exit()
    #
    # ## 1. 요구사항2. u는 더이상분리할 수 없는 균잡괄-> 가장 작은 균잡괄을 찾아야한다.
    # ## -> parse라는 함수로 구현하자.
    # ## -> 요구사항3. u가 올잡괄이면, u를 끝내고 + v만 처음부터 수행
    # # parse(p)
    #
    # ## 11. 정의한 parse는 2가지 처리(가장빠른u를 찾고, v 시작 pos  + 순서맞춤여부correct)
    # pos, correct = parse(p)
    #
    # ## 12. u,v를 value를 직접 받지 않고, pos로 건네주며, 이것을 직접 나눠야한다.
    # ## => 나누는 index는 항상 다음시작을 기준으로 잡아서, [:담시작] [담시작:]이 되도록하자 like pos + window
    # u = p[:pos]
    # v = p[pos:]

    ## 13. u가 올바른 문자열에 따라서 재귀처리
    ## => v부터가 새로운 p가 되므로 현재처리 과정을 재귀함수 solution으로 만들어야 한다.
    # if correct:

    ## 14. 재귀함수 만들기
    # -> 재귀함수는 종착역을 만들어야하는데, 문제에서 미리 주어졌다.
    def solution(p: str):
        if len(p) == 0:
            return p

        pos, correct = parse(p)

        u = p[:pos]
        v = p[pos:]

        if correct:
            return u + solution(v)

        ## 15. u가 올잡괄이 아니면, 요구사항대로 처리한다.
        answer = '(' + solution(v) + ')'
        ## u를 앞뒤빼고 짝괄호 뒤집기
        #### => u의 value를 바꾸는 작업은 index로 접근해야, 원소에 재할당이 가능하다.
        #### => 1~n-2까지만 돌면서, ( -> )로 재할당해주자.
        for i in range(1, len(u) - 1):
            if u[i] == '(':
                answer += ')'
            else:
                answer += '('

        return answer


    print(solution(p))





    pass