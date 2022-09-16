import sys

input = sys.stdin.readline
sys.setrecursionlimit(1_0000)


def recursive_solve(N, number, k, result):
    ## 연산의 제한으로 탐색실패를 준다.
    # -> 보통은 -1로 실패를 반환하지만, 자식node집계가 min(8이하 종착값)으로 집계되니, -1 대신 9를 준다.
    if k > 8:
        # return -1
        return 9

    ## 종착역에서의 연산횟수를 반환한다.
    if result == number:
        return k

    # 자신의 처리 -> 경우의 수별로 자식재귀 호출 후 집계
    temp_result = []
    ## stack을 k -> k +1 만 진행하는 것이 아니라
    # -> case별 연산에 들어가는 변수가, stack에 영향을 준다. N -> k + 1, NN -> k + 2
    # -> 누적결과값 변수에 반영할 [stack영향주는 다음 중간값]별로 stack을 건너띈다.
    # for i in range(1, 8 + 1):
    # => 다음에 붙일 N의 갯수는 1~8개까지인데, 현재 stack k에 대해,
    #    [현k -> k-1개를 쓰고], k번째를 선택하는 상태 -> 1 ~ 8 - (k-1)개까지 N을 붙일 수 있다.
    # => 현재스택k다 == k번째 연산을 case별자식재귀의 파라미터에서 선택하여 사용한다 == k-1개 연산한 상태다.
    for i in range(1, 8 - (k - 1) + 1):
        ## [1글자 숫자의 자리수] str으로 바꿔서 처리하는 것이 좋다.
        nn = int(str(N) * i)
        temp_result.append(recursive_solve(N, number, k + i, result + nn))
        temp_result.append(recursive_solve(N, number, k + i, result * nn))
        temp_result.append(recursive_solve(N, number, k + i, result - nn))
        temp_result.append(recursive_solve(N, number, k + i, result // nn))

    ## 자식들을 extend로 다 모아서 집계하지말고, 할 수 있다면, 모은 뒤 집계함수로 반환하는 것이 좋다.
    # -> 그래서 -1 반환이 아니라, 종착역 최대값 8에 대해 min() 집계에 안걸릴 9로 반환했었다.
    return min(temp_result)


if __name__ == '__main__':
    N, number = map(int, input().split())
    # 모든 경우의 수를 찾고, 그 중에 1개를 택해서 풀어야한다
    # => 연산횟수k를 stack변수로 잡고, 1부터, 각각 5case를 만들며 뻗어나간다 => 재귀
    #    종착역은 number == result이며, 그때의 k의 최소값을 구하면 된다.
    print(recursive_solve(N, number, 0, 0))
