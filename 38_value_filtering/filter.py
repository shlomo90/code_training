# -*- encoding:utf-8 -*-
import sys

'''
숫자 리스트를 입력 받고 공백글자로 나누어 저장한 다음 이 중에서 짝수만 들어
있는 새로운 배열을 만들어 출력하는 프로그램을 작성하라.

출력 예
Enter a list of numbers, separated by spaces: 1 2 3 4 5 6 7 8
The even numbers are 2 4 6 8.

제약 조건
* 입력 스트링을 배열로 변환할 것. 언어가 스트링을 배열로 쉽게 변환시킬 수
  있도록 함수를 제공한다. 이 함수들은 구분자를 제공받아 스트링을 배열로 변환
  시킨다.

* 자신만의 알고리즘을 작성할 것. 언어에서 제공하는 filter나 비슷한 열거 기능
  을 사용하지 말것.

* 이 로직을 다루는 함수 filterEvenNumbers 함수를 만들 것. 이 함수는 기존 배열을
  입력 받아 새로운 배열을 반환한다.

도전 과제
* 숫자를 일일이 입력 받는 대신 텍스트 파일로부터 숫자를 입력 받아 짝수 줄만
  출력하도록 하라.


'''

def filterEvenNumbers(num_list):
    ''' return new list which has only even numbers from num_list
    args:
        num_list: only integer numbers in it.

    ret:
        even_list: the list of numbers that are only even.
    '''
    even_list = [i for i in num_list if int(i) % 2 == 0]
    return even_list


def get_number():
    str_list = raw_input("Enter a list of numbers, separated by spaces: ")
    num_list = str_list.split()
    return num_list


def print_even(even):
    str_list = " ".join('{}'.format(k) for k in even)
    print("The even numbers are {}".format(str_list))


if __name__ == "__main__":
    try:
        with open("./nudmber.txt", "r") as f:
            for i, line in enumerate(f.readlines()):
                if i % 2 == 0:
                    nums = line.split()
                    even = filterEvenNumbers(nums)
                    print_even(even)
    except Exception as e:
        print(e)
        nums = get_number()
        even = filterEvenNumbers(nums)
        print_even(even)
