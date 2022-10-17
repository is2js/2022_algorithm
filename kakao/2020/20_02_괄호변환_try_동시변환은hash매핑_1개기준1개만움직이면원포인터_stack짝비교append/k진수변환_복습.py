# def convert_to_base(n, base):
#     q, r = divmod(n, base)
#     if not q:
#         return str(r)
#     return convert_to_base(q, base) + str(r)

def convert_to_base(n, base):
    div, mod = divmod(n, base)
    if div == 0:
        return str(mod)
    return convert_to_base(div, base) + str(mod)


if __name__ == '__main__':
    ## 진법변환은 (1) n을 base(진법수)을 나눈 나머지를 하나씩 다 구한 다음,
    ##          (2) 역순으로 1자리씩(문자열) 누적해서 더해야한다.
    ##          (3) 역순으로 더할 나머지를 제외하고, 몫은 다시 부분문제가 되어서 재귀를 호출한다.
    ##          (4) 종착역은 부분문제로 나올 몫이 0이 되는 순간, 끝이다.
    print(convert_to_base(n=5, base=2))
    pass
