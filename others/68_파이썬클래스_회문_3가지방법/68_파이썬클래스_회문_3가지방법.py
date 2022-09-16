import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## 회문
    # (1) 문장부호 제거
    # (2) 대소문자 구분x -> 소문자로 변경
    # (3) 글자수가 홀수라면, 가운데수 제외하고 양쪽끝을 비교

    ## (1) 반반씩 list에 담아서 한쪽을 뒤집어 비교하기
    # 1. 문자열을 1글자씩 원소가 되도록 list()로 1글자씩 분해한 list를 만든다.
    src = list("A man, a plan, a canal - Panama!")
    # 2. 문장부호를 제거 -> 알파뱃만 추출하자.
    #    선형탐색하니, 이 때 -> 소문자로 변경까지 해주자
    #    => 문장부호 제거(반대필터링) 과 소문자로변경 같이
    des = [x.lower() for x in src if x.isalpha()]
    # 3. 가운데 index를 구해야한다.
    # -> si+ei//2 -> 가운데 or 왼쪽    len() //2 -> 가운데 or 오른쪽
    # len을 써서 홀수 -> 가운데 -> 제외하고 사용  mid-1 까지 vs mid + 1부터
    #           짝수 -> 오른쪽 -> 오른쪽-1까지 vs 오른쪽 포함부터~ 로 나눈다.

    ## 4. 뒤에서부터 가져온다면, 인덱싱을 거꾸로 like range
    if len(des) % 2 == 0:
        mid_right = len(des) // 2
        left = des[:mid_right]
        right = des[mid_right:][::-1]
    else:
        mid = len(des) // 2
        left = des[:mid]
        right = des[len(des) - 1:mid + 1 - 1:-1]

    ## 5. list는 값과 순서가 같다면 == 비교가 가능하다.
    if left == right:
        print("회문입니다.")
    else:
        print("회문이 아닙니다.")


    ## (2) 동시에 움직이는 two point로 확인하자.(거리가 같으면서, 같이 움직일 경우)
    # -> 절반까지만 움직여야한다. 절반+1(오른쪽)까지 허용해주자.
    for i in range(len(des) // 2):
        end_index = len(des) - 1 - i
        # print( i, end_index)
        if des[i] != des[end_index]:
            print("회문이 아닙니다.")
            break
    else:
        print("회문입니다.")

    ## (3) queue이면서 stack으로 활용가능한 deque를 이용해서 비교하기
    # -> queue로 왼쪽부터 1개씩 뽑아내기
    # -> stack으로 오른쪽부터 1개씩 뽑아내기
    from collections import deque
    queue = deque(des)

    ## 동시에 뽑아낼 수 있게 2개이상 남아있을 때만 돌리기
    while len(queue) >= 2:
        ## dequeue는 popleft()와 pop()을 동시에할 수 있다.
        if queue.popleft() != queue.pop():
            print("회문이 아닙니다.")
            break
    ## for else분만 아니라 while else로도 flag처리를 할 수 있다.
    else:
        print("회문입니다.")
