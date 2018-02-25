#-*- encoding: utf-8 -*-

import math

'''
복리를 통해 투자 수익을 계산하는 프로그램을 작성하라. 프로그램은 원금, 투자 기간
연이율, 연간 수익이 지급되는 횟수를 입력 받는다.

A = P ( 1 + r/n)^(n*t)

P : 원금
r : 연이율
t : 투자 기간(연단위)
n : 연간 이자 지급 횟수
A : 원리금

출력 예
What is the principal amount? 1500
What is the rate: 4.3
What is the number of years? 6
What is the number of times the internet
is compounded per year: 4
$1500 invested at 4.3% for 6 years compounded 4 times per year is
$1938.84

제약 조건
* 연이율은 반드시 퍼센트 단위로 입력 받은 후(예: .15가 아니라 15) 프로그램에서
입력 값을 100으로 나누어 계산할 것
* 센트를 기준으로 하는 소숫점 다음에 숫자가 있을 때는 센트를 기준으로 올림
처리할 것.
* 출력되는 원리금은 화폐단위로 출력할 것

도전 과제
* 입력 값으로 숫자만 받을 수 있도록 프로그램을 수정해보자. 숫자가 입력될 때까지
진행되지 않도록 하라.
* 목표 원리금을 입력하면 필요한 초기 투자 원금을 계산하도록 프로그램을 수정해
'''


class compound_interest(object):

    def __init__(self):
        self.principal = 0
        self.rate = 0
        self.year = 0
        self.interest_per_year = 0
        self.need_principal = 0

    def input_interest(self):
        try:
            self.principal = int(raw_input("What is the principal amount? "))
            self.rate = float(raw_input("What is the rate: "))
            self.year = int(raw_input("what is the number of years: "))
            self.int_per_year =int(raw_input("What is the number of times "+\
                                             "interest\nis compounded per "+\
                                             "year: "))
        except:
            assert False
        self._validate_para()

    def _validate_para(self):
        if self.principal < 0:
            assert False

        if self.rate < 0:
            assert False

        if self.year < 0:
            assert False

        if self.int_per_year < 0:
            assert False

        if self.need_principal < 0:
            assert False

    def get_compounded_interest(self):
        p = self.principal
        r = self.rate / 100
        n = self.int_per_year
        t = self.year
        result = p * math.pow((1+r/n), n*t)
        return result

    def output_interest(self):
        result = self.get_compounded_interest()
        print "{} invested at {}% for years compounded {} times per year is"\
            .format(self.principal, self.rate, self.year, self.int_per_year)
        print math.ceil(result)

    def get_need_first_princ(self):
        p = 0
        a = self.need_principal
        r = self.rate / 100
        n = self.year
        t = self.int_per_year
        p = a / math.pow((1+r/n), n*t)
        print math.ceil(p)

    def input_need_principal(self):
        try:
            self.need_principal = float(raw_input("need principal is? "))
        except:
            assert False
        self._validate_para()

if __name__ == "__main__":
    x = compound_interest()
    x.input_interest()
    x.output_interest()
    x.input_need_principal()
    x.get_need_first_princ()

