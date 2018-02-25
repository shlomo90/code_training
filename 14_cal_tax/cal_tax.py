# -*- encoding: utf-8 -*-

import math



'''

입력한 가격에 대한 세금을 계산하는 간단한 프로그램을 작성하라. 프로그램은 주문

가격과 함께 주 이름을 입력 받는데, 주 이름이 'WI'인 경우 세율은 5.5%가 된다.

프로그램은 위스콘신 주 거주자에 해당하는 소계, 세율, 합계 금액을 출력하지만

다른 주에 거주하는 경우에는 합계 금액만 출력한다.



출력 예

What is the order amount? 10

What is the state?

the subtotal is $10.00

The tax is $0.55

The total is $10.55



또는 다음과 같이 작성할 수 있다.

What is the order amount?

What is the state?

The total is $10.55



제약 조건

* 오직 if 문만 사용하여 작성할 것 (else 사용 안됨)

* 모든 금액은 가장 가까운 센트로 반올림할 것.

* 프로그램의 마지막에 한 개의 출력문만 사용하여 결과를 출력할 것



도전 과제

* 주 이름의 약어를 대소문자가 섞인 상태로 입력해도 되도록 프로그램을 수정해

보자.

* 주 이름 전체를 대소문자가 섞인 상태로 입력해도 되도록 프로그램을 수정해보자.

'''





class tax():

    def __init__(self):
        self.get_value = []
        self.user_subtotal = 0.0
        self.user_tax = 0.0
        self.total = 0.0
        self.state_taxs = {'WA': {'tax': 0, 'state': 'Washington'},
                           'NY': {'tax': 0, 'state': 'NewYork'},
                           'WY': {'tax': 0, 'state': 'Wyoming'},
                           'SD': {'tax': 0, 'state': 'South Dakota'},
                           'AL': {'tax': 0, 'state': 'Alabama'},
                           'TX': {'tax': 0, 'state': 'Texas'},
                           'FL': {'tax': 0, 'state': 'Flolida'},
                           'ND': {'tax': 2.9, 'state': 'North Dakota'},
                           'IN': {'tax': 3.3, 'state': 'Indiana'},
                           'PA': {'tax': 3.07, 'state': 'Pennsylvania'},
                           'NH': {'tax': 5, 'state': 'New Hampshire'},
                           'TN': {'tax': 6, 'state': 'Tennessee'},
                           'OR': {'tax': 9.9, 'state': 'Oregon'},
                           'CA': {'tax': 13.3, 'state': 'California'},
                           'AZ': {'tax': 4.54, 'state': 'Arizona'},
                           'NM': {'tax': 4.9, 'state': 'New Mexico'},
                           'UT': {'tax': 5, 'state': 'Utah'},
                           'NC': {'tax': 5.75, 'state': 'North Carolina'},
                           'WV': {'tax': 6.5, 'state': 'West Virginia'},
                           'ME': {'tax': 7.15, 'state': 'Maine'},
                           }

        for state, tax in self.state_taxs.iteritems():
            print "state is {}, {}".format(state, tax)
        print '----------------------------------------'


    def input_msg(self):
        order_amount = raw_input("What is the order amount? ")
        self.get_value.append(order_amount)
        state = raw_input("What is the state? ")
        self.get_value.append(state)

        self._validate_value()
        self._calculate_tax()
    def _validate_value(self, upper=False):
        '''
        validate input_value list.
        '''
        full_name_states = [v['state'] for k, v in self.state_taxs.iteritems()]
        short_name_states = self.state_taxs.keys()
        amount = self.get_value[0]
        state = self.get_value[1]

        if amount < 0:
            print 'error value'
            assert False

        if state in short_name_states:
            self.get_value.append(self.state_taxs[state]['tax'])
            return True

        if state in full_name_states:
            short = ''
            for k, v in self.state_taxs.iteritems():
                if v['state'] == state:
                    short = k
                    break
            self.get_value.append(self.state_taxs[short]['tax'])
            return True
        return True

    def _calculate_tax(self):
        amount = float(self.get_value[0])
        tax = float(self.get_value[2]) * 0.01
        tax = tax * amount
        total = amount + tax
        total = math.ceil(total)
        self.user_tax = tax
        self.user_subtotal = amount
        self.total = total
        return total

    def output_msg(self):
        print 'The subtotal is {}'.format(self.user_subtotal)
        print 'The tax is {}'.format(self.user_tax)
        print 'The total is {}'.format(self.total)


if __name__ == '__main__':
    a = tax()
    a.print_state_tax()
    a.input_msg()
    a.output_msg()
