#-*- encoding: utf-8 -*-

'''
사용자로부터 사람의 키(인치 단위), 몸무게(파운드 단위)를 입력 받아 체질량치수
(BMI, Body Mass Index)를 계산하는 프로그램을 작성하라.

bmi = (weight/(height * height)) * 703

bmi 값이 18.5에서 25 사이로 나타나면 이 사람은 정상적인 몸무게라고 출력하고,
그렇지 않은 경우에는 과체중이나 저체중으로 나타낸 다음 의사와 상의하라는 문구도
출력해보자.

출력 예
Your BMI is 19.5
You are within the ideal weight range.

or
Your BMI is 32.5.
You are overweight. You should see your doctor.


제약 조건
* 입력 값으로 숫자만 받을 수 있도록 하여 숫자가 입력될 때 까지 진행되지
않도록 할 것.

도전 과제
* 사용자 인터페이스에서 인치/파운드 단위와 국제표준 단위를 모두 입력 받을 수
있도록 프로그램을 수정해보자. 국제표준 단위를 계산하기 위해 수식을 변경해야할
것이다.

* 인치/파운드 단위의 경우 피트와 인치 값을 섞어서 받은 다음 계산할 때 자동으로
인치 값으로 변환하여, 사용자가 굳이 인치 값으로 바꾸지 않아도 되도록 프로그램을
수정해보자.
'''


class bmi_test(object):
    def __init__(self):
        self.clients = {}

    def _validate_data(self, weight, height):
        if weight <= 0:
            raise "error weight <= 0"

        if height <= 0:
            raise "error height <= 0"

        return True

    def get_bmi(self, weight, height):
        self._validate_data(weight, height)

        bmi = 0.0
        bmi = (weight/(height * height)) * 703
        return bmi

    def result(self, bmi):
        if bmi >= 18.5 and bmi <= 25:
            print("You are within the ideal weight range.")
        else:
            print("You are not within the ideal weight ranghe.")


if __name__ == "__main__":
    weight = float(raw_input("What is your Weight? "))
    height = float(raw_input("What is your Height "))

    bmi = bmi_test()
    my_bmi = bmi.get_bmi(weight, height)
    bmi.result(my_bmi)
