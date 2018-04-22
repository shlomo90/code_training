# -*- encoding: utf-8 -*-


import requests
import json
import firebase
import datetime
from firebase import firebase

#firebase = firebase.FirebaseApplication("https://mynote-724e7.firebaseio.com/", None)

'''
일부 외부 서비스는 데이터를 읽어오는 것을 넘어 데이터를 업데이트 하는 기능도
제공한다. Firebase는 자신만의 데이터베이스를 만들도록 하여, 웹, 모바일, 데스크톱
애플리케이션을 위한 데이터를 저장할 수 있다. 그리고 어떤 프로그래밍 언어로도
JSON 기반의 API를 이용하여 저장된 데이터를 사용할 수 있다.

Firebase를 이용하여 노트를 저장하고 저장된 노트를 보여주는 간단한 애플리케이션을
작성하라. 이 애플리케이션은 다음과 같은 명령을 지원해야 한다.

* mynotes new Learn how to invert binary trees는 노트를 저장한다.
* mynotes show 명령을 사용하면 현재 저장된 모든 노트를 나타낸다.

출력 예

$ mynotes new Learn how to invert binary trees
Your note was saved.

$mynotes show
2050-12-31 - Learn how to invert binary trees
2050-12-30 - Notetaking on the command line is cool.

제약 조건
* 설정 파일을 만들어 API 키를 설정 파일에 저장하도록 할 것
* 미리 만들어진 별도의 클라이언트 라이브러리를 사용하는 대신
    https://www.firebase.com/docs/rest에서 제공하는 REST 문서를 사용할 것

도전 과제
* 노트를 검색하고 노트의 내용을 볼 수 있는 조금 더 일반화된 애플리케이션으로
  발전시켜 보자.
* 구현한 코드 중 하나를 클라이언트 라이브러리를 사용하여 구현해보자.
* 노트에 태그를 다는 기능을 추가하자.
* 8장의 일부 연습문제를 Firebase를 사용하는 버전으로 수정해보자.
'''

NOTE_URL = "https://mynote-724e7.firebaseio.com/test.json"


class MyNotes(object):
    def __init__(self, uid=None, passwd=None):
        self.firebase = firebase.FirebaseApplication(
                "https://mynote-724e7.firebaseio.com/", None)
        self.user_hash = None
        self.allowed = False
        try:
            self.users = self.firebase.get("/users/", None)
        except:
            print("Connection Error")
            pass

        if uid and passwd:
            self.login_account(uid, passwd)
        else:
            print("You don't input ID, PASSWD")
            ans = raw_input("Would you like create your own account?")
            
            if ans in ["yes", "y"]:
                self.enroll_account()
                print("Wel come!")
            else:
                print("Now is offline")

    def login_account(self, uid, passwd):
        for h, user in self.users.iteritems():
            if user["uid"] == uid and user["passwd"] == passwd:
                print("Login Success!")
                self.user_hash = h
                self.allowed = True
                break
            else:
                continue
        else:
            print("Login Fail!")
            self.allowed = False


    def enroll_account(self):
        uid = raw_input("your uid is ")
        name = raw_input("your name is ")
        passwd = raw_input("your passwd is ")


        user_path = "/users"
        data = {"uid": uid, "name": name, "passwd": passwd}
        notes = self.firebase.post(user_path, data)
        self.user_hash = notes["name"]
        self.allowed = True
        self.push_note("Now you can write note!")


    def get_all_notes(self):
        if self.allowed == False:
            print("You don't have authentication!")
            return
        
        path = "/users/{}/notes/".format(self.user_hash)

        notes = self.firebase.get(path, None)

        print("---------MESSAGE----------")
        for h, data in notes.iteritems():
            print(data)

    def push_note(self, msg):
        if self.allowed == False:
            print("You don't have authentication!")
            return

        path = "/users/{}/notes".format(self.user_hash)
        notes = self.firebase.post(path, msg)


if __name__ == "__main__":
    #m = MyNotes(uid="weeneen02", passwd="test")
    #m.push_note(msg="Yeah this is the first message")

    m = MyNotes(uid="test", passwd="test")
    #m.push_note("YEHAAHAHAHAH!:")
    m.get_all_notes()



