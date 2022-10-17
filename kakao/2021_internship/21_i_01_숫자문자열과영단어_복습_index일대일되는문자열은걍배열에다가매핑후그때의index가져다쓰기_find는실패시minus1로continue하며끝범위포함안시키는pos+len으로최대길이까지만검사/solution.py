import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## 숫자문자열과 영단어: https://school.programmers.co.kr/learn/courses/30/lessons/81301
    s: str = input().strip()
    ## 1. 문자열 -> 숫자 매핑은, dict로 하면 된다. 특히 여러차원의 문자열 -> index중복사용해서 map에 매핑한다.
    ## => [index와 매칭되는 문자열ex> 0-> zero]인 경우는
    ##   (1) 튜플(배열)에 index(숫자) -> 문자열로 매핑해도 된다. => index들과 1:1매칭되는 순서문자열
    ##   (2) 대신 쓸 때는, [for i 인덱스로 순회하며, arr[i] 문자열 -> i]로 매핑을 풀어나가야한다.
    words = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',)

    ## 2. 문자열 속에 [길이가 제각각인 매핑값 ->  부분 문자열로서 찾는다] 면,
    ## -> for 의 등차k를 쓸 수 없으므로, [pos while pos<len] + [if기본 해당안하는것 pos+=1 ]+[else s.find( pos, pos+매핑값 중 최대길이)  pos+=len]으로 처리한다.
    ## => [1개의 문자열 seq를, 1~k개씩 쓴 것을 날리면서 부분문자열 검색]한다면
    #  => queue로 직후를 보면서 날려도 되지만, queue처럼 1개씩 확인할 필요가 없다. -> [확인대상위치부터 매핑된 value 통째로 검사 필요]
    #  => queue없이, 0부터 강행하며 pos를 이동시키는 조합개념의 원포인터 -> while pos+= 로 발견시 원하는 만큼 움직일 수 있다.


    result = ''
    pos = 0
    while pos < len(s): # while로 index를 탐색할 때는, pos < len(s)으로 조건을 건다.
        # pos +=1
        ## 3.문자열 [1개로 이루어진 문자열 숫자]는 ascii코드를 가져 javachar처럼, 대소비교가 가능하다.
        ## => 1글자씩 검사를 기준으로 한다면, 숫자판별이 가능하다.
        if '0' <= s[pos] <= '9':
            ## 문자열 연산을 계산해야한다면, 문자열숫자를 미리 숫자로 바꾸지마라.
            result += s[pos]
            pos += 1
        # else:
            continue
        ## 4.문자열 숫자가 아니라면, index -> 문자열 매핑배열에서 해당 문자열을 현재위치로부터 가지고 있는지 검사
        ## => [현재위치에서 정해진종류/길이의 문자열을 검사한다면 => find(, 시작, 끝범위)를 쓰자 ]
        # -> 문자열 -> 숫자매핑대신 숫자->문자열 매핑해놓은 배열이 있다면, for i 로 value(문자열)로 검사 -> 그때의 숫자인 (indeX)를 사용한다.
        for i, word in enumerate(words):
            ## 현재위치로부터 +len이라면, 현재~len의 그다음index를 의미한다(window)
            ## => 문자열 최대길이까지만 검사하면 되므로, len - 1까지 검사한다.
            ## [w ord]   s
            #       |     \
            #   pos+len-1  pos+len
            # if s.find(word, pos, pos + 4 + 1) != -1:
            #     result += str(i) # 문자열 1글자씩 처리시 중간이 int라면 str으로 바꿔서 누적한다.
            #     pos = pos + len(word) # pos를 포함해서 word길이만큼 window간 것의 -> 그 직후
            #     ## words를 순회하다가 찾았으면 바로 break
            #     break
            ## 못찾았으면 continue ==> s.find는 못찾으면 -1반환
            if s.find(word, pos, pos + 4 + 1) == -1:
                continue
            result += str(i) # 문자열 1글자씩 처리시 중간이 int라면 str으로 바꿔서 누적한다.
            pos = pos + len(word) # pos를 포함해서 word길이만큼 window간 것의 -> 그 직후
            ## words를 순회하다가 찾았으면 바로 break <= 1개 탐색의 경우!
            break
    print(int(result))