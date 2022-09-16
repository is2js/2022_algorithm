import sys

input = sys.stdin.readline

if __name__ == '__main__':
    N, number = map(int, input().split())
    # (10) 정렬이나 탐색시 len == 1일때는 정답이 바로 튀어나오도록 예외처리를 해주자.
    if number == N:
        print(1)

    # (1) stack별 [정답후보들]을 담을 수 있는 [빈set()으로 구성된 dp테이블]을 마련해놓는다.
    # -> 보통은 점화식 -> 그 때의 정답을 1부터 기록해나가지만,
    #    여기서는 해당 stack에서 발생할 수 있는 모든 정답후보들을 연산별로 모아둔다. 정답을 바로 고를 수 없기 때문이다.
    dp = [set() for _ in range(8)]
    dp[0].add(N) # 첫번째 기본dp는 N 1개 밖이 못만든다.

    # (2) 각 stack별 [연산의 결과]가 아닌, [특수한 경우의 정답후보 NNN]연산과 별개이므로 미리 만들어서 넣어놓는다.
    # => 인덱스i를 내부에서 쓸거라면 그냥 enumerate()로 돌리는게 낫다.
    # for i in range(len(dp)):
    #     dp[i].add(int(str(N)*(i+1)))
    # print(dp)
    # [{5}, {55}, {555}, {5555}, {55555}, {555555}, {5555555}, {55555555}]

    # for i, candidates in enumerate(dp):
    #     candidates.add(int(str(N)*(i+1)))
    # => i + 1 대신, 인덱스 시작만 1부터 (원소는 0번째부터) 시작하게 하려면 , start=1 을 주면 된다.
    for i, candidates in enumerate(dp, start=1):
        candidates.add(int(str(N) * i))

    # (3) dp테이블에 정답후보들을 연산의 결과로 채워놓되, f(2) = f(1) X 4가지연산 하여, 매번 불려서 집어넣는다.
    # => dp는 보통 첫번째를 채우고 그 다음부터 채우지만
    # => 여기서는 [채우면서, 검사까지]하므로, 첫번째도 돌아가서 검사되어야한다.
    for i in range(len(dp)):
        # (4) i번째에서는, 0부터 i-1까지를 [j] -> [i-1에 대한 역인덱스 j]를 연산하여
        # => 직전까지를 대칭처리하려면, for문으로 i에 대한 직전(range(i)까지 돈다!!!!!
        for j in range(i):
            # (5) 각 j에 대해, 0~i-1를 기준으로 역인덱스 len - 1 - j == i개-1-j를 이용해서,
            # => 0(1회) 연산  i-1(직전) => i번째 값이 완성되게 할 예정이다.
            first_dp = dp[j]
            second_dp = dp[i - 1 - j]
            # (6) 2개의 배열읠 2중반복문으로 돌면서, 모든 연산을 수행하여 dp[i]를 만든다.
            #  3번째 연산 = 2번째연산값 연산 1번째연산값 = i-1 연산 0
            # => i번재 연산은, 0부터 시작한다면, i-1과 0이 연산하면 만들어지고, i-2와 1이 연산하면 만들어진다.
            #    0부터 시작하니 단순합으로 i를 생각해선 안됨.
            for x in first_dp:
                for y in second_dp:
                    # (7) 두 연산결과가 i번째의 dp 후보들로 넣을 수 있다.
                    dp[i].add( x + y)
                    dp[i].add( x - y) # 아무래도 앞쪽이 값이 클 것이다? 역순도 처리하니 괜찮다?
                    dp[i].add( x * y)
                    # 나누기는 y에 0이 포함될 수 잇으니 확인하고 해준다.
                    if y != 0:
                        dp[i].add( x // y)
        # (8) 매번 i번째가 채워졌을 때, dp[i]에 정답이 있는지 확인한다.
        # => 최소한의 횟수를 검사하기 위해서, 매번 보텀업으로 채워나가면서 있는지 검사해야한다.
        # => 채우면서 탐색할 땐, 한stack을 채울때마다 검사하여 탈출하게 한다.
        if number in dp[i]:
            # i는0부터시작하니 +1해서 정답으로 반환한다.
            answer = i + 1
            break
    else:
        # (9) 다돌았는데도 flag에 안걸려 탐색실패한다면 -1반환
        answer = - 1
    print(answer)






