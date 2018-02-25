# -*- encoding: utf-8 -*-
from enum import Enum
import string

'''
주어진 암호의 복잡도를 결정하는 프로그램을 작성하라. 복잡도는 다음과 같은 규칙
으로 정한다.

* 아주 약한 암호는 숫자로만 구성되고 길이도 8글자 미만임.
* 약한 암호는 영문자로만 구성이되고 길이도 8글자 미만임.
* 강한 암호는 영문자와 한 개 이상의 숫자로 구성되어 있으며 길이는 8글자 이상임.
* 아주 강한 암호는 영문자, 숫자, 특수문자로 구성되어 있으며 길이는 8글자 이상임

출력 예
The password '12345' is a very weak password.
The password 'abcdef' is a weak password.
The password 'abc123xyz' is a strong password.
The password '1337h@xor!' is a very strong password.

제약 조건
* 암호를 인수로 받은 다음 암호의 복잡도를 알 수 있는 값을 반환하는
  passwordValidator 함수를 작성할 것. 이때 passwordValidator 함수는 문자열을
  반환해서는 안된다. 왜냐하면 나중에 다국어를 지원하는 경우 문제가 생길수 있기
  때문이다.
* 한 개의 출력문만 사용할 것

도전 과제
* GUI 도는 웹 애플리케이션으로 작성하여 실시간으로 암호를 입력할 때 복잡도를
  그래픽 형태로 알려주도록 하라.
'''

'''
input
    * password 영어 소,대문자,특수문자로 이루어짐.

output
    * 영문자, 소,대문자 이외의 값은 InputError.
    * 영문자 8글자 이상이면? => 보통암호라 정의
    * 영문자 + 특수문자 8글자 미만 => 보통암호라 정의
    * 암호는 반드시 한글자 이상이어야 한다.
        * 값이 없으면 InputError.
    * 숫자로 8글자 이상 => 보통암호라 정의

'''


class InputError(Exception):
    pass


VERY_WEEK = 1
WEEK = 2
NORMAL = 3
STRONG = 4
VERY_STRONG = 5


class c(str):
    def __new__(cls, value):
        obj = str.__new__(cls, value)
        return obj

    def isspecialchar(self):
        special = set(string.punctuation)
        if self in special:
            return True
        else:
            return False


def passwordValidator(pw):
    classified = {'alpha': 0, 'digit': 0,
                  'special': 0, 'undefined': 0}
    for letter in list(pw):
        char = c(letter)
        if char.isalpha():
            classified['alpha'] += 1
            continue
        if char.isdigit():
            classified['digit'] += 1
            continue
        if char.isspecialchar():
            classified['special'] += 1
            continue
        raise InputError("invalid password")

    classified['total'] = classified['alpha'] + classified['digit'] \
        + classified['special']
    if classified['total'] < 8:
        if classified['digit'] == classified['total']:
            return VERY_WEEK
        if (classified['alpha'] and not classified['digit']
                and not classified['special']):
            return WEEK
    else:
        if (classified['alpha'] and classified['digit']
                and not classified['special']):
            return STRONG
        if (classified['alpha'] and classified['digit']
                and classified['special']):
            return VERY_STRONG
    return NORMAL


def msg_degree(degree):
    msg_dict = {1: 'VERY_WEEK', 2: 'WEEK', 3: 'NORMAL', 4: 'STRONG',
                5: 'VERY_STRONG'}
    try:
        msg = msg_dict[degree]
    except:
        return "Undifined"
    return msg


if __name__ == "__main__":
    pw = raw_input("Enter Password : ")
    ret = passwordValidator(pw)
    print(msg_degree(ret))
