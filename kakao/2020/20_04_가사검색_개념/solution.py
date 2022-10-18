import sys 
 
input = sys.stdin.readline 
 
 
if __name__ == '__main__':
    # 가사 검색: https://school.programmers.co.kr/learn/courses/30/lessons/60060
    words = list(input().split())
    queries = list(input().split())

    ## 개념
    ## 1. 단어검색인 경우, Tried 자료구조를 생각한다.
    ## -> 소문자만 가진다고 했으니, 총 26개의 node를 가진 link를 생각한다
    # 일반적인 tried 구조: https://raw.githubusercontent.com/is3js/screenshots/main/image-20221007204058401.png
    ## 2. 내려가면서 만드는데, 없으면 만들어서 새로 만들어/있으면 타고 들어가면 된다.
    ## 3. 검색은, 검색하고하는 단어의 끝단어가 leaf node일 경우 성공이다.
    ## -> 중간에 끝난다거나 or 검색글자가 남았는데 leaf node인 경우 실패한 경우다.
    ## 4. 여기서는 단어의 갯수가 정해져있기 때문에, depth가 다른 subtree를 가지고 있으면 갯수측정이 번거로워 진다.
    ## => 약간 변형해서 사용해야한다. [단어의 길이별  tried]를 따로 구성하고, 각각 검색한다.
    ## 5. 앞에서부터 ? 와일드카드로 시작한다면, 앞에서부터 tried 검색이 안되므로, [word자체를 뒤집은 상태로의 tried]도 따로 구성한다

    ## 6. 글자 5개로 이루어진 것부터 tried 구성하는 것 을 살펴보자.
    ## => subtree갯수는 미리 기록해 놓는다. 그때그때 계산하기 복잡하다.
    ## => root는 subtree에 포함안되서 cnt =0으로 시작하며, 다음link가 있으면, 이동하기 전에  += 1해준다
    ## => 마지막 단어라면, 그 다음은 NULL문자라고 생각하고, cnt만 1개 올려준다?! leaf node는 도달시마다 그냥 cnt+1해준다
    ##    root에서부터 글자마다 link에 매치되며, 같은 link가 나왔다면, link내리기전 node에  cnt +=1이다.
    ##   => 이렇게 카운팅하면, f로 시작하는 단어가 cnt개 있다는 뜻이다.
    ##   => 서로 다른 글자가 나왔다면? root node에 그래도 cnt+=1하는데, 그 뜻은 [단어길이가 5개인 글자]가 5개라는 의미가 된다.
    ##   root node의 cnt는 총 단어의 갯수다.
    ##   [cnt=5]
    ##  f/    \ k
    ##[cnt=4]  [cnt=1]

    # https://raw.githubusercontent.com/is3js/screenshots/main/image-20221007204837444.png)
    # https://raw.githubusercontent.com/is3js/screenshots/main/image-20221007204844419.png)
    # https://raw.githubusercontent.com/is3js/screenshots/main/image-20221007204852643.png)
    # https://raw.githubusercontent.com/is3js/screenshots/main/image-20221007204927965.png)
    # https://raw.githubusercontent.com/is3js/screenshots/main/image-20221007204935791.png)
    # https://raw.githubusercontent.com/is3js/screenshots/main/image-20221007205039232.png)
    # https://raw.githubusercontent.com/is3js/screenshots/main/image-20221007205127169.png)
    # https://raw.githubusercontent.com/is3js/screenshots/main/image-20221007205132521.png
    # https://raw.githubusercontent.com/is3js/screenshots/main/image-20221007205140830.png
    # https://raw.githubusercontent.com/is3js/screenshots/main/image-20221007205145700.png
    # https://raw.githubusercontent.com/is3js/screenshots/main/image-20221007205229235.png
    # https://raw.githubusercontent.com/is3js/screenshots/main/image-20221007205239821.png
    # https://raw.githubusercontent.com/is3js/screenshots/main/image-20221007205331360.png
    # https://raw.githubusercontent.com/is3js/screenshots/main/image-20221007205343584.png
    # https://raw.githubusercontent.com/is3js/screenshots/main/image-20221007205349009.png
    # https://raw.githubusercontent.com/is3js/screenshots/main/image-20221007205616626.png

    ## 검색 예시도 한번 살펴보자
    # fro?? -> 글자5개짜리 tried에서 검색을 시작한다.
    # fro까지만 타고내려갔다가, 그 뒤의 문자열은 안타고 내려가도된다. 몇개인지만 알면되므로, 그 node에서의 갯수를 반환하면 도니다.
    # https://raw.githubusercontent.com/is3js/screenshots/main/image-20221007205819610.png
    # https://raw.githubusercontent.com/is3js/screenshots/main/image-20221007205903805.png

