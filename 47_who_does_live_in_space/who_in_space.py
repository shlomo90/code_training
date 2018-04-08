# -*- encoding: utf-8 -*-

'''
지금 현재 누가 우주에서 살고 있는지를 알아내는 방법이 있다는 사실을 알고 있는가
Open Notify API는 이러한 정보를 제공한다.

http://api.open-notify.org/astros.json 에 방문을 하면, 얼마나 많은 사람이 현재
우주에 있는지 뿐만 아니라, 우주인 이름과 거주하고 있는 우주선 이름도 확인할 수
있다.

  앞의 API를 이용하여 정보를 가져온 다음 표 형태로 결과를 루력하는 프로그램을
작성하라.

출력 예
There are 3 people in space right now:

Name                | Craft
--------------------|-------
Gennady Padalka     | ISS
Mikhail Kornieko    | ISS
Scott Kelly         | ISS

제약 조건
* 프로그램이 실행할 때마다 매번 APPI에서 데이터를 직접 읽은 다음 결과를
  출력할 것. 데이터를 텍스트로 다운 받은 후 이를 읽는 방식으로 구현하지 말 것

도전 과제
* 제목 컬럼의 길이(Width)는 길이가 가장 긴 값에 맞추도록 하자.
* 우주선 이름을 반복하여 출력하는 대신 우주선 이름을 기준으로 우주인들을
  그룹핑 하라.
* 데이터를 읽은 결과를 성(Last Name)을 기준으로 하여 알파벳순으로 정렬할 수
  있겠는가? 이때, "Mary Sue Van Pelt"와 같이 간혹 이름에 공백을 넣는 사람도
  있으니 주의하자.
'''

import json
import requests

URL = "http://api.open-notify.org/astros.json"

def show_table(data):
    '''
    table consists of with, delimit, data
    column_name =()

    '''

    ldata = list(data)
    if ldata[0]:
        col_width = {}
        cols = data[0].keys()
        for col in cols:
            col_width[col] = len(col)
    else:
        print("Nothing in data")
        return

    delim = '|'
    table = []
    for elem in data:
        e = []
        for col in cols:
            try:
                val = elem[col]
                e.append(val)
            except KeyError:
                print("{} is Invalid Column.".format(col))
                print("{} is skipped.".format(col))

                # default len is bigger than len of "None"
                e.append("None")
                continue

            lval = len(val)
            if lval > col_width[col]:
                col_width[col] = lval

        table.append(tuple(e))

    first_time = False
    for t in table:
        if first_time is False:
            elem = []
            row_delim = []
            for col in cols:
                width = col_width[col]
                elem.append('{}'.format(col).ljust(width, ' '))
                row_delim.append('-'.ljust(width, '-'))
            line = delim.join(elem)
            print(line)
            print(delim.join(row_delim))
            first_time = True
        else:
            elem = []
            for i, val in enumerate(t):
                width = col_width[cols[i]]
                elem.append('{}'.format(val).ljust(width, ' '))
            line = delim.join(elem)
            print(line)


def who_live_space():
    '''
    URL("http://api.open-notify.org/astros.json") 으로 연결하여, json 형식의
    파일을 읽어 테이블 형식으로 리턴한다.

    param:
        void

    return:
        show a table who live in space.
    '''

    response = requests.get(URL)
    data = response.text
    js = json.loads(data)
    show_table(js['people'])


if __name__ == "__main__":
    who_live_space()
