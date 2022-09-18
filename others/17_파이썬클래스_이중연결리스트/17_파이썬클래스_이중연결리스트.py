import sys

input = sys.stdin.readline


class Section:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class Sections:
    def __init__(self):
        # [2] prev데코객체를 사용하는 class는 self.head로서 시작특이점을 가지고 태어난다.
        # -> 실제 실무 구간처리를 위해서는 to값를 기억해놓고, 직전node의 to값을 현재node을 from으로 잡으므로
        # -> 시작특이점 객체가 필요하다.
        self.node_count = 0
        self.head = Section(None)
        # [2-2] 추가적으로 next데코객체 역할도 하려면, 알아서 add시 마지막이 끝 특이점객체(next필드 None)가 되므로
        #       객체는 필요없었지만, 이번엔 마지막도 연결(.prev와)되어야하므로
        #       끝 특이점 객체도 함께 만든다.
        self.tail = Section(None)

    def append_left(self, data):
        # [4] add시 먼저, head뒤에 실제 요소가 있나 본다.
        # -> 첫 결합의 형태라 [챙겨서 끊고 맺음]이 없는 특이구조니 확인한다
        #    + 바로 head.next , tail.prev에 넣어주기만 하면 된다.
        #    + node를 생성할 때, .next나 .prev의 인자도 없이 생성된다.
        # -> 방향 연결리스트는 add시 아무것도 없을 때를 체크하여 head와 tail 어디에 붙는지 양쪽 다 생각한다.
        if not self.head.next:
            # head뒤에 tail제외 아무것도 붙은게 없다면, 첫 요소는 head와 tail 둘다 붙는다.
            self.head.next = self.tail.prev = Section(data)
            # 이전node의 next필드 + tail쪽 다음node의 .prev까지 다 챙겨야한다.
            self.node_count += 1
            return self.head.next
        # [5] 만약, head담에 뭔가가 있는상태에서 생성해서 끼워넣는 것이라면
        # -> popleft에서는 prev=는 self.head가 고정이며
        # -> next는 0번째 있던 요소이다. 객체 정보는 이전node의 next필드에서 찾을 수 있다.
        # -> 0번째 자리는 self.head.next를 덮어쓰는 것이므로, 그이전에 챙겨놨다가 활용한다.
        next = self.head.next  # (1) 이전node필드 덮어쓰기 전에 챙기기
        # python에서는 똑같은 것 할당을 동시에 할 수 있음.
        # next.prev = self.head.next = Section(lst_2d, prev=self.head, next=next)  # (2) 새node에 챙긴 것 활용
        section = Section(data, prev=self.head, next=next)
        self.head.next = section  # (2) 새node에 챙긴 것 활용
        next.prev = section
        ## 다음node은 다음node입장에서 .prev만 생각한다.
        # (3) 다음node.prev(head) 덮어쓰여지지만, 안챙겨도, [시작점이 필드값에 self.head]로 있어서 append_left시에는 안챙겨도 된다.
        # next.prev = self.head.next
        # [6] 추가할때마다 컬렉션클래스(Sections)는 사이즈를 조회 찾기보다는
        #    컬렉션단위라서 객체들을 관리한다면, 클래스 변수에 챙겨놓자
        # -> .size()를 제공할 수 도 있게 된다.
        self.node_count += 1
        return self.head.next

    # [7] append_left시 추가한 node갯수 필드를 조회할 수 있 size()메서드를 바로 정의해주자.
    # -> python이라면, 사실 len+gettiem을 구현해야할 것이다.
    def size(self):
        return self.node_count

    def __len__(self):
        return self.node_count

    # def print_section(self):
    # [20] 출력방식은 외부에서 값context로 건네줄 것이다. -> 안주면 기본값 false
    def print_section(self, reverse=False):
        # [21] reverse를 주었다면, tail부터 출력하면 된다.
        count = 1
        if reverse:
            curr = self.tail.prev
            # 시작특이점 객체 있으므로 필드로 검사한다.
            while curr.prev:
                if count == self.node_count:
                    print(f"{curr.lst_2d}")
                    break
                print(f"{curr.lst_2d}", end=" ")
                count += 1
                curr = curr.prev
            return
        curr = self.head.next
        # data가 없는 tail이라는 끝 특이점 객체가 존재하므로
        # -> while문의 기준을 객체로두면, 시작특이점 객체
        # -> 그 전까지 가려면, self.node_count를 확인하면 될 것 같다.
        # for row in range(self.node_count):
        #     print(f"{curr.lst_2d}", end=" ")
        #     curr = curr.next
        # => data가 없는 끝 특이점(tail)이 존재하면, 그것만 .next가 null이기 때문에
        #    while문을 필드검사한다.
        while curr.next:
            # print(count, self.node_count)
            if count == self.node_count:
                print(f"{curr.lst_2d}")
                break
            print(f"{curr.lst_2d}", end=" ")
            count += 1
            curr = curr.next
        # print(f"({self.node_count}개)")
        # [19] reverse 프린트 가능하게 하게

    def append(self, data):
        # [11] append_last와 마찬가지로 첫요소는 특이점들 사이에 처음 들어오므로
        # -> 첫 결합의 형태라 [챙겨서 끊고 맺음]이 없는 특이구조니 확인한다
        #    + 바로 head.next , tail.prev에 넣어주기만 하면 된다.
        #    + node를 생성할 때, .next나 .prev의 인자도 없이 생성된다.
        # -> 마지막에 더하는 것이므로 tail에서 .prev로 확인한다.
        if not self.tail.prev:
            self.head.next = self.tail.prev = Section(data)
            self.node_count += 1
            return self.tail.prev
        # node가 존재한다면, 마지막요소 <-> tail간의 중간삽입이다.
        # [기준 중에 하나인 tail]에서 시작하여,
        prev = self.tail.prev  # (1) 이전node(tail)필드 덮어쓰기 전에 챙기기
        # (2) 활용하여 객체 만들기 -> 여기서도 이전node.next필드는 챙길필요없이 sefl.tail로 바로 갖다쓰면 된다.
        section = Section(data, prev=prev, next=self.tail)
        # (3) 원래는 챙겨야하지만, 필드에서 갖다쓰므로 덮어쓰면 된다.
        prev.next = section
        # (4) tail(바뀐자리의 양쪽 챙김필드?)의 prev를 업데이트 안해줬다...
        self.tail.prev = section
        self.node_count += 1
        return section

    def delete(self, data):
        # [13] 일단 시작은 self.head를 기준으로, 한칸 next한 0번째 원소다.
        # -> [연결된 것들의 차례대로 접근 처리] = 지역변수 + 반복문
        curr = self.head.next  # 이 행위를 통해 나는 do -while을 안써도 되게 된다.
        # my) 삭제 전에 존재검증을 해야하는데, 그것 또한 반복문이라서
        # -> 다 돌아서 찾다가, 반복문 다돌았는데 없으면 탈락 처리하면된다.
        # 0번째요소부터 방문하면서 데이터를 검증할 건데
        # 끝특이점만 .next가 Null이므로 while 객체.next로 검사한다.
        # while curr.next :
        #     curr = curr.next
        while curr.next:
            # [14] 데이터를 발견했다면 -> 처리하고 return해야한다. 반복문 빠져나가면 못찾은 것으로 설정
            #                       -> while문에서는 공통 업뎃문이 있기 때문에 early continue는 업뎃문반복할 거아니면 못쓴다.
            # 여기서 다르면 early continue하고 싶지만, 공통업뎃문이 존재해서..
            # -> 찾으면 break이므로 공통없뎃문이 아니네?!!
            if curr.lst_2d != data:
                curr = curr.next  # 업뎃문 + continue -> 아닌 경우에는 break라서 가능
                continue
            # [16] 데이터가 head vs tail  vs 중간에 있는 것에 따라 처리가 또 달라진다.
            # (1) head에 붙은 놈일 경우,
            if curr == self.head.next:
                # 필드없어쓰기 전에 보존할 것?? -> 삭제할놈의 위치가 담긴 주소 -> curr에 담김
                # 사라지는객체의 필드들 curr.next -> 챙겨야함.
                # 덮어써질 필드들 = self.head.next -> curr라 챙길필요없음
                # => 삭제는, 이전node의 필드는 챙길필요없고, 사라질놈 속 next필드를 챙긴 뒤, 이전node의 next에 넣어준다.
                next = curr.next

                next.prev = self.head
                self.head.next = next
                # next를 챙겼으면 prev도...
                # next.prev = self.head
                # => 정리 (1) 삭제할놈의 .next 챙김(기준과 반대방향) -> 이전node.next로 연결 + (2) 챙긴next의 .prev -> 이전node를 넘음
                self.node_count -= 1
                return curr
            # (2) tail에 붙는 놈일 경우
            if curr == self.tail.prev:
                # (1) 삭제할놈의 .prev챙김
                prev = curr.prev
                # next = curr.next # 기준점이라면 안챙김
                # (2) 삭제할놈은 변수상태니 놔두고, 연결부터
                prev.next = self.tail
                self.tail.prev = prev
                # (3) 챙긴prev객체의 .next 연결
                # prev.next = self.tail

                self.node_count -= 1
                return curr
            # (3) 중간 것을 삭제하는 경우 -> 기준필드를 바로 못쓰니 챙길게 많다
            # => 중간 삽입/삭제시, 연결이 완전히 끊기는 경우를 조심하자!
            # (1) 삭제할놈의 .prev 먼저 챙김 -> 챙김node.필드에 [삭제될객체curr.다음챙길필드]를 연결
            # prev = curr.prev
            # (2) 챙기자마자 챙긴것.필드에 [삭제될놈.다음챙길반대방향필드]에서
            # prev.next = curr.next
            # (3) 삭제할놈의 .next챙김
            # next = curr.next
            # (4) 챙김node.필드, 기존에 챙긴 것 연결
            # next.prev = prev

            # 다시정리) 삭제될놈 필드 챙겨놓기 -> 챙긴node의.반대필드에 = 객체연결(주로 반대에서 챙긴 것)
            # -> 안전빵으로 처리하면, inline할게 보인다
            curr_prev = curr.prev
            # curr_next = curr.next
            # curr_prev.next = curr_next # 필드 대입은 위치값만 기억시키니, 손상걱정x
            curr_prev.next = curr.next  # inline ( \ 형태이며, 중간에 트랜잭션x)
            # curr_next.prev = curr_prev # inline으로 사라진 변수를 쩜으로..
            # => 이 경우, 사라진 변수가 중간에 타격 안변해야함.
            #    그래야 필드로 찾아가서 대입하는것을 그대로..
            curr.next.prev = curr_prev

            ## 강의 정리
            # t = curr.prev # 이전node를 뽑은 뒤,
            # t.next = curr.next # 이전node의 next를, 삭제할node의 next(객체)를 가리키게한다.
            # 현재node는 이제 삭제한다.(삭제할node의 next, prev 필드 다 사용)
            # del n
            # 나머지 연결안된 변수를 node와 연겨랗ㄴ다.
            # t.next.prev = t

            # 갯수 변화 주기
            self.node_count -= 1
            return curr
        # [15] 다돌앗는데도 해당 데이터가 없다면 -> 에러내야한다.
        raise RuntimeError("no lst_2d")

    def insert(self, index_, data):
        # [17] index 범위 검사 with nodeCount
        if index_ < 0 or index_ > self.node_count - 1:
            raise RuntimeError("invalid index")
        # -> 이부분은 append_left와 append와도 관련된다.
        # 0에 삽입은. 사실상 append_left()이다.
        # => insert는 append_left, append 구현후, 재활용한다.
        if index_ == 0:
            # print("insert 중 index 0은 append_left()로 대신한다.")
            return self.append_left(data)
        # if index_ == self.node_count - 1:
        # => insert란...
        # => 01 -> len 2 -> insert1로는 맨마지막에 넣는 것x inesrt 2여야한다. 갯수랑 같아야한다.
        # => 012 -> len 3 -> 갯수랑 동일한 index가 와야 맨 마지막에 append와 동일하다
        if index_ == self.node_count:
            # print("insert 중 index == n-1은 append()로 대신한다.")
            return self.append(data)

        # indexing시 기본적인 기준은 tail이 아니라 head로 시작한다.
        # (원래는 중간에서 더 가까운 순으로 해야할 듯 -> 찾아보기)
        curr = self.head
        # [18] insert기본은 for문으로 횟수반복하여 i-1까지 와서 이전node로 처리한다.
        # -> 0부터 증가하니 index - 1까지 오면 된다.
        # for row in range(index_ - 1):
        for _ in range(index_):
            curr = curr.next
        # (1) 삭제될놈처럼, 현재자리에 있는 놈의 정보를 챙겨놓는다.
        # -> 이전node에 시작하므로 현재자리 객체부터 만든다.
        next = curr.next

        # prev = next.prev next의 prev또한, curr이므로 챙길 필요없다??
        # next node의 next는 챙길필요없다.
        # => 이전node로 왔으면, 이전node의 필드인, next객체만 챙겨놓자
        section = Section(data, prev=curr, next=next)
        curr.next = section
        next.prev = section

        self.node_count += 1
        ## 강의 정리
        # t = Section(lst_2d, next=curr.next)
        # -> 일단, 현재.next로 next필드만 채운 상태로 새로운 node를 생성한다.
        # t.prev= n -> 생성후 prev필드를 현재node로 채운다.
        # t.next.prev=t -> 끊어진 node를 앞뒤로 연결한다
        # n.next = t


