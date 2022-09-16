import sys 
 
input = sys.stdin.readline


def get_prime_numbers(n):
    # (1) n까지의 배열을 생성하여 보텀업으로 처리한다.
    # -> 이 때, True로 초기화해놓고, 소수마다 소수의 배수들을 처리한다.
    che = [True] * (n + 1)
    che[0:2] = [False, False]
    # (2) 소수 판별은 for i 를 2~ 제곱근N까지만 하고,
    #    소수일 경우, 소수의 배수들을 모두 비소수처리해서
    #    소수만 True로 남긴다.
    for i in range(2, int(n**(1/2)) + 1):
        if che[i]:
            for j in range(2 * i, n + 1, i):
                che[j] = False
    # (3) 2부터, True로 남아있는 소수들(index) 반환한다.
    # print(che)
    return [i for i in range(2, n + 1) if che[i]]


if __name__ == '__main__':
    ## 세 소수의 합
    ## https://chaelinyeo.github.io/%EC%BD%94%ED%85%8C/Level01%EC%84%B8%EC%86%8C%EC%88%98%EC%9D%98%ED%95%A9/

    n = int(input().strip())

    # (1) N이하의 소수를 모두 구하기 위해서는 체 알고리즘을 써야한다.
    prime_numbers = get_prime_numbers(n)

    # (2) 세수의 합 -> 교환법칙 성립하는 수의 나열이므로 조합이다.
    # => 조합은 2~3개는 투포인터로 푼다.
    result = [] #my
    count = 0
    for i in range(len(prime_numbers)):
        srt_index = i + 1
        end_index = len(prime_numbers) - 1
        while srt_index < end_index:
            temp_sum = prime_numbers[i] + prime_numbers[srt_index] + prime_numbers[end_index]
            if temp_sum == n:
                count += 1
                result.append([prime_numbers[i], prime_numbers[srt_index], prime_numbers[end_index]]) # my
                srt_index += 1 # end_index -=1을 해줘도 될 것같은데, 작은 것을 올려주는 식으로 해보자.
                # continue  #while은 마지막에 공통 업글과정이 있어서 early continue하면 무한반복이다.
            if temp_sum < n:
                srt_index += 1
            if temp_sum > n:
                end_index -= 1

    print(count)
    print(result)
