# -*-encoding:utf-8 -*-

import os
import re
from word_manip import WordManip

'''
하나의 파일을 읽고 그 내용을 수정한 후 수정한 버전을 새로운 파일에 저장하는
경우도 생길 것이다.

  입력 파일을 제공받고 파일을 읽은 다음 'utilize'라는 단어가 얼마나 나오는지를
확인한다. utilize를 use로 바꾸고, 새로운 파일에 변경된 내용을 저장하는 프로그램
을 작성하라.

출력 예
제공되는 입력 파일 내용:

One should never utilize the word "utilize"
writing. Use "use" instead.

프로그램이 생성한 파일 내용:

One should never use the word "use" in
writing. Use "use" instead.

제약 조건
* 출력 파일의 이름을 입력 받도록 구현할 것
* 새로운 파일에 결과를 작성할 것

도전 과제
* 치환된 횟수를 기록한 다음 프로그램이 끝났을 때 화면에 채환한 개수를 출력하
  도록 프로그램을 수정해보자.

* 설정파일을 만들어 이 안에 'bad'를 'good'으로 변경하도록 하는 맵을 넣은 후,
  코드에 치환할 단어를 넣는 대신 이 설정파일을 사용하도로고 프로그램을 수정해
  보자.

* 한 개의 파일을 사용하지 않고, 폴더를 지정하면 폴더에 들어있는 모든 파일에
  적용시킬 수 있도록 프로그램을 수정해보자.
'''

'''
입력 : file, or directory. with conf 파일.

1. 해당 디렉토리에 conf파일을 읽도록 한다.
    없으면? nothing.

conf 파일 구조
    기본적으로 map 형식이다. directive를 쓰도록 하자.

word_manip {
  test  test
}

# TODO 추후 개발 하고싶은것.
directory_name {
  test  test
}


결과 : 새로운 파일

1. 프로그램 실행시 현재 디렉토리를 기반으로 하도록 한다.
2. 현재 위치에 config.conf 파일을 찾도록 한다.
3. directive 맵을 파싱한다.
4. directive 이름에 따라 각 기능으로 이돟한다.
5. (word_manip 일 경우,) 디렉토리 내에 모든 txt파일의 test 단어를 test'으로 치환.


1차 개발 목표

텍스트 문자 파일을 입력 받고 찾고자 하는 문자열과 치환할 문자열 두개를 입력
해당 파일에 대해서만 치환하는 것이 목표.
'''





'''
class ShellToy(object):
    def __init__(self, path):
        self.conf = ConfParser(path)


class ConfParser(object):
    def __init__(self, path):
        self.conf_file = path + "/config.conf"
        self.cfile = None


        try:
            self.cfile = open(self.conf_file, "r")
        except IOError:
            print("No config file")
            return

        # TODO 일단은 하나만 받도록한다.
        prog = re.compile("location\s[{](.*)[}]")
        prog2 = re.compile("\s
        if prog:
            location = prog.match(self.cfile.read())
        else:
            print("Invalid config.")


        directives = location[1].strip()




        conf_data = self.cfile.readlines()
        for line in conf_data:
            line = line.strip()

            if line.strip[0] = "#":
                continue

'''

class LocationBlock(object):
    '''
    Variables:
        self.path = The path for processing directives.
        self.d_list : The list of directives for Location
            1. There are the list of directives for Location.
               The directives in the list should be available.
        self.e_list : The list of directives executing  in Location.
    '''
    d_list = ['word_manip',]

    def __init__(self, path):
        ''' .으로 시작하면, 상대, /으로 시작하면 절대, 그 외 에러.'''
        self.is_abspath = None
        self.path = self._validate_path(path)
        self.cur_loc = os.getcwd()
        self.e_list = []

    def _validate_path(self, path):
        path = path.strip()
        if path[0] == '.':
            self.is_abspath = False
        elif path[0] == '/':
            self.is_abspath = True
        else:
            raise InputError("Location Path is invalid.")
        return path

    def execute(self):
        for d in self.e_list:
            d.execute(self)

    def set_directive(self, directives):
        self.e_list.append(directives)


class InputError(BaseException):
    pass


class SearchReplace(object):
    def __init__(self, path, match, replace):
        self.cur_dir = os.getcwd()
        self.path = path
        self.match = match
        self.replace = replace
        print(self.cur_dir, self.path, self.match, self.replace)


if __name__ == "__main__":
    #input_file = raw_input("Input the file you wanna change words: ")
    match = raw_input("Match: ")
    replace = raw_input("Replace: ")

    loc = LocationBlock("./")
    w = WordManip(match, replace)
    loc.set_directive(w)
    loc.execute()
