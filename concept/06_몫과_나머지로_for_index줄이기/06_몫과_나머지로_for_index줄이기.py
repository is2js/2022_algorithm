import sys 
 
input = sys.stdin.readline 
 
 
def solution():
    # 3중 반복문 N by N by N -> N^3
    for i in range(5):
        for j in range(5):
            for k in range(5):
                #i, j, k process()
                pass
    # python indent 줄이기
    # N ** 3만큼을 range()로 도는 것은 동일한데
    # (1) i = num // (N**2) : N제곱을 나눈 몫
    # (2) j = num // N % N : N을 나눈 몫을 N으로 나눈 나머지
    # (3) k = num % N : N으로 나눈 나머지
    for num in range(5**3):
        i, j, k = num//(5**2), num//5%5, num%5
        # print(f"{i}{j}{k}")
        # k부터 -> j -> i순으로 순차적으로 올라간다.

    # 2차원
    # (1) i: (N**2을 진행 중)반복문index를 N으로 나눈 몫[ index//N ]
    # N**2만큼 진행하는데, 행렬로 보고
    # 0부터 N-1까지를 1행을 -> (해당구간의 수 전체를) 0으로 본다.
    # N부터 2N-1까지를 2행을 -> 1로 본다.
    # N**2-(N)+1~ N**2    -> N-1로 본다.     b-a +1 = N ->  a = b - N + 1
    # -> 몫이란, 구간을 나눈 수 만큼을 퉁쳐서 0부터 증가하도록 하여, 각 구간별 값들을 모두 0으로 보고, 1로 보고...
    #           구간이 N*2인데, N으로 나누면 0부터 N-1까지 N개의 구간이 된다.

    # (2) j: 반복문index를 N으로 나눈 나머지 [ index%N ]
    # 0, N, 2N 등을 -> 0으로본다.
    # 1, N+1, 2N+1 -> 1으로 본다.
    # N-1, 2N-1, N**2-1 -> N-1로본다.
    # -> 나머지란, 나눈 수만큼의 구간들에 대해, 다 첫번째 구간의 열과 같은 값으로 본다
    #    첫구간이 0~N-1이면, 나머지 구간들은 모두 0~N-1로 구성되게 한다.
    for num in range(5**2):
        i, j = num//5, num%5
        print(f"{i}, {j}")

 
if __name__ == '__main__': 
    solution() 
