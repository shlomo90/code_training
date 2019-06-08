#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import pastie_shell
import sys
from threading import Thread

'''
텍스트로 구성된 짧은 소식을 공유하는 http://pastie.org 와 유사한 웹
어플리케이션을 작성하라. 이 프로그램은 다음을 만족해야 한다.

* 사용자는 텍스트 영역에 텍트스를 입력한 다음 텍트스를 저장해야 한다.
* 텍스트는 데이터 저장소에 저장되어야 한다.
* 프로그램은 저장된 텍스트를 조회할 수 있는 URL 을 생성해야 한다.
* 그래서 사용자가 해당 URL에 접속하면 저장된 텍스트가 나타나면서 이와 함께
  텍스트를 수정할 수 있는 [Edit] 버튼을 제공한다.
* [Edit] 버튼을 클릭하면, 텍스트는 복사되고 새로운 텍스트를 만들었던
  인터페이스와 동일한 인터페이스를 붙여 넣어 수정될 수 있도록 하자.

제약 조건

* URL에 대한 일차 키 대신 별도로 생성한 별칭을 사용할 수 있도록 할 것.
  SHA 또는 MD5 해시에 대한 내용을 조사해보자.

도전 과제

* 마크다운(Markdown) 형식을 지원하도록 프로그램을 수정해보자.
* edit 기능을 통해 저장된 노트는 새로 저장되도록 하여 기존의 노트가 모두 유지
  되도록 프로그램을 수정해보자.
* API 를 구현하여 명령줄, 데스크톱, 모바일 어플리케이션이 새로운 내용을
  추가하거나 이미 작성된 텍스트를 볼 수 있도록 구현해보자

'''

'''
I do make a "pastie" in command uesr interface instead of GUI.
The program "pastie" simply does ..
    1. Get the data from URI user input
    2. Edit the data
    3. Save the data

The program "pastie" is Server-Client model.
It simply provides its own shell prompt "pastie> ".

'''

if __name__ == "__main__":

    pastie_shell.do_shell("pastie", 10)
    '''
    t = Thread(target=pastie_shell.do_shell, kwargs={"prompt": "pastie >", "timeout":100})
    t.start()
    t.join(10)
    '''
    print "done"
