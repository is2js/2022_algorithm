import sys

input = sys.stdin.readline

class Section:
    def __init__(self, data, prev=None):
        self.data = data  # 구간별 정보 (구간의 to, 구간처리시 비용money)
        self.prev = prev

    def calculate(self, target_data):
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
        if target_data in self.data:
            print(f"<{self.data!r}> 구간에 걸렸다")
            return 1000
        return 0  # 누적연산의 기본값 반환

    def __repr__(self):
        return f"{self.__class__.__name__}({self.data!r})"


class Sections:
    def __init__(self):
        self.section = Section(None)  # (2) prev데코객체 소유객체는, 시작특이점 객체(head)를 가진 체 태어난다.
        self.section_count = 0  # (3) insert시 활용하기 위해, add 등 count를 세주면 좋다.

    def add(self, data):
        # prev데코객체는, new Node만 유지할 예정인데,
        # 기존node의 연결이 끊어지지 않게, new Node 생성시, prev필드에 연결만 해주면 된다.
        # (2)
        # temp = self.section
        # self.section = Section(lst_2d, prev=temp)
        self.section = Section(data, prev=self.section)
        # -> add한 new Node가 필드로 유지되니 return할 필요는 없다.
        self.section_count += 1

    def __len__(self):
        return self.section_count

    # (5) 각 구간들을 돌면서, 자기구간에 걸리면 처리/아니면 기본값 반환해서 누적시킨다.
    # -> 구간들을 다 돌고나서 처리결과를 반환한다.
    def calculate(self, before_money, target_data):
        result = 0
        curr = self.section
        while curr.prev:
            result += curr.calculate(target_data)
            curr = curr.prev
        if result < 0:
            raise RuntimeError("[ERROR] 잘못된 계산 결과")  # 기준을 정해서 연산 후, post condition검사
        return before_money + result

    # (4) repr를 구현해도 출력해도, 뒤에서 부터 보이지만, string을 담아 역순으로 join한다
    def __repr__(self):
        infos = []
        curr = self.section
        while curr.prev:  # data없는 시작특이점(prev=None) 객체가 존재한다면, 그 전까지만 걸리게, prev필드로 검사한다
            infos.append(str(curr))
            curr = curr.prev
        return f"{self.__class__.__name__}({', '.join(infos[::-1])})"


if __name__ == '__main__':
    sections = Sections()  # 내부에 시작특이점 객체들 들고 태어난다.
    sections.add("target_data를 포함하는 구간")
    sections.add("안포함하는 구간")
    print(len(sections))
    print(sections)  # Sections(Section('target_data를 포함하는 구간'), Section('안포함하는 구간'))
    result = sections.calculate(0, "target_data")
    print(result)
    pass
