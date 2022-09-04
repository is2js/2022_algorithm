import sys 
 
input = sys.stdin.readline 
 
 
if __name__ == '__main__':
    ## greedy예제 : 모험가 길드
    # N명의 모험가의 공포도가 주어지는데, 공포도X인 모험가는 X명이상으로 구성
    # -> 최대 몇개의 모험가그룹을 만들 수 있을까
    # -> 모두 포함될 필요는 없다.
    # ex> 2 3 1 2 2 -> 213 + 22 -> 2개 그룹
    N = int(input().strip())
    people = list(map(int, input().split()))

    # (1) 일단 정렬부터 하고 시작한다( 순열이 아니라 뽑는 조합 문제인 경우!)
    # 1 2 2 2 3
    people.sort()
    # (2) 최대한 많은 그룹을 생성하여야하므로, 낮은 순으로 공포도를 확인하면서
    #   -> (현재 그룹에 포함된 모험가의 수)가 [현재 공포도보다 크거나 같다]다면 이를 그룹으로 설정해버리면 된다.
    # 1(1) | 2(1) 2(2) | 2(1) 3(2) ...
    #   -> 오름차순 정렬되어있다면, 항상 최소한의 모험가 수만 포함하여 그룹을 결성하게 된다.

    current_group_count = 0
    total_group_count = 0
    for person_gage in people:
        # (3) 현재그룹의 카운팅 누적부터 하고, 그 카운트 >= 공포도(최소k명이상)이면,
        #   -> 빠르게 그룹을 맺어버린다.(total에 count)
        #   => 공포도를 최소k명이상 모였으면 통과로 해석한다.
        current_group_count += 1
        if current_group_count >= person_gage:
            total_group_count += 1
            # (4) 그룹이 결성되면 현재그룹원수 는 초기화해야하낟.
            current_group_count = 0
    print(total_group_count)




    pass 
