#-*- encoding: utf-8 -*-

'''
화씨 온도와 섭씨 온도를 서로 변환시키는 프로그램을 작성하라.
먼저 변환할 타입을 입력 받은 다음 온도를 입력 받아 해당 타입으로 변환시키자.
여기에서 사용하는 공식은 다음과 같다.

C = (F-32) * 5/9
F = (C*9/5) + 32

출력 예
Press C to convert from Fahrenheit to Celsius.
Press F to convert from Celsius to Fahrenheit.
Your choice: C

Please Enter the temperature in Fahrenheit: 32
The temperature in Celsius is 0.

제약 사항
* C와 F는 대소문자에 관계없이 입력 받을 수 있도록 할 것.
* 출력문의 개수를 최소화하면서도 출력 문자열을 반복해서 사용하지 않도록 할것

도전 과제
* 입력 값으로 숫자만 받을 수 있도록 프로그램을 작성해보자. 숫자가 입력 될 때
까지 진행되지 않도록 만들어라.
* 계산만을 수행하는 함수를 만들어 프로그램을 분리하라.
* 이 프로그램을 GUI버전으로 구현하여 입력 값이 변경되는 즉시 결과가 업데이트
되도록 하라.
* 절대온도도 지원하도록 프로그램을 수정하라.
'''


class temperature(object):
    def __init__(self):
        pass

    def routine(self):
        tmp = 0.0
        ftoc = True   # default

        tmp, ftoc = self.input_info()

        # convertor
        out = self.tmp_cnvtr(tmp, ftoc)
        self.print_tmp(out)

    def metric_convertor(self, target_metric, temperature):
        pass

    def input_info(self):
        ftoc = True
        cel = ['c', 'C']
        feh = ['f', 'F']

        print("Press C to convert from Fahrenheit to Celsius.")
        print("Press F to convert from Celsius to Fahrenheit.")

        while(1):
            select = raw_input()

            # validate select
            if select in cel:
                ftoc = True
                break

            elif select in feh:
                ftoc = False
                break

            else:
                print("Must be c, C, f, F")
                continue

        while(1):
            try:
                if ftoc:
                    tmp = raw_input(
                        "Please Enter the temperature in Fahrenheit: ")
                else:
                    tmp = raw_input(
                        "Please Enter the temperature in Celsius: ")
                self.validate_tmp(tmp)
                break

            except Exception as e:
                print("temperature is not valid")
                continue

        return tmp, ftoc

    def tmp_cnvtr(self, tmp, ftoc=True):
        ret = 0.0

        if ftoc:
            ret = (float(tmp) - 32) * 5/9

        else:
            ret = (float(tmp) * 9/5) + 32

        return float(ret)

    def validate_tmp(self, tmp):
        try:
            check = float(tmp)
        except ValueError:
            raise "temperature error"

        return check

    def print_tmp(self, tmp, ftoc=True):
        if ftoc:
            print("The temperature in Celsius is {}".format(tmp))
        else:
            print("The temperature in Fahrenheit is {}".format(tmp))


if __name__ == '__main__':
    cnvtr = temperature()
    cnvtr.routine()
