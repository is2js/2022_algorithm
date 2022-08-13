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


