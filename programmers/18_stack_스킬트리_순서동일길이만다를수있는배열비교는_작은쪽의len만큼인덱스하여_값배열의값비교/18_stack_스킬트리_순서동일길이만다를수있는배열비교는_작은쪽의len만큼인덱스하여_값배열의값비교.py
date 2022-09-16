import sys 
 
input = sys.stdin.readline 
 
 
if __name__ == '__main__':
    ## 스킬트리: https://school.programmers.co.kr/learn/courses/30/lessons/49993
    skill = input().strip()
    skill_trees = input().split()
    # print(skill_trees, skill)
    # ['BACDE', 'CBADF', 'AECB', 'BDA'] CBD

    ## 처음부터 시작하고, 순서가 완전히 동일해야한다면 => 인덱싱으로 비교한다
    # -> 튜플과 리스트는 값만 있다면, 같은 놈으로 취급받는다.
    # print([1, 2] == [1, 2]) #True
    # print('abc' == list('abc')) # False

    for skill_tree in skill_trees:
        ## 확인이 필요한 원소들만 추출한다. 배열에서 여러원소 삭제/필터링은?
        # -> 여러개 원소의 삭제는 삭제list에 모아서 not in
        # -> 여러개 원소의 필터링은 필터링list에 모아서 in으로 검사하여 필터링
        # => 원자열에서 여러개 삭제는 re.sub('[^여러개]', '', x)로 날릴 수 있다
        for x in [x for x in skill_tree if x in skill]:
            ## 순서과 완벽히 동일해야하고, 길이만 다르다면
            # => 인덱싱으로 길이만 맞추어서 값 배열 자체를 비교한다.
            # =>  lst[:k] 0부터 k-1까지 k개만 추출
            # if x == skill[:len(x) - 1 + 1]:
            if x == skill[:len(x)]:
                print(True)
                break
            else:
                print(False)
                break


