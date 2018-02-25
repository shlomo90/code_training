#-*- encoding: utf-8 -*-

'''
다섯 개의 숫자를 입력 받은 다음 입력 받은 수의 합을 계산하는 프로그램을
작성하여라.

출력 예
Enter a number: 1
Enter a number: 2
Enter a number: 3
Enter a number: 4
Enter a number: 5
The total is 15

제약 조건
* 숫자를 입력 받는 부분은 다섯 개의 입력문-대신 개수가 제한된 루프와 같은
  반복문으로 구현할 것.
* 프로그램을 작성하기 전에 순서도를 그릴 것.

도전 과제
* 입력 받은 숫자의 개수를 프로그램에 지정하지 않는 대신 사용자로부터 입력
  받도록 프로그램을 수정해보자. 루프에서 비교하는 용도로 사용하기 전에 반드시
  숫자로 변환해야 한다.
* 숫자만 입력 받고 숫자가 아닌 입력은 거부하도록 프로그램을 수정해보자.
  대신, 숫자가 아닌 입력도 전체 입력 횟수에 포함시킨다. 즉, 다섯 번 입력
  받는 것으로 결정했다면, 숫자든 비 숫자든 총 다섯번만 입력 받은 후 결과를
  나타야 한다.
'''

''' 순서도.

Do program_prompt()

if ret is Number?
    Add ret to sum.
else
    show err msg and go to program_prompt()

if count is 5?
    program done.
else
    go to program_prompt()

'''


class AddNumber(object):
    def __init__(self):
        self.total_sum = 0
        self.total_count = 0
        self.error_count = 0

    def start(self):
        ''' Program이 시작하는 함수.
        Do      : 반복문을 돌면서 값을 입력 받고, 그의 총 합계값을 구하고 출력
        return  : X
        '''
        while(True):
            try:
                r = int(raw_input("Range is ? "))
                if r <= 0:
                    print("Range should be upper 0.")
                    continue
            except ValueError:
                print("Range should be Number")
                continue
            break

        for count in range(1, r + 1):
            try:
                num = int(raw_input("Enter a number: "))
            except ValueError:
                print("Should be Number.")
                self.error_count += 1
                continue
            self.total_count += 1
            self.total_sum += num

        print("The total is {}".format(self.total_sum))

if __name__ == "__main__":
    prog = AddNumber()
    prog.start()
