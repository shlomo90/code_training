# -*- encoding: utf-8 -*-

'''
환율을 변환하는 프로그램을 작성하라. 여기에는 유로에서 미국 달러로 변환시킨다.
먼저 유로 금액을 입력 받은 다음 유로 환율을 입력 받는다. 그리고는 유로에
해당하는 미국 달러 값을 출력한다. 환율 변환식은 다음과 같다.

amount(to) = amount(from) * rate(from) / rate(to)

amount(to) 는 변환될 미국 달러 가격이다.
amount(from) 은 유로 가격이다.
rate(from) 은 현재의 유로 환율이다.
rate(to) 는 현재의 미국 달러 환율이다. == 100.0

출력 예
How many Euros are you exchanging? 81
What is the exchange rate? 137.51
81 Euros at an exchange rate of 137.51 is
111.38 dollars

제약 조건
* 센트를 기준으로 하는 소숫점 다음에 숫자가 있을 때는 센트를 기준으로 올림
처리를 할 것
* 한 개의 출력문만 사용할 것

도전 과제
* 환율표를 프로그램에 넣은 다음 환율 대신 국가 이름을 입력 받도록 프로그램을
수정해보자.
* 애플리케이션에 별도의 API를 적용하여 현재의 업데이트된 환율을 적용하는
프로그램으로 수정해보자.
'''
'''
input
    1. 기준 나라 환율은 미국.
    2. 환율표를 넣도록 한다. (dictionary을 이용해야할 듯.)
    3. 업데이트가 되도록 해야한다...

output
    1. 그나라의 환율이겠지.

plan
    유로에서 미 달러로 변환.
    즉, 많은 나라 -> 미 달러

    dictionary : {Euros: 137.51, Koreas: ....}
'''


class exchange_rate:
    country_from = ""
    country_to = ""

    def __init__(self, country_from="Euros", country_to="dollars"):
        # look up for the country exchange rate dictionary to find an exchange
        # rate with input country_from.
        # The default values are "Euros" at country_from, "USA" at country_to.

        # if there is no match the country to the dictionary key,
        # print an error and abort.

        self.rate_to = 100.0
        self.amount_to = 0
        self.amount_from = float(
            raw_input("How many "+country_from+" are you exchanging? "))
        # TODO: Validation Check.
        self.rate_from = float(raw_input("What is the exchacnge rate? "))
        # TODO: Validation Check.
        print str(self.amount_from), "Euros at an exchange rate of ",\
            str(self.rate_from), " is"
        return

    def exchange(self):
        self.amount_to = self.amount_from * self.rate_from / self.rate_to

    def output_print(self):
        print self.amount_to, " Euros at an exchange rate of"
        print self.rate_from, " is ", self.amount_to, " dollars"
        # print self.rate_from, " is ", self.amount_to, " ", country_to

    def error_values(self):
        pass


if __name__ == "__main__":
    x = exchange_rate("Euros", "USA")
    x.exchange()
    x.output_print()
