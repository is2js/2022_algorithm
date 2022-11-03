import sys

input = sys.stdin.readline


def is_valid(ch: str):
    if ch.isalnum():
        return True
    if ch in ['-', '_', '.']:
        return True
    return False


if __name__ == '__main__':
    ## 신규아이디 추천: https://school.programmers.co.kr/learn/courses/30/lessons/72410
    new_id = input().strip()

    # print(new_id)
    # ...!@BaT#*..y.abcdefghijklm
    new_id = new_id.lower()


    new_id = ''.join(ch for ch in new_id if is_valid(ch))
    dot_flag = False
    answer = ''
    for ch in new_id:
        if ch == '.':
            if dot_flag:
                continue
            else:
                dot_flag = True
                answer += ch
        else:
            ## 연속방지외의 문자열이 나올 경우, flag 다시 초기화
            dot_flag = False
            answer += ch

    new_id = answer.strip('.')

    new_id = 'a' if not len(new_id) else new_id

    new_id = new_id[:15] if len(new_id) >= 16 else new_id
    new_id = new_id.rstrip('.')

    while len(new_id) == 3:

        new_id += new_id[-1]

    print(new_id)




    pass
