# -*- coding: utf-8 -*-
"""
위에 코드를 추가하면 한글을 쓸 수 있다.이거 한글 써도 되나?
This is a program calculating your retire day.

input:
    1. your age.
    2. the age you want to retire.

output:
    1. years left until your  retire days.
    2. this year.
    3. the year when you retire.

restraint
    input should be a number
    should implement the system date by using programming language
"""

""" this means I am gonna use datetime from datetime package"""
"""
you may wondering what is difference between from import and import
Here is the anwer!

from urllib import request
# access request directly.
mine = request()

import urllib.request
# used as urllib.request
mine = urllib.request()
"""

from datetime import datetime


def get_this_year ():
    """ Return This year """
    now = datetime.now()
    return now.year


"""
start!
"""
if __name__ == "__main__":

    # int(_) is the way to convert string or something to inteager.***
    your_age = int(raw_input("What is your current age? "))

    while (1):
        retire_age = int(raw_input("At what age would you like to retire? "))

        # retire age - your age
        left_age = retire_age - your_age

        if (left_age < 0):
            print("you should input retire age over your age")
            continue
        else:
            break


    this_year = int(get_this_year())
    retire_year = this_year + left_age

    # if you wanna use inteager to print, you should use str() function.
    print("you have " + str(left_age) + " years left until you can retire.")
    print("It's " + str(this_year) +
          ", so you can retire in " + str(retire_year) + ".")
