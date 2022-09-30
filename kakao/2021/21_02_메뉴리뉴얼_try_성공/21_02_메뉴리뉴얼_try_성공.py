import itertools
import sys

input = sys.stdin.readline

from collections import defaultdict, Counter

if __name__ == '__main__':
    ## 메뉴리뉴얼: https://school.programmers.co.kr/learn/challenges?order=recent&page=1&partIds=20069
    orders = input().split()
    course = list(map(int, input().split()))

    # counter = defaultdict(int)
    # for order in orders:
    #     for menu in order:
    #         counter[menu] += 1
    #  print(counter)

    ## 개별 등장횟수가 아니라
    ## 조합으로 몇번 등장햇는지가 중요하다...-> 몇개조합으로 할 것인지는 course에 주어져있따

    counter = defaultdict(int)
    for count in course:

        for order in orders:
            for subset in itertools.combinations(sorted(order), count):
                counter[subset] += 1

    # print(counter)
    # {('A', 'B'): 2, ('A', 'C'): 2, ('A', 'D'): 3, ('A', 'E'): 2, ('B', 'C'): 1,
    # ('B', 'D'): 1, ('B', 'E'): 1, ('C', 'D'): 3, ('C', 'E'): 1, ('D', 'E'): 2,
    # ('X', 'Y'): 2, ('X', 'Z'): 2, ('Y', 'Z'): 2, ('A', 'B', 'C'): 1,
    # ('A', 'B', 'D'): 1, ('A', 'B', 'E'): 1, ('A', 'C', 'D'): 2,
    # ('A', 'C', 'E'): 1, ('A', 'D', 'E'): 2, ('B', 'C', 'D'): 1,
    # ('B', 'C', 'E'): 1, ('B', 'D', 'E'): 1, ('C', 'D', 'E'): 1,
    # ('X', 'Y', 'Z'): 2, ('A', 'B', 'C', 'D'): 1, ('A', 'B', 'C', 'E'): 1,
    # ('A', 'B', 'D', 'E'): 1, ('A', 'C', 'D', 'E'): 1, ('B', 'C', 'D', 'E'): 1})

    ## 조합갯수별 greedy로 모은다. 여러개 발견시 -> 같이 모은다.
    ## 일단 2개이상 주문한것으로 커팅한다.
    ## -> dict 필터링은 k:v dict comp + if문으로 하자.
    # counter = {menu: count for menu, count in counter.items() if count >= 2}

    ## 매 course에 적힌 갯수마다 greedy
    answer = []
    for n in course:
        max_count = 0
        max_menu = None
        max_menus = []
        for menu, count in counter.items():
            if not count >= 2: continue
            if len(menu) != n: continue

            if count == max_count:
                max_menus.append(menu)

            elif count > max_count:
                max_count = count
                max_menu = menu
                max_menus = [menu]

        ## greedy는 탐색은 발견 못할 수도 있다.
        if len(max_menus):
            max_menus = list(map(''.join, max_menus))
            answer.append(max_menus)
    if answer:
        answer = sorted(itertools.chain.from_iterable(answer))
    print(answer)

    print(Counter([1, 1, 2, 2, 3]).most_common())