import itertools
import sys
 
input = sys.stdin.readline


def combination(m, weights,
                # count,
                position, result):
    if result == m:
        return 1

    if position >= len(weights):
        return 0

    # print(position, result)

    temp_result = 0
    temp_result += combination(m, weights,
                position + 1, result + weights[position])

    temp_result += combination(m, weights,
                position + 1, result)

    return temp_result



if __name__ == '__main__':
    ## 사탕담기: https://velog.io/@illstandtall/Programmerspython-9.-%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4-%EC%8B%A4%EC%8A%B5-4-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%82%AC%ED%83%95-%EB%8B%B4%EA%B8%B0
    m = int(input().strip())
    weights = list(map(int, input().split()))
    # 가방을 정확히 m 그램으로 채우는 경우의 수
    # => 합이 정확히 3000이 되게 하는 수 중복없이 뽑기...
    # => 투, 쓰리 포인터가 아니라, N포인터네.. => 몇개뽑을지 알 수 없다? => comnination
    #   weights 3~ 15개.. 총 15포인터까지..
    # (1) 일단 정렬부터
    weights.sort()

    # (2) [경우의 수가 몇개 안되면 api로 모든 조합]뽑아서 필터링하기
    # => 그리고 List weights의 최대 길이가 15로 아주 작습니다. 경우의 수를 뽑는 알고리즘을 이용해도 될 것 같습니다.
    ## => 뽑은 조합을 합으로 변경한 map(sum_, )도 iter라서 for 문에 돌릴 수 있다.
    count = 0
    for i in range(1, len(weights) + 1):
        count += len([x for x in map(sum, (itertools.combinations(weights, i))) if x == m])
    print(count)

    # (3) 조합을 재귀로 풀되, 종착역의 조건이 조합뽑는 갯수n이 아니라 무게 m으로 둔다?!
    print(combination(m, weights,
                      0, 0))