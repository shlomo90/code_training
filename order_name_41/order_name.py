# -*- encoding: utf-8 -*-

import time

'''
다음과 같은 이름 리스트가 저장된 파일을 읽는 프로그램을 작성하라.

Ling, mai
Johnson, Jim
Zarneck, Sabrina
Jones, Chris
Jones, Aaron
Swift, Geoffrey
Xiong, Fong

앞의 리스트를 읽은 다음 알파벳순으로 정렬하라. 그런 다음 정렬된 리스트를 다음의
출력 예와 같은 형태로 파일에 저장하라.

출력 예
Total of 7 names
-----------------
Ling, mai
Johnson, Jim
Jones, Aaron
Jones, Chris
Swift, Geoffrey
Xiong, Fong
Zarneck, Sabrina

제약 조건
* 이름 개수를 하드코딩하지 말 것 v

도전 과제
* 사용자로부터 이름 리스트를 한번에 입력 받은 다음, 정렬된 결과를 파일에 저장
  하도록 프로그램을 수정해보자. v
* 대규모 데이터를 이 프로그램에 적용하여 프로그램 성능이 얼마나 나오는지 확인
  하라. v
* 이 프로그램을 함수형 프로그래밍 언어로 작성한 다음 프로그램을 비교하라.
'''

class LoadError(BaseException):
    pass


class InputError(BaseException):
    pass


class LoadName(object):
    def __init__(self, path):
        if path is None:
            raise LoadError("Incorrect path")

        try:
            with open(path, 'r') as f:
                lines = f.readlines()
                lines = [x.strip() for x in lines]
        except IOError:
            print("File Open error")

        self.elapsed = 0.0
        self.path = path
        self.names = lines

        # Do last.
        self._update_msg()

    def add_name(self, name):
        if name is None:
            raise InputError("Name is Empty")

        self.names.append(name)
        self.modified = True

    def delete_name(self, idx):
        if idx < 0:
            raise InputError("Index should be more then 0")

        del(self.names[idx])
        self.modified = True

    def find_name(self, name, case_sens=True):
        '''
        arg:
            name        : person name
            case_sens   : True is case sensitive (default)
        ret:
            index : self.n_list's index, if not found, -1
        '''
        for i, n in enumerate(self.names):
            if n == name:
                return i

        return -1

    def _update_msg(self):
        num_name = len(self.names)
        info_lines = []
        info_lines.append("Total of {} names".format(num_name))
        if self.elapsed != 0.0:
            info_lines.append("Time elapsed: {} ms".format(self.elapsed))
            self.elapsed = 0.0

        info_lines.append("-----------------")

        self.result = []
        self.result += info_lines
        self.result += self.names
        self.modified = False

    def save(self, to=None):
        path = self.path
        if to is not None:
            path = to

        if self.modified is True:
            self._update_msg()

        with open(path, "w") as f:
            f.write('\n'.join(self.result))

    def preview(self):
        if self.modified is True:
            self._update_msg()

        print '\n'.join(self.result)

    # decorator는 self.를 쓰지 않는다.
    def _deco_timer(func):
        def wrap_func(self, key):
            start = time.time() * 1000
            #Decorator 를 클래스 안에서 쓰는 경우.
            func(self, key)
            self.elapsed = round(time.time() * 1000 - start, 2)

        return wrap_func

    @_deco_timer
    def order(self, key):
        ordered = sorted(self.names, key=key)
        self.names = ordered
        self.modified = True


if __name__ == "__main__":
    d = LoadName("./names.txt")
    d.order(str.lower)
    d.preview()
    d.save(to="./new_names.txt")
