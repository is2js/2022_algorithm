import sys

input = sys.stdin.readline

if __name__ == '__main__':
    # 정렬 예시: 두 배열의 원소 교체
    # 두배열 A, B는 각각 N개의 원소로 구성 -> K번 바꿔치기 가능
    # -> A배열의 원소의 합이 최대가 되게 하는 최대K번 바꿔치기시,
    # -> A배열의 모든 원소합의 최대값은?
    # => A배열의 작은값과 <-> B배열의 큰 값을 바꿔치기 하면 된다.
    # a에서는 작은 순대로 b에서는 큰순서대로 바꿔치기 하되
    # swap원소가 같아지거나 a가 더 커지면 그만하면 된다.
    # 1 <= N <= 100,000(10^6) , 0<=K<N
    # 원소는 10^7보다 작은 자연수

    # ## 내풀이
    # # -> 일단 a와 b를 정렬해야한다.
    # # -> 우선순위큐를 써서 정렬을 유지해도 좋을 것 같으며
    # # -> 정수&&데이터최대값한정&&반복가능성이 있지만 -> 계수정렬(N + K) -> 최대값K가 너무 커서 안된다.
    # # -> 그다음 정렬이 퀵/병합인데, sort()랑 같이 nlgN이니까.. 그냥 sort로 정렬하는게 낫다
    # N, K = map(int, input().split())
    # a = list(map(int, input().split()))
    # b = list(map(int, input().split()))
    # a.sort()  # 2초라서.. NlgN -> 10^10 < 10^14
    # b.sort()
    #
    # # 원소swap은 어떻게할가? -> 그냥 python swap으로 인덱싱해서 덮어쓰면 됡것 같다.
    # swap_count = 0
    # # 길이가 같으니 대칭인덱스를 스면 된다.
    # #  0    5-1
    # #    1 5-2
    # #     i len()-(1+i)
    # for i in range(len(a)):
    #     # for문으로 돌릴 경우, 탈출조건은 맨 앞에 설정한다.
    #     if swap_count >= K or a[i] >= b[len(a) - (i + 1)]:
    #         break
    #     # print(f"a의 {a[i]}와 b의 {b[len(a) - (i + 1)]} swap")
    #     a[i], b[len(a) - (i + 1)] = b[len(a) - (i + 1)], a[i]
    #     swap_count += 1
    #
    # print(sum(a))

    ## 풀이
    # -> 각 배열이 최대 10^5까지 들어오므로 N제곱의 삽입정렬/선택정렬은 불가하다
    # -> 최악에도 NlgN를 보장해주는 표준라이브러리로 해결할 수 있다.
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()  # NlgN
    b.sort(reverse=True)  # (1)역순으로 정렬하면, 같은 index로 a최소값/ b최대값을 비교할 수 있다.

    # (2) 최대 k번 비교한다면, for in range(k) + 그전에 끝나면 break를 걸면 된다.
    # -> 최대 N번도 for문 + if break를 쓰자.
    for i in range(K):
        # (3) 작을때만 swap하고 그게 아니라면 break다.
        if a[i] >= b[i]:
            break
        a[i], b[i] = b[i], a[i]

    print(sum(a))
