import itertools
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## 주사위게임: https://chaelinyeo.github.io/%EC%BD%94%ED%85%8C/Level02%EC%A3%BC%EC%82%AC%EC%9C%84%EA%B2%8C%EC%9E%84/
    # 문제 이미지: https://velog.velcdn.com/images%2Frapsby%2Fpost%2F994f0891-7431-4c80-97a7-e5649c24aaa5%2Fimage.png
    # 문제그림포함: https://velog.io/@rapsby/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A3%BC%EC%82%AC%EC%9C%84-%EA%B2%8C%EC%9E%84-python-edmg8xrg

    monster = list(map(int, input().split()))
    S1, S2, S3 = map(int, input().split())
    ## 주사위는 모든 경우의수가 확률이 동일하니 -> 동일한 확률은 경우의 수를 세서 확률로 해결한다
    ## => 몬스터를 만나지 않을 확률 -> 1 - (몬스터를 만날 확률) ->  1 - ( 몬스터 경우의 수 / 전체 경우의 수)
    # prob_S1 = 1 / S1
    # prob_S2 = 1 / S2
    # prob_S3 = 1 / S3

    # min_location, max_location = 3, S1 + S2 + S3
    ## 중복허용 배열의 차이 -> Counter
    ## 중복없는 배열의 차이 -> set으로 차집합
    # none_monster = set(range(3, max_location+1)) - set(monster)

    ## 1개 배열 3개 뽑기 -> 3포인터 (index 3개)
    ## 3개 배열 1개씩 뽑기 -> for 3개 or product 곱집합(조합)으로 뽑기

    product_s1s2s3 = list(map(sum, itertools.product(range(1, S1 + 1), range(1, S2 + 1), range(1, S3 + 1))))
    count = 0
    for x in product_s1s2s3:
        ## 출발이 1에서 출바라힉 때문에 [주사위합 + 1 == 몬스터위치가 되어야한다]
        ## => 1부터 시작하는 주사위합 -> 몬스터위치까지 가려면 주사위합 + 1을 해야한다
        if x + 1 in monster:
            count += 1

    total = len(product_s1s2s3)
    print(int((1 - (count / total)) * 1000))




