import sys
from collections import deque

input = sys.stdin.readline

if __name__ == '__main__':
    ## 문자열 압축: https://school.programmers.co.kr/learn/courses/30/lessons/60057
    s = input().strip()

    ## (1) stack은 순회배열의 원소x를 append하는 시점에서만 검사한다. -> [각 시점]의 직전들만 탐색하므로, 동일한 원소가 뒤에 들어올 경우 같이 처리가 안된다.
    ## (2) queue는 다 넣어놓은 상태에서, [연결된 모든 직후들을 다 검사]할 수 있다. -> queue를 써서 직후들과 묶어준다.

    min_len = float('inf')
    # for k in range(1, len(s) + 1):
    ## (3) 자르는 단위k는 최대 절반or절반에서 1칸오른쪽까지만 자르면, 최대 2개로 압축이다.
    # -> 그 이후부터는 압축이 안되므로 검사해봤자 의미가 없다.
    for k in range(1, len(s) // 2 + 1):
        e = []
        e_counter = []
        ## queue(deque)는 popleft()를 여러개 못하는데, slincing[:k]도 안된다. => 글자1개로 이루어진 문자열이므로 문자열seq로 만들어 slicing한다
        # => print(deque([1, 2, 3])[:2])
        #    TypeError: sequence index must be integer, not 'slice'
        q = str(s)

        ## 확인주체(기준)을 꺼낸다. 이 때, 1개만 하는 게 아니라, k개를 꺼내야하므로 len >= k로 검사한다.
        ## => 1개이상꺼낼 땐, 중간에 다꺼내기전 break와 마찬가지로, 못꺼내고 남아있는 것이 있을 수 있으니 마지막에 처리
        while len(q) >= k:
            curr = q[:k]
            q = q[k:]  ## popleft()대신 꺼내고 -> 그만큼 seq를 직접 줄여줘야한다.

            # 직후(들)인 peek(q[0])과 비교해나간다
            counter = 1  # q는 자신에 대해 직후를 비교하니 1부터 시작
            while len(q) >= k:
                peek = q[:k]
                if peek == curr:
                    q = q[k:]
                    counter += 1
                else:
                    ## queue는 확인실패시 그냥 break해서, 다음원소가 popleft()되어 확인기준이 되게 한다.
                    break

            ## 현재 기준인 curr에 대한 정보를 따로 저장해둬야한다.
            # -> 갯수와 중복원소를 따로따로 배열에 index매핑하여 저장해보자 -> zip으로 묶을 수 있다.
            e.append(curr)
            e_counter.append(counter)

        ## queue를 1개씩이 아닌, 2개이상 popleft()하는 경우, 못 빼내는 경우가 있으니, 나머지는 이어붙여준다.
        ## -> stack은 중간에 break되는 경우, 나머지 순회원소들을 stack에 넣어준다.
        ## -> queue는 1개이상을 pop하는 경우 or 중간에 break하는 경우, q에 남은 원소들을 pop해준다.
        if q:
            e_counter.append(1)
            e.append(q[:])

        # print(list(zip(e_counter, e )))
        ## 집계한 것 중에 1은 생략하고, 붙인다.
        result = ''.join((str(num) if num != 1 else '') + char for num, char in zip(e_counter, e))
        # print(len(result))
        min_len = min(min_len, len(result))
    print(min_len)
