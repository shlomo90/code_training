# -*- encoding:utf-8 -*-

import time

from math import sqrt
from getkeygen import get_pask_key


''' 사용자 입력에 대한 통계를 계산하는 프로그램. '''

'''
1. start_time   : 요청할 때 시간.
2. end_time     : 요청에 대한 응답이 온 시간.
3. elapsed_time : end_time - start_time

책에서는 경과시간(elapsed_time)을 임의로 입력하지만, 기존에 내가 구현한
웹페이지에 요청을 보내는 바이너리 파일을 실행해서 값을 구하도록 한다.

파일        : 경로
getkeygen   : ./getkeygen.py

'''


def time_deco(func):
    ''' 함수의 총 걸리는 시간을 측정해주는 데코레이터 '''

    def func_wrapper(serial, host):
        start_time = round(time.time() * 1000, 2)
        func(serial, host, mute=True)
        elapsed_time = round(time.time() * 1000, 2) - start_time

        return "elapsed: %s" % elapsed_time, round(elapsed_time, 2)

    return func_wrapper


def input_msg():
    ''' 유저의 입력값을 받는 함수.
    done을 입력하였을 시에는 True,
    그 외의 값을 입력하면 False로 처리한다. '''

    ans = str(raw_input("Enter a number: "))
    if ans == 'done':
        return True
    return False


if __name__ == "__main__":
    time_list = []

    while (1):
        if input_msg() is True:
            break

        kgen = time_deco(get_pask_key)
        m, t = kgen("TEST", "XXXXXX")
        time_list.append(t)

    print("Numbers: {}".format(time_list))
    t_min = round(min(time_list), 2)
    t_max = round(max(time_list), 2)
    num_time = len(time_list)
    if num_time == 0:
        exit(1)

    avg = sum(time_list) / float(num_time)
    devn = sum(map(lambda x: (avg - x) ** 2, time_list)) / float(num_time)
    std_devn = round(sqrt(devn), 2)
    print("The average is %s" % avg)
    print("The minimum is %s" % t_min)
    print("The maximum is %s" % t_max)
    print("The standard deviation is %s" % round(std_devn, 2))
