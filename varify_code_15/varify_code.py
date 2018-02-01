#-*- encoding:utf-8 -*-

'''
암호는 미리 저장한 값과 사용자가 입력한 값을 비교하는 것으로 검증한다.
그래서 암호는 맞거나 틀리는 경우만 발생한다.
  사용자 로그인 증명을 검증하는 간단한 프로그램을 작성하라.
  프로그램은 사용자 이름과 암호를 입력 받은 다음, 미리 저장된 사용자 이름에 대한
  암호를 비교하여 암호가 일치하면 "ㅉ디채드!"을, 그렇지 않으면 "That password
  is incorrect."를 출력한다.

출력 예
What is the password: 12345
That password is incorrect.

또는

What is the password: abc$123
Welcome!

제약조건
* 이문제를 해결하기위해 if/else문을 사용할 것
* 사용자 이름과 암호는 대소문자를 구별하도록 할 것

도전과제
* 암호를 입력할 때 화면에 아무것도 나타나지 않도록 하기 위해서는 어떻게 해야
  할지 고민해보자
* 사용자 이름과 암호로 구성된 지도(map)를 만들어 사용자 이름과 암호 조합을
  찾도록 하라.
* 암호를 평문으로 저장하는 대신 비크릡트를 이용하여 암호화한 다음 저장하자.
  그리고는 사용자로부터 입력 받은 암호를 비크립트로 동일하게 암호화한 후
  지도에 저장된 암호화 비교하도록 프로그램을 수정해보자.
'''

MAX_ID_LEN = 12
MAX_PW_LEN = 12

class program():
    def __init__(self):
        self.id = ''
        self.pw = ''
        self.users = self._load_users()

    def __str__(self):
        return 'This is the login program!'

    def login(self):
        verified = False

        guest_id = raw_input("What is your id? ")
        guest_pw = raw_input("What is your pw? ")

        # validate
        if not (self.validate_guest(guest_id, guest_pw)):
            print 'input error'
            return False

        # verify
        if not (self.verify_guest(guest_id, guest_pw)):
            print 'no match'
            return False

        print 'welcome {}'.format(guest_id)
        return True

    def _encrypt_method(self, plain_pw):
        # TODO
        encrypted_pw = plain_pw
        return encrypted_pw

    def _load_users(self):
        users = {}
        # file open.
        try:
            f = open("./users.txt", 'r+')
        except IOError as e:
            print e
        i = 0
        for line in f.readlines():
            user = line.split(':')
            user = map(lambda s: s.strip(), user)
            users[i] = {}
            users[i]['id'] = user[0]
            users[i]['pw'] = user[1]
            i = i + 1
        f.close()
        return users

    def validate_guest(self, user_id, user_pw):
        import re
        reg = re.compile('^[a-zA-Z0-9]+$')
        if len(user_id) > MAX_ID_LEN:
            return False

        if len(user_pw) > MAX_PW_LEN:
            return False

        if not reg.match(user_id):
            print "ID only use Eng and numbers"
            return False

        if not reg.match(user_pw):
            print "PW only use Eng and numbers"
            return False
        return True

    def verify_guest(self, user_id, user_pw):
        users = self.users
        for key, value in users.iteritems():
            if value['id'] == user_id:
                real_pw = self._encrypt_method(user_pw)
                if value['pw'] == user_pw:
                    return True
        return False

if __name__ == '__main__':
    a = program()
    a.login()
