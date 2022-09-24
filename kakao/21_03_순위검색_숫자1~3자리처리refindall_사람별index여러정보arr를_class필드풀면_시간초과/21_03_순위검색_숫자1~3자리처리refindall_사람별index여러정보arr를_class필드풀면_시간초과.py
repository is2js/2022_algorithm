import re
import sys

input = sys.stdin.readline

class Applier:

    def __init__(self, language, career, position, soulfood, score):
        self.language = language.strip()
        self.career = career.strip()
        self.position = position.strip()
        self.soulfood = soulfood.strip()
        self.score = int(score)

    def is_language(self, language):
        return self.language == language
    def is_career(self, career):
        return self.career == career
    def is_position(self, position):
        return self.position == position
    def is_soulfood(self, soulfood):
        return self.soulfood == soulfood
    def equal_and_greater_than(self, score):
        return self.score >= int(score)


    def __repr__(self):
        return f"{self.language, self.career, self.position, self.soulfood, self.score!r}"


def query_list(appliers, language, career, position, soulfood, score):
    ERROR = '-'
    if language != ERROR:
        appliers = [x for x in appliers if x.is_language(language)]
    if career != ERROR:
        appliers = [x for x in appliers if x.is_career(career)]
    if position != ERROR:
        appliers = [x for x in appliers if x.is_position(position)]
    if soulfood != ERROR:
        appliers = [x for x in appliers if x.is_soulfood(soulfood)]
    appliers = [x for x in appliers if x.equal_and_greater_than(score)]
    return appliers

if __name__ == '__main__':
    ## 순위검색: https://school.programmers.co.kr/learn/courses/30/lessons/72412
    info = [ input().strip() for _ in range(6)]
    query = [ input().strip('\n') for _ in range(6)]


    appliers = [Applier(*data.split()) for data in info]

    answer = []
    for q in query:
        ## 뒤에 숫자가 자리수가 달라서 -3으로 하면 안된다.
        score = re.findall('([0-9]+)', q)[0]

        data = [x.strip() for x in q.replace(score, '').split('and')]

        data += [int(score)]
        count = len(query_list(appliers, *data))
        answer.append(count)

    print(answer)



