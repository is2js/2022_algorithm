import itertools
import sys
from collections import Counter
from collections import defaultdict

input = sys.stdin.readline 
 
 
if __name__ == '__main__':
    ## 22-01-신고결과받기: https://school.programmers.co.kr/learn/courses/30/lessons/92334

    id_list = input().split()
    report = []
    for _ in range(int(input().strip())):
        report.append(input().split())
    k = int(input().strip())

    ## 유저당 신고당한 사람들을, id별 set에 매핑하여 중복을 제거한다.
    # -> 이차원배열? map?
    # -> 이미 순서가 있으니.. 2차원배열에? ㄴㄴ id가 숫자가 아닐 때는 dict에
    id_of_subjects = defaultdict(set)
    for id, subject in report:
        id_of_subjects[id].add(subject)

    # print(id_of_subjects)
    # {'muzi': {'frodo', 'neo'}, 'apeach': {'frodo', 'muzi'}, 'frodo': {'neo'}})

    ## (2) 중복을 제거한 신고당한사람들만 모아서 id별 카운팅하여, k번이상이면 당첨
    subject_of_count = Counter(itertools.chain(*id_of_subjects.values()))
    print(subject_of_count)
    # Counter({'frodo': 2, 'neo': 2, 'muzi': 1})

    ## (3) id별 신고한사람들 / 신고받은 횟수 를 id순으로 나열 없으면 0
    # -> 순서대로 id 매핑된 배열 + dict매핑은 호출순서에 종속되어 그 순서대로 불러올 수 있다.
    # print([subject_of_count[id] for id in id_list])
    # [1, 2, 0, 2]

    ## (4) 유저별 신고당한 횟수가 아니라 유저별 신고대상 중 k회를 넘게 신고당한 사람으 갯수
    ## 유저 - 신고대상들   / 신고대상(들) - 신고당한횟수
    ## => 순서대로 매핑은 for을 이용해서 join해준다?
    answer = []
    for id in id_list:
        subjects = id_of_subjects[id]
        result = []
        for subject in subjects:
            count = subject_of_count[subject]
            if count < k:
                continue
            result.append(subject)
        result = len(result)
        answer.append(result)
    print(answer)







