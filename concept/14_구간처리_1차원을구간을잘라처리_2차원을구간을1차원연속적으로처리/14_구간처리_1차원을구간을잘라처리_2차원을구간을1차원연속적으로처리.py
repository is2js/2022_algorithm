import sys 
 
input = sys.stdin.readline 
 
 
if __name__ == '__main__':
    ##### 1차원 -> n개씩 pair로 짤라 -> 2차원처럼, 해당 구간별 요소접근 후 처리

    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    pair = 2
    pairs = []
    # for section_index in range(len(lst_2d)//pair): # 몫만 구하면 나머지를 남기는 구간은 제외된다.
    ### 1,2,3,4,5 //2 -> 구간의 index는 0부터 1까지 2구간인데, 몫은 2가 나온다.
    for section_index in range(len(data) // pair - 1):  # -> 차라리 직전구간까지만 처리하고 + 마지막구간과 나머지 배열들은 합치자.
        ### 배열과 몫구간의 매핑은 N(pair) *구간index를 곱한 것이 구간의 첫째항이고
        # 인덱스는 +1씩 증가하며, 끝항은 0, 1, 2...N-1까지다.
        # first = lst_2d[pair * section_index + 0]
        # second = lst_2d[pair * section_index + 1]
        # ... lst_2d[pair * section_index + (pair - 1)]까지 각각 접근 가능
        section_values = [data[pair * section_index + i] for i in range(pair)]
        ### 구간별 집계가 가능.
        pairs.append(section_values)
    ### 마지막 구간과, 나머지는 합쳐서 처리한다. -> 몫 자체값 - 1: 마지막구간 index
    last_section_index = len(data) // pair - 1
    # 마지막구간의 첫째항 : 구간 첫째항index 부터 끝까지
    # -> 만약 나누어떨어지더라도, 마지막항까지 더하니까 상관없다.
    last_section_values = data[pair * last_section_index:]
    pairs.append(last_section_values)
    print(pairs)
    # [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10, 11]]

    ##### 요약
    # (1) 배열에 직접 구간을 짜른 몫으로 for문을 돌리면 [배열과 무관한 index]지만,
    #    -> 맨 끝 구간을 제외하고, 각 구간에 접근할 수 있다.
    # (2) 원본배열[구간index * 각구간별갯수]는, 각 구간의 첫번째 값
    # (3) 원본배열[구간index * 각구간별갯수 + (0~ 각구간별갯수-1)으로 각 요소의 값으로 접근 및 집게 가능하다
    # => 1차원의 구간별 처리가 가능해진다.
    # => 구간별로 append한다면, 순서대로 2차원 행렬도 만들 수 있을 것 같다.


    ##### 2차원 행렬 -> row구간별로 나누어졌지만 -> 이중반복문안에서 0부터 순서대로 값을 줄 수 있다.
    matrix_3_by_3 = [[i for i in range(3)] for _ in range(3)]
    # print(matrix_3_by_3)
    # (1) 2차원 행렬을 1차원으로 접근하기 위해서는  x, y 이중반복문 속에서
    # -> [row_index * col갯수(구간별갯수) + col_index] 로 접근하면 된다.
    for row in range(len(matrix_3_by_3)):
        for col in range(len(matrix_3_by_3[0])):
            matrix_3_by_3[row][col] = row * len(matrix_3_by_3[0]) + col
    print(matrix_3_by_3)
    #[[0, 1, 2], [3, 4, 5], [6, 7, 8]]


    ##### 요약
    # 2차원 행렬에 0부터 연속적인 값을 배정할 수 있다.
    # -> 구간이라고 생각하고 [구간index * 각구간별갯수 + 구간내번호(0~N-1)]을 통해,
    # -> 구간과 구간사이를 연속적으로 넘어갈 수 있다.



