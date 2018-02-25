# -*- encoding: utf-8 -*-

'''
전문가 시스템은 일종의 인공지능 프로그램으로, 축적된 노하우와 규칙 집합을
사용하여 전문가가 직접 하는 것 처럼 작업을 수행하도록 한다. 실제로
많은 웹사이트에서는 여러 질문을 통해 자기 스스로 병에 대한 진단을 알 수 있도록
도와준다. 또한 많은 하드웨어 소프트웨어 회사는 온라인 문제 해결 도구를 통해
간단한 기술 문제로 콜센터에 전화를 걸기전에 문제를 해결하 ㄹ수 있도록 지원한다.

  이번에는 자동차에 대한 문제를 해결하는 프로그램을 작서아라. 이를 위해 다음
의사 결정 트리를 이용하라.


출력 예
Is the car silent when you turn the key? y
Are the battery terminals corroded? n
The battery cables may be damaged.
Replace cables and try again.

제약 조건
* 한 번에 모든 입력을 받지 말고 상황과 답변에 맞는 질문이 나타나도록 할 것.

도전 과제
* 규칙 엔진(Rules engin)과 추론 엔진(Inference engine)에 대해 조사하라.
  이 두 가지 엔진은 각각 규칙과 사실에 기반하여 복잡한 문제를 해결하는 강력한
  도구이다. 여러분의 프로그래밍 언어를 위한 규칙 엔진을 구현하고, 앞의 문제를
  해결하는데 사용하라.

'''

'''
start: 열쇠를 꽂고 돌렸을 때 차가 조용한가?
    yes: 배터리 단자가 부식되었는가?
        yes: 단자를 깨끗하게 하고 다시 시도하라.
        no: 케이블을 교체하고 다시 시도하라.
    no : 차에서 달깍거리는 소리가 나는가?
        yes: 배터리를 교체하고 다시 시도하라.
        no: 시동이 완전히 걸리지 않는가?
            yes: 점화플러그 연결상태를 점검하라.
            no: 엔진이 동작한 후 바로 꺼지는가?
                yes: 차에 연료 분사 장치가 있는가?
                    yes: 초크가 제대로 여닫히는지 확인하라.
                    no: 서비스 센터에 의뢰하라.
'''

def car_decision_tree():
    if question_and_answer("열쇠를 꽂고 돌렸을 때, 차가 조용한가? "):
        if question_and_answer("배터리 단자가 부식되었는가? "):
            return "단자를 깨끗하게 하고 다시 시도하라."
        else:
            return "케이블을 교체하고 다시 시도하라. "
    else:
        if question_and_answer("차가 달깍거리는 소리가 나는가? "):
            return "배터리를 교체하고 다시 시도하라. "
        else:
            if question_and_answer("시동이 완전히 걸리지 않는가? "):
                return "점화 플러그 연결상태를 점검하라."
            else:
                if question_and_answer("엔진이 동작한 후 바로 꺼지는가? "):
                    if question_and_answer("차에 연료 분사 장치가 있는가? "):
                        return "초크가 제대로 여닫히는지 확인하라"
                    else:
                        return "서비스 센터에 의뢰하라"


def question_and_answer(quest):
    """ return True or False
    show the quest. and get the answer from user.

    >>> question_and_answer("you are a boy? ")
    you are a boy? yes
    True
    """

    ans = ''
    ans = str(raw_input(quest))
    while(1):
        try:
            if (validate_answer(ans) == 'y'):
                ret = True
            else:
                ret = False
        except Exception as e:
            continue
        break
    return ret


def validate_answer(answer):
    answer_no_list = ['n', 'N', 'No', 'NO', 'no', 'nO']
    answer_yes_list = ['y', 'Y', 'Yes', 'YES', 'yes', 'yEs', 'yeS']

    if answer in answer_yes_list:
        return 'y'

    if answer in answer_no_list:
        return 'n'
    raise


if __name__ == "__main__":
    solution = car_decision_tree()
    print(solution)


