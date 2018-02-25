# -*- encoding: utf-8 -*-
import math

'''
천장을 칠하는데 필요한 페인트의 양을 구하는 프로그램을 작성하라
길이와 폭을 입력 받은 다음, 1리터에 9m^2 를 칠한다고 가정하여 계산하자
그리로 천장을 칠하는데 필요한 페인트의양을 구하라

제약 조건
* 상수를 사용하여 변환 상수를 저장할 것
* 반드시 올림을 해서 정수 단위로 구할 것

도전 과제
* 입력 값으로 숫자만 받을 수 있도록 프로그램을 수정해보자. 숫자가 입력 될 떄
까지 진행되지 않도록 한다.
* 원 모양의 방도 계산할 수 있도록 하라
* ㄴ자 모양의 방도 계산할 수 있도록 하라

input
    length(길이)
    width(폭)

output
    amount of paint
    square_area
'''

'''
천장이 원형일 때 해결하는 함수를 추가한다.
'''


def get_paint_amount(square_area):
    need_paint = 0
    ppl = 9

    # round up
    need_paint = float(square_area)/float(ppl)
    need_paint = math.ceil(need_paint)
    return need_paint


def get_circle_area(width, length):
    pi = 3.14159265
    area = pi * width * length
    return area


if __name__ == "__main__":
    width = 0
    length = 0
    shape = 0
    area = 0

    width = float(raw_input("input the width? "))
    length = float(raw_input("input the length? "))
    shape = raw_input("circle (y/n)? ")

    if (shape == 'y' or shape == 'Y'):
        area = get_circle_area(width, length)
    else:
        area = width * length

    print("You will need to purchase " + str(get_paint_amount(area)) +
          " liters of\npaint to conver " + str(area) + " square meters.")
