# -*- encoding: utf-8 -*-
import math

'''
단리를 계산하는 프로그램을 작성하라. 원금을 입력 받은 다음 이자를 퍼센트 단위로
입력 받고, 기간을 연단위로 입력 받은 후 원리금(원금 + 이자)를 출력해보자.
  단리 공식은 다음과 같다.

  A = P(1 + rt)

  P: 원금
  r: 연이율
  t: 기간(연단위)
  A: 원리금

출력 예
Enter the principal: 1500
Enter the rate of interest: 4.3
Enter the number of years: 4
After 4 years at 4.3%, the investment will be worth $1758

제약 조건
* 연 이율은 반드시 퍼센트 단위로 입력 받은 후(예: .15가 아니라 15)
프로그램에서 입력 값을 100으로 나누어 계산할 것
* 센트를 기준으로 하는 소숫점 다음에 숫자가 있을 때는 퍼센트를 기준으로 올림
처리할 것.
* 출력되는 원리금은 화페 단위로 출력할 것.

도전과제
* 입력 값 원금, 이율, 기간은 모두 숫자로만 받을 수 있도록 프로갬을 수저해보자.
숫자가 입력될 떄 까지 진행되지 않도록 하라.
* calculateSimpleinterest 라는 이름의 함수를 만들어 사용하도록 프로그램을
수정해보자. 이 함수는 원금, 이율, 기간을 파라미터로 받으며 원리금을
반환한다.
* 기간 도래 후의 원리금만을 출력하는 대신 매년 원리금의 변화를 알 수 있도록
연단위로 원리금을 출력하도록 프로그램을 수정해보자.
'''
'''
input interest per year = float
        years = int
        principal = int
'''


class simple_interest():
    def __init__(self):
        pass

    def input_interest(self):
        self.principal = int(raw_input("Enter the principal: "))
        self.rate = float(raw_input("Enter the rate of interest: ")) / 100
        self.years = int(raw_input("Enter the number of years: "))

    def print_compound_interest(self):
        pass

    def set_invest(self):
        result = self.principal * (1 + self.rate * self.years)
        return result

    def print_result(self):
        result = math.ceil(simple_interest.set_invest(self))
        print'After {} years at {}%, the investment will be worth {}'.format(
            self.years, self.rate*100, result)


if __name__ == "__main__":
    x = simple_interest()
    x.input_interest()
    x.print_result()
