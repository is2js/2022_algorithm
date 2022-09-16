import sys
from collections import Counter

input = sys.stdin.readline 
 
 
if __name__ == '__main__':
    participant = list(input().split())
    completion = list(input().split())

    # (1) 2 배열의 원소 차이를 구해야하는데, [중복허용된 배열의 값 차이]는 count를 차이로 차이를 발견한다.
    # -> set을 쓴다면, 중복이 사라져서 안된다.
    # -> Counter를 써서, dict형태로 갯수를 세고, 반대로 빼주자.
    # => 중복허용했을 때, 차이는 dict로 Counter를 센다

    counter = Counter(participant)
    for person in completion:
        counter[person] -= 1
    print([p for p, c in counter.items() if c != 0][0])


