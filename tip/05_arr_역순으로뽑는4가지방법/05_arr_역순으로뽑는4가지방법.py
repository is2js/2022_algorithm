import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## 배열 거꾸로 출력
    arr = [1, 2, 3, 4, 5]

    # (1) [::-1]
    for x in arr[::-1]:
        print(x, end='')
    print()

    # (2) 마지막인덱스부터
    for i in range(len(arr) - 1, 0 - 1, -1):
        print(arr[i], end='')  # 54321
    print()

    # (3) 0부터 i에 대해서, 역인덱스 len-1-i
    for i in range(len(arr)):
        print(arr[len(arr) - 1 - i], end='')  # # 54321
    print()

    # (4) python전용 0부터 i에 대해서 [-(i+1)]인덱싱  뒤에서 1번재는 -1부터
    for i in range(len(arr)):
        print(arr[-(i + 1)], end='')  # # 54321
    print()
