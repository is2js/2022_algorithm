import sys 
 
input = sys.stdin.readline 
 
 
if __name__ == '__main__':
    ## https://school.programmers.co.kr/learn/courses/30/lessons/12909
    s = input().strip()

    stack = []

    ## 배열 탐색하며 [자신의 종착역(닫괄만나면끝)이 있는 확인의 주체]로서 [stack에 저장하며 진입] <-> dfs [첫node부터 모든node를 stack에 넣고 peek종착역 확인하며 탐색]
    ## (1) 배열탐색하며, 여는 괄호는 [닫는괄호 등장시 자신이 종착역으로서 확인]하기 위해 [stack에 저장]
    # => stack은 확인 후 pop하여 갖다쓰면 undo로 돌아갈 수 있는 진입상태
    #    모든 원소들을 확인 후 pop하여 갖다쓰면, 역순으로 갖다쓸 수 있다(dfs, 진행중인 모든 것을 기록만)
    #    여러원소가 담긴 배열을 탐색하면서, [일부만 원소들만 stack에 쌓고, 나머지 원소들을 확인용]으로만쓰고 pop후 역순으로 안갖다쓸 수도 있다.
    ## (2) 배열탐색하며, 닫는 괄호는 [stack에저장된 여는괄호node의 확인대상]이 되어 stack에 저장

    ## 모든 원소를 저장하며 확인하지 않을 수 있다. / 모든 원소를 저장 확인 후 역순으로 받아오지 않을 수 있다.
    for x in s:
        # (3) 여는 괄호는 저장했다가 확인대상이다. -> 확인node에 진입한 것이다.
        # => 타원소의 확인용도로만 사용하면, 자신의 처리는 하지 않고, continue로 다음놈으로 넘어간다?!
        if x == '(':
            stack.append(x)
        else:
            # (4) 닫는 괄호는 stack에 저장하여 확인하는 주체가 아니라서, stack에 담긴 여는괄호의 확인 대상이다.
            # (4-1) 확인대상은 현재 확인주체가 stack에 담겨있는지 보고 사용한다. -> 확인 주체가 없으면 잘못된 상태이다.
            if not stack:
                print('false')
                break

            # (4-2) 현재진입한 확인node는 peek으로 검사후, 확인완료시 pop한다
            peek = stack[-1]
            if peek == '(':
                # 제일 바깥의 확인용 node가 확인되었다면, pop으로 날려서, 직전의 확인용 node에 진입하게 한다.
                stack.pop()

            ## 확인대상 입장에서는 stack이 비거나 or ( 여는 괄호가 있는 경우만 다루면되서 끝이다.

    ## (5) 일부만 stack에 저장하고, 일부만 검사하는데, [1:1 매칭 확인인데 그 짝이 안맞아서 확인주체가 남아있다면] -> 확인대상이 부족한 것이다.
    #  1:1 검사기 때문에, 매칭이 다 안되었다면, stack을 검사해야한다.
    # -> 1:1매칭 stack에서는 다 확인하고 나서 남아있는지도 확인한다.
    print('false' if stack else 'true')














