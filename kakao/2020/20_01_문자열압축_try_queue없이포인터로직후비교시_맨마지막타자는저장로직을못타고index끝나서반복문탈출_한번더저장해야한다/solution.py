import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## 문자열 압축: https://school.programmers.co.kr/learn/courses/30/lessons/60057
    ## 1개, 2개.. 압축단위는 최대 절반index 이다.
    s = input().strip()

    answer = s
    ## 직후를 보는 방법은 queue도 있지만, for i-1, i / for (직후, , k) while curr next의 포인터도 있다.
    ## -> 초기화해놓고, 직후꺼부터, 같을 때까지 cursor를 k칸씩  옮긴다.
    ## -> 첫번째 것을 빼놨다면 count는 1로 시작한다
    for k in range(1, len(s) // 2 + 1):
        temp_answer = ''
        count = 1
        curr = s[:k]
        ## 직후와의 비교 -> 초기값을 prev미리 빼놓고 , 직후pos/직후value를  curr로 비교하자.
        # for i in range(k, len(s), k): # => 이렇게 주면.. 마지막 것을 한번 더 저장해야한다.
        ## => i라는 것은, k씩 건너띄는 pos인데, 직전<->직후의 비교 혹은 시작<->끝까지구간의 비교라면,
        #     직후index+1/구간끝index+1(i+k) == 다음시작index가 len(s)보다 작을때까지 돌아야한다.
        #  => 현재 통과후 업데이트된 값으로 검사를 받던지, 다음index업뎃한 것을 검사하던지 해야한다.
        #  for에서 i는 검사없이 돌고 다음index로 업뎃후 검사가 안되기 때문에,
        #  => 다음시작인덱스로 업데이트된 i가 못돌아가게 range범위를 |    마지막구간     len(s)-1 | len(s)  담구간
        #                                                                     -----k----
        #                                                                          -----k----
        #                                                                               -----k----  여기까지 range허용
        #                                                                                -----k---- 여기부턴 안됨.
        # => 마지막 구간이 n-1에 걸렸다고 가정하고, 허용되는 끝 인덱스는, len(s)-1부터 k개 => len(s) + k -1
        # => 다음구간으로 k개를 가버리는 끝인덱스는 len(s) + k 까지 허용시

        for i in range(k, len(s) + k, k):
            next = s[i:i + k]
            if curr == next:
                count += 1
            ## 다음과 다르면 그냥 올려 저장한다.
            else:
                ## 다음타자로 넘어가기 전에, 저장한다.
                ##
                temp_answer += str(count) + curr if count != 1 else curr

                ## => 다음타자로 넘어갈 땐 가변변수들은 다 초기화해줘야한다!
                count = 1
                curr = next

        ## 문제는 맨 마지막 타자가.. index가 끝에 도달해서, 내부로직을 못타 -> 저장안되고 종료된다.
        ## => 직후와의 비교는, 맨 끝놈 처리를 따로 해줘야한다.
        ## => 직후와의 비교시 저장해야한다면, 맨 마지막 타자가 index를 다돌고 반복문을 벗어나 저장로직을 못탄다.
        ## => 마지막 index면, [비교할 직후]가 없으니 로직태우지말고 저장한다???????
        ##    k간격이면, i에 도달안할텐데??
        ## => 나중에 생각하고, 다돌고 가변변수에 남아있는 정보드들을 한번더 저장한다.
        # temp_answer += str(count) + curr if count != 1 else curr

        # print(temp_answer)
        ## temp_answer의 길이가 제일 작은 것을 선택하도록  min 돌린다
        if len(temp_answer) < len(answer):
            answer = temp_answer

    print(len(answer))
