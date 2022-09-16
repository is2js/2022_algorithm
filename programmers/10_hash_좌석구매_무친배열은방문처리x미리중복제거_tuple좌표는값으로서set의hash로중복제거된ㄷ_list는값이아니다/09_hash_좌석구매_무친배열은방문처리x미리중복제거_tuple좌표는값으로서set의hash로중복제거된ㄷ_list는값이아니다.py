import sys
from collections import Counter

input = sys.stdin.readline

if __name__ == '__main__':
    # https://chaelinyeo.github.io/%EC%BD%94%ED%85%8C/Level01%EC%A2%8C%EC%84%9D%EA%B5%AC%EB%A7%A4/
    seat = list(map(int, input().split()))
    pair = 2
    sections = len(seat) // pair
    seat = [[seat[section * 2 + 0], seat[section * 2 + 1]] for section in range(sections)]
    # print(seat)
    # board = [[0] * 1_000_000 for _ in range(1_000_000)]
    # count = 0
    # for row, col in seat:
    #     if board[row][col]: continue
    #     board[row][col] = 1
    #     count += 1


    ## 사용하는 것에 비해 엄청나게 많은 배열은 비효율적이다.
    # => 다른 방법을 생각한다.
    # => id가 없는 value는, 값context로서, 미리 중복을 제거할 수 있다.

    ## set()으로 미리 중복제거 -> 튜플(좌표)또한 값이라서 중복제거처리가 된다.
    # => 2차원배열은 set()이 안씌워진다. 각 원소를 hash에 넣는데, list는 안들어간다. but tuple은 들어간다.
    # => list는 값이 아니다. tuple은 값으로서 set에 들어갈 수 있다.
    # print(len(set(seat)))
    # TypeError: unhashable type: 'list'

    # print(len(set(map(tuple, seat))))

    ## cf) 중복허용 2배열의 값의 차이는 Counter의 dict를 활용한다
    # print(Counter(map(tuple, seat)))
    # Counter({(2, 1): 3, (1, 1): 1, (1, 2): 1, (3, 4): 1})

    ## cf) 개별 중복갯수를 확인하려면, 1개별이라도 Counter를 활용하면 된다.
    # 여기서는 중복제거만 하면 되므로 set()으로 처리했다.

