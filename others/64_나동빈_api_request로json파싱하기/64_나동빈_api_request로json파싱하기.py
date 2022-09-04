import sys

import requests

input = sys.stdin.readline

if __name__ == '__main__':
    ## 개발형 코딩 테스트
    # 알고리즘 코테: 하나의 모듈 개발(시복, 공복 계산)
    # 개발형 코테: 완성도 높은 하나의 프로그램 개발 -> 모듈을 조합하는 능력 요구
    # -> 분야와 상관없는 개념과 도구를 학습
    # -> 서버 client, json, rest, api

    ## http : 웹상 데이터(hyptertext)를 주고받기(transfer) 위한 프로토콜(protocol)
    # -> html파일 or json
    # -> http메서드를 이용해 통신 -> GET조회(접속html/검색json), POST생성(가입/글쓰기), PUT수정, DELTE삭제 요청 메서드

    ## requests로 GET ->  접속
    # target = 'http://google.com'
    # response = requests.get(url=target)
    # print(response.text)

    ## 2020 카카오 2차 코딩테스트 -> RESTAPI호출과 JSON 데이터 파싱할 parser코드
    ## REST란?
    # -> rest: http는 http메서드를 지원하지만, 실제 서버는 메서드 기본설명을 따르지 않아도 프로그램 개발 가능
    #           => 저마다 다른 방식 개발시 문제 => ## http메서드 바탕의 기준이 되는 아키텍쳐 ##
    #    => rest(REpresentational State Transfer) : 표현.과 함께. 자원상태.에 대한 정보를 주고받는. 개발방식
    #    => rest 구성요소 3가지: 자원+행위+표현
    #     (1) 자원(resource): 서버속 사용할 자원을 => uri를 이용해서 접근
    #     (2) 행위(verb) : 자원에 대한 행위를 => http메서드로
    #     (3) 표현(representations): 상세 데이터를 표현 => 페이로드를 이용
    #
    # 사용자(자원 by uri)  회원 등록(행위 by post)을 하고 싶습니다.
    # 아이디는 xxx, 비번은yyyy로 설정하고 싶어요(상세 데이터 표현 by 페이로드)
    #
    # => HTTP 패킹 정보 구성
    # -----------------------
    # URI: https://www.example.com/users
    # HTTP Method: POST
    # Payload: {'id': 'xxxx', "password": 'yyyy'}

    ## REST API란?
    # API(Application Programming Interface): 프로그램이 상호작용하는 인터페이스
    # REST API: REST 아키텍처를 따르는 API
    # REST API 호출: REST방식을 따르고 있는 서버에 특정 요청을 전송

    ## 추가 약속: 주고받는 데이터의 형식
    ## JSON( js Object Notation): 데이터를 주고 받는데 사용하는 / 경량의 데이터 형식
    # -> [키와 값의 쌍]으로 이루어진 [데이터 객체]를 저장한다.

    ## dict형의 데이터 -> json객체 변경가능하다. by dumps( , indent= )
    import json

    user = {
        "id": "gildong",
        "password": "!@#!@#",
        "age": 30,
        "hobby": ["football", "programming"],
    }

    # json.dumps로 dict -> json으로 변환
    json_data = json.dumps(user, indent=4)
    # print(json_data)

    ## dict -> json객체를 파일로 저장 + json객체 return by dump( , file객체, indent= )
    with open("user.json", "w", encoding="utf-8") as file:
        json_data = json.dump(user, file, indent=4)

    ## 목킹: 기능있는 것처럼 흉내내어 구현
    # 가상 REST API 제공 서비스: https://jsonplaceholder.typicode.com/

    service = 'https://jsonplaceholder.typicode.com'
    resource = '/users'
    resource_id = '/1'

    ## json 조회(GET)
    import requests

    target = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url=target)

    # (1) json형식 응답이라면, .json()으로 dict list(여러개) or dict(1개) 로 바로 받아올 수 있다.
    user_lst = response.json()
    # print(type(user_lst)) # <class 'list'>
    # print(user_lst)

    # (2) 각 사용자들의 name만 받아오기
    name_lst = []
    for user in user_lst:
        name_lst.append(user.get('name', None))

    print(name_lst)



