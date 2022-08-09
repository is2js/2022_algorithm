import sys

input = sys.stdin.readline


## 자료구조
# python에서는 Collections에서 많이 제공한다.

## stack -> (python) list -> 담아놓고 직전꺼 undo / 중첩된구조에서 담아놓은 직전 짝 확인( 같은값의 여러개짝이 존재할 수 있으니, 직전 원소와 검사)
## LI->FO by pop()
## 방금전 행동을 담아놨다가, pop하면 -> undo를 구현할 수 있다.
## -> python에서는 [] lst배열을 바로 활용할 수 있다.
## undo이외에 중첩된구조에서 짝 확인하고 싶은 것들은 넣어두고 꺼내서 확인한다.
## 괄호의 짝 순서를 기억할 때, 여는괄호를 넣어놓고, 닫는괄호나올 시, 여는괄호를 꺼내 짝을 확인한다
def stack_pair():
    stack = []
    data = input().strip()
    for x in data:
        ## 요소가 2개밖에 안되니까 if로 쉬운 역할을 나눈다.
        if x == '(':
            stack.append(x)
            continue
        # (가아닐때 -> )일때
        ## 교훈) dict/db말고 []배열 컬렉션을 조회할 땐, [특정원소 존재검증] 이전에, [배열 null검증 존재유무] size로 -> python은 if 컬렉션: 으로 빈배열 배제
        ## 시작 원소는 저장한데이터가 없어서 넘어가야한다. 그래서 존재검증하고 조회를 실시한다.
        ## stack자료구조의 [특정원소 검증]은 존재유무검사는 stack[-1]로 하고 난 뒤, pop해야한다.
        if stack and stack[-1] == '(':
            # 짝이 맞으면, 검증완료로서 날려서 그 전에 담긴놈이 검사되게 한다.
            stack.pop()
            continue

        ## ) 인데, 빈배열이거나, (가 존재하지 않을땐... printNO하고 Break
        ## break직전에 처리를 해주고, break때린다
        print("NO")
        break
    ## break에 안걸리는 정답후보들은 else로 나머지 처리를 해준다.
    else:
        ## 짝맞춤을 위한stack은 사용후 다 비어져잇어야한다.
        ## (()) (의 경우 짝 안맞은체로 반복문이 append하고 끝난다.
        if stack:
            print("NO")
        else:
            print("YES")


def solution():
    # https://www.acmicpc.net/source/34450862
    N = int(input())

    for _ in range(N):
        stack_pair()



if __name__ == '__main__':
    solution()
