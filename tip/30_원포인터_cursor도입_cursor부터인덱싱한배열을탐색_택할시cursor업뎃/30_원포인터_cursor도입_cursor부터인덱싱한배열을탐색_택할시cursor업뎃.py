import sys 
 
input = sys.stdin.readline 
 
 
if __name__ == '__main__': 
    items = [3, 2, 1, 10]
    people = ['조재성', '조재경', '조아라']

    items.sort()

    result = []
    ## 원포인터
    # -> 배열에서 택1할 때, queue or stack -> pop을 안쓰는 경우
    # -> [cursor -> cursor부터 인덱싱하며 탐색 -> 택1시 cursor +=1 ]를 도입해서 진행한다.
    cursor = 0
    for num, person in enumerate(people, start=1):
        q = []
        ##
        for item in items[cursor:]:
            if num < item:
                break
            q.append(item)
            ## 택할때 cursor + 1
            cursor += 1
        result.append(q)

    # print(result)
    # [[1], [2], [3]]