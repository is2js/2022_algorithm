import sys 
 
input = sys.stdin.readline 
 
 
if __name__ == '__main__':
    ##
    items = [3, 2, 1, 10]
    people = ['조재성', '조재경', '조아라']

    ## (1) items 수치배열 탐색은, 정렬 후 탐색하면 제한 검사에 continue후 뒤를 탐색안해도 된다.
    items.sort()

    result = []
    for num, person in enumerate(people, start=1):
        q = []
        for item in items:
            if num < item:
                # continue
                break
            q.append(item)

        result.append(q)

    # print(result)
    ## continue 사용시 -> item O(i)탐색
    # [[1], [1, 2], [1, 2, 3]]
    ## break사용시     -> item을 num보다 넘은 탐색안함 O(i-num)?
    # [[1], [1, 2], [1, 2, 3]]


