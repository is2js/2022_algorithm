import sys 
 
input = sys.stdin.readline 
 
 
if __name__ == '__main__':
    ## 문자열 압축: https://school.programmers.co.kr/learn/courses/30/lessons/60057
    ## 새로운 풀이: 낙타 : https://camel-it.tistory.com/112
    s = input().strip()

    ## (1) 배열 input -> 길이 1일때를 생각해서 예외처리하자.
    # => 0과 1일 떠올려, 배열의 길이가 1이면 -> 탐색 0번 / 정렬 0번/ 길이 1으로 바로 예외처리가 가능하다
    # => 예외처리른 배열길이 1을 생각하자
    if len(s) == 1:
        print(1)
        exit()

    # min_sub_string = float('inf')
    min_sub_string = len(s)

    ## (2) 부분문자열 문제
    ## => 현재시점 기준으로 직전들을 날리는 stack으로, [중간 부분문자열]을 구성할 수 있다.
    ## => 순서가 동일하지만, 길이만 다르다면 [:len(x)]로 순서유지 길이만 다른 부분문자열을 원본과 비교할 수 있다.
    ## => k개씩 묶은 부분문자열
    #     -> (1) for i in range range(0, , k) 등차k로 시작 커서를 매번 옮길 수 있다.
    #     -> (2) 내부에서는 str[i:i+k] (i서부터k개)로  [시작커서~k개묶음의끝]원소를 슬라이싱 할 수 있다.
    for k in range(1, len(s)//2 + 1):
        result = []
        # (5) k개묶음씩 돌면서, 비교기준을 선언한다. -> 비교탈락시 -> 지금까지 저장 + 바뀌는 순간 비교기준도 바뀐다.
        # => head라는 이름을 붙인다.?!
        curr_head = s[:k] # 처음부터 k개
        counter = 0 # 비교기준이라도, 0부터 돌아서 카운팅 되므로, 0부터 시작한다.
        # (3) 시작커서가 0부터 k씩 움직인다.
        # for i in range(0, len(s), k):
        ## => queue와 꺼낼때와 마찬가지로, k개씩 건너뛴다면, 나머지가 존재한다.
        ##    나머지도 i:i+k에 탐색될 수 있도록, len(s) + k까지 해줘야한다!! 안그럼 틀림
        for i in range(0, len(s), k):
            # (4) 시작커서i에 대해 k개를 묶는다.
            next_sub_string = s[i:i + k]
            if next_sub_string == curr_head:
                counter += 1
            else:
                # (6) 기준과 다른 문자열이 나타난 경우, 그 문자열이 curr_head가 되고,
                #     지금까지 세준 counter를 저장한다.
                result.append((counter, curr_head))
                # (7) head와 count를 초기화한다.
                curr_head = next_sub_string
                # (8) 비교기준이 바뀔 때는, 그 새 기준의 시작i부터 세는게 아니라, 이미 진입한 상태이므로
                #  => 처음에만 비교기준을 잡아둔 상태에서, 비교기준이 있는 0부터 출발했었지만
                #     i:i+k에서 비교기준이 바뀐 상태에서는, 다시 한번 세는게 아니라, 그 다음부터 비교하므로 1부터 센다
                # ryan = 0
                counter = 1
        ## (9) 현 k개씩 묵음의 압축결과가 result에 저장되엇다.
        ## => 그 결과를 요구사항에 맞게 수정해준다.
        # print(result)
        # [(1, 'a'), (1, 'b'), (1, 'c'), (1, 'a'), (1, 'b'), (1, 'c'), (1, 'a'), (1, 'b'), (1, 'c'), (1, 'a'), (1, 'b'), (1, 'c'), (1, 'd'), (1, 'e'), (1, 'd'), (1, 'e'), (1, 'd'), (1, 'e'), (1, 'd'), (1, 'e'), (1, 'd'), (1, 'e'), (1, 'd')]
        # [(1, 'ab'), (1, 'ca'), (1, 'bc'), (1, 'ab'), (1, 'ca'), (1, 'bc')]
        # [(4, 'abc'), (1, 'ded'), (1, 'ede'), (1, 'ded')]

        ## 카운터가 1이면 문자열만, 2개이상이면 숫자+문자열
        compressed_string = ''.join( (str(count) if count > 1 else '') + sub_string  for count, sub_string in result)
        print(compressed_string)
        # abcabcabcabcdededededed
        # abcabcabcabc
        # 4abcdedededed

        ## => 각 결과값의 len가 최소가되도록 greedy업데이트한다.
        min_sub_string = min(len(compressed_string), min_sub_string)

    ## 출력
    print(min_sub_string)