if __name__ == '__main__':
    ## 이중 연결리스트 -> dequeue구현인듯.
    # -> 시작 특이점객체( for prev데코객체, or head로 접근하는 next연결리스트)
    # -> 끝 특이점객체( for next데코객체에선 자동)
    # head와 tail이 함께  존재해야며, 서로 접근가능해야한다.

    ## node만으로 구현할 수 없다. node를 사용하는 Dlist클래스가 따로 존재해야한다.
    # [1] 일단 생성하면, 시작특이점객체(for prev) + (끝특이점객체는 마지막add하는 것-next필드가 빈 것)
    sections = Sections()
    # [3] 이중연결리스트는 add시, head에 추가(append_left)/ tail에 추가(append) 2가지가 다 가능해야한다.
    # [3-1] 일단 head에 추가하는 방법이다.
    # -> node를 생성해서 넣지말고, data만 넣어서 내부 생성한다.
    sections.append_left("구독")
    sections.append_left("좋아요")
    print((len(sections)))
    # [8] 잘 add되었는지 확인하기 위해 print부터 개발한다
    sections.print_section()

    # [9] node를 추가/수정/삭제할 때 조심해야할 것은, 연결이 끊어지는 순간 GC에 의해 객체가 소멸되므로
    #    -> node간의 연결이 완전히 끊어지지 않게 해야한다.

    # [10] 이제 뒤쪽에 append하는 메서드를 구현해보자.
    sections.append("광고시청")
    print(len(sections))
    sections.print_section()  # 좋아요 구독 광고시청 None (3개)

    # [11] 이렇게 기준이 2(head, tail)개가 있으면, 양쪽에서 빠르게 접근할 수 있다.

    # [12] node삭제는 단일연결리스트는 index기준으로 했는데, 이번엔 data기준으로 비교하면서 한다
    sections.delete("구독")
    sections.print_section()  # 좋아요 구독 광고시청 None (3개)

    # [16] insert구현
    # -> 삭제는 data로만 찾아서, 삽입은 index+ data로 구현한다.
    sections.print_section()
    # 좋아요 광고시청 (2개)
    sections.insert(1, "python") # 1의 자리에 넣는 다는 것은, 01 -> 0   2 사이에 넣는다는 것이다.
    # => 그렇다면, 01 이라면, 2의 자리에 insert하는 것이 append와 동일한 것이다.
    # => 원래 있던 것에 insert하는 것은, 기존 것을 뒤로 1칸 물리는 것
    # => 01 요소가 있는상황에서 insert 1 -> 마지막에 넣는 것 아니다.
    # insert index가 맨마지막과 동일하려면?
    # 01 -> len 2 갯수
    # => 012 -> len 3 -> 갯수랑 동일한 index가 와야 맨 마지막에 append와 동일하다

    sections.print_section()
    sections.print_section(reverse=True)
    # 좋아요 광고시청 python (3개)
    pass
