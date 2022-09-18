import math
import sys
from collections import deque

input = sys.stdin.readline

if __name__ == '__main__':
    ## 기능개발: https://school.programmers.co.kr/learn/courses/30/lessons/42586
    ## 풀이 구루미: https://gurumee92.tistory.com/169?category=782306
    ## queue: (기본) 1개부터 넣어놓고 매번 탐색해서 추가한된 순서대로 빼서쓰기
    ##        (확인용) 다 넣어놓고, 1개씩 빼서, peek직후들과 비교한뒤, 확인될 시 그만큼 묶어서 처리하기
    progresses = list(map(int, input().split()))
    speeds = list(map(int, input().split()))

    # (1) 미리 1개씩 확인하면서 빼서 쓸 queue를 만들어놓는다.
    left_days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    q = deque(left_days)

    # (2) 직후와 비교해서 조건을 만족했을 때, [묶음처리]를 저장할 공간을 만들어둔다.
    result = [] # 묶음마다 원소들을 저장할 2차원배열 저장소
    result_count = [] # 묶음마다 갯수를 저장할 공간

    # (3) queue가 존재해야시 [현재 확인주체]를 꺼낼 수 있다.
    # -> stack은 [현재 확인주체들(직전들peek)]를 append해서 진입해놓고, 확인대상들이 확인하고 append
    #    queue는 [현재 확인주체(popleft)]를 while q후 꺼내놓고, 이미 남겨진 확인대상들(직후들) 또한 while q로 확인 뒤  검사한다
    while q:
        # (4) 확인주체는 일단 꺼내놓고 / 갯수라면 1로 초기화 / 모음이라면 [curr]자신을 집어넣어놓고 시작한다
        # => 매번 확인주체가 [확인실패후 새로운 묶음]을 만들기 위해 새롭게 꺼내질때마다 초기화시킨다.
        curr = q.popleft()
        curr_count = 1  # 꺼낸것부터 세기
        curr_result = [curr]  # 직후들과 검사하며 묶을 공간 => 자신도 넣어놓을 것

        ## (5) 직후if q or 직후들 while q:을 존재확인후 peek확인하여 꺼내든지 / 다시 확인주체로서 처음으로 가서 꺼낸다
        while q:
            peek = q[0]
            # if 확인 성공시 현재 확인주체와 묶어주기 위해 꺼내서, 카운트 or 원소를 모은다
            if peek <= curr:
                curr_count += 1
                curr_result.append(q.popleft())
            # else 확인 실패시 직후검사 종료 -> 새로운 확인주체가 그 다음부터 새로운 묶음처리준비를 하기 위해
            # => 확인주체 curr를 초기화하러 가기 위해 [직후들 탐색 while q를 break]한다
            else:
                break

        ## (6) 직후들 검사가 break or 다써서 끝났다면, [현재 확인대상과의 묶음결과를 저장]한다
        result_count.append(curr_count)
        result.append(curr_result)

    ## (7) 결과를 다룬다.
    # => 만약, stack처럼 직전검사들이 중간에 끊겨서, append될 확인주체들이 남았다면, 그대로 싸잡아서 넣어주면 되는데
    #    queue는 이미 다 넣어놓은 것에 대해 사라질때까지 다 꺼내는 상황이므로, 끝처리가 없다
    print(result, result_count)






