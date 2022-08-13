import sys 
 
input = sys.stdin.readline 
 
 
if __name__ == '__main__':
    # 비트연산자

    # &
    # x 00000011 = 3
    # y 00000110 = 6
    # x & y -> 둘다 1일 때 1
    #   00000010 = 2

    # |
    # x | y -> 하나라도 1인 경우 1 -> 둘다 0인 경우 0
    #   00000111 = 7

    # ^y (XOR연산자) -> 둘다 같은 경우 0, 다르면 1
    # x 00000011 = 3
    # y 00000110 = 6
    #   00000101 = 5

    # ^y^y -> 2번째 피연산자를 다시 ^하면 다시 첫번째 피연산자 x로 원래값으로 돌아간다
    #   00000101 = 5
    # y 00000110 = 6
    #   00000011 = 3 (x^y)^y

    # ~ (not) -> 각 비트 반전
    # x 00000010 = 2
    # ~ 11111101 = -3 (2의 보수)

    # << (left shift) << 후 얼마를 shift할지 적어준다
    # -> 하나 왼쪽으로 이동할때마다 x2씩 해주면 된다.
    # -> 2진수이기 때문에 한자리 올리면 x2
    # x 00000001 = 1
    # x << 2  00000100 = 4

    # >> (right shift)
    # -> 1개 이동할때마다 //2 와 동일
    # x 00000100 = 4
    # x >> 2 0000001 = 1








    pass
