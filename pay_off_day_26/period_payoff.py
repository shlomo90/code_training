#
*- encoding: utf-8 -*-

'''
카드 대금을 상환하는 데 걸리는 개월 수를 계산하는 프로그램 작성하라. 총 대금,
연이율(Annual Percentage Rate, APR), 월 상환 금액을 입력 받은 다음 상환에
소요되는 개월 수를 출력하면 된다.

  이 프로그램에 사용되는 공식은 다음과 같다.
         1    log(1 + b/p(1 +(1 + i)^30))
  n = - -- X  ---------------------------
        30             log(1 + i)


    n: 개월 수
    i: 일이율(ARP/365)
    b: 총 대금
    p: 월 상환 금액

  출력 예
What is your balance? 5000
What is the APR on the card (as a percent)? 12
What is the monthly payment you can make? 100

It will take you 70 months to pay off this card.

  제약 조건
* 카드의 연이율을 입력 받은 후 내부적으로 일이율을 계산할 것
* 연이율은 10진수가 아닌 퍼센트 단위로 받을 것
* 총 대금, 연이율, 월 상환 금액을 인수로 받고 상환 개월 수를 반환하는
  calculateMonthsUntilPaidOff 함수를 작성할 것. 이때 인수는 함수 바깥에서
  접근하지 않도록 한다.
* 금액은 센트 단위로 올림할 것.

  도전 과제
* 공식을 변형하여 상환할 개월 수를 입력하면 월 상환 금액을 반환하도록 하라.
  그런 다음 사용자로 하여금 상환하는 개월 수를 원하는지, 아니면 월 상환 금액을
  원하는지를 선택하도록 하여 이에 맞는 답을 제시하도록 하라.
'''
'''
per_interest : percent.
day_interest : internal..
year_interest :

'''

import math


def start_payoff():
    while (True):
        try:
            b = float(raw_input("What is your balance? "))
            y = float(raw_input("What is the APR on the card(as a percent)? "))
            p = float(raw_input("What is the monthly payment you can make? "))
            break
        except ValueError:
            print("숫자만 입력해주세요.")
            continue

    b = round(b, 2)
    p = round(p, 2)
    print("{} {}".format(b, p))
    period = calculateMonthsUntilPaidOff(b, y, p)

    print("It will take you {} months to pay off this card.".format(period))
    return


def calculateMonthsUntilPaidOff(b, y, p):
    '''
    parameter.
    b : 총 대금.
    y : 연 이율
    p : 월 상환 금액.

    d : 일 이율.

    >>> calculateMonthsUntilPaidOff(5000, 12, 100)
    70

    '''
    i = y/(365 * 100)
    print(i)
    n = math.log10(1 + b/p * (1 + math.pow((1 + i), 30)))
    n /= -30 * math.log10(1 + i)
    print(n)

    # 일이율 계산.
    # 상환개월수 반환.
    return n


if __name__ == '__main__':
    start_payoff()

