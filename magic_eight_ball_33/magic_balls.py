# -*- encoding: utf-8 -*-
'''
배열은 프로그램에서 가능한 대답을 저장하는데 아주 좋다. 무작위 번호 추출기와
같이 엮는다면 배열에 저장된 아이템을 무작위로 추출할 수 있으며, 이러한 기능은
게임에 적용하기 좋다.
  Magic 8 Ball 게임을 작성하라. Magic 8 Ball 게임은 사용자로부터 질문을 입력
받아 이에 대한 답을 "Yes", "No", "Maybe", "Ask again later" 등 중에서 무작위로
대답해주는 게임이다.

출력 예
What's your question? Will I be rich and famous?
Ask again later.

제약 조건
* 대답하는 값은 pseudo 무작위 숫자 생성기를 이용하여 선택되도록 할 것.
  이때 가능한 선택지를 배열에 넣은 다음 무작위로 한 개가 선택되도록 해야 한다.

도전 과제
* 이 프로그램을 GUI 애플리케이션으로 제작하라.
* 가능하다면 장치 라이브러리를 사용하여 8 ball을 '흔들'수 있도록 하라.

'''

import random

answers = ["Yes", "No", "Maybe", "Ask again later"]


def get_answer(q):
    ''' Question의 길이를 기반으로 seed 작성. 그에 따른 답변을 준비한다.
    '''

    random.seed(len(q))
    a_num = len(answers)
    r_num = random.randrange(0, a_num)
    return answers[r_num]


def ask_question():
    q = raw_input("What's your question? ")
    return q


if __name__ == "__main__":
    q = ask_question()
    print(get_answer(q))
