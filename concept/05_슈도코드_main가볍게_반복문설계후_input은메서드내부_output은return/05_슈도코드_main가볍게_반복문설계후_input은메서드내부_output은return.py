import sys 
 
input = sys.stdin.readline





def solution():
    ## TestCase별 처리 방법 2가지
    # (1) 메인에서 while로 TC만큼 다 돌리기
    TC = int(input())

    while TC:

        N, M = map(int, input().split())
        answer = process()
        print(answer)

        TC -= 1

    ## main함수는 최소화 해서 가벼워야한다. 내용들은 다 함수로 보낸다.
    ## 반복문을 돌되, 각 TestCase마다 따로 처리되도록 함수로, TC별 처리되도록 하는 함수를 만들어서 돌린다.

    ## (2) main TC만큼 반복문을 돌되
    #  -> 반복문내 CASE별로 매 메서드 내부에서 입력
    #  -> 반복문으로 CASE별로 정답을 return
    #  -> 반복문에서 print
    #  --> 모든 처리는 반복문내 CASE별 메서드가 처리
    TC = int(input())
    for _ in range(TC):
        print(process())

    def process():
        N, M = map(int, input().split())
        # 로직
        return answer

    ## 문제 읽는 순서
    ## (0) 시간 -> N수를 보고 알고리즘 판단하기 (단순반복문 1초당 10^7이하 -> 그 이상 다른 알고리즘)
    ## (1) 그림에서 수치따기 -> input예시보고 대응하기 -> 이후 요구사항 중 출력요구사항을 먼저보기
    #  (2) main함수는 횟수위주로 간단하게 만들기 위해
    #      -> 반복문 어떻게 돌릴지 판단하기
    #      -> #process()등 슈도코드로 기능별 메서드 작성해서 배치하기
    #   ex> i에 기능? j에? k에? -> 슈도메서드로 기능배치부터 한다.
    #       제일 안쪽 k에 배치한다면 인자(파라미터)는 i, j, k를 다 먹는 메서드를 만든다.
    #      -> 돌면서 정답을 찾는 것이라면 answer -> 반복문 -> answer업뎃한다.
    #   cf) answer를 상한 값으로 초기화한다면 [반복문내 찾기] ->  answer = min(answer, p)
    #   cf) answer를 하한 값으로 초기화한다면 [반복문내 찾기] ->  answer = max(answer, p)

    answer = 4
    for i in range(ALL):
        for j in range(i, ALL):
            for k in range(j, ALL):
                p = check(i, j, k) # pseudo-code
                if p and result(): # pseudo-code
                    answer = min(answer, p) # ansewr가 상한이며, 더 작은 값을 작는 중이네
    print(answer)

    pass

 
 
if __name__ == '__main__': 
    solution() 
