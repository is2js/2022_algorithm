import sys

input = sys.stdin.readline

if __name__ == '__main__':
    # 가사 검색: https://school.programmers.co.kr/learn/courses/30/lessons/60060
    words = list(input().split())
    queries = list(input().split())


    ## 1. 주어진 단어들을 학습(insert)시키고, 해당하는 단어가 몇개인지 문자열 검색한다면, trie 자료구조를 쓴다.
    ## => [starts_with count]뿐만 아니라, [starts_with 모든단어]  / 존재유무(search)를 직접 받아올 수 도 있다.
    class TrieNode:
        ## (1) trie node는 [현재까지 타고온 글자link에 대해 존재하는 count]필드와 [타고갈 자식글자link dict]필드를 기본적으로 가진다.
        def __init__(self):
            self.count = 0
            self.children = dict()

        ## (2) trie node는 [root node에 한해 사용될 insert/search]를 기본적으로 가진다.
        def insert(self, string: str):
            ## (3) link를 타는 방법은, curr을 빼놓고, next link값을 기준으로 curr = next 직접 업뎃하며, curr을 처리한다.
            ##  => next기준 for순회하며 curr처리한다면 => 마지막 next는 자신의 next가 없어서 순회를 못타고  curr처리가 안되므로 반복문끝나고 직접 한번더 해준다.
            curr = self  # root node만 사용할 것이며, curr에는 현재 자신(TrieNode)를 빼놓으면 된다.
            for char in string:
                ## (4) insert 학습은 기본적으로  자식link를 없으면 생성하며 타기전에, 부모node로서 카운팅을 해주는 것이다.
                ##  => 부모node에서 카운팅하면, 그 아래 몇개의 단어들이 존재하는지 알 수 있게 된다.
                ##     root node라면, 모든단어의 갯수  /  char link를 탄 node라면, 해당 char로 시작하는 단어의 갯수
                curr.count += 1
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                ## (5) 직접 자식char link 속 node를 next로보고 업뎃해준다.
                curr = curr.children[char]
            ## (6) for next기준 순회는, 마지막 node는 curr처리를 못하므로 반복문끝나고 직접해준다.
            ## => 마지막node에 cnt +=1를 해줌으로써.. 마지막char로 끝나는 단어의 갯수가 1개가 됨을 알 수 있다.
            curr.count += 1

        ## (7) trie node는 [root node에 한해 사용될 insert/search]를 기본적으로 가진다.
        def search(self, query: str):
            ## (8) search역시 insert처럼, root node에서부터 curr로 빼놓고 직접 next업뎃하며 처리한다.
            curr = self
            for char in query:
                ## (9) 일단 ? 와일드카드가 나온 순간부터는, [단어길이 상관없이?] 현재node에서 자식link타기전, 모든 자식단어들 갯수인 curr.count를 반환하면 된다.
                ## => 길이별 trie를 따로 생성할 것이다. 길이까지 고려하면, 뒤에 남은 단어들을 depth를 고려해서 처리해야해서 복잡해진다.
                if char == "?":
                    return curr.count
                ## (10) next char에 대해, link가 없다면, 존재하지 않는 단어다.(insert시 학습안된) -> 갯수 0을 반환
                if char not in curr.children:
                    return 0
                ## (11) 와일드카드가 아니면서 && 링크가 존재할때만 링크를 타고 간다.
                ## -> insert시 link없으면 생성해서 타고가기 vs search link없으면 학습안된 문자열로서 탈락
                curr = curr.children[char]  # 사실상 select시 존재검사라고 할 수 있다.

            ## (12) search는 curr, next없뎃하면서, 무조건 걸리게 되어있다? 맨마지막 node는 처리할 필요가 없다?
            ##      존재하면, curr에는 맨마지막node가 curr처리안된체(여기선 없음)로 걸려있고 자신의 갯수반환한다.
            ##      존재안하면 0으로 반환되고, 와일드카드면 미리 반환된다.
            return curr.count


    ## 2. trie검색을 insert된 모든 word가 아니라, word길이 -> depth별로 끊어서 처리해야한다면 너무 복잡해진다.
    ##   insert시 1글자씩 cnt하기 때문에, cnt는 단어길이랑 상관없이 섞여있다.
    ## => 애초에 trie 구조를 단어길이별로 만든다. 단어길이의 제한을 문제에서 살펴본다. => 각 가사 단어의 길이는 1 이상 10,000 이하로 빈 문자열인 경우는 없습니다.
    ## => trie구조(사실상 root갯수)를 애초에 10000개를 만들어놓고, 길이-1에 매핑해서 사용한다.
    #### root만 객체 생성하고, 자식객체들은 내부 children link에 생성되어 연결되어있다.
    trie_roots = [TrieNode() for _ in range(10000)]
    ## 3. 또한, trie는 start_with밖에 처리하지 못하기 때문에, 뒤에 앞에??? 뒤에 단어가 존재하는 경우는 검색못한다
    ## => word를 뒤집어서 insert하고, search하는 reverse용 trie를 만들어두면 된다.
    re_trie_roots = [TrieNode() for _ in range(10000)]

    ## 4. 각 단어들을, 단어길이에 맞는 root node에 insert시키기,
    for word in words:
        trie_roots[len(word) - 1].insert(word)
        ## 거꾸로도 학습시키기
        re_trie_roots[len(word) - 1].insert(word[::-1])

    ## 5. query를 통해 단어갯수 반환받기
    answer = []
    for query in queries:
        ## 만약, 첫글자가 ?로 시작한다면, query를 뒤집고 -> revserse trie 학습시킨 것을 사용한다.
        if query[0] != "?":
            count = trie_roots[len(query) - 1].search(query)
            answer.append(count)
        else:
            count = re_trie_roots[len(query) - 1].search(query[::-1])
            answer.append(count)

    print(answer)
