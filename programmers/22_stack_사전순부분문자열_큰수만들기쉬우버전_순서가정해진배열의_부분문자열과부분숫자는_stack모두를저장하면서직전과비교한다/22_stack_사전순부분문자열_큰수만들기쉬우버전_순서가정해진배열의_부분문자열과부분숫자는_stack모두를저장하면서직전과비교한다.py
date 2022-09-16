import itertools
import sys
 
input = sys.stdin.readline 
 
 
if __name__ == '__main__':
    ## 사전순 부분문자열: https://chaelinyeo.github.io/%EC%BD%94%ED%85%8C/Level02%EC%82%AC%EC%A0%84%EC%88%9C%EB%B6%80%EB%B6%84%EB%AC%B8%EC%9E%90%EC%97%B4/
    s = input().strip()
    # 순서가 정해졌는데 부분문자열을 만들기
    # -> 이미 정해진 순서대로 뽑는 조합으로 만들고나서, 앞글자 가장 큰 것으로 정렬하기?(정렬하면 앞글자 기준으로 됨)
    #    글자수만큼 조합을 다 만들어야함 1~n
    # -> 큰수만들기 => stack에 직전과 비교해서 더 큰것이 나오면 앞에거 다 날리고 큰 것만 남기기
    #    작은수는 그냥append해서 모으기
    # => [순서가 정해진  부분문자열 | 부분숫자]를 구성할 때는, stack -> [순차적으로 확인대상으로서 저장하면서, 직전보다 큰 것이 나오는 순간 pop으로 다날리기]
    #    시간복잡도만 괜찮으면 => 순서정해진데로 글자수대로 조합으로 뽑아서 역순 정렬하기

    ## 조합 풀기
    # result = set()
    # for i in range(1, len(s) + 1):
    #     result |= set(map(''.join, itertools.combinations(s, i)))
    # print(sorted(result, reverse=True)[0])

    ## stack으로 풀기
    ## => 순서가 이미 정해진 것을 순회하면서, 모든원소를 검사대상으로 append하되, 직전과 비교해서 더 큰게 나오면 앞에것들 pop
    stack = []
    for x in s:
        # (2) 2번재원소부터 stack에 저장된 직전과 비교해서 채운다
        # if stack:
        #     if x > stack[-1]:
        #         stack.pop()
        #         stack.append(x)
        #     else:
        #         stack.append(x)

        # (3) 앞에것들을 다 날려야하므로 while로 바꾼다
        # => 성공/실패시 모두 append하므로 아래 공통과정을 겪게 한다
        # => else문이 없는 중첩if문은 합친다.
        while stack and x > stack[-1]:
            stack.pop()
        # stack.append(x)

        # (1) 일단은 append해서 stack을 채운다.
        stack.append(x)

    print(''.join(stack))