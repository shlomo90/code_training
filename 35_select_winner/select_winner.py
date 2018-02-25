# -*- encoding:utf-8 -*-
'''
대회 또는 그리기 대회의 수상자를 선택하는 프로그램을 작성하라.
프로그램은 아무것도 입력하지 않을 대 까지 대회 참가자 이릉믈 입력 받은 다음
이 중에서 무직위로 수상자를 선정한다.

출력 예

Enter a name: Homer
Enter a name: Bart
Enter a name: Maggie
Enter a name: Lisa
Enter a name: Moe
Enter a name:
The winner is... Maggie.

제약 조건
* 사용자 입력을 배열에 저장하는 부분을 루프로 구현할 것
* 배열에 있는 값을 선택하기 위해 무작위 숫자 생성기를 사용할 것
* 빈 이름은 배열에 추가하지 말 것
* 어떤 언어는 미리 배열 크기를 정의하도록 요구하기도 하는데 이럴 경우에는
  ArrayList 같은 다른 자료구조를 찾아볼 것

도전 과제
* 수상자가 결정되면 참가자 리스트에서 수상자를 제거한 다음 다른 수상자가 선정
  되도록 구현해보자


flow
1. 이름을 입력 받는다.
2. 이름이 빈 값 또는 whitespace인가?
    yes 이름 입력에 대한 루프를 종료.
    no 이름을 배열에 추가하고, 1번으로 이동.
3. 2번이 yes에 한해서 난수를 생성한다.
4. 생성된 난수에 대해서 이름이 들어있는 배열의 범위로 modulus 연산을 한다.
5. 해당하는 인덱스의 이름을 출력한다.


참가자 정보를 관리하기 위해서 Participant 라는 클래스로 관리한다.
class Participant(dict):
    pass
정보
1. 사용자 이름 (추후 정보 추가 가능)

대회를 관리하기위한 class를 생성한다.
해당 클래스는 참가자들을 관리, 또는 우승자 선택등 다양한 기능을 가진다.
class Competition(object):
    pass

기능
1. 대회 참가자들을 추가.
2. 대회 참가자 삭제
3. 대회 참가자 수정
4. 대회 참가자 리스트 출력.
5. 참가자들 중 우승자 선택
5-1  난수 발생으로 우승자 선택.
5-2  ...

'''

import random


class PersonNameError(BaseException):
    pass


class Person(object):
    def __init__(self, name, age=0, sex='male'):
        if not name.strip():
            raise PersonNameError("Name is Empty")

        self.name = name
        self.age = age
        self.sex = sex

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_name(self, new_name):
        self.name = new_name

    def set_age(self, new_age):
        self.age = new_age

    def set_sex(self, new_sex='male'):
        pass


class Participant(Person):
    def __init__(self, name, contest_name, age=0, sex='male'):
        if not name.strip():
            raise PersonNameError("Name is Empty")

        self.name = name
        self.age = age
        self.sex = sex
        self.contest_name = contest_name
        self.order_id = 0

    def get_order_id(self):
        return self.order_id


class Competition(object):
    def __init__(self):
        self.list_parti = []
        self.last_order_id = 0
        self.total_parti = 0

    def attend(self, parti):
        cur_id = self.last_order_id
        parti.order_id = cur_id
        self.list_parti.append(parti)
        self.last_order_id = cur_id + 1
        self.total_parti = self.total_parti + 1

    def update(self, order_id):
        # get Participant from list
        # set name, age, ...
        pass

    def delete(self, order_id):
        for parti in self.list_parti:
            if parti.get_order_id() == order_id:
                self.list_parti.remove(parti)
                break
        self.total_parti = self.total_parti - 1

    def print_list_parti(self):
        for parti in self.list_parti:
            p_name = parti.get_name()
            order_id = parti.get_order_id()
            print("order:{}, name: {}".format(order_id, p_name))

    def get_winner(self):
        rand_num = self._gen_random_num(self.total_parti)
        winner = self.list_parti[rand_num]
        return winner.name

    def _gen_random_num(self, last):
        random.seed()
        ret = random.randrange(last)
        return ret


if __name__ == "__main__":
    c = Competition()

    while(True):
        try:
            u_name = raw_input("Enter a name: ")
            p = Participant(name=u_name, contest_name="draw")
            c.attend(p)
        except PersonNameError:
            break

    winner = c.get_winner()
    print("The winner is... {}".format(winner))
