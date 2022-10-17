import string
import sys
from collections import deque

input = sys.stdin.readline

if __name__ == '__main__':
    ## 숫자문자열과 영단어: https://school.programmers.co.kr/learn/courses/30/lessons/81301
    s = input().strip()
    ## my) 0~9의 숫자는 정해진 종류라서 map을 경계로 문자열 -> 숫자 -> index로 암묵적 매핑?!
    ## 1차원이며, 숫자니까 map 속 차원별 중복가능 index가 아니라.. 배열에 매핑해도 된다?
    # digits = string.digits
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    # words_hash = dict(zip(words, range(0, 10)))
    ## => 숫자를 1개씩 다룬다면, 숫자로 매핑할게아니라, 문자열 숫자로 매핑하도록 한다.
    words_hash = dict(zip(words, string.digits))
    ## 숫자 -> 문자열 : 배열로 매핑
    ## 문자열 -> 숫자 or 저장을 위한 숫자index로 매핑 -> hash
    ## -> 2개배열이며, key값들이 순서대로 배열에 담겨있다면 dict(zip())으로 map매핑가능
    # print(words_hash)
    # {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    ## 현재 append되는 차례에서 직전들 보기(stack) (X), 현재에서 직후들 다보기 -> queue
    # q = deque([s])
    ## => queue는 문자열1개를 iter하지 않고, 1개 통채로 뽑아내버리니 list로 만들어서
    q = deque(list(s))
    answer = ''
    while q:
        print(answer)
        curr: str = q.popleft()
        # (1) 문자열 숫자면 직후들과 비교하지않고 넘어가서 모은다.
        if curr.isdigit():
            answer += curr
            continue
        # (2) 문자열이면 직후들과 비교하면서 popleft하여 모아놓고, 매핑된 것을 골라낸다.
        # temp_answer = ''
        ## => 현재curr에 합쳐야하므로 새롭게 모으면 안된다.
        while q:
            peek: str = q[0] # stack의 [-1] 아니니 조심.
            # print(peek)

            if peek.isdigit(): break
            ## => 숫자일때 break뿐만 아니라, 영단어 1개가 나오면 break되어야한다.
            ## => 지금까지 모은 것을 wordmap의 문자열->숫자매핑의 key에 잇나 봐야한다.
            if curr in words_hash: break

            ##  =>? 현재 대상과 직후들을 연결해야한다!
            curr += q.popleft()
        # print(curr)
        ## 알파벳만 다 뽑았으면, 변환해야함
        answer += words_hash[curr]

    # 중간에 남겨두고 나오는 break는 없어서.. 나머지 처리 꼭 안해줘도 된다.
    if q:
        answer += ''.join(q)
    print(answer)

