import math
import sys
from collections import deque

input = sys.stdin.readline

if __name__ == '__main__':
    ## 기능개발: https://school.programmers.co.kr/learn/courses/30/lessons/42586
    ## 풀이 구루미: https://gurumee92.tistory.com/169?category=782306
    ## my) 넣어놓은 직전들과 비교하고 넣기 -> stack
    ##    <->  다넣어놓고, 빼낸 뒤, while queue 남은 직후들과 비교해서 묶기 -> queue(deque)
    ##         나보다 뒤쪽이 먼저끝냈으면, 같이 묶어주기
    progresses = list(map(int, input().split()))
    speeds = list(map(int, input().split()))

    ## (1) index로 매핑된 value들을 동시에 다루려면, zip을 쓴다.
    # => 기존 배열을 업데이트를 한다면,  index로만 접근해도 된다.
    #    그러나, [2개의 배열을 사용한 결과가 col_index순서대로 새로운 배열]을 만든다면
    #    zip으로 묶어서 col_index매핑된 value들만 사용해도 된다.
    ## (2) (작업량 / 속도 ) 올림 -> 남은 일수는   올림으로 처리한다.
    # =>  나누어 떨어지면 멈추고, 나머지가 조금이라도 있으면 1개를 올리는 작업량 계산
    #    (1) 나누어 떨어지면 그대로두고 (2) 나머지가 생기면 소수부짜르고 +1 => 올림
    left_days = []
    for p, s in zip(progresses, speeds):
        remain_work = (100 - p) # 남은 작업량
        remain_days = math.ceil(remain_work / s)
        left_days.append(remain_days)
    # print(left_days) # [7, 3, 9]

    ## my) 남은 일 수 계산을 [1일씩 실시간]으로 업데이트한 뒤, 확인하면 너무 복잡해진다.
    ##     7 3 9 => 남은 일수들을 미리 계산(나누기 + 올림)하고난 뒤,
    #               queue를 통해서, 앞에서부터 pop하면서, 직후와 비교한다.
    #      뒤에 남은 일수가 나보다 빨라 끝났다? => 직후도 pop해서 묶어주기
    #                                         while 나보다 빨리 끝낸 뒤에애들 다 pop해서 묶어주기

    ## (3) 직후와 비교해서, 같이 땡겨오기 -> 기존배열을 queue(dequeue)에 넣어놓고 시작한다.
    ##     queue는 FIFO기 때문에, 필요하다면 뒤에 더 추가해도 되지만,
    ##    [일단 다 넣어놓고 시작하기] deque() 생성자에 기존배열을 넣어놓고 시작한다
    q = deque(left_days)
    # print(q)
    ## (4) queue는 먼저 1개를 꺼내놓고 while을 돌면서 2번째부터 비교하면 된다
    # -> stack은 먼저 1개를 넣어놓을 수도 있지만, 배열순회 append(x)를 기본으로 하고 if stack2번째부터 검사하게 했다.
    curr = q.popleft()
    # 묶이는 갯수를 세기 위한 count
    # => queue는 일단 1개 빼고 직후와 검사하기 때문에 count = 1을 넣어준다.
    # curr_count = 0
    curr_count = 1
    result = []

    ## (5) q가 있는 동안 직후와 검사하고, 직후는 q[0]이 peek이다.
    while q:
        peek = q[0]
        # 먼저 나온놈보다 더 일찍끝났거나 같이 끝났다면 묶어주기 위해 popleft()를 확정한다.
        if peek <= curr:
            q.popleft()
            curr_count += 1
        # 직후가 더 크다면 묶이지 않는다. -> 직후가 다음 curr가 되도록 해준다.
        # => 기존까지 묶었던 것을 처리해줘야한다
        else:
            result.append(curr_count)
            # curr_count = 0
            curr_count = 1
            curr = q.popleft()

    ## (6) q도 다썼는지 확인해야한다.
    # => 더이상 비교할 직후가 없으면, 현재를 마지막 따로 또 처리해줘야한다.
    # cf) stack은 비교할 직전이 없다면, 현재를 몰아서 처리해준다.
    # cf) queue는 비교할 직후가 없다면, 현재를 몰아서 처리해준다.
    result.append(curr_count)

    print(result)