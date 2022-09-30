import sys 
 
input = sys.stdin.readline 
 
 
if __name__ == '__main__':
    ## 숫자문자열과 영단어: https://school.programmers.co.kr/learn/courses/30/lessons/81301
    s = input().strip()

    ## (1) 변환을 편하게 하기 위해서
    ## 정해진 종류의 1차원 문자열 -> 숫자 매핑이라도, dict가 아닌  [tuple]로 매핑한다.
    ## -> 정해진 종류의 매핑인데, 바꿀게 아니라면, list가 아닌 tuple로 해야 성능상 유리하다.
    ## -> [문자열 -> 숫자 매핑]이지만, [숫자가 순서]가 정해져있어 [s.find(문자열, 시작범위,끝범위) -> 바로 index로 매핑되는 경우]에는 tuple로 한다
    Word = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')

    result = ''

    ## (2) 반복문으로 1글자씩 이동하면서 1글자씩만 확인한다.
    ## => 이 때, 인덱스가 2칸 이상 움직일 수 도 있는 경우에는, 원포인터로서 cursor + while + 조건에 따라 jump를 사용한다.
    ## => 직후들과 비교하는데, queue를 굳이 안쓰고 cursor로 이동하면서 처리할 수 도 있다.
    pos = 0
    while pos < len(s):
        ## (3) 문자열 숫자 0~9사이만 필터링하려면, [숫자처럼 ascii코드로서 대소비교가 가능]하다
        if '0' <= s[pos] <= '9':
            result += s[pos]
            pos += 1
        else:
            ## (4) 문자열 0~9사이가 아니라면, 숫자가 아닌 문자열이다.
            ##  현재 숫자 -> 문자열 매핑tuple이므로 value -> s.find(문자열, srt,end범위)로 매핑된 idx를 바로 가져온다.
            ##  => 문자열 전체s 중에서  find하되, Word들도 다 순회해서 찾아야한다.
            ##  => 해당 Word가 발견되었을 떄, 그 때의 index가 필요하므로, for i 로 돌고 있다.
            for i in range(len(Word)):
                # 10개의 word 중 현재word[i] 가 s내부에 있는지 검사하고, 있으면 그것의 index를 추출한다.
                #### 이 때, s의 현재cursor위치인 pos부터 ~ word는 최대 5글자이므로, [pos~,pos+4 + 1]안에서 찾아야한다.
                #### [find는 못찾으면 -1이] 나온다.
                if s.find(Word[i], pos, pos + 5) != -1:
                    #### 찾았다고 하면, 찾은 word[i]의 index를 append하고, 그만큼 pos를 여러칸 뛴다.
                    result += str(i) # idx는 숫자로 반환된다.
                    #### 건너띄는 범위는 동적으로서, 단어의 길이만큼 건너띈다. 현재위치 포함 window
                    pos += len(Word[i])
                    #### 해당 단어를 찾았으면, word는 더이상 볼필요없으므로 break
                    break

    answer = int(result)
    print(answer)
