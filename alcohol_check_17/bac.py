#-*- encoding:utf-8 -*-

'''
몸무게, 성별, 음주량(잔 수), 마신 술에 해당하는 알코올량 마지막으로 술을 마신
후 경과 시간을 입력 받은 다음 다음 식을 이용하여 혈중 알코올 농도를 구하는
프로그램을 작성하라

BAC = (A * 5.14 / W * r) - .015*H

A : 총 알코올 소비량(온스 단위)
W : 몸무게( 파운드 단위)
r: 성별에 따른 알코올 흡수비 계수
    - 0.73 : 남자
    - 0.6 : 여자
H : 술을 마신 후 경과시간.

(미국에서)법적으로 운전가능한 BAC값인 0.08미만인지를 비교하여 운전 가능 여부를
출력해보자.

출력 예
Your BAC is 0.08
It is not legal fo ryou to drive/

제약 조건
* 숫자 값에 숫자가 입력되도록 보장할 것.
도전과제
* 국제 표준 규격을 사용할 수 있도록 프로그램을 수정해보자.
* 거주하고 있는 미국 주를 입력 받아 미국 주 별 BAC 허용 수치와 비교한 다음,
현재 거주하고 있는 주에서의 운전 가능 여부를 출력하도록 수정해보자.

'''

'''
현재 모든 주가 0.08을 고수하고 있다.
'''


def bac_checker(bac, country=None):
    standard = 0.08

    if bac > standard:
        return False

    return True


def bac_calculator(user_info):
    weight = user_info['weight']
    drinking = user_info['drinking']
    elapsed_time = user_info['elapsed_time']
    alcohol_per_drinking = user_info['alcohol_per_drinking']
    gender = user_info['gender']

    alcohol_coef = 0.73
    bac = 0.0

    if gender == 'female':
        alcohol_coef = 0.6

    bac = ((float(drinking) * float(alcohol_per_drinking))
           * 5.14 / float(weight) * alcohol_coef)
    bac -= (0.015 * float(elapsed_time))
    return bac


def input_info():

    user_info = {}

    user_info['weight'] = raw_input("Your weight? ")
    user_info['gender'] = raw_input("Your gender? ")
    user_info['drinking'] = raw_input("How many drinking? ")
    user_info['alcohol_per_drinking'] = raw_input("alcohol per drinking is? ")
    user_info['elapsed_time'] = raw_input(
        "How long does it past from drinking? ")

    # validate check.
    try:
        validate_info(user_info)
    except:
        print("Value is not Correct")
        return None

    return user_info


def validate_info(user_info):

    number_key_list = ['weight', 'drinking', 'alcohol_per_drinking',
                       'elapsed_time']

    for key in number_key_list:
        if not is_number(user_info[key]):
            raise ValueError

    if user_info['gender'] not in ['female', 'male']:
        raise ValueError


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    # start program.
    user = {}

    # input user info
    user = input_info()

    # calculator BAC
    user['bac'] = bac_calculator(user)

    print("Your BAC is {}".format(user['bac']))
    if bac_checker(user['bac']):
        print("It is legal for you to drive.")
    else:
        print("It is not legal for you to drive.")
