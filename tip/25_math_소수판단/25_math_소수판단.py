import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## 단일 소수 판별
    N = 4

    # (1) 2~ N-1를 약수로 해서 number 하나라도 발견되면 소수탈락 다돌면 ㅇㅋ
    for k in range(2, N - 1):
        if N % k == 0:
            print('not 소수')
            break
    else:
        print('소수')

    # (2) 단일 소수 upgrade
    # -> 2~N-1 -> 2~ N제곱근만큼 까지만을 약수로
    mid_factor = int(N ** (1 / 2))
    for k in range(2, mid_factor + 1):
        if N % k == 0:
            print('not 소수')
            break
    else:
        print('소수')

    # (3) dp처럼 2서부터 N까지 모든 수의 소수 판단
    #    2~N-1 or 2~제곱근N까지 약수를 매번 돌리지말고
    # -> 특이하게 True로 초기화해놓고, (1)for i 소수 발견 -> (2) for j  소수의 2배수부터 배수들을 N까지 순회하며 False소수처리한다
    N = 50
    che = [True] * (N + 1)
    # -> 특이하게 2부터 제곱근N까지만 순회하면서 && 그것들의 배수들을 N까지 순회하며 처리한다.
    for i in range(2, int(N ** (1 / 2)) + 1):
        # -> 특이하게 초기값True로 소수인 2부터, 2배수~N까지의 배수들을 비소수 처리한다.
        if che[i]:
            for j in range(i * 2, N + 1, i):
                che[j] = False

    # -> 2부터 소수들만 출력한다
    # => value가 True일때, i를 출력하고 싶어 enum을 쓴다면, 2부터 출력시, index가 그만큼 꼬인다.
    # => 매핑index배열을 앞에 몇개빼서 출력하고 싶다면, enum의 start도 같이 땡겨준다.
    for i, value in enumerate(che[2:], start=2):
        if value:
            print(i, end=' ')
