# -*- encoding: utf-8 -*-


import pyperclip
import random
import time

'''
input:
    l   (length)
    s_c (special character)
    n_d (number of digit)

output:
    password.
'''

class CompareError(BaseException):
    pass


class InputError(BaseException):
    pass


class GenPassword(object):
    chars = 'abcdefghijklmnopqrstuvwxyz'
    specials = '~!@#$%^&*()_+?\'\"'
    digits = '1234567890'
    min_length = 8
    max_length = 20
    num_special_char = 2
    num_digit = 2

    def __init__(self, save_clip=False, recommand=False):
        self.save_clip = save_clip
        self.recommand = recommand

    def _get_rand_elem(self, target_list, num):
        ret = []
        for _ in range(0, num):
            index = random.randint(0, len(target_list) - 1)
            ret.append(target_list[index])
        return ret

    def gen_password(self):
        sank = []
        random.seed(time.time())
        length = random.randint(self.min_length, self.max_length)
        n_spec = self.num_special_char
        n_digit = self.num_digit

        sank = self._get_rand_elem(list(self.specials), n_spec)
        sank += self._get_rand_elem(list(self.digits), n_digit)
        sank += self._get_rand_elem(list(self.chars),
                                      length - (n_spec + n_digit))
        random.shuffle(sank)
        self.password = ''.join(sank)
        return self.password

    def print_password(self):
        if self.save_clip is True:
            pyperclip.copy(self.password)

        if self.recommand is True:
            print("Your recommanded passwords are")
            print("1. ", self.gen_password())
            print("2. ", self.gen_password())
            print("3. ", self.gen_password())
        else:
            print("Your password is")
            print(self.gen_password())

    def set_password_info(self):
        leng = int(raw_input("What's the minimum length? "))
        spec = int(raw_input("How many special characters? "))
        digit = int(raw_input("How many numbers? "))
        self._validate_input(leng, spec, digit)

        self.min_length = leng
        self.num_special_char = spec
        self.num_digit = digit

    def _validate_input(self, length, special, digit):
        self._is_gt(length, 0)
        self._is_gt(special, 0)
        self._is_gt(digit, 0)

        if (special + digit) > length:
            raise InputError(
                "The sum of special and digit should be less than length.")
        if (length > self.max_length):
            self.max_length = length

    def _is_gt(self, target, standard):
        if int(target) <= int(standard):
            raise CompareError("Target is not greater than the standard")


if __name__ == "__main__":
    g = GenPassword(save_clip=False, recommand=True)
    g.set_password_info()
    g.print_password()

