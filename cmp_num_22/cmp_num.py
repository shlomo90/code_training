# -*- encoding: utf-8 -*-

'''
한 개의 입력 값을 비교하는 것은 이제 익숙해졌을 것이다.
이번에는 여러 개의 입력 값을 처리하는 경우를 살펴보자.
  세 개의 숫자를 입력 받은 다음, 먼저 세 개의 숫자가 서로 다른지를 확인하여
같은 숫자가 있다면 프로그램을 종료시키고, 그렇지 않는 경우에는 입력한 세 개의
숫자 중 가장 큰 수를 출력시키는 프로그램을 작성하라.

출력 예
Enter the first number: 1
Enter the second number: 51
Enter the third number: 2
The largest number is 51.

제약 조건
* 가장 큰 수를 찾기 위해 함수 등을 사용하지 말고 직접 알고리즘을 작성하여 구현
  할 것.

도전 과제
* 입력된 숫자를 모두 추적하여 사용자가 지금까지 입력한 값과 동일하지 않는 값을
  입력하도록 프로그램을 수정해보자.
* 세 개가 아닌 10개의 숫자를 입력하도록 프로그램을 수정해보자.
* 입력하는 숫자의 개수를 제한하지 않도록 프로그램을 수정해보자.
'''
'''

'''

def get_ordinal_str(number):
    suffix = ''
    if number == 1:
        suffix = 'st'
    elif number == 2:
        suffix = 'nd'
    elif number == 3:
        suffix = 'rd'
    else:
        suffix = 'th'
    return str(number) + suffix


if __name__ == '__main__':

    input_vars = []
    INPUT_MSG = 'Enter the {} number: '
    big_num = 0

    try:
        i = 1
        while(True):
            while(True):
                input_var = int(raw_input(INPUT_MSG.format(get_ordinal_str(i))))
                if input_var in input_vars:
                    print("Your value is duplicated.")
                    continue
                break
            input_vars.append(input_var)
            big_num = input_var if input_var > big_num else big_num
            i += 1
    except Exception as e:
        ''' for ending this sequence, press cntl+d'''
        pass

    print("The largest nuber is {}".format(big_num))
