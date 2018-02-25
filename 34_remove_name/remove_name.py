# -*- encoding:utf-8 -*-

'''
사원 명단이 들어있는 프로그램을 작성하라. 프로그램이 실행되면 리스트안에 있는
모든 사원을 출력한 다음, 명단에서 삭제할 이름을 입력 받고 해당하는 이름을
제거한다. 그리고는 나머지 명단을 한 줄 씩 출력한다.

출력 예
There are 5 employees:
John Smith
Jackie Jackson
Chris Jones
Amanda Cullen
Jeremy Goodwin
Enter an employee name to remove: Chris Jones
Therre are 4 employees:
John Smith
Jackie Jackson
Amanda Cullen
Jeremy Goodwin


제약 조건
* 이름을 저장하기 위해 배열이나 리스트를 사용할 것

도전 과제
* 입력한 이름이 리스트에 없다면 해당 이름을 나타내며 이름이 없다는 에러 메세지를
  출력하도록 한다.
* 파일에서 사원 명단을 읽은 다음, 이름 하나 당 한 줄씩 출력하도록 수정해보자.
* 읽은 파일과 동일한 파일에 저장하도록 하라.

'''


def print_employee(employees):
    num_employees = len(employees)
    plural = 's' if num_employees > 1 else ''
    msg = "There are {} employee{}:".format(num_employees, plural)
    print(msg)


def load_employee(personal_file=''):
    employees = []
    if not personal_file:
        names = '''John Smith
Jackie Jackson
Chris Jones
Amanda Cullen
Jeremy Goodwin'''
        employees = names.split("\n")
    else:
        #file open.

    return employees


if __name__ == "__main__":
    employees = load_employee()

    print_employee(employees)
    ask_remove()
    pass
