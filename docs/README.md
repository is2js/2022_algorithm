## 2022 알고리즘 풀이 폴더

## 학습 세팅
- [Algorithm) Pycharm 알고리즘 풀이 세팅 • Jul 7, 2022](https://blog.chojaeseong.com/python/algorithm/pycharm/boj/batch/input/output/2022/07/07/pycharm_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98_%ED%92%80%EA%B8%B0_%EC%84%B8%ED%8C%85.html)

- `sol.bat`
    - `./sol.bat bj[pg|lc|cpt] 폴더명`
    - `./sol.bat reset`
    - 예시
        ```shell
        # backjoon/101/Solution(heap).py + input, output.pxt 백업
        ./sol.bat bj 101 heap 
        
        # programmers/101/Solution.py + input, output.pxt 백업
        ./sol.bat pg 101
        
        # leetcode/101/Solution(heap).py + input, output.pxt 백업
        ./sol.bat lc 101 heap
        
        # concept/101/Solution.py + input, output.pxt 백업
        ./sol.bat cpt 101
        ```
      
### 나만의 규칙
1. 배열 중 원소를 2개 이상 뽑아서 case를 만든다면 `순열 or 조합`문제다
   1. 만약, 조합 문제인데, 2~3개만 뽑아도 된다면, `투포인터` 문제다
   2. 조합과 투포인터 문제는 순서와 무관하니, 필요시 미리 정렬해놓고, `주어진 순서가 고정이라고 생각`하고 문제를 푼다

#### bit를 이용한 부분집합 원소 포함여부 + 상태비트
1. bit관련 암기사항
   1. `if bit & 1 leftshift 자리수`는 bit속 해당자리 수가 불 들어왔으면 true를 반환해준다.
      -`if bit & 1`은 bit의 0번째 자리수가 불 들어왔는지 확인 -> 1의 갯수 직접 셀 때, >>1업데이트하면서 검사할 때 사용
   2. `bit & ~(1<<자리수)`는 자리수만 0을 만들고 &로 죽여 -> 해당자리수 원소를 제외시키는 bit로 update
   3. `bit | (1<<자리수)`는 자리수만 1을 만들고 |로 살려 -> 해당자리수 원소를 포함시키는 bit로 udpate
      - 상태배열 대신 상태비트로 사용하는 경우, `0`을 0000이라 생각하고 초기값을 시작
      - 사용 확인 시 `if bit & (1<<자리수)`로 확인 
      - 포함 시킬 시 `bit | (1<<자리수)`로 1로 살리기
      - 배제 시킬 시 `bit & ~(1<<자리수)`로 0으로 죽이기


### 재귀를 태우는 이유
1. 정해진 횟수만큼 인자를 바꿔 업데이트할 수 있으며(n, cnt, 상태값 초기인자 -> 종착역에서 제한)
   - [재귀의 초기인자 = 반복문위 가변변수 초기화] -> 재귀의 파라미터 -> 반복문의 가변변수 업데이트
2. 현재상태를 가지고 다음 연산시 여러 경우의 수(case)를 다뤄야하는 경우,
   - case별 업뎃된 인자을 넣은, 여러 개의 다음재귀를 호출하여 동적트리순회가 가능하며
   - 자식진입 전, 전역변수를 건들이지 않으면 서로 독립인 상태로 업데이트된 인자로 다음 연산을 이어간다
   - 최초자식진입 전, 마지막 자식진입후에는 자식들을에 대한 처리를 해줄 수 있다
3. 전역변수에 마킹 등 응답값이 없는 행위도 가능하지만,
   - 정해진 횟수동안 업데이트되는 인자에, 누적결과값을 넣어서
   - 재귀함수 정의부 내부에서, 자식으로부터 최종반환 받아, 집계하거나 활용할 수 있다.
   - 이 땐, 종착역에서 누적결과값 반환 -> 자식들이 빽하며 반환
   - 자신의 끝처리에 반환해야, 자식들도 자신의 마지막에 반환하게 된다.

#### 순열탐색 재귀
1. solve( cnt0, used_bit0 (,result0))
2. 다음 case만큼 독립적인 재귀(상태값을 들고다니는)를 호출하면, 그만큼 node로서 경우의 수 가 생긴다.
   1. 반복문으로 재귀를 호출하더라도, 그만큼 node가 생김을 인지하자. 
3. 자신의처리가 없이, 반복문부터 시작하는 재귀는
   1. root node없이 case별 node가 1번 node가 되는 것이다.
4. 보통 다음재귀호출 순서 or 반복문내 i번재 재귀 -> 배열의 i번재 인덱싱후 인자에 반영하여 [재귀호출순서 <-> 요소선택]을 매핑한다.
   1. 만약, i번째 다음재귀를 건너띈다면, 요소선택도 없고, node도 못뻗게 된다.
5. result변수 누적연산식은, 초기값을 넣어놓고 첫번째 뽑힌값과 연산하여 -> 첫번째 나온값이 나오도록 짜면 쉬울 것 같다.
   1. 다 짜면, 초기값 대신 직전까지의 old_result인 파라미터 result로 대체한다

```python
# permutation(cnt, used_bit, result)
permutation(0, 0, 0)

def permutation(prev_cnt, used_bit, prev_result):
    if prev_cnt == 2:
        return prev_result
    aggregator = float('-inf')
    for index in range(N):
        if used_bit & 1 << index: continue
        result = permutation(prev_cnt + 1, used_bit | 1 << index, prev_result * 10 + numbers[index])
        aggregator = max(aggregator, result)
    return aggregator
```

#### 조합 완전탐색 재귀
1. solve(prev_cnt, prev_position, prev_result)
2. 자신의 처리없이 반복문 or 다음호출재귀 여러개 호출하낟면, root node없이 그만큼 node로 시작하는 것
3. 순서가 중요치 않기 때문에, 주어진 순서의 첫번째 원소부터 `선택node vs 선택X node` 2개 node로 출발해나가며
4. 한번 쳐다본 원소는 back해서 다시 확인하지 않기 때문에 position변수는 무조건 증가한다.
   - 현재 position의 요소를 선택하는 경우 `cnt+1, result 파라미터 업뎃` vs 선택 안하는 경우 `cnt그대로, result그대로`
5. 순열과 달리, 선택안하고 무한정 뻣어나가다가, cnt를 못채우고, position만 증가할 수 있는 완전 탐색이다.
   - 그로 인해, 종착역 조건이 position검사 추가되며, 종착역에선 결과값이 아닌, 집계시 없어질 값으로 반환한다.

```python
# solve(prev_cnt, prev_position, prev_result)
combination(0, 0, 0)

def combination(prev_cnt, prev_position, prev_result):
    if prev_cnt == 2:
        return prev_result
    if prev_position == N:
        return float('-inf')
    selected = solve(prev_cnt + 1, prev_position + 1, prev_result + numbers[prev_position])
    unselected = solve(prev_cnt, prev_position + 1, prev_result)
    return max(selected, unselected)
```

#### 조합 대신 투포인터 (2~3개 조합까지)
1. 순서가 중요하지 않기 때문에 주어진 배열의 순서를 하나씩, 조합처럼, back하지 않고 탐색한다.
2. start, end index를 가변변수로 정해놓고 while start < end로 만나기전까지 반복한다.
3. while 업데이트시 start를 올려야할지, end를 내려야할지 판단하기 위해, 주어진 것을 미리 오름차순 정렬해놓는다.
4. 조합문제로서, 순서중요X한 합이나 곱의 문제일텐데, if 요구사항에 맞춰 정답에 가깝도록: start +=1 else: end -=1로 하나를 업데이트해서 탐색한다.
5. 만약 3개를 뽑는 조합문제면
6. 1개는 반복문으로 돌리면서 고정해놓고, 나머지 2개를 투포인터로 돌리되, 반복문의 범위는 최대 2개포인터가 마지막에 1개씩 위치한 len()-2까지 돌아가야한다. 

#### composite객체의 재귀는 root부터가 아니라 root의 자식들부터
- **재귀함수를 정의할 때 고려해야할 것은**

  1. 다음stack결정변수 

     1. 값이라면: cnt(0)-> cnt+1, n->n-1

        - 종착역 if cnt == 2, n == 1 등

     2. **연결된 객체라면:** 

        1. 객체 -> `객체 = 객체.next`, 
        2. **객체 -> `반복문속 자식객체`,** 
        3. 외부에서 사용한다면 `객체.재귀메서드() -> 다음객체로 업뎃 -> 다음객체.재귀메서드()`

        - 종착역 
          - if  객체 == 시작특이점객체
          - **아예 자식객체가 없어서 반복문 x -> 다음재귀 호출x**
            - **반복문속의 자식객체.재귀호출()는 종착역이 따로 필요없다**

  2. 필요정보 변수(전역변수면 노상관이지만 객체에선 x)

  3. 계속 업데이트되는 가변변수

  4. 연산식을 직접 적어서 업데이트하는 누적결과값

- 반환값을 자기는 재귀
  - 종착역반환 -> 자식재귀 반환 -> 재귀정의부 반환 -> 외부에 반환


#### 단일 연결리스트 prev데코 객체
1. prev객체는 new node만 필드로 유지될 예정이다. 
   - 기존 객체와의 연결은, 새 객체의 prev필드에 넣어서 생성하면, 따로 연결해줄 필요없다.
2. 구간처리
   ```python
   # 구간별 데이터 처리 -> target_data가 내 구간에 안들어오면, 전체 구간의 누적연산 기본값 반환
   #######
   # (1) 직전구간의 to를 from으로, (2) 나의 to를 끝구간으로
   # [1] 직전 구간이 없는 시작특이점 객체거나, 내 lower bound커야한다.(작거나 같으면 내구간 아니다)
   # lower_bound = self.prev.to
   # if not self.prev or target_data <= lower_bound: return 0
   # [2] target_data에 따라서 처리구간이 내 구간의 중간으로 짤리는지, 내 구간전체를 넘어가는지 확인한다.
   # upper_bound = self.to if target_data > self.to else target_data
   # target_section = upper_bound - lower_bound
   # return target_section * money
   #######
   ```
#### 이중 연결리스트 prev, next데코객체
1. node객체는 data필드를 제외하고, prev, next는 default None의 kwargs로 정의한다.
2. list객체는, head와 tail필드를 시작/끝 특이점객체로 초기화하도록 정의하고, node_count는 0으로 초기화해서 생성한다.
   1. 특이점node객체는 data필드 position args None으로, prev/next는 default로 None으로 생성
   2. count가 있어야, 전체 repr(순회)시 0개시 / get구현시 index 순회의 끝값인 len값 / insert 등이 쉬워진다.
3. `append_left`메서드부터 구현한다. node의 data값만 받고, 관리객체는 내부생성한다.
   1. 이중연결리스트는 head, tail을 가지고 있으므로, append_left라도 insert와 유사하다
      1. `이전node`(self.head)에 위치한 상태에서
      2. 이전node의 next필드를 통해 -> 이동당할 `다음node`를 챙겨놓는다.
      3. 챙겨진 양 옆의 node를 바탕으로 `가운데 new node`를 생성할 때, `prev=, next=`필드에 `챙긴 2객체`를  채워넣는다.
      4. 생성된 `new node`를 양 옆 객체들의 필드(`이전node.next = 다음node.prev` = new node)를 동시할당해주면 연결된다.
   2. 만약, head.next에 챙길 객체가 없다면, head와 tail사이이고, `미리 2개의 node를 챙겨놓을 필요가 없`이 바로 생성에 head, tail을 사용하여 연결까지한다.
   3. node_count를 올린다.
4. **아래 delete를 만드는 방식대로, append_left에서 `요소가 없을 때(next인 tail안챙김)` vs `요소가 있는 상태 add(다 챙김)`의 로직 중, 내부context를 파라미터화 하여, 중복코드를 제거한다**
   1. 중복 제거할 때는, `특수한 경우, 내부context를 쓰는 로직`을 추출 -> 내부context를 파라미터로 추출 -> 인자 대입 -> 다른 경우에도 사용
5. append류 개발과 함께 증감하는 self.node_count필드를 이용하여 `__len__` -> `__repr__`를 구현한다
   1. sections의 repr은 seciton의 repr부터 구현하고 온다.
   2. 시작을 data node로 하기 위해 curr = .next로 잡고 -> while에서 curr.next를 치니 최소 1개 이상 연결되어야한다는 말이다.
      1. node_count를 통해 empty string을 return하는 예외처리를 해주자.
   3. `while curr_node.next`를 통해, next가 None인 특이점객체를 거를 수 있으면서 data가 있는 node만 돌지만
   4. while 내부에서 `if curr_node.next.next` -> 다음 것의 필드를 조회하여, `다음객체(curr_node.next).next필드의 존재유무`를 검사할 수 있다.
      1. if 현재.next필드검사 -> 끝 특이점객체 거르는 검사
      2. **if 현재.next.next필드검사 -> 끝 특이점객체 바로 직전의 data node거르는 검사**
      3. **`if not 현재.next.next필드`검사 -> 끝 특이점객체 바로 직전의 data node를 선별하는 검사**
6. `append`메서드를 구현한다. left와 반대로 끝이 tail로 고정이라 미리 안챙겨도 된다.
   1. tail.prev 챙길 객체가 없다면, head와 tail사이이고, `미리 2개의 node를 챙겨놓을 필요가 없`이 바로 생성에 head, tail을 사용하여 연결까지한다.



6. `insert`등을 구현 하기 전 index를 통한 순회가 반복될 것이므로 `내수용 self.get()`을 먼저 구현해놓는다.
7. `get(index)`을 구현한다.
   1. index 검사 -> len//2 기준으로 head출발 vs tail출발 순회하여 index번째 요소를 반환한다.
8. `insert(index)`를 get()를 활용해서 구현한다
   1. 인덱스 검사하되, len index를 허용해야한다. append개념은 len index입력이다.
   2. 0에 insert는 append_left / len자리  insert는 apppend를 재활용한다
   3. get()으로 이전 node를 찾고, 필드에서 다음node까지 챙긴 다음 -> 챙긴객체로 curr를 만들고 -> 연결한다
9. `popleft()` ->`pop()` -> get(index)이용 -> `remove(index)`를 구현한다
    1. insert는 len index도 허용이지만, remove는 0~len-1검사이다.
   


10. `delete`메서드를 구현한다. index가 아닌 `data(unique해야할 것이다)로 삭제`해보자.
    1. 순회 전, 존재유무 검사를 먼저 한다
    2. 순회하면서, data를 가진 curr를 못찾으면 continue, 찾으면 `curr를 바탕으로 3개의 node를 필드로부터 챙긴 뒤 -> 삭제할node를 빼고 서로 연결한다.`
        - 이 때, `(1) 첫요소 삭제 (2) 마지막요소 삭제 -> 끝+curr로 2개 자동챙김 -> curr로 1개만 챙김 (3) 중간 삭제 -> curr로부터 양옆 2개챙김`의 로직이 달라진다.
        1. `필드에 해당 data를 가진 curr`를 순회(바텀업)해서 먼저 찾는다.
        2. head에 붙은 것은 prev를 안챙겨도 되니, head + curr로 next를 챙겨서 삭제한다.
        3. tail에 붙은 것은 next를 안챙겨도 되니, curr + tail로 prev를 챙겨서 삭제한다.
        4. **중간 삭제는 위 `2가지 방식을 메서드화` by `안챙겨도 되는 내부context을 변수로 챙기도록`추출한 뒤, 둘 중에 1개 메서드를 재활용한다**
           1. delete_with_prev( self.head, curr) -> delete_with_prev( curr.prev, curr)로 중간삭제를 만들면 된다.
           2. tail을 삭제하는 방식으로 하려면, delete_with_next(curr, self.tail) -> delete_with_prev(curr, curr.next)로 중간삭제를 만들면 된다.
11. `update(data1, data2)`를 구현한다.
    1. delete에서 쓰인 `순회 전 empty검사` + `처음부터 돌며 curr찾기`를 메서드화해서 재활용한다
    2. 필드 속 데이터만 바꾸니까.. 할당으로 간단하게 처리하고 반환한다.
    3. 객체를 꺼냈으면, 수정만 하면 알아서 컬렉션, linkedlist에 반영되어있을 것이다.

12. 2개의 linkedlist를 `연결`해주는 `concat`을 구현한다.
    - left의 prev로 마지막요소를, right-head의 next로 첫요소를 챙겨서 삭제될 것은 놔두고 양옆을 연결하면 된다.
    - concat의 결과 요소갯수의 변화가 잇으니 node_count를 업뎃해줘야한다.

13. 전체 순회하여 요소들만 `list로 뽑아서 처리하여 반환`해주는 것들인, `traverse` + `reverse`를 먼저 구현한다
    1. 그냥 첨부터 끝까지 순회하며 요소만 뽑는  repr 메서드를 복사해와서 참고한다.
    2. traverse -> reverse 구현한다. `list로 요소들을 반환`한다.

14. traverse를 통해 얻은 list로 `내장sorted를 활용`하여 + `새로운 linkedlist를 만들어 반환`해줄  `sorted`을 구현한다.
    - sorted는 `traverse`이 반환하는 list  +  `내장sorted`를 활용하여, key와, reverse여부를 받는다.
    - 내부에서 sort된 node list를 가지고, 새로운 sections를 생성한 뒤, append해서 만들어서 반환한다.
    - **기존node들로 새로운linked들을 만들 땐, `data만 건네주기`가 되어야한다. append는 node가 아닌 data를 받기 때문에**
15. dd
16. `merge_sorted`는 concat과 다르게, 2개의 linkedlist를 `traverse + 내장sorted`로 `이미 정렬된 2개의 list`를 확보해놓고,
    1. merge_sort 알고리즘 자체가, 이미 오름차순 정렬된 상태에서 비교하므로, 
       1. traverse시 무조건 오름차순으로 list2개를 확보한다
       2. 알고리즘에 의해 result에 작은 순으로 append한다.
    2. merge_sort된 list를 reverse를 줬을 때, list.sort(reverse)로 다 끝나고 마지막에 준다.
    3. list를 앞에서 만든, list로부터 객체를 만드는 정적팩토리메서드(@classmethod)로 linkedlist를 만들어서 반환한다.
