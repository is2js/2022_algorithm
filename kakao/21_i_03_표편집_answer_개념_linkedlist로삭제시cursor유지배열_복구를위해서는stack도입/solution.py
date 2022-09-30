import sys 
 
input = sys.stdin.readline 
 
 
if __name__ == '__main__': 
    ##표 편집:https://school.programmers.co.kr/learn/courses/30/lessons/81303
    n, k = map(int, input().split())
    cmd = []
    for _ in range(9):
        cmd.append(input().strip())

    #### 개념
    # -> cursor를 직접움직이는게 아니라, cursor는 복구된다고하더라 value에 해당하는 객체를 가리키도록 유지해야한다.
    # => 삭제하며 cursor유지하는 배열은, cursor + linkedlist: removed필드(prev/next)로 관리한다.
    #    복구(undo)까지 되려면, stack을 추가해서 관리한다.

    #### 설명
    # => 삭제/삽입시 cursor가 유지되는 문제는 node를 정의하고 linkedlist(prev, next, remove)를 정의해서 풀 것이다.
    # (1) 초기화시 for문을 돌면서 prev / next node를 연결해야한다. 처음 0번node는 head라는 특이점 객체를
    # https://raw.githubusercontent.com/is3js/screenshots/main/image-20220927230220513.png
    # => 특정node는 indexing이 아니라 prev/next link를 타고 들어가게 한다
    # (2) 초기 cursor는 어차피 변수로 초기화해야한다 curr = 2
    # (3) 삭제를 처리할 때는, removed필드에 True를 준다(next/prev는 유지되는데, 건너띄기 때문?에 희미하게 색칠해둠)
    # : https://raw.githubusercontent.com/is3js/screenshots/main/image-20220927230702789.png
    # (4) 직전 복원하려면, stack이 어차피 필요하다. 삭제node는 removed True뿐만 아니라 pop해서 stack에 넣어둔다.
    # : https://raw.githubusercontent.com/is3js/screenshots/main/image-20220927230827146.png
    # (5) 삭제되는node는, pop되기 전에, prev/next를 옮겨줘야한다.
    # : https://raw.githubusercontent.com/is3js/screenshots/main/image-20220927231013311.png
    # (6) cursor는 다음node를 가리키도록 직접 바꿔줘야한다.
    # : https://raw.githubusercontent.com/is3js/screenshots/main/image-20220927231047408.png
    # (7) 삭제 이후 이동은, 삭제시 건너띄고 이어준 prev/next로 link이동마다 +1칸씩 움직이는 것으로 친다.
    # => 삭제시 link를 업데이트 해놓으면, 이동시 알아서 자리를 찾아간다
    # : https://raw.githubusercontent.com/is3js/screenshots/main/image-20220927231204582.png
    # (8) 또 삭제를 만나면 [1] removed True마킹 [2]stack push [3] link 업데이트 [4] curr 다음node
    # : https://raw.githubusercontent.com/is3js/screenshots/main/image-20220927231252524.png
    # (9) 마지막행 삭제를 만날때만 [1] removed True마킹 [2]stack push [3] link 업데이트 [4] curr 이전node
    # => curr가 가리키는 node만 달라진다.
    # => linke 업데이트시, next는 null을 가리키게 해야한다.(시작은head?)

    #### 복원은, stack기준으로 마지막에 들어온 것부터 처리한다.
    # (1) stack pop -> (2) 해당node의 removed False
    # (3) link살려주기
    #### => prev를 타고가서 next를 복구된놈 다음 -> 복구된놈으로 바꾼다
    ####    next를 타고가서 prev를 복구된놈 이전 -> 북구된놈으로 바꾸도록 업데이트

    #### 정답을 낼 때는
    #### for문으로 index를 돌면서, removed가 True면 X를 쓰면된다.


