import sys 
 
input = sys.stdin.readline


def check_skill(skill, skill_tree):
    stack = []

    ## (1) [직전or직전부터역순 node들]에 대해 확인 주체 or 대상에 해당하는 원소들만 배열에 돌린다.
    for x in [x for x in skill_tree if x in skill]:
        # (2) 만약, 확인대상에는 해당안하고, 확인주체로서 stack에 바로 들어간다면
        # if x in [확인주체들]: stack.append(x) continue 로 조건없이 먼저 stack에 바로 올려준다.

        # (4) stack에 1개라도 찬 순간(위 or 밑의 append) if stack/while stack으로 조건을 걸어서 현재원소를 peek과 비교해서 검사한다.
        #   -> 모든 node가 검사대상이자 검사주체면, 검사성공시 -> append가 이루어져야한다.
        # => 직전과의 비교만 필요하면, (4-1) if stack:
        #    직전 및 역순으로 다 비교하면 (4-2) while stack and 언제까지역순검사할건지조건들: pop()으로 역순으로 직전것들을 모두 검사 준비한다.
        if stack:
            # (5) stack의 peek(직전)과 검사시
            #    if 성공시 -> 주체이자 대상이면, append
            #    else(실패)시 -> return False or flag처리를 해준다.
            if skill.index(x) == skill.index(stack[-1]) + 1:
                stack.append(x)
            else:
                # 검사 실패시 -> return False  or  flag처리
                return False

        # (6) 현재node가 올라갔으면, 배열의 다음 원소로 넘어가야한다.
        #    넘어가기 전에 처리해야할게 있으면 처리해준다.
        #   만약, while로 다 pop된다면, append가 되어야할 것 같고
        #   추가조건이 남았으면 추가조건을 처리해줘야한다.


        # (3) stack에 들어갈 대상들이라면 바깥배열의 첫원소부터 append해야한다.
        #    -> dfs라면 바깥에서 탐색배열 반복문없이, 첫원소를 미리 stack에 집어넣고, 확인하며 append한다
        #    => 한번 append되고나서, 다음원소부터는 더 위쪽에서 if stack while stack에 의해 확인검사한다.
        # stack.append(x)

        # (3-2) 하지만 여기서는 정확하게 첫원소는 skill의 첫번재원소와 동일한 것만 들어가야한다.
        #    => stack으로 안풀어도 되지만, 일단 억지로 푼다.
        if not stack:
            if x == skill[0]:
                stack.append(x)
            # stack이 안찬 첫번째원소인데, skill첫번째 원소와 다르면, 실패다.
            else:
                return False


    # (7) 배열을 다 탐색했는데, 확인검사에서 실패안했으면 성공이다.
    else:
        return True






if __name__ == '__main__':
    ## 스킬트리: https://school.programmers.co.kr/learn/courses/30/lessons/49993
    # my) 배열을 탐색하되, 일부원소들은 직전과 (순서를) 확인해야 통과한다.
    skill = input().strip()
    skill_trees = input().split()
    # print(skill_trees, skill)
    # ['BACDE', 'CBADF', 'AECB', 'BDA'] CBD
    count = 0
    for skill_tree in skill_trees:
        if check_skill(skill, skill_tree):
            count += 1

    print(count)
