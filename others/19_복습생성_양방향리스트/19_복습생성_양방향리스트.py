import sys

input = sys.stdin.readline


class Section:
    # data객체를 제외하고, prev, next는 default None의 kwargs로 정의한다.
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        return f"{self.__class__.__name__}({self.data!r})"


class Sections:
    def __init__(self):
        self.section_count = 0
        self.head = Section(None)
        self.tail = Section(None)

        self.head.next = self.tail
        self.tail.prev = self.head

    def append_left2(self, data):
        # 1) 끝에 붙일 때는, 끝의 다음 것이 [필드]를 통해 있나없나 먼저 본다.
        #   -> 끝의 다음게 없으면, 최초라서, [챙김]없이 바로 [양끝의 필드]에 붙여주면 된다.
        # if not self.head.next:
        if self.section_count == 0:
            # 2) 생성되어 붙는 객체는, 생성시 필드로 넣어줄 node를 미리 챙겨놓고 [연결node 대입해서 생성]해야하지만
            #   -> 양옆이 끝이라면, 미리 안챙겨도 된다.
            self.head.next = self.tail.prev = Section(data, prev=self.head, next=self.tail)
            self.section_count += 1  # 요소변화시 카운팅도 하자.
            return self.head.next
        # 3) 원소가 기존에 하나라도 있었더라면, insert의 과정이다. 끝은 따로 안챙겨도 되지만
        #    [이전node위치]에서 시작하며, [이동 당하는node]는 [반대방향필드]를 미리 챙겨놔야한다.
        # (1) [이전node]의 [필드]에서  [이동당하는 start]객체를 미리 챙김한다. -> 이것이 덮어쓰기로 끊어지면 객체는 소멸한다? 그 다음node의prev에 있긴할 것이다.
        next = self.head.next
        # (2) 이전node의 챙김을 당한 필드(연결고리)는 새로운node를 연결하도록 덮어쓰기한다
        #    -> 이 때, 필드로부터 챙겨놓은 객체를 활용해서 새 node를 생성한다.
        # next.prev = self.head.next
        # (3) 이제 챙긴node(이동당하는 start)의 필드를 연결해준다.
        next.prev = self.head.next = Section(data, prev=self.head, next=next)
        # => add라는 것은 [이전node필드 -> 이동당한node(next)챙김 + 이전node]를 통해, new node의 필드에 연결해주면서 생성하고
        #    생성된 node는, 양옆의 [next, prev필드에 동시할당]으로 한번에 정리할 수 있다.
        self.section_count += 1
        return self.head.next

    def append_left(self, data):
        if self.section_count == 0:
            return self.append_left_with_next(self.tail, data)

        return self.append_left_with_next(self.head.next, data)

    def append_left_with_next(self, next, data):
        self.head.next = next.prev = Section(data, prev=self.head, next=next)
        self.section_count += 1  # 요소변화시 카운팅도 하자.
        return self.head.next

    # 4) len 및 repr 구현
    def __len__(self):
        return self.section_count

    def __repr__(self):
        # 밑에서 .next(None).next를 검사하는 순간, 연결된 node가 최소 1개는 연결되어있어야한다.
        # -> head.next부터 시작할때, 0개 예외처리해줬어야한다.  더군다나, .next.next도 있다.
        # AttributeError: 'NoneType' object has no attribute 'next'
        # -> node_count를 통해 0개 일땐, 존재유무검사에 탈락으로서 그냥 emtpy 메세지를 건네주자
        if self.section_count == 0:
            return f"{self.__class__.__name__} is empty."

        information = ''
        curr_section = self.head.next  # head다음 or tail이전인 lst_2d node부터 사용한다.
        while curr_section.next:
            # if 현재.next 검사 -> 끝 특이점객체 거르는 검사
            # if 현재.next.next필드 검사 -> 끝 특이점객체 바로 직전의 lst_2d node거르는 검사
            # if not 현재.next.next필드 검사 -> 끝 특이점객체 바로 직전의 lst_2d node를 선별하는 검사**
            # -> 특이점객체 직전의 객체를 선별하여, 트레일링 콤마를 제외하고 문자열을 더한다.
            information += repr(curr_section) if not curr_section.next.next \
                else repr(curr_section) + ' -> '
            curr_section = curr_section.next
        return f"[{information}]"

    # 5)
    def append2(self, data):
        # if not self.tail.prev:
        if self.section_count == 0:
            self.head.next = self.tail.prev = Section(data, prev=self.head, next=self.tail)
            self.section_count += 1
            return self.tail.prev
        # (1) 이전node에 해당하는 tail을 바탕으로 다음node(prev)를 챙겨놓는다.
        prev = self.tail.prev
        # (2) 챙긴 2개의 객체를 이용해서, 새로운 객체를 생성과 동시에 연결
        prev.next = self.tail.prev = Section(data, prev=prev, next=self.tail)
        self.section_count += 1
        return self.tail.prev

    def append(self, data):
        if self.section_count == 0:
            return self.append_with_prev(self.head, data)
        return self.append_with_prev(self.tail.prev, data)

    def append_with_prev(self, prev, data):
        prev.next = self.tail.prev = Section(data, prev=prev, next=self.tail)
        self.section_count += 1
        return self.tail.prev

    # 7)
    def get(self, index):
        # 순회메서드가 index를 사용한다면, index검사부터 한다.
        self.check_index_range(index)
        # 순회의 기준은 head, tail 2가지다. //2 (홀수면 가운데, 짝수면 0123- (4//2=2) -> 가운데서 오른쪽)
        # -> 짝수로서  가운데보다 오른족index라 생각하고, head(index < 몫) - tail( index >= 몫)으로 시작한다.
        # if index < (self.section_count // 2):
        #     curr = self.head.next
        # else:
        #     curr = self.tail.prev
        if index < (self.section_count // 2):
            curr = self.head.next
            # 단순 횟수 반복은 while이 아닌 for row 문을 이용한다.
            # index 0 -> 0번이동(반복문x) / 1->1번이동이므로, range(n)을 그대로 이용하면 된다.
            for _ in range(index):
                curr = curr.next
            return curr
        # tail기준으로 뒤에서 움직인다.
        curr = self.tail.prev
        # 뒤에서 움직인다면, index는 앞에서 움직이는 것을 기준으로 하므로
        # [0 [1] 2 3] -> 1번 움직일 거, 뒤에선 2번 움직여야한다
        # [0 1 [2] 3] -> 2번 움직일 거, 뒤에선 1번 움직여야한다 -> 3 - index = 4 -1 - (index)
        # [0 1 [2] 3 4 5] -> 2번 vs 3번
        # [0 1 2 3 [4] 5] -> 4번 vs 1번 -> 5 - (index) = 6-1-(index)
        # => 앞에서 움직일 횟수를, 뒤에서 움직인다면, [-><----] 화살표의 합이 일정하고, 앞에 화살표가 변한다
        #   range(  n - 1 - index[앞에서 움직이는 횟수] )
        for _ in range(self.section_count - 1 - index):
            curr = curr.prev
        return curr

    def check_index_range(self, index):
        if index < 0 or index > self.section_count - 1:
            raise IndexError('invalid index.')

    # 8)
    def insert(self, index, data):
        # insert는 마지막인덱스를 넘어선 len 인덱스까지 허용해야한다. -> len인덱스아닐때만 check하도록 해서, len인덱스는 입력한다.
        if index != self.section_count:
            self.check_index_range(index)

        # 순회를 안해도 되는 0, len-1(x) len 인덱스 insert
        # -> ex> h012t 중 3인덱스가 append이다. 2index는 2를 뒤로 몰아내고 자기가 2로 들어간다
        if index == 0: return self.append_left(data)
        if index == self.section_count: return self.append(data)
        # 이제 index번재 요소를 뒤로 밀어내가 삽입되는 경우
        # -> delete(3개)와 달리 append/append_left의 생성처럼 이전node를 curr로 잡아 node2개를 먼저 챙긴다
        # -> delete는 lst_2d 필터링 순회후 찾는 curr vs 여기선 index 순회용 get(index)로 curr
        prev = self.get(index - 1)
        next = prev.next  # add에서는 curr가 생기니, 양옆객체만 챙겨놓는다.

        curr = Section(data, prev=prev, next=next)
        prev.next = next.prev = curr

        self.section_count += 1
        return curr

    # 9)
    def pop_left(self):
        if self.section_count == 0:
            raise RuntimeError('no lst_2d.')
        # head / 첫 객체 / 다음객체를 챙긴다
        curr = self.head.next
        next = curr.next
        # curr을 빼고 2개만 연결한다.
        self.head.next = next
        next.prev = self.head

        self.section_count -= 1
        return curr

    # 10)
    def pop(self):
        if self.section_count == 0:
            raise RuntimeError('no lst_2d.')
        # 이전객체 / 마지막객체 / tail를 챙긴다
        curr = self.tail.prev
        prev = curr.prev
        # curr을 빼고 2개만 연결한다.
        prev.next = self.tail
        self.tail.prev = prev

        self.section_count -= 1
        return curr

    # 11)
    def remove(self, index):
        # index 검사
        self.check_index_range(index)
        # index 0, 마지막일 때 재활용
        if index == 0: return self.pop()
        if index == self.section_count - 1: return self.pop()
        curr = self.get(index)
        prev = curr.prev
        next = curr.next

        prev.next = next
        next.prev = prev

        self.section_count -= 1
        return curr

    # 12)
    def delete(self, data):
        # (1) select(read)/update/delete는 돌면서 해당데이터를 가진 node를 찾아야한다.
        # -> 순회 전에 lst_2d node가 있는지 확인한다.
        self.check_empty()
        # 필드에 원하는 데이터있는지 바텀업으로 탐색
        curr = self.search(data)
        # 2) 찾아서 break 후 아래로 온다.
        # 3) 데이터 삭제는, append, append_left -> insert(index) 내에서 0,len index처럼
        #   ->  맨앞(curr==self.head.next), 맨뒤(curr=self.tail.prev)삭제를 먼저 함수로 정의할 필요가 없기 때문에
        #   -> 일반적인 중간삭제 -> prev, next를 인자를 받는 메서드로 추출 -> prev를 self.head로, next를 self.tail.prev로 주면 될듯??
        if curr == self.head.next:
            return self.delete_with_prev(self.head, curr)  # prev(head)와 2개로 next까지 만들어서 삭제
        if curr == self.tail.prev:
            return self.delete_with_next(curr, self.tail)  # next(tail)과 2개로 prev까지 만들어서 삭제
        return self.delete_with_prev(curr.prev, curr)  # delete with prev를 재활용

    def search(self, data):
        curr = self.head.next
        for _ in range(self.section_count):
            if curr.lst_2d == data:
                break  # 다 검사해서 찾으면 break -> else안거치고 아래로  vs 못찾으면 else문 -> raise
            curr = curr.next
        else:
            raise ValueError(f"no {data} in lst_2d.")  # 1) 못찾을 시
        return curr

    def delete_with_next(self, curr, next):
        prev = curr.prev
        # 챙긴 객체를 바탕으로 curr를 빼고 서로를 연결한다.
        prev.next = next
        next.prev = prev
        self.section_count -= 1
        return curr

    def delete_with_prev(self, prev, curr):
        next = curr.next  # 다다음node챙기기 (self.head / curr / next )
        # 챙긴 객체를 바탕으로 curr를 빼고 서로를 연결한다.
        prev.next = next
        next.prev = prev
        # 갯수차감 + 삭제한node return한다.
        self.section_count -= 1
        return curr

    def check_empty(self):
        if self.section_count == 0:
            raise RuntimeError('no lst_2d.')

    def update(self, before_data, after_data):
        self.check_empty()
        curr = self.search(before_data)

        curr.lst_2d = after_data

        return curr

    def concat(self, right):
        # 앞쪽의 마지막요소, tail(delete), 뒤쪽의 head(delete), 첫요소를 연결해야한다.
        # (1) tail을 통해 마지막요소를 챙기고, head를 통해 첫요소르 챙긴다
        last_of_left = self.tail.prev
        first_of_right = right.head.next
        # (2) 삭제될 것들은 놔두고 양옆을 연결한다.
        last_of_left.next = first_of_right
        first_of_right.prev = last_of_left
        # (3) 요소갯수의 변화가 있으니, 카운팅해줘야한다.
        self.section_count += right.section_count

    def traverse(self):
        if self.section_count == 0:
            return []

        elements = []
        curr_section = self.head.next
        while curr_section.next:
            elements.append(curr_section)
            curr_section = curr_section.next
        return elements

    def reverse(self):
        if self.section_count == 0:
            return []

        elements = []
        curr_section = self.tail.prev
        while curr_section.prev:
            elements.append(curr_section)
            curr_section = curr_section.prev
        return elements

    def sorted(self, key=None, reverse=False):
        sorted_section_lst = sorted(self.traverse(), key=key, reverse=reverse)
        return self.of(sorted_section_lst)

    @classmethod
    def of(cls, raw_sections):
        target = cls()
        for section in raw_sections:
            # 조심.. 새로운 것을 만들 때는, node가 아닌 data만 받는다.
            target.append(section.lst_2d)
        return target

    def merge_sorted(self, other, key=None, reverse=False):
        first = sorted(self.traverse(), key=key)
        second = sorted(other.traverse(), key=key)

        merge_sorted_sections = self.merge_sort(first, second)
        if reverse:
            merge_sorted_sections.sort(key=key, reverse=True)

        return self.of(merge_sorted_sections)

    def merge_sort(self, first, second):
        result = []
        first_index = second_index = 0
        while first_index < len(first) and second_index < len(second):
            first_section, second_section = first[first_index], second[second_index]
            target = first_section
            if first_section.lst_2d < second_section.lst_2d:
                result.append(target)
                first_index += 1
                continue
            target = second_section
            result.append(target)
            second_index += 1
        if first:  # 둘 중에 first가 먼저 끝났다고 가정하면
            result += second[second_index:]
        else:
            result += first[first_index:]
        return result


if __name__ == '__main__':
    sections = Sections()
    print(sections)
    sections.append_left("첫번째로 넣음")
    sections.append_left("2번째로 넣음")
    print(len(sections), sections)  # 2 Sections(Section('2번째로 넣음'), Section('첫번째로 넣음')))
    sections.append("3번째로 넣음")
    print(len(sections), sections)  # 3 Sections(Section('2번째로 넣음'), Section('첫번째로 넣음'), Section('3번째로 넣음')))
    sections.delete("2번째로 넣음")
    print(len(sections), sections)  # 2 [Section('첫번째로 넣음') -> Section('3번째로 넣음')]
    sections.append("추가")
    sections.append("추가2")
    print(len(sections), sections)  # 1 [Section('3번째로 넣음')]
    print(sections.get(0))
    print(sections.get(1))
    print(sections.get(2))
    sections.insert(1, "인서트")  # 3 [Section('3번째로 넣음') -> Section('추가') -> Section('추가2')]
    print(len(sections), sections)
    # 4 [Section('3번째로 넣음') -> Section('인서트') -> Section('추가') -> Section('추가2')]
    sections.insert(0, "인서트0")  # 3 [Section('3번째로 넣음') -> Section('추가') -> Section('추가2')]
    print(len(sections), sections)
    sections.insert(sections.section_count, "인서트len")  # 3 [Section('3번째로 넣음') -> Section('추가') -> Section('추가2')]
    print(len(sections), sections)

    print(sections.pop_left())
    print(len(sections), sections)
    print(sections.pop())
    print(len(sections), sections)
    print(sections.remove(1))
    print(len(sections), sections)

    sections.delete('첫번째로 넣음')
    print(len(sections), sections)  # 3 [Section('3번째로 넣음') -> Section('추가') -> Section('추가2')]
    sections.delete('3번째로 넣음')  # head쪽 with prev
    print(len(sections), sections)  # 2 [Section('추가') -> Section('추가2')]
    sections.delete('추가2')  # tail쪽 with next
    print(len(sections), sections)  # 1 [Section('추가')]
    sections.append('추가2')
    sections.append('추가3')
    print(len(sections), sections)  # 3 [Section('추가') -> Section('추가2') -> Section('추가3')]
    sections.delete('추가2')  # 가운데 with prev
    print(len(sections), sections)  # 2 [Section('추가') -> Section('추가3')]

    sections.update('추가', '추가5')
    print(len(sections), sections)  # 2 [Section('추가5') -> Section('추가3')]

    sections2 = Sections()
    sections2.append("2-1")
    sections2.append("2-2")
    sections.concat(sections2)
    print(sections)  # [Section('추가5'), Section('추가3'), Section('2-2'), Section('2-1')]

    print(sections.traverse())  # [Section('추가5'), Section('추가3')]
    print(sections.reverse())  # [Section('추가3'), Section('추가5')]
    print(sections.sorted(key=lambda x: x.lst_2d))  # data필드 기준 정렬
    # [Section(Section('2-1')) -> Section(Section('2-2')) -> Section(Section('추가3')) -> Section(Section('추가5'))]
    print(sections.sorted(key=lambda x: x.lst_2d, reverse=True))  # node의 data필드 기준 정렬
    # [Section(Section('추가5')) -> Section(Section('추가3')) -> Section(Section('2-2')) -> Section(Section('2-1'))]

    merged_1 = Sections()
    merged_1.append(1)
    merged_1.append(3)
    merged_1.append(2)
    merged_2 = Sections()
    merged_2.append(5)
    merged_2.append(4)
    merged_2.append(7)
    print(merged_1.merge_sorted(merged_2, lambda x: x.lst_2d))
    print(merged_1.merge_sorted(merged_2, lambda x: x.lst_2d, reverse=True))
    new = merged_1.merge_sorted(merged_2, lambda x: x.lst_2d)
    print(new)