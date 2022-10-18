import sys

input = sys.stdin.readline

if __name__ == '__main__':
    # 가사 검색: https://school.programmers.co.kr/learn/courses/30/lessons/60060
    words = list(input().split())
    queries = list(input().split())


    ## 1. trie자료구조 먼저 구현
    class Trie:
        def __init__(self):
            ## 2. 객체 처음생성시, 초기화할 것은 dict()로 초기화하는 child link이다.
            ## => 다음에 이어질 문자char를 key로, 그 문자로 시작되는 cnt를 세줄  node를 value로 가지고 있는다.
            self.child = dict()
            ## 3. 해당문자열 진입까지의 갯수를 세는 cnt필드도 초기화
            self.count = 0

        ## 4. 문자열을 통째로 입력받아, root에서부터, 연결된 모든 node를 메서드 1개에서서 처리한다.


        def insert(self, str):
            ## 5. curr를 self로 한다. 시작을 항상 root node에 호출하는 법칙을 정해놓고, 시작self는 root node라 생각한다.
            ## -> 있던 link를 바꾸는 것은 항상 [curr 등  변수로 keep해놓고 + curr업뎃전에 link되는 필드에 옮겨담아서 사라지지 않게]하는 것이 핵심이다.
            ## -> 여기서는 link를 바꾸는게 아니라, 링크가 dict에 저장되어 사라지지 않으니, 타고 내려가기만 한다.
            curr = self
            ## 6. 입력으로 받은 문자열 하나하나를 다 처리한다.
            ## => root node에서부터, ch node까지 child link를 타고 깊어진다.
            ## => 1) link타기전에 직전node의 cnt올리고 2) 문자열 순서대로 없으면 child link에 등록하면서 3) link를 타고 내려가 마지막 문자열의 node까지 깊어진다
            ##    카운팅 + chlid link 없으면 등록 + 문자열순서대로 leaf node까지 curr node를 업뎃하며 깊어진다.
            for ch in str:
                ## 7. link를 타고 아래node로 내려가기 전에, count를 하나 올려준다.
                curr.count += 1
                ## 8. 최초 문자ch라면, link가 없으니, 해당ch를 key로 줘서 link를 만들고, Trie노드를 value로 줘서 타고 내려간다.
                if ch not in curr.child:
                    curr.child[ch] = Trie()
                ## 9. ch마다, child dict의 key로 등록된 자신의 link타고 내려간다.
                curr = curr.child[ch]
                ## 여기까지하면, f의 node에 도착한 상태로 curr가 [root -> f node]로 업뎃하고 끝난다
                ## 다음은 f에서 r에 대해 없으면 등록하고, r로 이동하고 끝난다.

            ## 10. 만약, curr빼놓고 [for next를 돌면서] 빼놓은 curr만 처리후 curr=next업뎃한다면
            ##     맨마지막 next는 curr로 업뎃됬지만, 자신의 next가 없어서 반복문X -> curr처리 X가 된다.
            ##     비슷하게, root node를 curr로 미리 빼놓고
            ##     => 순회는 (root)front의 f부터 한다. => for next를 도는 것
            ##        next를 돌되, curr.count +=1 밑 link+node생성은 curr에 하고 있으므로
            ##       f시 root+=1 / r시 f+=1 / ... / t시 n+=1
            ##    => t자신은 curr로만 업뎃되더라도 순회할 next가 없으므로  curr.count+=1 + 자식node생성은 못탄다
            ##       t는 자식이 없으므로 자식node생성은 안하지만, 자신의 node curr에 count +=1은 해주기로 했다.

            ####  curr = next(or curr.link) 업뎃시, for next돌고 있다면, 맨마지막 curr이 된 next는 반복문 끝나고 curr처리를 한번더해주자!!
            #### => 대신, next자체도 처리가 필요할 경우만!!! (i-1, i의 비교의 문제라면 딱히X)
            #### => curr빼놓고, curr = next업뎃은 [index+1로 next로 넘어갈 수없는 경우, 직접link나 업뎃을 통해 next를 지정해줘야하는 경우]
            ####    그 때 처리하며, next처리없이 curr만 처리한다면, 맨마지막 curr에 대한 처리는 직접해줘야한다.
            curr.count += 1  # t의 node.count를 +1 해주기


        ## 12. 다음은 검색시 사용할 search
        def search(self, str):
            curr = self  # root에서만 부를 예정.
            for ch in str:
                ## 13. 현재 글자가 ?면, 현재node에 적힌 count를 반환하면, root였다면, 모든 단어들의 갯수
                ##     f에 도착한 이후로 ?가 나왔다면, f로 시작하는 모든 단어들의 갯수
                if ch == '?':
                    return curr.count
                ## 14. insert와 달리, 탐색시에는 다음글자의 링크가 없다면 link에 Trie node생성이지만
                ##    search에서 다음글자의 link가 없다면,  해당key워드가 tried tree에 없다는 뜻
                ##   => 갯수 0을 반환한다
                if ch not in curr.child:
                    return 0
                ## 15. ?도 아니고 link가 있따면, 타고내려가면 된다.
                curr = curr.child[ch]
                ## 문제 조건상 for문 내부에서 early rerturn 된다.
                ## -> ?가 항상 포함되어있기 때문에
            ## 디버깅을 위한
            return curr.count


    ## 13. root는 미리 생성해둔다. => 근데 단어길이 종류별로 1개씩 root가 필요하다.
    ## => 단어의 길이는 1~10000이라고 하니, 각 길이당 index매핑한 root node들을 만들어둔다.
    ## => 문제조건을 보니, 단어의길이는 10000이하므로 미리 node를 만들어둔다.
    trie_root = [Trie() for _ in range(10000)]
    ## 14.물음표가 뒤에 달린 경우는, 거꾸로 된 trie가 필요하다 -> 미리 reverse로 만들어준다.
    re_trie_root = [Trie() for _ in range(10000)]

    ## 15. 이제 words를 돌면서, 각 (word의 길이-1)번째 root node를 이용해서 insert한다.
    for word in words:
        trie_root[len(word) - 1].insert(word)
        ## 16. 뒤집어서도 insert해야한다.
        re_trie_root[len(word)-1].insert(word[::-1])

    ## 16. 이제 query별로 길이에 맞는 root node를 뽑아서 search한다.
    answer = []
    for query in queries:
        ## 17. 첫번째 단어가 물음표가 아니면, 정방향 trie를 사용한다.
        if query[0] != "?":
            answer.append( trie_root[len(query)-1].search(query) )
        else:
            answer.append( re_trie_root[len(query)-1].search(query[::-1]))

    print(answer)
