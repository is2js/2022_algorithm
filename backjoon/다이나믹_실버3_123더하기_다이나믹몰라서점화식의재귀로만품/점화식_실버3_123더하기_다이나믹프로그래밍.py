import sys

input = sys.stdin.readline


# 1 = 1
# 1+1, 2 = 2
# 1+1+1, 1+2, 2+1, 3 = 4
# 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 1+3, 2+2, 3+1, (4->쓰면안됨) = 7
#-> 1+1+1+1, 1+1+2, 1+2+1, 1+3(1+[3])/ 2+1+1, 2+2 (2+[2]) /3+1(3+[1]) = 7
def process():
    def solve(n):
        if n <= 2:
            return n
        if n == 3:
            return 4

        return solve(n - 1) + solve(n - 2) + solve(n - 3)

    return solve(int(input().strip()))


if __name__ == '__main__':
    for _ in range(int(input().strip())):
        print(process())
