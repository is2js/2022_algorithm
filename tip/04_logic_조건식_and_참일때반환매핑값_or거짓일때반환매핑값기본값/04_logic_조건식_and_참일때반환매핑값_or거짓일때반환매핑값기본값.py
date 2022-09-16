import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## 논리연산
    # (1) and 연산의 결과는 False값을 만나면 바로 False값(0,..)를 반환
    #    => 다 True면 맨 뒤의 True값(값이 존재하면 값)
    print('python' and 'JS')  # JS
    print('python' and 'JS' and 'TS')  # TS
    print('python' and 0)  # 0
    print(0 and 'JS')  # 0

    # (2) or 연산은 그 True값을 만나면 바로 반환
    #    => 다 False면 맨 뒤의 False값을 반환
    print('python' or 'JS')  # python
    print('python' or 0)  # python
    print(0 or 'JS')  # JS
    print(0 or False)  # False
    print(False or 0)  # 0

    # (3) or연산은 True값을 만나면 그 값을 반환하니
    # => [False값 or defaultTrue값]으로 기본값을 줄 수 있다.
    arr = []
    print(arr or -1) # -1 => -1은 False값이 아닌 True값이라 만나면 반환되어 기본값이 된다.

    ## 논리 응용
    # 1. ([False가능한조건식] [and True일때 매핑값(and의 맨마지막반환)]) [or False일때 default값]
    score = 85
    result = (score >=80 and 'True입니다.') or '거짓입니다.'
    print(result) # True입니다.

    result = (score >=90 and 'True입니다.') or '거짓입니다.'
    print(result) # 거짓입니다.
    pass
