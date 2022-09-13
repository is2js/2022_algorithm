import sys

input = sys.stdin.readline


def solve(prev_cnt, prev_position, prev_result):
    # 1) stack결정변수로 종착역을 만든다.
    if prev_cnt == 2:
        return prev_result
    # 6) 조합재귀 탐색의 경우, 2개씩 node가 갈라지면서, node가 죽지 않는 경우가 없는 완전 탐색이다.
    # -> 그 결과 prev_cnt가 2로 차지않고 계속 증가하면서 node를 뻗어나갈 수도 있다.
    # -> stack결정변수가 업데이트되지 않는 경우(조합탐색 중 원소선택x start)
    # -> 항상 업데이트 되는 원소position으로 종착역을 걸되,
    #    정답 집계시 사라질 값으로 건다 ex> 최대값 -> -1반환
    if prev_position == N:
        return float('-inf')

    # 2) 자신의 처리없이 다음재귀호출로 시작하는 재귀는
    #    여러case의 여러node로 시작하게 된다.
    #   -> 조합탐색은, 주어진 순서부터, 선택O vs 선택X 2개의 node로 나아간다
    #   cf) 순열은, 배열의 갯수만큼 원소선택하는 node로 시작하여
    #      배열의 갯수만큼 반복문으로 다음재귀를 호출했다.

    # 3) 조합에서는 배열 <-> 재귀호출순서 반복문을 매핑하지 않는다.
    #   -> 반복문이 등장하지 않고, 직접 index를 업뎃(pos+1)하며
    #   -> **현재의 상태에 있는 prev_position의 index 배열값을 선택**하는 것이기 때문에
    #   -> pos+1과 별개로 lst[pos]의 값으로 누적연산한다.

    # 4-1) 현재 수numbers[prev_position]이 선택된 start -> cnt+1  /  pos는 무조건 증가 / 현재 뽑으로 뽑은 원소로 -> 누젹결과연산 업데이트
    # -> 가장 큰, 두수의 합-> 초기값을 활용해서 두수의 합을 누적하도록 result를 업데이트한다.
    # solve(prev_cnt + 1, prev_position + 1, selected_tuple + lst[prev_position])
    # 4-1) 현재 수numbers[prev_position]이 선택안되 start -> cnt그대로 / pos증가 / 뽑힌 원소x -> 누적결과변화x
    # solve(prev_cnt, prev_position + 1, selected_tuple)

    # 5) 각 node는 누적된 결과값을 반환해주므로 -> 1개로 집계해야한다.
    #   -> 요구사항대로 두 수의 합이 담긴 누적결과값 selected_tuple 중 최대값을 뽑게 한다.
    selected = solve(prev_cnt + 1, prev_position + 1, prev_result + numbers[prev_position])
    unselected = solve(prev_cnt, prev_position + 1, prev_result)
    return max(selected, unselected)

    pass

    # 조합 완전탐색 템플릿 만들기
    # solve(prev_cnt, prev_position, selected_tuple)
    solve(0, 0, 0)

    def solve(prev_cnt, prev_position, prev_result):
        if prev_cnt == 2:
            return prev_result
        if prev_position == N:
            return float('-inf')
        selected = solve(prev_cnt + 1, prev_position + 1, prev_result + numbers[prev_position])
        unselected = solve(prev_cnt, prev_position + 1, prev_result)
        return max(selected, unselected)


if __name__ == '__main__':
    ### 원소 2개이상을 완전탐색 && 선택에 순서가 없는 교환법칙 성립 연산이 요구될 때
    ### -> 교환법칙성립(+/*) 하는 피연산자 2개이상의 연산
    ### -> 재귀를 통한 조합으로 탐색한다
    ### -> 재귀로 탐색하는 것은 완전 탐색이며, node가 중간에 끊기기도 한다.

    ### 조합과 같이 뽑는 순서가 중요하지 않는 경우,
    ### (1) 주어진 순서대로 고정해놓는다.(순서가 중요치 않다. 순서대로 앞으로만 선택한다. 이해가 쉽게 오름차순 정렬하면 쉽다)
    ### (2) 매핑된 배열의 원소선택은, cnt + 1 vs cnt 로 가르되
    ###     선택 안하더라도 pos는 무조건 증가하도록 start(다음 재귀)를 뻗는다.
    ###     -> 선택안하더라도(cnt->cnt) 한번 도달한 원소는 뒤돌아보지 않는다(position -> position + 1)

    ### cf) 순열에서는 원소 선택을 상태비트를 업데이트 & 확인하되
    ###     선택안함은 continue로 건너띄었었다.
    ###     조합은 상태비트는 이용안하고, 지나가되, cnt를 세지 않는 방법으로 선택안한다.

    # ex> 가장 큰, 두수의 합, 구하기
    N = 4
    numbers = [1, 2, 3, 4, ]

    # 조합을 위한 탐색을 재귀로 하는 이유
    # -> stack결정변수로 업데이트된 연산의 횟수를 제한할 수 있으며
    # -> 현 상태를 가지고, 여러 case를 동시에 탐색할 수 있다(N개의 다음재귀 호출)
    # solve(prev_cnt, prev_pos, selected_tuple)
    print(solve(0, 0, 0))

    pass
