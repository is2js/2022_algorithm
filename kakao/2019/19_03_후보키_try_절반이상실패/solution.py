import itertools
import sys
from collections import defaultdict

input = sys.stdin.readline


def is_valid(col_comb, database):
    for col in col_comb:
        for ans in result:
            if col in ans:
                return False

    temp = [''] * len(database[0])
    for col in col_comb:
        for i in range(len(database[col])):
            temp[i] += database[col][i]

    if len(temp) == len(set(temp)):
        print(temp)
        return True
    return False


if __name__ == '__main__':
    ## 후보키: https://school.programmers.co.kr/learn/courses/30/lessons/42890
    relation = []
    for _ in range(6):
        relation.append(input().split())

    database = defaultdict(list)
    for col in range(len(relation[0])):
        for row in range(len(relation)):
            database[col].append(relation[row][col])

    result = []
    for n in range(1, len(relation[0]) + 1):
        for col_comb in itertools.combinations(database.keys(), n):
            if is_valid(col_comb, database):
                result.append(col_comb)

    print(result)
