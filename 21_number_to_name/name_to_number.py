# -*- encoding: utf-8 -*-

'''
숫자에 해당하는 이름 바꾸기.
많은 프로그림이 최종 사용자에게 하나의 양식으로 정보를 제공하지만,
프로그램 내에서는 각기 다른 형태로 정보를 사용하기도 한다.
예를들면 화면에 Blue라는 단어를 출력하기 위해 프로그램상에서는 이 색깔에 대한
숫자 값을 사용할 수도 있다. 왜냐하면 스페인어 사용자를 위해서는 스페인어로
출력문을 만들어야 할 수 도 있기 때문이다.
  1부터 12까지의 숫자를 해당하는 달로 변환시키는 프로그램을 만들어보자.
  먼저 숫자를 입력 받은 다음 이에 해당하는 달 이름을 출력한다.
  만일 범위를 넘어서는 숫자를 입력 받은 경우 적절한 에러 문구를 출력해보자.

출력 예

Please enter the number of the month: 3
The name of the month is March.

제약 조건

* Switch -case 문을 사용하여 프로그램을 작성할 것.
* 출력문은 한 개만 사용할 것.

도전 과제

* Map 또는 Dictionary 를 사용하여 프로그램에서 switch 문을 제거하라.
* 다국어를 지원하도록 프로그램을 변경하라. 이를 위해 프로그램이 시작될 때
사용하는 언어를 입력 받도록 하라.


# 현재 python은 switch - case 문을 지원하지 않아 dictionary로 코드를 만든다.
'''


class MyCalander(object):
    def __init__(self):
        # 1 : en
        # 2 : kr
        # 3 : jp
        self.langs_month_name = {
            1: ['january', 'faburary', 'march', 'april', 'may', 'june',
                  'july', 'august', 'september', 'october', 'november',
                  'december'],
            2: ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월',
                  '9월', '10월', '11월', '12월'],
            3: ['いちがつ', 'にがつ', 'さんがつ', 'しがつ', 'ごがつ',
                  'ろくがつ', 'しちがつ', 'はちがつ', 'くがつ', 'じゅうがつ',
                  'じゅういちがつ', 'じゅうにがつ']
        }

    def get_month_name(self):
        while True:
            try:
                input_lang = int(raw_input("Select Language (1-3): "))
                self.check_int_range(input_lang, (1, 3))
                break
            except ValueError:
                print("It's not inteager. try agin.")
            except Exception:
                pass
        while True:
            try:
                input_month = int(raw_input(
                    "Please enter the number of the month:(1-12) "))
                self.check_int_range(input_month, (1, 12))
                break
            except ValueError:
                print("It's not inteager. try again.")
            except Exception:
                pass
        return self.langs_month_name[int(input_lang)][int(input_month) - 1]

    def check_int_range(self, input, range):
        # range is tuple. (min, max)

        if input < range[0] or input > range[1]:
            print('input range should be {}-{}'.format(range[0], range[1]))
            raise Exception("range Error")

if __name__ == '__main__':
    calander = MyCalander()
    print(calander.get_month_name())
