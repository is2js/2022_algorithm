import sys 
 
input = sys.stdin.readline 
 
 
if __name__ == '__main__':
    ## 최대 용량이 정해진 FIFO 큐 클래스 :https://yeahajeong.tistory.com/217
    # 원래 queue는 deque로 구현해서 popleft()를 쓴다 -> O(1) by 양방향 링크드 리스트
    #     stack인 list로 pop(0) -> index에 의존하여 pop하고 0 자리로 1칸씩 땡겨가야하므로 O(N)
    # => stack 2개로 queue를 구현할 수 있다.
    # stack1(1->2->3)에서 pop(3->2->1)한 것을 stack2에 옮겨담으면
    # stack2에는 3-> 2 -> 1로 담긴다.
    # 앞쪽stack의pop순서 -> stack2 입장에서배열탐색의 순서 -> 원래배열의 역순 으로 탐색

    ## redo를 위한 또다른 [undo후 버려지는 것을 최근 것부터 역순으로 복구해서 do]하는 removed stack
    # https://raw.githubusercontent.com/is3js/screenshots/main/image-20220916131835059.png
    # 코드1:cursor로 redo : https://github.com/LenKIM/object-book/blob/a5be03c5087f5b4ef456e048f0700129ee19cd64/object11/src/CommandTask.java
    # 코드2: removed stack추가로 redo: https://github.com/imcts/code-spitz/blob/64cf34a914ddf1883e08a7c6b52fa318ee2dd147/codespitz84/src/listen4/command/CommandTask.java
    # -> removed에서 pop시 최근것부터 뽑아와야하는데 removed(0)오타인듯?

    ## undo / redo -> 직전 것부터 역순으로 카운터치고 싶어, 실행시마다 append하고 시행(확인하고 append X 들어오는 대로 append)
    stack = []
    removed = []
    stack.append('A')
    stack.append('B')

    ## 원래 최근순으로 undo하면, stack에서 pop해서 가져와서 쓰므로 사라진다.
    print(stack)
    # ['A', 'B']
    # B
    # ['A'] []

    # undo
    prev = stack.pop()
    print(prev) # undo: 다음 것 가기 전에 직전것을 stack에서 pop해와서 카운터
    # pop해온것으로 카운터치는 동작 생략
    print(stack, removed)



    ## redo도 하려면 pop해온 것을 카운터 친 뒤, removed에 저장해놓기
    removed.append(prev)
    print(stack, removed)
    # ['A'] ['B']


    ## redo
    # ['A'] ['B']
    # next = removed.pop(0) # redo : 직전에 undo로 버려진 것을 다시 실행하고 stack에 쌓는다.
    next = removed.pop() # redo : 직전에 undo로 버려진 것을 다시 실행하고 stack에 쌓는다.
    # removed에서 pop해온 것으로 do하는 과정 생략
    stack.append(next)
    print(stack, removed)
    # ['A', 'B'] []



    #### 2번을 undo하고 2번을 redo해보기
    # ['A', 'B'] []
    # B가 undo되었습니다.
    # ['A'] ['B']
    # A가 undo되었습니다.
    # [] ['B', 'A']
    # A가 redo되었습니다.
    # ['A'] ['B']
    # B가 redo되었습니다.
    # ['A', 'B'] []
    prev1 = stack.pop()
    removed.append(prev1)
    print(f'{prev1}가 undo되었습니다.')
    print(stack, removed)

    prev2 = stack.pop()
    removed.append(prev2)
    print(f'{prev2}가 undo되었습니다.')
    print(stack, removed)



    next1 = removed.pop()
    print(f'{next1}가 redo되었습니다.')
    stack.append(next1)
    print(stack, removed)


    next2 = removed.pop()
    print(f'{next2}가 redo되었습니다.')
    stack.append(next2)
    print(stack, removed)





