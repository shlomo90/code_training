# -*- encoding: utf-8 -*-

import sys

'''
피자를 정확하게 나누는 프로그램을 작성하라.
피자수, 사람 수, 피자 개수, 조각 개수를 입력 받는데, 이때 조가가 개수는
짝수어야 한다. 일단 한 사람이 받게 되는 피자 조각 개수를 출력해보자.
만일 남는 조각이 있다면 그 개수도 나타내 보자.

도전 과제
* 입력 값으로 숫자만 받을 수 있도록 프로그램을 수정해보자.
숫자가 입려될 때 까지 진행 되지 않아야 한다.

* 출력 내용은 변경하여 수일치가 되도록 한다.

* 남은 피자 조각도 위와 같이 수일치를 하여 출력되도록 한다.

* 사람 수와 한 사람당 원하는 피자 조각 수를 입력 답ㄷ은 다음, 피자를
몇판 구매해야 하는지 계산하는 프로그램을 작서아라.

* 출력 예
How many people? 8
How many pizzas do you have? 2

How many pieces are in a pizza? 8
8 people with 2 pizzas
Each person gets 2 pieces of pizza.
There are 0 leftover pieces.

'''

def print_divide_pizza(people, pizzas, per_pizza):
    print(str(people)+" people with "+str(pizzas)+" pizzas")
    if per_pizza[0] > 1:
        print("Each person gets "+str(per_pizza[0])+" pieces of pizza.")
    elif per_pizza[0] == 0 or per_pizza[0] == 1:
        print("Each person gets "+str(per_pizza[0])+" piece of pizza.")
    else:
        print("error it shouldn't be below zero")

    if per_pizza[1] > 1:
        print("There are "+str(per_pizza[1])+" leftover pieces.")
    elif per_pizza[1] == 0 or per_pizza[1] == 1:
        print("There are "+str(per_pizza[1])+" leftover piece.")
    else:
        print("error leftover should be over zero")


def order_pizza(pieces, want_pieces):
    order = 0
    order = want_pieces / pieces
    if ((want_pieces % pieces) == 0):
        pass
    else:
        order += 1
    return order


if __name__ == "__main__":
    ''' start '''
    # 원하는 피자 개수.
    want_pieces = 0
    whole_want_pieces = 0
    whole_pieces = 0
    per_pizza = [0,0]
    #each_person = 0
    #leftover = 0
    people = int(raw_input("How many people? "))
    pizzas = int(raw_input("How many pizzas do you have? "))
    print '\n'
    pieces_of_pizza = int(raw_input("How many pieces are in a pizza? "))

    whole_pieces = pieces_of_pizza * pizzas
    per_pizza[0] = whole_pieces / people
    per_pizza[1] = whole_pieces % people

    print_divide_pizza(people, pizzas, per_pizza)

    want_pieces = int(raw_input("What do you want to have pieces of pizza?"))
    total_want_pieces = want_pieces * people


    print ("You should order "
            +str(order_pizza(pieces_of_pizza, total_want_pieces))+" pizzas.")
