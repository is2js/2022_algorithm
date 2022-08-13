import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ### bit를 이용한 원소 N개의 모든 부분집합 나타내기
    ###  1<<n == 2^n == 부분집합의 갯수
    ###  bin(정수) -> 문자열 이진수로 출력 0bxxxx
    # -> 0부터 (2^n - 1)까지를 range( 1<<n or 2**n ) 돌리면서 & 비트연산자를 붙이면
    # -> 알아서 0(0000) ~ 15(1111)까지 [원소포함여부를 01로 나타낸 이진수 부분집합들]이 된다
    N = 3
    for bit in range(1 << N):
        print(bin(bit)[2:])
    # 0
    # 1
    # 10
    # 11
    # 100
    # 101
    # 110
    # 111

    ### [원소포함여부 부분집합 이진수bit]에,
    ###   (->순으로)매핑되는 배열index이자 & (<-순으로) 이진수0자리부터 left shift를 돌리는 반복문 속에서
    ###   if bit & (1<<자리수)  [bit and  1 left shift]를 통해
    ###     - 1<< 는 해당자리수만 1, 나머지는 0을 만든다.
    ###   if bit & (해당자리수1나머지0)
    ###     - & 는 둘다 1일때만 살아남는다.
    ###   if 해당자리수의 bit속포함여부가 1이면 True, 0이면 False

    ###   [if bit and 1 leftshift 해당자리수]는
    ###  => bit속에 해당자리수가 1이면 True로 확인해주는 문이다.

    # ex>   0100 ->  int( '0100', 2) by int( 'n진수문자열', base진법)
    maaping_lst = [1, 2, 3, 4]
    index = 2
    if int('0100', 2) & (1 << index):
        print(
            f"반복문 속 정수지만, bit로 {int('0100', 2)}는 이진수 {bin(int('0100', 2))} {index}번째자리, 매핑배열 속 {maaping_lst[index]}이 포함된 부분집합")
    else:
        print(
            f"반복문 속 정수지만, bit로 {int('0100', 2)}는 이진수 {bin(int('0100', 2))} {index}번째자리, 매핑배열 속 {maaping_lst[index]}은 포함안되어있어요")
    # 반복문 속 정수지만, bit로 4는 이진수 0b100 2번째자리, 매핑배열 속 3이 포함된 부분집합

    ### 원소의 갯수만큼 정수를 돌리면서, bit로 생각하여 불들어왔는지 확인하고
    ### 불들어왔으면, 그 자리수의 매핑배열의 값을 인덱싱해서 출력해보자.
    lst = [
        'A',
        'B',
        'C'
    ]
    N = len(lst)
    for bit in range(1 << N):
        # 부분집합마다 원소 출력전 괄호
        print('{', end=" ")
        for index in range(N):
            # 해당 자리수(index) 불들어왔으면, 암묵적index 매핑배열에서 값을 뽑아 출력
            if bit & (1 << index):
                print(lst[index], end=" ")
        # 모든 원소 다돌고 끝처리 (자식들 돌면 끝처리 )
        print('}', end=" ")
        # 부분집합 종류(bit)마다 줄바꿈
        print()

    # { A } 
    # { B } 
    # { A B } 
    # { C } 
    # { A C } 
    # { B C } 
    # { A B C } 

    ### [원소포함여부 부분집합 이진수bit] 속 [1로 포함원소 갯수]
    ### -> bin(정수) -> 문자열이진수 반환 -> .count('1')로 1을 센다. (0b가 붙기 때문에 0세면 안된다)
    ##
    print(bin(int('0110', 2)).count('1'))
    # 2
    print(bin(int('1111', 2)).count('1'))
    # 4

    ### 직접 구현하려면, 이진수 0번째자리만 검사하되
    ### 이진수를 right shift 1하도록 업데이트하여, 매번 1의 자리만 검사한다
    ### -> right shift의 결과, 왼쪽부터 마지막자리까지 일을자리로 갈땐
    ###    0 00 000 모두 0으로 가득차서 0이되니, 업데이트용 while문을 이진수로 두면 된다.
    ###
    bit = int('1111', 2)
    # while bit:
    #     bit = bit >> 1

    count = 0
    while bit:
        # 1과 &연산 (& 1)하면, 0번째 자리만 불들어왔는지 확인하는 것이다.
        if bit & 1:
            count += 1
        bit = bit >> 1
    print(count)
    # 4

    ### 원소의 갯수만큼 돌아 [부분집합 포함여부 이진수]로 처리하는 것은 [모든 부분집합]을 돈다는 가정이다.
    ### 전체를 다 도는 것은, 알고리즘상 시간초과가 뜰 수 있다.

    ### 모든 부분집합을 만나면서, 조합문제 해결해보기
    ### ex> 두 수의 합이 7인 경우의 수(갯수) -> 합은 교환법칙이 성립하여 조합문제 == 부분집합의 문제가 된다.
    ###     두 수 -> 부분집합의 갯수가 2개인 것만 if bin().count('1') == 2로 필터링한다
    N = 6
    lst = [1, 2, 3, 4, 5, 6]
    count = 0
    for bit in range(1 << N):
        if bin(bit).count('1') != 2:
            continue
        # 원소가 2개인 부분집합 상태
        # -> 합이 7인지 확인하려면, bit의 자리수를 돌면서
        #    매핑배열에서 값을 가져와야한다.
        #    bit의 자리수이자 배열의 index를 반복문으로 돌려서, 1인 것만 확인해서 담아야한다.
        #    -> 개당을 모아서 하지말고, 1개씩 원소를 찾으니, 합을 누적해서 구한다.
        sum_of_two = 0
        for index in range(N):
            if bit & (1 << index):
                sum_of_two += lst[index]

        if sum_of_two == 7:
            count += 1

    print(count) # 3 -> 1 7 / 2 5 / 3 4
