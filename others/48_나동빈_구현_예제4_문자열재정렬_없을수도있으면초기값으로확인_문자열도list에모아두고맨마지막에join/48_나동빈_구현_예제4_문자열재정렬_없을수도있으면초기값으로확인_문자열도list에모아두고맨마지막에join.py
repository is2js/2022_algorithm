import sys

input = sys.stdin.readline


def process():
    ## 내풀이
    data = input().strip()
    "".isalpha()
    "".isnumeric()
    chars = []
    numbers = []
    for c in data:
        if c.isalpha():
            chars.append(c)
        if c.isnumeric():
            numbers.append(int(c))

    print("".join(sorted(chars)) + str(sum(numbers)))


if __name__ == '__main__':
    ## 문자열 재정렬
    # 알파벳 대문자와 숫자0~9로만 구성된 문자열 입력
    # -> 알파벳을 오름차순 정렬하여 출력한 뒤, 모든 숫자를 더한 값을 이어서 출력한다
    # ex> K1KA5CB7 -> ABCKK13
    # => 수(10, 100, 700) vs 숫자(0~9사이 1글자 데이터)

    ##  내풀이
    # => 숫자가 안주어졌을 때 sum_()str
    # for row in range(2):
    #     process()

    ##  풀이
    # => 문자열도 list에 다 모아 놓은 뒤, 맨 마지막에 출력하기
    # => 숫자는 초기값이 아닐 때만 붙여 출력하기!
    # ==> 문자열이든, 숫자든 포함이 안될 수 있는 case도 생각하자.
    # => 숫자가 안주어졌을 때의 sum_()은 0을 반환하여 오답처리될 수 있다.

    data = input().strip()
    result = []
    value = 0

    for x in data:
        if x.isalpha():
            result.append(x)  # 문자열은 일단 더한다.
            continue
        value += int(x)  # 숫자는 일단 집계를 한다.

    result.sort()
    # 숫자가 존재하는 경우에만 삽입해야한다.
    # 1 <= S <= 10**4인데, S 1글자에 숫자가 포함안될 수도 있다.
    # => 집계에서 원소가 없을 경우는, 그 집계함수의 기본값 or 누적집계전 초기값 -> 0이 들어가있으므로
    # => 집계함수의 기본값이나 , 누적전 초기값으로 확인한다.
    if value != 0:
        # 문자열끼리 join하기 전에 일단 싹다 list로 모은다.
        result.append(str(value))

    print(''.join(result))
