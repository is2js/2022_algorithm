import sys

input = sys.stdin.readline


def dfs(graph, src):
    if visited[src]: return
    visited[src] = True
    print(src)

    for next_node in graph[src]:
        if visited[next_node]: continue
        parent_table[next_node] = src
        dfs(graph, next_node)


def comb(visited, position, result):
    if visited == all_visited:
        return result

    if position >= len(sales):
        return

    curr_team = None
    for team, teams in teams_of_team.items():
        if position in teams and not visited & 1 << team:
            curr_team = team
    if not curr_team: return

    temp_result = float('inf')
    sel = comb(visited | 1<<curr_team, position + 1, result + sales[position])
    if sel:
        temp_result = min(temp_result, sel)
    unsel = comb(visited, position + 1, result)
    if unsel:
        temp_result = min(temp_result, unsel)

    return temp_result


if __name__ == '__main__':
    ## 매출하락 최소화: https://school.programmers.co.kr/learn/courses/30/lessons/72416
    sales = list(map(int, input().split()))
    links = []
    for _ in range(9):
        links.append(list(map(int, input().split())))

    sales = [0] + sales

    graph = [[] for _ in range(len(sales))]
    for u, v in links:
        graph[u].append(v)

    ## graph정보로 -> dfs로 depth를 넣어서, depth_table -> parent_table 채우기
    ##            -> depth테이블은... LCA (1) 같은depth까지 이동 (2) 동시 등산을 위한 것이니 까 꼭 안해도 된다?
    parent_table = [i for i in range(len(sales))]
    ## depth테이블은 visited + dfs의 node탐색으로 밖에 못채운다.

    ## 좌표탐색은 visisted가 안필요하다? -> 1개로 다 갈라쓴다(back은 visited영향안받고 빽된다)
    ## -> 순열 같이.. 매 경우의 수마다 [다른숫자를 선택하는 상태값]이 필요할때만 파라미터로 들고 다닌다ㅣ
    ## -> 순열이 아닌 좌표탐색 dfs는 visisted를 들고다니지 않는다. 1개만 필요. board로 대신쓸 수도 있다.
    # dfs(src=1, visited=1)
    visited = [False] * len(sales)
    dfs(graph=graph, src=1)

    # print(parent_table)
    # [0, 1, 10, 1, 5, 1, 10, 9, 10, 1, 5]
    ## 1번을 제외하고, 자기자신이 아닌, 부모로 1번이라도 거론되면, 팀장자격이 있다.
    ## parent_table -> 동일 부모별(value) 자식들(index)을 hash에 매핑하면, 팀원을 만들 수 있음.
    teams_of_team = {}
    for child, team_maker in enumerate(parent_table[1:], start=1):
        if team_maker in teams_of_team:
            # teams_of_team[team_maker].append(child)
            teams_of_team[team_maker].add(child)
        else:
            # teams_of_team[team_maker] = [child]
            ## {1: [1, 3, 5, 9], 10: [2, 6, 8], 5: [4, 10], 9: [7]}
            ## => 문제: 1번을 제외하고.. 자신의 자신의 팀에 안들어가게 해놨네..
            # 초기화할때 1번으로 자신을 팀원으로 추가
            # -> 중복될 수있으니, set으로 구성
            teams_of_team[team_maker] = {team_maker, child}

    # print(teams_of_team)
    # {1: {1, 3, 5, 9}, 10: {8, 10, 2, 6}, 5: {10, 4, 5}, 9: {9, 7}}

    ## 팀원별 1명씩 뽑되, 팀장을 뽑으면 더 좋은데? 빠지면서 뽑는 조합인데..
    ## 팀별 visited를 체킹해서 조합한다?!
    teams = teams_of_team.keys()
    ## 팀별visisted를 다 쓴 것이 종착역이다.
    ## -> bit를 종착역으로 쓸려면 [all marking bit]가 미리 값으로 만들어놔야한다.
    visited = 0
    all_visited = 0
    for team in teams:
        all_visited |= 1 << team
    # print(bin(all_visited)) # 0b11000100010
    print(comb(visited=0, position=1, result=0))
