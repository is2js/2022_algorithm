import itertools
import sys

input = sys.stdin.readline


def is_prime_number(n):
    # 판단은 2 ~ 제곱근N을 약수로 하므로, 2이하의 수는 예외처리한다.
    if n < 2:
        return False
    if n == 2:
        return True
    for k in range(2, int(n ** (1 / 2)) + 1):
        if n % k == 0:
            return False
    else:
        return True

    pass


if __name__ == '__main__':
    # https://school.programmers.co.kr/learn/courses/30/lessons/42839
    numbers = input().strip()
    # print(list(set(itertools.permutations(numbers, 1))))
    # print(list(set(itertools.permutations(numbers, 2))))
    # print(list(set(itertools.permutations(numbers, 3))))

    ## 문자열011에 int를 씌우면 알아서 앞쪽 0은 사라진다.
    ## 문자열011에 permutation을 때리면, 1은 서로 다른 숫자로 인식하여 011 011 씩 2개씩 생긴다. -> set으로 제거한다.
    # case = []
    ## 개별 순열에서 뿐만 아니라, 갯수별 순열결과에도 11 vs int(011)에서도 중복이 생긴다. => 중복을 제외하고 모으기 위해 애초에 set()에 add한다.
    case = set()
    for i in range(1, len(numbers) + 1):
        # print(list(map(int, map(''.join, set(itertools.permutations(numbers, i))))))
        # [1, 0]
        # [10, 1, 11]     => 11과
        # [11, 101, 110]  => 011 의 중복이 또 생긴다.
        # => 각 배열을 extend로 합친다.
        # case += list(map(int, map(''.join, set(itertools.permutations(numbers, i)))))
        # => set끼리의 extends는 |= 합집합으로 한다.
        case |= set(map(int, map(''.join, set(itertools.permutations(numbers, i)))))
    # print(case)
    # {0, 1, 101, 10, 11, 110}
    # max_case = max(case)
    ## 가장 큰수까지의 모든 소수를 che를 이용해서 만들 수도 있지만, 사용량이 적으므로
    ## -> 각각을 소수 판별한다
    count = 0

    ## 또한, permutation해놓고도.. 중복이 생긴다.  11(2)  vs 011(3) -> 11
    # for x in set(case):
    # for x in case:
    #     if is_prime_number(x):
    #         # print(x)
    #         count += 1

    ## 소수후보들을 set으로 모은 상태에서, 배열을 따로 만들지 않고도, set의 차집합은 해당안되면 빼도 그대로를 이용해서
    # => set을 이용해서 체 알고리즘의 소수배수들들
    # (1) 2~max값의 제곱근N까지만 순회하면서,
    for i in range(2, int(max(case) ** (1 / 2)) + 1):
        # (2) 모두 소수라고 가정하고, 그것들의 배수들을 차집합 한다.
        # 원래는 소수발견시, 소수의 2배수~ 들은 모두 비소수므로 제외시켜야하는데
        # if che[i]:
        # 소수의 배수뿐 -> 비소수, [일반수의 배수 -> 비소수] 이므로,
        # 모든 수의 배수 -> 비소수로서 set의 차집합대상이므로 다 끼워넣어서 날린다.
        case -= set(range(2 * i, max(case) + 1, i))
    # (3) 원래 2부터 탐색하여 배수들을 비소수로서 날리므로, 0과 1은 따로 제외시켜준다.
    case -= set(range(0, 1 + 1))

    print(len(case))

