import heapq
import sys
 
input = sys.stdin.readline 
 
 
if __name__ == '__main__':
    ## 배상비용최소화:
    # 제곱의 합이 가장 작은 경우를 찾는 문제
    # -> 제곱의 합이 가장 작은 경우 '최소자승합' 이라고 부른다.
    # -> '최소자승합'은 각 수 사이의 편차가 가장 적을 때 나온다.
    # -> 즉, 리스트에서 제일 값이 큰 item에서 계속 1씩 빼준 다음, item의 제곱의 합을 구하면 최소자승합이 나온다.
    # ->  파이썬이 제공하는 힙은 최소힙이므로 주의하도록하고 삽입 별 시간 복잡도는 O(logN)이다.

    # => 우선순위큐를 최대힙으로 사용할 때 -를 달고 넣고, -를 달고 꺼내지 말고
    #  => -를 단 값을 원소에 추가해서 튜플로 구성해도 된다.
    N = int(input().strip())
    works = list(map(int, input().split()))

    ## 최대힙으로 사용하기 위해 비용을 원소에 추가하여 튜플리스트로 구성하기
    # -> 데이터 변형이므로 map or list comp를 활용한다
    # -> 그러나 비용이 바뀌면, 원본도 같이 바꿔서 push해줘야한다.
    works = [(-x, x) for x in works]

    heapq.heapify(works)

    for _ in range(N):
        cost, value = heapq.heappop(works)
        ## 원본인 value에 -1을 해주고, cost는 그냥 역수취해서 다시 넣어준다.
        #  value기준으로 업뎃시켜놓고, cost도 같이 업뎃시켜서 넣어줌
        value -= 1
        heapq.heappush(works, (-value, value))
    # print(works )

    ## 집계는 value로만 한다.
    # -> lambda는 tuple을 언패킹 못한다.
    # print(sum_(map(lambda x: x[1]**2, works)))
    # -> for는 튜플을 언패킹할 수 있다
    print(sum(value ** 2 for cost, value in works))
