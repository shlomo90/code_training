#-*- encoding: utf-8 -*-

'''
0부터12까지의 곱셈표를 만드는 프로그램을 작성하라.

출력 예

0 X 0 = 0
0 X 1 = 0
....
12 X 11 = 132
12 X 12 = 144

제약 조건
* 중첩된 루프를 사용할 것

도전 과제
* 드롭다운 리스트를 사용하여 숫자를 선택하면, 선택된 숫자에 해당하는 곱셈표가
  나타나는 그래픽 프로그램을 작성하라.
* 다음과 같은 곱셈표를 작성하라.

    | 0 | 1 | ....        | 12|
| 0 | 0 | ....

| 12| ...

'''


def show_multi_table(r):
    """ This function Do Show the multiples table from 0 to range.
    Return 0 if Successfuly multiple table is printed and 1 if error occurred

    >>> show_multi_table(3)
    0 x 0 = 0
    0 x 1 = 0
    0 x 2 = 0
    0 x 3 = 0
    1 x 0 = 0
    1 x 1 = 1
    1 x 2 = 2
    1 x 3 = 3
    2 x 0 = 0
    2 x 1 = 2
    2 x 2 = 4
    2 x 3 = 6
    3 x 0 = 0
    3 x 1 = 3
    3 x 2 = 6
    3 x 3 = 9
    """
    for i in range(r):
        for j in range(r):
            result = i * j
            print("{} x {} = {}".format(i, j, result))


if __name__ == "__main__":
    show_multi_table(12)
