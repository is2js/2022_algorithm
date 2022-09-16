import sys

input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input().strip())
    lost = list(map(int, input().split()))
    reserve = list(map(int, input().split()))

    # 기본적으로 체육복은 가지고 있다
    # => i-1, i+1 양쪽을 봐야한다면, 양쪽에 특이점 객체를 만들어놓자.
    # students_state = [1] * (n + 1)
    students_state = [1] * (n + 2)

    for i in lost:
        students_state[i] -= 1
    for i in reserve:
        students_state[i] += 1

    # for i in range(1, len(students_state) - 1 + 1):
    # => 양쪽에 특이점 객체가 존재한다면, for문내부에서 index조건 없이 1~n까지 살펴봐도 된다.
    for i in range(1, n + 1):
        # => 로직에 안걸리는 value를 가졋다면, 특이점 객체로서 index검사를 피할 수 있다.
        # if i == 0:
        # if i == len(students_state) - 1:

        # => 업데이트 되는 배열의 값은 함부로 지역변수로 담아 여러로직에서 사용하지 말 것
        # curr = students_state[i]
        if students_state[i]:
            continue
        # if i != 1 and students_state[i - 1] > 1 and not students_state[i]:
        # => i를 기준으로, 체육복이 없으면 양쪽을 살펴본다. 특이점0, n+1이 있으므로, 인덱스 검사않해도 되지만
        #   특이점 객체 value는 아예 로직에 안걸리는 값(2빌려옴 0채움)인 기본값 1을 채워놨어야한다.
        if not students_state[i] and students_state[i - 1] == 2:
            # students_state[i-1] += 1
            # students_state[i] -= 1
            # => 인접한 list의 원소들은 value할당을 [인덱싱 = [value, 배열] ]로 한번에 처리할 수 있다.
            students_state[i - 1:i + 1] = [1, 1]
        if not students_state[i] and students_state[i + 1] == 2 :
            # students_state[i+1] -= 1
            # students_state[i] += 1
            students_state[i:i + 1 + 1] = [1, 1]

    # 특이점 객체를 제외하고 출력한다.
    # => [앞에서제낄갯수: - (뒤에서 제낄갯수)]
    print(len([x for x in students_state[1:-1] if x]))
