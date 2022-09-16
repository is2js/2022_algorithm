import heapq
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## 배상비용최소화: https://chaelinyeo.github.io/%EC%BD%94%ED%85%8C/Level02%EB%B0%B0%EC%83%81%EB%B9%84%EC%9A%A9%EC%B5%9C%EC%86%8C%ED%99%94/
    ## 문제주소2: https://intrepidgeeks.com/tutorial/programmers-lv2-minimize-compensation-costs

    ## my) -> works 중에 [매번 가장 큰 수]를 뽑아 -1씩 N번 깍아줘야한다.
    ## 매번 정려하기 N * NlgN vs 매번 우선순위 만들어놓기 -> 이진힙heap정렬의 우선순위큐
    N = int(input().strip())
    works = list(map(int, input().split()))

    ## 예외처리 -> 1씩빼주는 횟수 N이, 깍임대상비용보다 더 커버리면.. 음수가 계산된다
    # => 돈계산은 음수가 나오면 안되도록 처리한다.
    if N * (-1) >= sum(works):
        print('작업을끝내 비용이 0원이하입니다')
        exit

    ## 큰수일수록 제곱하면 더 커지므로, 가장 큰수를 찾아 1씩 N번 빼줘야한다.
    # -> 매번 업데이트 후 다시 큰수를 찾아야하므로, 정렬을 자동으로 유지하는 것이 좋다
    # -> 뽑았다가 다시 넣어줘야한다.
    # -> 우선순위큐
    works = list(map(lambda x:-x, works))
    heapq.heapify(works)

    for _ in range(N):
        heapq.heappush(works, -(-heapq.heappop(works) - 1))
    # print(works)

    print(sum(map(lambda x: pow(x, 2), works)))
