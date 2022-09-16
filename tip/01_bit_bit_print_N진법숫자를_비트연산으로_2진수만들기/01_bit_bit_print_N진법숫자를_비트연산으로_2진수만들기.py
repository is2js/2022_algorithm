import math
import sys

input = sys.stdin.readline


def bit_print(number, bit=8):
    # (1) number가 가지고 있는 최대 bit수를 확인하여 그만큼 우쉬프트를 활용하여 마지막 자리를 확인한다.
    min_of_bit = int(math.log2(number)) + 1
    if min_of_bit > bit:
        bit = min_of_bit

    # (2) 필요한 bit수만큼 돌면서, >> 우shift로 매번 1의 자리(0번째자리)에 불이 켜지는지 확인한다.
    stack = ''  # 2진법 등 N진법 수로 변환할 땐 문자열로! (무조건 1자리수)
    # -> 음수표시를 위해서 끝에서부터, 필요bit + 1만큼 처리한다.
    for _ in range(bit + 1):
        stack += '1' if number & (1 << 0) else '0'
        number = number >> 1

    # 우측부터 확인하니, 나열은 역순으로
    return stack[::-1]


if __name__ == '__main__':
    n = 2
    # left shift는 (1) 10진수 -> 2의 n승 (2) 2진수 -> n번째 자리수만 1 나머지 0 -> 0 or 1로 구성된 used_bit와 연산용으로 사용
    print(1 << n)

    ## 1. 10진법 숫자 -> 2진법 문자열 변환 by 우shift
    # -> 비트연산으로 자동 2진법 변환되니, 우shift하면서 1의 자리를 확인한다.
    # cf) 2진법의 10진법 변환은 (1) 문자열숫자를 [::-1]로 뒤집고 -> (2) 앞에서부터 enumerate로..
    number = -5

    # (1) 우shift가 반복될건데, 0이 되면 종료
    # stack = []
    stack = ''
    curr_number = number
    # while curr_number:
    calc_count = int(math.log2(abs(curr_number))) + 1
    num_of_digits = 8  # 기본 8bit로 나타내자
    if calc_count < num_of_digits:
        calc_count = num_of_digits
    for _ in range(calc_count + 1):
        # (2) 00001 과 &연산으로 2진법 1의자리가 1인지 0인지 자리 확인
        # -> 1이면 문자열 1을 갖춤. -> 먼저나와도 맨 뒤에 가져야하므로.. stack에 넣어놔야한다.
        # => 한자리 문자열이면, 문자열누적합으로 보관해도 된다.
        if curr_number & (1 << 0):
            stack += '1'
        else:
            stack += '0'
        curr_number = curr_number >> 1
    # (3) 0과 1의 역순으로 출력하면 된다.
    # print(number, stack[::-1])
    ## 함수화
    print(bit_print(5))

    ## 2. 2(n)진법 문자열 -> 10진수 로는 int(, base=)로 해결하면 쉽다.
    #        N진법 숫자 with시작문자 -> 문자열변환하던지 or print()로 바로 출력가능
    # print(int('110', base=2))  # 6

    # -> n진법 숫자 -> 10진수는 print만 해도 나온다.
    # print(0b110)  # 0b2진법-110 -> 6
    # print(0X011)  # 0X16진법-11 -> 17

    # -> n진법 숫자 ->  우쉬프트 0으로 10진수 숫자로 변환가능하다.
    print(0x010 >> 0)
    # 16
    print(0b011 >> 0)
    # 3

    ## 3. 4byte 16진수2자리(1bit)가 4개 -> 2진법8자리가 4개 끊어서 계산해야한다.
    # -> 4byte는 1byte씩 읽는다.
    # -> 1byte는 이진수 8bit로서, 2진수 8개가 들어가있다
    # -> 16진수는 1자리당 2진수 4개씩으로 표현된다. -> 4bit가 16진수 1자리다.
    #    16진수는 0x로 시작하며, 10~15의 2자리수들은 1글자의 A~F로 표현한다.
    # (1) 좌쉬프트 << n -> 2진수로 변환후 ->  bit계수마다 x 2^n의 새로운 값이 된다.
    print(1 << 6)  # 1*2^0 -> 1*2^6 => 64
    print(3 << 6)  # 1*2^1 + 1*2^0 -> 1*2^7 + 1*2^6 => 128 + 64 -> 192
    # (2) 우쉬프트 >> n -> 2진수로 변환후 -> bit계수마다 n씩 2**(x-n)이 된다.
    # cf) n진수숫자 >> 0 은 n진법숫자를 10진수로 바꿔준다.
    # ==> 비트연산 우쉬프트는 2진수로 n자리 이동이지만, 16진수로는 n//4 자리 이동이다.
    # ==> 16진수는 1자리는 2진수 4자리에 해당한다.
    #     그렇다면, 16진수를 1자리씩 처리 -> 우쉬프트 4개씩 처리하면 된다.
    #     1byte = 2진수 8bit(8자리) = 16진수로는 2자리
    # print(bit_print(0x11))

    ## 4byte -> 1btye * 4개를 각각 끊어서 계산한다.
    x = 0x01020304


    ## 16진수 -> 2진수로 나타내고 싶다면, 2자리식 끊어서 계산해야한다.
    # => 비트연산으로는 8칸씩 땡겨서 계산해야한다.
    # => 4byte라서 4번이다.
    # 2진수로는 4byte는 32자리다... 첨엔 3*8만큼 땡겨놓고 앞에것들만 남겨야한다.

    def bit_print_for_byte(number, bit=None):
        # (1) 1byte는 8bit씩 끊어 계산되므로, 최대 8자리만 처리하도록 한다.
        if not bit:
            bit = 8

        # (2) 앞에 더 있더라도  -> 뒤에서부터 8개 중 7번째 자리부터 0까지 8개만 확인한다.
        # => 이렇게 해야, 끊어서 계산할 때, 우쉬프트로 8개 넘기면 앞에 있던 8개가 그대로 처리가능하다.
        #    ex> 16bit -> 처음8개 -> 우shift >>8 -> 뒤에 8개만 처리가능
        result = ''
        for i in range(bit - 1, 0 - 1, -1):
            result += '1' if number & (1 << i) else '0'

        return result


    for i in range(0, 8 * 3 + 1, 8):
        print(bit_print_for_byte(0x01020304 >> i), end=' ')
