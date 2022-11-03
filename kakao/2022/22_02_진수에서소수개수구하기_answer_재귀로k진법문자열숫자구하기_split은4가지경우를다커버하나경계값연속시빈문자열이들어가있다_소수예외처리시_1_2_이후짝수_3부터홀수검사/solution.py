import sys 
 
input = sys.stdin.readline


def convert_to_base(n, base):
    #### (1) 일단 자신의 처리까지하고 종착역을 확인한다
    #       -> 종착역이 마지막 부분문제를 푼 것을 포함시켜 끝낸다
    q, r = divmod(n, base)
    #### (2) 몫이 0이 되면, 종료다. -> 종착역에서는 직전node에 자신의 처리만 넘겨준다.
    #### my) 자신의 처리를 하고 종착역을 확인하는 것은,
    ####     직전stack의 파라미터 속 누적결과값변수 or 직전stack의 자신의 처리 + 자식들 처리누적집계할 값을 반환해준다
    if not q:
        #### 맨 마지막 나머지 값만 return하여, 직전stack에서 += 누적할 것이다.
        return str(r)

    #### (3) 자신의 처리 + 자식들이 반환해준 값 누적해서 반환
    ####     역순으로 붙여나가려면, [자식들재귀 + 자신처리]
    ####    => 부분문제가 1개라면, 꼬리재귀로서return문에 다 들어가게 해준다
    return convert_to_base(q, base) + str(r)


def check(number):
    #### 소수탐색은 3이상부터 2~제곱근k까지 하므로, 1,2는 따로 처리한다.
    #### + 2를 제외한 모든 짝수 또한 따로 처리한다.
    ####  => 2부터 처리하고 -> 그 밑에 짝수검사하면 [2를 제외한 짝수 검사]가 된다.
    if number == 2:
        return True
    #### => 밑으로는 (2가 아닌경우) #######

    #### cf) or 조건은 return값이 같다면, 따로따로 분리해서 처리된다.
    ####     return값이 다른 분리처리는, or관계가 아니다.
    #### => (앞에 처리가 아닌 경우)의 배반의 의미다.
    if number <= 1 or number % 2 == 0:
        return False
    #### return값이 같은 or는 따로 분리처리해도 되지만, ~가 아닌 경우의 배반이 아니라면 붙여처리하자.

    #### 2와 짝수들을 모저리 처리했으니, 3부터 홀수들만 검사하면 된다.
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
    else:
        return True



    pass


if __name__ == '__main__':
    # 진수에서소수개수구하기: https://school.programmers.co.kr/learn/courses/30/lessons/92335
    n, k = map(int, input().split())

    #### n진법 -> 10진수를 k묶음(0-k-1)씩 묶어서 1단계 올려주는 것
    #### 몫이 0이 될때까지 반복해서 나누고, 몫이 0이 되는순간 저장한 나머지들을 역순으로
    # https://raw.githubusercontent.com/is3js/screenshots/main/image-20220921011618803.png

    #### 소수확인 -> 자기자신과 1만 약수로서 나누어떨어져야함 -> 2~k-1은 나누어떨어지면 flag탈락
    #### 나누어떨어지는 수의 후보를 2~k-1까지 나누어떨어지는지 flag확인한다
    #### -> 2~k-1까지, k의 약수가 있는지 탐색하는데,
    ####    [만약 있더라도, 곱대칭을 이루고 있을 테니 제곱근k까지만 확인하면 된다.]
    ####    flag탐색이라서 그전에 이미 잡힌다.
    #### cf) 2를 제외한 짝수는 무조건 소수가 아니다. 98 -> 소수아니다.



    #### (1) 10진수 -> 문자열 k진법므로 변환하기 위한 재귀함수
    ####     문제에서 문자열 1글자씩 살펴보기 위해서 문자열로 변환한다
    ####     자신의 처리 + 1개 줄은 부분문제
    string_num = convert_to_base(n=n, base=k)
    # 211020101011
    #### (2) 10진수는 그냥 str(n)만 씌우면 된다.
    string_num = str(n) if k == 10 else convert_to_base(n=n, base=k)

    #### (3) 부분문자열의 경계로 특정문자열이 있을 땐 split('0')을 활용한다.
    #### => split으로 하면, 0P0 P0 0P P 모두 알아서 구분된다고 한다.
    ####    대신 0이 연속으로 존재할 경우, 경계값이 없어서 ''로 들어가는 경우도 있으니 len으로 예외처리해주면 된다.
    # print(string_num.split('0'))
    # ['211', '2', '1', '1', '11']
    string_num = string_num.split('0')
    print('00100'.split('0'))

    answer = 0
    for value in string_num:
        #### (4) flag 체크 메서드는 함수로 만들되, [변환필요시 파라미터해서 먼저 하고] 들어간다
        # if check(value):
        #### (5) split('0')은 00일 경우 빈문자열이 들어오게 도니다.
        #### 00100 -> ['', '', '1', '', '']
        #### if len(value)
        if len(value) and check(int(value)):
            answer += 1

    print(answer)




