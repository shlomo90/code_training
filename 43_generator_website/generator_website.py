#-*- encoding:utf-8 -*- 

import os
import shutil

'''
프로그래밍 언어는 파일과 폴더를 생성할 수 있다.

  다음의 조건을 만족하는 웹사이트 골격을 생성하는 프로그램을
작성하라 

* 사이트 이름을 입력 받는다.
* 사이트 필자를 입력 받는다.
* 자바 스크립트 파일을 위한 폴더를 만들 것인지를 입력받는다.
* CSS 파일을 위한 폴더를 만들 것인지 입력 받는다.
* index.html 파일을 생성한다. index.html 파일에는 <title>태그
  를 이용한 사이트 이름과 <meta> 태그를 이용한 필자 이름이 들어있다.

출력 예
Site name: awesomeco
Author: Mac Power
Do you want a folder for JavaScript?
Do you want a folder for CSS?
Created ./awesomeco
created ./awesomeco/index.html
Created ./awesomeco/js/
Created ./awesomeco/css/


도전 과제
* 이 프로그램을 윈도, OSX, 리눅스에서 스크립트 언어를 이용하여
  구현해보자.

* 이 프로그램을 특정 사이트를 zip 파일로 제공하는 웹 에플리케이션으로
  구현해보자
'''
'''
RFC1034 : The full domain name may not exceed the length of 253 characters in its textual representation

input:
    site name
        * case-insenstive (convert to lowercase.)
        * less than 253
        * available characters (if www.naver.com, except www. or .com)
            Reference RFC1034
            :abcdefghijklmnopqrstuvwxyz
            :ABCDEFGHIJKLMNOPQRSTUVWXYZ
            :1234567890
            :-
        * handle space
            : Remove the spaces in the name user input.
    Auther
        * Any characters
        * case-sensitive
        * space allowed
        * less than 255

    Qustions
        * Ask list
            JavaScript
            CSS
        * Answer
            :avaliable characters (y, n, yes, no) and case-insensitive.
output:
    Create file or directory
        * Directory
            :site name
            :sitename/js if user wanted js
            :sitename/css if user wanted css
        * file
            :default index.html
    
'''
class InputError(BaseException):
    pass


class GenerateError(BaseException):
    pass


class GenWebSite(object):
    MAX_SITE_NAME = 253
    MAX_AUTHOR_NAME = 255

    def __init__(self):
        self.current_dir = os.getcwd()
        self.javascript = False
        self.css = False
        self.site_name = ''
        self.author = ''

    def get_user_requirement(self):
        ''' It shows questions to user to get their requirements interactively.
        '''
        site_name = raw_input("Site name: ").replace(" ", "").lower()
        author = raw_input("Author: ").strip()
        ask_java = raw_input("Do you want a folder for JavaScript? ")
        ask_css = raw_input("Do you want a folder for CSS? ")

        ''' validate '''
        if len(site_name) > self.MAX_SITE_NAME:
            raise InputError("You must input string less than 255")
        else:
            for c in site_name:
                if (c.isalpha() is False
                        and c.isdigit() is False
                        and c != '-'):
                    raise InputError("You must input string"
                                    "in alpha or digit or hypen")
            self.site_name = site_name

        if len(author) > self.MAX_AUTHOR_NAME:
            raise InputError("You must input string less than 255")
        else:
            self.author = author


        self.javascript = True if ask_java.lower() in ['yes', 'y'] else False
        self.css = True if ask_css.lower() in ['yes', 'y'] else False


    def gen_files(self):
        ''' Make a site directory in the current dir. '''

        site_dir = '{}/{}'.format(self.current_dir, self.site_name)
        if not os.path.exists(site_dir):
            os.makedirs(site_dir)
            print("Created {}".format(site_dir))
        else:
            raise GenerateError('File already exists')

        #index file.
        index_cnt = []
        index_cnt.append('<title>{}</title>'.format(self.site_name))
        index_cnt.append('<meta>{}</meta>'.format(self.author))

        with open('{}/index.html'.format(site_dir), 'w') as f:
            f.write('\n'.join(index_cnt))
            print("Created {}/index.html".format(site_dir))


        if self.javascript is True:
            js_dir = '{}/js'.format(site_dir)
            if not os.path.exists(js_dir):
                os.makedirs(js_dir)
                print("Created {}".format(js_dir))
            else:
                raise GenerateError('Javascript Dir already exists')

        if self.css is True:
            css_dir = '{}/css'.format(site_dir)
            if not os.path.exists(css_dir):
                os.makedirs(css_dir)
                print("Created {}".format(css_dir))
            else:
                raise GenerateError('CSS Dir already exists')

    def close(self):
        ''' delete the generated folders '''
        site_dir = '{}/{}'.format(self.current_dir, self.site_name)
        if os.path.exists(site_dir):
            shutil.rmtree(site_dir)


if __name__ == "__main__":
    web = GenWebSite()
    web.get_user_requirement()
    web.gen_files()
    #web.close()
