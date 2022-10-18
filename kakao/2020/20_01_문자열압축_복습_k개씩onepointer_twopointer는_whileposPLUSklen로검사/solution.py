import sys 
 
input = sys.stdin.readline 
 
 
if __name__ == '__main__':
    ## 문자열 압축: https://school.programmers.co.kr/learn/courses/30/lessons/60057
    s = input().strip()
    ## 1. 압축단위는 고정이므로 경우의수별 for로 돌면서 압축된 것의 길이 최소값을 greedy로 찾아야함
    ## => 압축문자열을 직접 찾는 문제가 아니므로, 원본에서 줄여가며 count의 최소값 -> max는 len(s)
    ## => 압축단위는 절반까지가 최대 -> 반복 2번, for 압축단위k k는 1, len(s)//2까지만 본다. 넘어가면 반복 안된다.
    min_length = len(s)
    for k in range(1, len(s)//2 + 1):
        ## 2. 커서는 현재pos = 0부터 시작하여 k개 확인후, 다음pos(pos+k)로 업데이트 되어야한다.
        ## 3. 첫 length는 len(s)부터 반복되는 갯수만큼 줄어들어야한다
        pos = 0
        length = len(s)
        ## 4. k구간씩 기준을 one pointer하려면, while pos + k <= len 으로 검사하며 업뎃하며 슬라이싱한다.
        while pos + k <= len(s):
            unit = s[pos:pos + k]
            pos += k
            ## 5. 현재 unit을 기준으로, pointer가 담구간 시작으로 업뎃된 상황에서
            ##    다시 구간 one pointer를 탐색을 시작한다.
            ##    unit와 같은 게 있으면, 반복되었다고 카운팅한다.
            repeat_count = 0
            while pos + k <= len(s):
                next = s[pos:pos + k]
                if next == unit:
                    repeat_count += 1
                    ## 6. 같은 게 나타나면, 다음 포인터로 넘어간다.
                    pos += k
                ## 7. 하나라도 다른게 나타나면 다음unit로 넘어가기 위해, break한다.
                else:
                    break
            ## 8. 현재unit에서  카운팅이 끝났으면, 그만큼 length를 줄여줘야한다.
            ## -> 반복갯수가 0이면, 그대로, 반복갯수가 1개이상이면, k구간만큼 length를 줄여야한다.
            if repeat_count > 0:
                length -= (repeat_count * k)
                ## 9. 이제 반복되는갯수만큼 그 count를 앞에 기입해야한다. 그래서 length가 늘어난다.
                # -> 반복횟수 1 == 갯수2이다. 2 -> 3이다.. 앞에 기입할 숫자는 횟수+1로 확인해야해서
                #    자리 수를 생각해야한다.
                if repeat_count + 1 < 10:
                    length += 1
                elif repeat_count + 1 < 100:
                    length += 2
                elif repeat_count + 1 < 1000:
                    length += 3
                ## 10. 자리수는 최대 1000번 반복이라 했으니 4자리까지 더해질 수 있따.
                else:
                    length += 4

        ## 11. 현재 unit로 만드는 length를 min greedy한다.
        min_length = min(min_length, length)

    print(min_length)





