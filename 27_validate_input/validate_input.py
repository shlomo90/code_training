#-*- encoding: utf-8 -*-

'''
이름과 성, 사번, 우편번호를 입력 받은 다음, 다음과 같은 규칙에 맞는지를 점검
하는 프로그램을 작성하라.

* 이름은 반드시 넣어야 한다.
* 성은 반드시 넣어야 한다.
* 이름과 성은 최소한 두 글자 이상이어야 한다.
* 사번은 AA-1234의 형태가 되어야 한다. 즉, 두 글자의 알파벳, 하이픈, 4자리 숫자
  로 구성이 되어야 한다.
* 우편번호는 반드시 숫자여야 한다.
  잘못된 데이터가 입력되면 적절한 에러 메세지를 출력해야 한다.

출력 예
Enter the first name: J
Enter the last name:
Enter the ZIP code: ABCDE
Enter an employee ID: A12-1234
"J" is not a valid first name. It is too short.
The last name must be filled in.
The ZIP code must be numeric.
A12-1234 is not a valid ID.

또는

Enter the first name: Jimmy
Enter the last name : James
Enter the ZIP code: 55555
Enter an employee ID: TK-421
There were no errors found.

제약 조건
* 입력 데이터를 검증하는 함수를 각각 만들고, validateInput 함수를 만들어 모든
  입력 데이터를 인수로 받은 다음 각각의 경우마다 별도로 만든 입력 데이터 검증
  함수들을 호출하여 입력 값을 검증하도록 구현할 것.

* 결과를 출력하는 출력문은 한 개만 사용할 것.

도전 과제
* 입력 값을 검증하기 위하여 정규표현식(Regular Expression)을 사용하라.
* 이 프로그램을 GUI 버전으로 작성한 후, 입력 필드가 활성화되었다가 다시
  비활성화될 때 입력 값에 대한 결과를 바로 출력하라.
* 잘못된 입력 값이 들어온 경우 다시 입력 부분부터 반복하도록 프로그램을 수정
  해보자.
'''

'''
1. tuple을 만들어 입력값을 받도록 하자.
   input
   person = (fname, lname, zip, id)
   output
   ret, errmsg
    ret = False : 정상. (errmsg 없음)
    ret = True : 에러. (errmsg 출력)
    errmsg = 에러 메세지들이 join되어 출력된다.
        errmsgs 는 list형식.
        errmsg는 errmsgs를 join한 한 문자열.

2. flag 변수(errflag = False)를 두어 에러 발생시 True로 세팅.
    한번 True 설정되면 다음 결과에 상관없이 True로 세팅.
'''


def validateFirstName(name):
    err = False
    msg = ''
    if not name:
        err = True
        msg = 'The first name must be filled in'
        return err, msg
    if len(name) < 2:
        err = True
        msg = '"{}" is not a valid first name. It is too short.'.format(name)
    return err, msg

def validateLastName(name):
    err = False
    msg = ''
    if not name:
        err = True
        msg = 'The last name must be filled in'
        return err, msg
    if len(name) < 2:
        err = True
        msg = '"{}" is not a valid last name. It is too short.'.format(name)
    return err, msg

def validateZipcode(zipcode):
    err = False
    msg = ''
    try:
        int(zipcode)
    except ValueError:
        err = True
        msg = 'The ZIP code must be numeric.'

    return err, msg


def validateEmploeeId(eid):
    import re
    err = False
    msg = ''

    m = re.search('[a-zA-Z][a-zA-Z]-[0-9][0-9][0-9][0-9]$', eid)
    if not m:
        err = True
        msg = '"{}" is not a valid ID.'.format(eid)

    return err, msg


def validateInput(person):
    ''' 들어온 값에 대한 유효값 검사를 하는 함수.'''

    errflag = False
    errmsgs = []

    err, msg = validateFirstName(person[0])
    errflag = err if err else errflag
    errmsgs.append(msg)

    err, msg = validateLastName(person[1])
    errflag = err if err else errflag
    errmsgs.append(msg)

    err, msg = validateZipcode(person[2])
    errflag = err if err else errflag
    errmsgs.append(msg)

    err, msg = validateEmploeeId(person[3])
    errflag = err if err else errflag
    errmsgs.append(msg)

    if errflag:
        pass

    errmsgs = [x for x in errmsgs if x]

    return errflag, '\n'.join(errmsgs)


def inputValue():
    ''' 처음 시작할 대 input을 받는 함수.'''
    fname = raw_input("Enter the first name: ")
    lname = raw_input("Enter the last name: ")
    zipcode = raw_input("Enter the ZIP code: ")
    eid = raw_input("Enter an employee ID: ")
    person = (fname, lname, zipcode, eid)
    return person


if __name__ == "__main__":
    while (True):
        p = inputValue()
        (ret, errmsg) = validateInput(p)
        if ret:
            print(errmsg)
            continue
        break
    print("There were no errors found")
