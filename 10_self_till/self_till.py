# -*- encoding: utf-8 -*-

'''
간단한 셀프계산대 시스템을 만들어보자. 세가지 물건의 가격과 수량을 각각
입력 받은 다음 소계를 구하고 소계에 대한 5.5%의 세금을 계산하자. 그리고
물건 종류별 수량과 전체 수량을 출력한 후 가격 소계, 세금, 합계 금액을 출력하라.

출력 예
Price of item 1: 25
Quantity of item 1: 2

Price of item 2: 25
Quantity of item 1: 2

Price of item 3: 25
Quantity of item 1: 2

Price of item 4: 25
Quantity of item 1: 2
Subtotal: $64.00
Tax: $3.52
Total: $67.52
'''

'''
제한되지 않는 숫자만 받도록 하는 도전과제에서 최대 65535 을 최대로 하도록
정한다.
'''


TAX = 0.055
MAX_COUNT = 65535

class self_till:


    def __init__(self, product_num):
        if product_num == 0:
            product_num = MAX_COUNT
        self.num_items = product_num
        self.items = []
        self.sum_prices = 0

    def __add_items(self, price, quanti):
        self.sum_prices +=  price * quanti

    def get_tax_prices(self):
        return self.sum_prices * TAX

    def get_sum_prices(self):
        return self.sum_prices

    def get_total_prices(self):
        return self.sum_prices + self_till.get_tax_prices(self)

    def print_result(self):
        print "Subtotal: $"+str(self_till.get_sum_prices(self))
        print "Tax: $"+str(self_till.get_tax_prices(self))
        print "Total: $"+str(self_till.get_total_prices(self))

    def input_items(self):
        price = 0
        quanti = 0
        for i in range(self.num_items):
            while(True):
                try:
                    price = float(raw_input("Price of item "+str(i+1)+": "))
                    quanti = float(raw_input("Quantity of item "+str(i+1)+": "))
                except ValueError:
                    print("only Number input")
                    continue
                break
            self_till.__add_items(self, price, quanti)
            self.print_result()

if __name__=="__main__":
    till = self_till(0)
    till.input_items()
    # till.print_result()
